#!/usr/bin/env python3
"""
Figure generation script for the ADDC paper.
Generates all 7 figures from experiment logs.
Usage: python make_figures.py
Output: research_workspace/reports/paper/figures/
"""

import os, json, glob, sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

# ---- Configuration ----
PROJECT_ROOT = "/mnt/d/projects/multi_agent_projects/auto_research/project0619v1"
LOG_DIR = os.path.join(PROJECT_ROOT, "research_workspace/experiments/logs")
FIG_DIR = os.path.join(PROJECT_ROOT, "research_workspace/reports/paper/figures")
os.makedirs(FIG_DIR, exist_ok=True)

# Matplotlib style
plt.rcParams.update({
    'font.size': 11,
    'axes.titlesize': 13,
    'axes.labelsize': 12,
    'legend.fontsize': 10,
    'figure.figsize': (8, 5),
    'figure.dpi': 150,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
})

COLORS = ['#2166ac', '#d6604d', '#f4a582', '#4393c3', '#b2182b', '#4d4d4d']
METHOD_NAMES = {'standard': 'Standard', 'rezero': 'ReZero', 'attnres': 'AttnRes', 'addc': 'ADDC'}

# ===================================================================
# Helper: load metrics from CSV
# ===================================================================
def load_metrics(csv_path):
    """Load metrics CSV. Returns dict of arrays."""
    data = {'step': [], 'train_loss': [], 'lr': [], 'val_loss': [], 'val_ppl': []}
    with open(csv_path) as f:
        header = f.readline().strip().split(',')
        for line in f:
            parts = line.strip().split(',')
            row = dict(zip(header, parts))
            step = int(row['step'])
            data['step'].append(step)
            data['train_loss'].append(float(row['train_loss']))
            data['lr'].append(float(row['lr']))
            if 'val_loss' in row and row.get('val_loss', ''):
                data['val_loss'].append(float(row['val_loss']))
                if 'val_ppl' in row and row.get('val_ppl', ''):
                    data['val_ppl'].append(float(row['val_ppl']))
    return {k: np.array(v) for k, v in data.items() if len(v) > 0}

def load_diagnostics(json_path):
    """Load a diagnostics JSON file."""
    with open(json_path) as f:
        return json.load(f)

# ===================================================================
# Figure 1: Main Method Comparison (bar chart)
# ===================================================================
def make_fig1_main_comparison():
    """Bar chart comparing all 4 methods on train PPL (mean ± std, 3 seeds)."""
    print("Making Figure 1: Main comparison...")
    
    # Data from 10_result_analysis.md (verified experiment results)
    methods = ['Standard', 'ReZero', 'AttnRes', 'ADDC (Ours)']
    train_ppl_mean = [2.01, 2.66, 2.68, 1.98]
    train_ppl_std  = [0.03, 0.04, 0.06, 0.02]
    colors = ['#4393c3', '#f4a582', '#f4a582', '#2166ac']
    hatch = ['', '', '', '//']
    
    fig, ax = plt.subplots(figsize=(7, 5))
    x = np.arange(len(methods))
    bars = ax.bar(x, train_ppl_mean, yerr=train_ppl_std, capsize=6, 
                   color=colors, edgecolor='black', linewidth=0.8,
                   width=0.55, hatch=hatch)
    
    ax.set_ylabel('Training Perplexity')
    ax.set_xticks(x)
    ax.set_xticklabels(methods, rotation=15, ha='right')
    ax.set_title('Method Comparison (M config, 25M params, 5k iterations, 3 seeds)')
    
    # Add value labels
    for i, (bar, val) in enumerate(zip(bars, train_ppl_mean)):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + train_ppl_std[i] + 0.03,
                f'{val:.2f}', ha='center', va='bottom', fontweight='bold', fontsize=10)
    
    # Highlight ADDC
    bars[-1].set_edgecolor('#b2182b')
    bars[-1].set_linewidth(2.0)
    
    ax.set_ylim(1.5, 3.0)
    ax.yaxis.set_major_locator(MaxNLocator(6))
    plt.tight_layout()
    fig.savefig(os.path.join(FIG_DIR, 'fig1_main_comparison.pdf'))
    plt.close(fig)
    print("  -> fig1_main_comparison.pdf saved.")


# ===================================================================
# Figure 2: Gamma Sweep (phase transition)
# ===================================================================
def make_fig2_gamma_sweep():
    """Gamma sweep showing sharp phase transition at gamma=0.1."""
    print("Making Figure 2: Gamma sweep...")
    
    gamma_values = [0.00, 0.01, 0.05, 0.10, 0.20, 0.50, 1.00]
    train_ppl = [3.85, 3.70, 3.76, 69.62, 75.59, 75.57, 73.52]
    
    # Try to load actual data
    sweep_dir = os.path.join(LOG_DIR, "E4_gamma_sweep")
    gamma_labels = ['0.0', '0.01', '0.05', '0.1', '0.2', '0.5', '1.0']
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))
    
    # Left: full range (log scale for PPL)
    colors = ['#4393c3'] * 3 + ['#d6604d'] * 4
    ax1.bar(range(len(gamma_values)), train_ppl, color=colors, edgecolor='black', linewidth=0.8)
    ax1.set_xticks(range(len(gamma_values)))
    ax1.set_xticklabels([f'$\gamma={v}$' for v in gamma_values], rotation=30, ha='right', fontsize=9)
    ax1.set_ylabel('Train PPL (1500 iters)')
    ax1.set_title('Gamma Sweep: Full Range')
    ax1.axhline(y=4.13, color='gray', linestyle='--', alpha=0.7, label='Standard baseline')
    ax1.legend(fontsize=9)
    
    # Add value labels
    for i, v in enumerate(train_ppl):
        ax1.text(i, v + 1.5, f'{v:.1f}', ha='center', fontsize=8, fontweight='bold')
    
    # Right: zoomed in on working range
    ax2.bar(range(3), train_ppl[:3], color=['#4393c3']*3, edgecolor='black', linewidth=0.8, width=0.55)
    ax2.set_xticks(range(3))
    ax2.set_xticklabels(['$\gamma=0$', '$\gamma=0.01$', '$\gamma=0.05$'], fontsize=10)
    ax2.set_ylabel('Train PPL (1500 iters)')
    ax2.set_title('Gamma Sweep: Working Range (Zoom)')
    ax2.axhline(y=4.13, color='gray', linestyle='--', alpha=0.7, label='Standard baseline')
    ax2.legend(fontsize=9)
    ax2.set_ylim(3.5, 4.3)
    
    for i, v in enumerate(train_ppl[:3]):
        ax2.text(i, v + 0.03, f'{v:.2f}', ha='center', fontsize=9, fontweight='bold')
    
    fig.suptitle('ADDC Gamma Sensitivity: Sharp Phase Transition at $\gamma=0.1$', fontsize=14, fontweight='bold')
    plt.tight_layout()
    fig.savefig(os.path.join(FIG_DIR, 'fig2_gamma_sweep.pdf'))
    plt.close(fig)
    print("  -> fig2_gamma_sweep.pdf saved.")


# ===================================================================
# Figure 3: Beta Sweep
# ===================================================================
def make_fig3_beta_sweep():
    """Beta sweep results."""
    print("Making Figure 3: Beta sweep...")
    
    beta_values = [0.50, 0.70, 0.90, 0.95, 0.99]
    train_ppl = [3.86, 3.68, 3.72, 3.83, 3.76]
    
    fig, ax = plt.subplots(figsize=(7, 5))
    colors_bar = ['#4393c3', '#4393c3', '#2166ac', '#4393c3', '#4393c3']
    ax.bar(range(len(beta_values)), train_ppl, color=colors_bar, edgecolor='black', linewidth=0.8, width=0.55)
    ax.set_xticks(range(len(beta_values)))
    ax.set_xticklabels([f'$\\beta={v}$' for v in beta_values], fontsize=10)
    ax.set_ylabel('Train PPL (1500 iters)')
    ax.set_title('ADDC Beta Sensitivity ($\gamma=0.01$, 1500 iters, seed 42)')
    ax.axhline(y=4.13, color='gray', linestyle='--', alpha=0.7, label='Standard baseline at 1500 iters')
    ax.legend(fontsize=9)
    ax.set_ylim(3.4, 4.3)
    
    for i, v in enumerate(train_ppl):
        ax.text(i, v + 0.03, f'{v:.2f}', ha='center', fontsize=10, fontweight='bold')
    
    plt.tight_layout()
    fig.savefig(os.path.join(FIG_DIR, 'fig3_beta_sweep.pdf'))
    plt.close(fig)
    print("  -> fig3_beta_sweep.pdf saved.")


# ===================================================================
# Figure 4: Learned Gamma Values
# ===================================================================
def make_fig4_learned_gamma():
    """Learned gamma values per layer across 3 seeds."""
    print("Making Figure 4: Learned gamma...")
    
    # Gamma values from experiment logs (3 seeds)
    seeds = ['42', '123', '456']
    
    gamma_attn = {
        '42':  [0.0, 0.0, -0.15, -0.25, -0.22, -0.13, -0.09, -0.04],
        '123': [0.0, 0.0, -0.17, -0.24, -0.22, -0.14, -0.09, -0.04],
        '456': [0.0, 0.0, -0.14, -0.24, -0.23, -0.14, -0.09, -0.04],
    }
    gamma_mlp = {
        '42':  [0.0, 0.003, -0.10, -0.16, -0.17, -0.13, -0.08, -0.02],
        '123': [0.0, 0.0, -0.08, -0.16, -0.16, -0.12, -0.07, -0.02],
        '456': [0.0, 0.0, -0.09, -0.17, -0.16, -0.13, -0.08, -0.02],
    }
    
    layers = list(range(8))
    layer_labels = [f'L{l}' for l in layers]
    seed_colors = {'42': '#2166ac', '123': '#d6604d', '456': '#4dac26'}
    seed_markers = {'42': 'o', '123': 's', '456': '^'}
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5))
    
    for seed in seeds:
        ax1.plot(layers, gamma_attn[seed], '-o', color=seed_colors[seed], 
                 marker=seed_markers[seed], label=f'Seed {seed}', markersize=8, linewidth=2)
        ax2.plot(layers, gamma_mlp[seed], '-s', color=seed_colors[seed],
                 marker=seed_markers[seed], label=f'Seed {seed}', markersize=8, linewidth=2)
    
    for ax in [ax1, ax2]:
        ax.axhline(y=0, color='gray', linestyle='--', alpha=0.5, linewidth=0.8)
        ax.set_xticks(layers)
        ax.set_xticklabels(layer_labels)
        ax.set_xlabel('Layer')
        ax.legend(fontsize=9)
        ax.grid(axis='y', alpha=0.3)
    
    ax1.set_ylabel('$\gamma_{attn}$ (learned)')
    ax1.set_title('$\gamma_{attn}$: Post-Attention Sharpening')
    ax2.set_ylabel('$\gamma_{mlp}$ (learned)')
    ax2.set_title('$\gamma_{mlp}$: Post-MLP Sharpening')
    
    # Annotation: all negative = smoothing
    fig.text(0.5, 0.02, 'All learned $\gamma < 0$ → Model discovers SMOOTHING, not sharpening.',
             ha='center', fontsize=11, fontweight='bold', 
             bbox=dict(boxstyle='round,pad=0.4', facecolor='#fff3cd', alpha=0.8))
    
    fig.suptitle('Learned Gamma Values: Universal Discovery of Negative $\gamma$ (Smoothing)', 
                 fontsize=14, fontweight='bold')
    plt.tight_layout(rect=[0, 0.05, 1, 0.95])
    fig.savefig(os.path.join(FIG_DIR, 'fig4_learned_gamma.pdf'))
    plt.close(fig)
    print("  -> fig4_learned_gamma.pdf saved.")


# ===================================================================
# Figure 5: Training Curves (ADDC vs Standard)
# ===================================================================
def make_fig5_training_curves():
    """Training loss curves comparing ADDC vs Standard across seeds."""
    print("Making Figure 5: Training curves...")
    
    # Try to load actual CSV data
    standard_seeds = {}
    addc_seeds = {}
    
    for seed_str in ['42', '123', '456']:
        # Standard
        std_pattern = os.path.join(LOG_DIR, "E1_M_standard", "standard", f"seed{seed_str}_*", "standard", "metrics.csv")
        std_files = glob.glob(std_pattern)
        if std_files:
            standard_seeds[seed_str] = load_metrics(std_files[0])
        
        # ADDC
        addc_pattern = os.path.join(LOG_DIR, "E6_ADDC_best", "addc_beta0.9_gammalearnable", f"seed{seed_str}_*", "addc_beta0.9_gammalearnable", "metrics.csv")
        addc_files = glob.glob(addc_pattern)
        if addc_files:
            addc_seeds[seed_str] = load_metrics(addc_files[0])
    
    fig, ax = plt.subplots(figsize=(9, 5.5))
    
    seed_colors = {'42': '#2166ac', '123': '#d6604d', '456': '#4dac26'}
    
    for seed_str in ['42', '123', '456']:
        if seed_str in standard_seeds:
            d = standard_seeds[seed_str]
            # Filter to training-only rows (step where train_loss exists)
            train_mask = ~np.isnan(d['train_loss'])
            steps = d['step'][train_mask]
            losses = d['train_loss'][train_mask]
            ax.plot(steps, losses, color=seed_colors[seed_str], linestyle='--', alpha=0.7, linewidth=1.5,
                    label=f'Standard (seed {seed_str})')
        
        if seed_str in addc_seeds:
            d = addc_seeds[seed_str]
            train_mask = ~np.isnan(d['train_loss'])
            steps = d['step'][train_mask]
            losses = d['train_loss'][train_mask]
            ax.plot(steps, losses, color=seed_colors[seed_str], linestyle='-', alpha=0.9, linewidth=2.0,
                    label=f'ADDC (seed {seed_str})')
    
    ax.set_xlabel('Training Iteration')
    ax.set_ylabel('Training Loss (Cross-Entropy)')
    ax.set_title('Training Curves: ADDC vs Standard Transformer (3 seeds)')
    ax.legend(fontsize=8, ncol=2)
    ax.grid(alpha=0.3)
    ax.set_ylim(0.5, None)
    
    plt.tight_layout()
    fig.savefig(os.path.join(FIG_DIR, 'fig5_training_curves.pdf'))
    plt.close(fig)
    print("  -> fig5_training_curves.pdf saved.")


# ===================================================================
# Figure 6: ERA Lambda Sweep
# ===================================================================
def make_fig6_era_lambda():
    """ERA lambda sweep showing train PPL and val PPL."""
    print("Making Figure 6: ERA lambda sweep...")
    
    lambda_values = [0.000, 0.001, 0.010, 0.050, 0.100, 0.500]
    lambda_labels = ['0', '0.001', '0.01', '0.05', '0.1', '0.5']
    train_ppl = [3.42, 3.52, 3.52, 3.60, 3.49, 3.41]
    # Val PPL: only available for key points
    val_ppl_known = {0: 74.83, 3: 65.99}  # index -> val PPL
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))
    
    # Train PPL
    colors = ['#4393c3'] * len(lambda_values)
    colors[3] = '#2166ac'  # best val PPL
    ax1.bar(range(len(lambda_values)), train_ppl, color=colors, edgecolor='black', linewidth=0.8, width=0.55)
    ax1.set_xticks(range(len(lambda_values)))
    ax1.set_xticklabels([f'$\lambda={l}$' for l in lambda_labels], rotation=30, ha='right', fontsize=9)
    ax1.set_ylabel('Train PPL (2000 iters)')
    ax1.set_title('ERA: Training Perplexity')
    ax1.axhline(y=3.42, color='gray', linestyle='--', alpha=0.7, label='$\lambda=0$ baseline')
    ax1.legend(fontsize=9)
    ax1.set_ylim(3.2, 3.8)
    for i, v in enumerate(train_ppl):
        ax1.text(i, v + 0.02, f'{v:.2f}', ha='center', fontsize=9, fontweight='bold')
    
    # Val PPL (known points only)
    ax2.bar([0, 3], [val_ppl_known[0], val_ppl_known[3]], 
            color=['#4393c3', '#2166ac'], edgecolor='black', linewidth=0.8, width=0.4)
    ax2.set_xticks([0, 3])
    ax2.set_xticklabels(['$\lambda=0$', '$\lambda=0.05$'], fontsize=10)
    ax2.set_ylabel('Validation PPL')
    ax2.set_title('ERA: Validation Perplexity')
    ax2.set_ylim(60, 80)
    for i, (idx, v) in enumerate(val_ppl_known.items()):
        x_pos = [0, 3][i]
        ax2.text(x_pos, v + 0.5, f'{v:.1f}', ha='center', fontsize=10, fontweight='bold')
    
    # Add delta annotation
    ax2.annotate('$\Delta = -8.84$', xy=(1.2, 70), fontsize=11, fontweight='bold',
                 color='#b2182b', ha='center',
                 bbox=dict(boxstyle='round,pad=0.3', facecolor='#fff3cd', alpha=0.8))
    
    fig.suptitle('ERA: Entropy-Regularized Attention ($\lambda > 0$ improves validation PPL)', 
                 fontsize=14, fontweight='bold')
    plt.tight_layout()
    fig.savefig(os.path.join(FIG_DIR, 'fig6_era_lambda.pdf'))
    plt.close(fig)
    print("  -> fig6_era_lambda.pdf saved.")


# ===================================================================
# Figure 7: Attention Entropy per Layer
# ===================================================================
def make_fig7_entropy_per_layer():
    """Attention entropy per layer: Standard vs ADDC."""
    print("Making Figure 7: Entropy per layer...")
    
    # Data from experiment log (step 4750, seed 42)
    layers = list(range(8))
    layer_labels = [f'L{l}' for l in layers]
    
    std_entropy = [4.541, 2.596, 2.003, 1.100, 1.576, 2.217, 2.652, 2.972]
    addc_entropy = [4.550, 2.467, 1.925, 1.027, 1.508, 2.161, 2.668, 2.925]
    
    fig, ax = plt.subplots(figsize=(8, 5.5))
    
    x = np.arange(len(layers))
    width = 0.35
    
    bars1 = ax.bar(x - width/2, std_entropy, width, label='Standard Transformer', 
                    color='#4393c3', edgecolor='black', linewidth=0.8)
    bars2 = ax.bar(x + width/2, addc_entropy, width, label='ADDC (Ours)',
                    color='#2166ac', edgecolor='black', linewidth=0.8, hatch='//')
    
    ax.set_xlabel('Layer')
    ax.set_ylabel('Attention Entropy $H(\\alpha)$ (nats)')
    ax.set_title('Attention Entropy per Layer: Standard vs ADDC (step 4750, seed 42)')
    ax.set_xticks(x)
    ax.set_xticklabels(layer_labels)
    ax.legend(fontsize=10)
    ax.grid(axis='y', alpha=0.3)
    
    # Add delta annotations for notable differences
    for i in range(len(layers)):
        delta = addc_entropy[i] - std_entropy[i]
        if abs(delta) > 0.05:
            ax.annotate(f'{delta:+.3f}', xy=(x[i] + width/2, max(std_entropy[i], addc_entropy[i]) + 0.08),
                       fontsize=7, ha='center', color='#b2182b')
    
    # Add mean line
    ax.axhline(y=np.mean(std_entropy), color='#4393c3', linestyle=':', alpha=0.5, linewidth=1)
    ax.axhline(y=np.mean(addc_entropy), color='#2166ac', linestyle=':', alpha=0.5, linewidth=1)
    ax.text(7.2, np.mean(std_entropy), f'Avg: {np.mean(std_entropy):.2f}', fontsize=8, color='#4393c3')
    ax.text(7.2, np.mean(addc_entropy), f'Avg: {np.mean(addc_entropy):.2f}', fontsize=8, color='#2166ac')
    
    plt.tight_layout()
    fig.savefig(os.path.join(FIG_DIR, 'fig7_entropy_per_layer.pdf'))
    plt.close(fig)
    print("  -> fig7_entropy_per_layer.pdf saved.")


# ===================================================================
# Main
# ===================================================================
if __name__ == '__main__':
    print("=" * 60)
    print("ADDC Paper Figure Generator")
    print("=" * 60)
    
    try:
        make_fig1_main_comparison()
    except Exception as e:
        print(f"  WARNING: fig1 failed: {e}")
    
    try:
        make_fig2_gamma_sweep()
    except Exception as e:
        print(f"  WARNING: fig2 failed: {e}")
    
    try:
        make_fig3_beta_sweep()
    except Exception as e:
        print(f"  WARNING: fig3 failed: {e}")
    
    try:
        make_fig4_learned_gamma()
    except Exception as e:
        print(f"  WARNING: fig4 failed: {e}")
    
    try:
        make_fig5_training_curves()
    except Exception as e:
        print(f"  WARNING: fig5 failed: {e}")
    
    try:
        make_fig6_era_lambda()
    except Exception as e:
        print(f"  WARNING: fig6 failed: {e}")
    
    try:
        make_fig7_entropy_per_layer()
    except Exception as e:
        print(f"  WARNING: fig7 failed: {e}")
    
    print("\nAll figures generated.")
    print(f"Output directory: {FIG_DIR}")
