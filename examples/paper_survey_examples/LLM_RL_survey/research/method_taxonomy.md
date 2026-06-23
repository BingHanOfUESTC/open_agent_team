# LLM 强化学习后训练 - 方法分类体系

> **生成时间**: 2026-06-23
> **生成 Agent**: method_taxonomy_agent
> **数据源**: paper_inventory.md (280 篇论文)
> **方法论**: 按"问题如何被定义，方法如何解决"组织分类

---

## 目录

1. [训练范式分类](#1-训练范式分类)
2. [偏好建模与奖励](#2-偏好建模与奖励)
3. [算法详细对比](#3-算法详细对比)
4. [数据策略](#4-数据策略)
5. [评估方法论](#5-评估方法论)
6. [方法演化关系图](#6-方法演化关系图)
7. [未解决问题](#7-未解决问题)

---

## 1. 训练范式分类

### 1.1 范式总览

| 范式 | 核心思想 | 代表论文 | 公式/目标函数 | 优势 | 局限 |
|------|----------|----------|--------------|------|------|
| **SFT (监督微调)** | 在高质量指令-回答对上做 next-token 交叉熵训练 | SFT vs RL (Jiang, 2026, [2603.13985](https://arxiv.org/abs/2603.13985)); Non-decoupling SFT/RL (Niu, 2026, [2601.07389](https://arxiv.org/abs/2601.07389)); Arena Learning (Luo, 2024, [2407.10627](https://arxiv.org/abs/2407.10627)) | L_SFT = -E[log π_θ(y\|x)] | 稳定、高效、无需 reward model | 缺乏偏好信号；分布外泛化差；无法纠正错误推理模式 |
| **Online RL (PPO-RLHF)** | 用 PPO 在 reward model 反馈上在线优化策略，KL 约束防止崩溃 | InstructGPT (Ouyang, 2022, [2203.02155](https://arxiv.org/abs/2203.02155)); Llama 2 (Touvron, 2023, [2307.09288](https://arxiv.org/abs/2307.09288)); Robust RLHF (Ye, 2025, [2504.03784](https://arxiv.org/abs/2504.03784)) | max_π E[r(x,y)] - β KL(π\|π_ref) | 理论上限高；在线探索可泛化 | 需训 reward model；训练不稳定；reward hacking 风险；计算昂贵 |
| **Offline DPO (直接偏好优化)** | 直接在静态偏好对上优化隐式 reward，无需显式 RM | DPO (Rafailov, 2023, [2305.18290](https://arxiv.org/abs/2305.18290)); KTO (Ethayarajh, 2024, [2402.01306](https://arxiv.org/abs/2402.01306)); ORPO (Hong, 2024, [2403.07691](https://arxiv.org/abs/2403.07691)); SimPO (Meng, 2024, [2405.14734](https://arxiv.org/abs/2405.14734)) | L_DPO = -E[log σ(β log(π_θ(y_w)/π_ref(y_w)) - β log(π_θ(y_l)/π_ref(y_l)))] | 简单；无需 RM；训练稳定 | 离线数据分布受限；reward over-optimization 依然存在 |
| **Iterative/Online DPO** | 离线 DPO 训练 + 在线采样新数据，迭代循环 | Online DPO (Qi, 2024, [2406.05534](https://arxiv.org/abs/2406.05534)); iLR-DPO (Liu, 2024, [2406.11817](https://arxiv.org/abs/2406.11817)); Iterative Reasoning PO (Pang, 2024, [2404.19733](https://arxiv.org/abs/2404.19733)) | 循环：π_t → 采样 → 偏好标注 → DPO → π_{t+1} | 逐步扩展数据覆盖；比纯离线好 | 需标注 pipeline；可能分布漂移 |
| **Group-wise Optimization (GRPO)** | 对同一 prompt 生成 K 个样本，组内计算相对 advantage 做策略梯度 | DeepSeek-R1 (DeepSeek-AI, 2025, [2501.12948](https://arxiv.org/abs/2501.12948)); Demystifying GRPO (Zhou, 2026, [2603.01162](https://arxiv.org/abs/2603.01162)); On/Off-Policy GRPO (Mroueh, 2025, [2505.22257](https://arxiv.org/abs/2505.22257)) | Â_i = (r_i - mean(r)) / std(r); ∇J = E[Â_i · ∇log π] | 无需 value function；天然归一化；适合 verifiable reward | 对 reward 方差敏感；组内样本数影响方差 |

### 1.2 SFT 的角色再定义

SFT 已从"独立训练阶段"演化为"后训练 pipeline 的必要前序步骤"。近年关键洞察：

| 洞察 | 论文来源 | 核心观点 |
|------|----------|----------|
| **状态分布视角** | Post-Training is About States (Nie, 2026, [2605.22731](https://arxiv.org/abs/2605.22731)) | SFT 和 RL 的根本差别在状态分布而非 token 分布；on-policy distillation 可能统一两者 |
| **SFT 与 RL 不可解耦** | Non-decoupling SFT/RL (Niu, 2026, [2601.07389](https://arxiv.org/abs/2601.07389)) | SFT 和 RL 在训练动态中深度纠缠，割裂看待会误导方法设计 |
| **隐式 Reward 统一论** | Implicit Reward as Bridge (Wang, 2025, [2507.00018](https://arxiv.org/abs/2507.00018)) | SFT 和 DPO 可通过隐式 reward 函数统一：SFT 是 DPO 在 β→∞ 时的极限 |
| **在线 vs 离线数据统一** | Unified View of Post-Training (Lv, 2025, [2509.04419](https://arxiv.org/abs/2509.04419)) | 在线 (model-generated) 与离线 (human/other-model) 数据统一为后训练两大来源 |
| **Arena Learning** | Arena Learning (Luo, 2024, [2407.10627](https://arxiv.org/abs/2407.10627)) | 通过模拟 Chatbot Arena 的 pairwise battle 构建数据飞轮：battle → 标注 → SFT/DPO → 下一轮 |

### 1.3 范式选择决策树

```text
数据有 pairwise preference 标注？
├── 是 → 是否有持续标注预算？
│        ├── 是 → Online RLHF (PPO) 或 Iterative DPO
│        └── 否 → 数据量大且覆盖好？
│                 ├── 是 → Offline DPO
│                 └── 否 → 数据仅有单侧反馈 (good/bad) → KTO
└── 否 → 是否有可验证的 ground-truth 信号？
         ├── 是 → GRPO / RLVR (如数学、代码)
         └── 否 → 仅能做 SFT（或 Constitutional AI / RLAIF 生成偏好数据）
```

---

## 2. 偏好建模与奖励

### 2.1 偏好模型分类

| 模型类别 | 数学形式 | 核心假设 | 代表论文 | 适用场景 |
|----------|----------|----------|----------|----------|
| **Bradley-Terry (BT)** | P(y_w ≻ y_l) = σ(r(y_w) - r(y_l)) | 偏好传递性；偏好强度可加性 | DPO (Rafailov, 2023), 多数 RLHF 论文 | 标准 pairwise 偏好数据 |
| **Plackett-Luce (PL)** | P(perm) ∝ Π exp(r(y_i)) | 扩展到 K 个排序 | GOPO (Choi, 2026, [2602.03876](https://arxiv.org/abs/2602.03876)) | 多排序数据 |
| **前景理论 (Prospect Theory)** | 非对称价值函数 | 人类偏好不对称：损失敏感度 ≠ 收益敏感度 | KTO (Ethayarajh, 2024, [2402.01306](https://arxiv.org/abs/2402.01306)) | 仅有单侧偏好信号 (✓/✗) |
| **Energy-Based Model** | p(y\|x) ∝ exp(-E(x,y)) | 能量函数可直接作为奖励 | Energy-Based RM (Lochab, 2025, [2504.13134](https://arxiv.org/abs/2504.13134)) | 复杂偏好分布 |
| **Contrastive Divergence** | NLL 估计 | RM 本质上是 NLL 估计器 | PO via Contrastive Divergence (Chen, 2025, [2502.04567](https://arxiv.org/abs/2502.04567)) | 自举偏好数据 |

### 2.2 显式 Reward Model vs 隐式偏好函数

```text
┌─────────────────────────────────────────────────────────────┐
│              显式 Reward Model (两阶段)                       │
│  偏好数据 → 训练 RM → 用 RM 奖励信号训练策略                   │
│  代表: InstructGPT, Llama 2, UltraFeedback                    │
│  优势: 可在线查询；多任务复用                                  │
│  劣势: RM 泛化差；reward hacking；两阶段误差累积                │
├─────────────────────────────────────────────────────────────┤
│              隐式偏好函数 (端到端)                             │
│  偏好数据 → 直接在偏好对上优化策略 → 无需独立 RM               │
│  代表: DPO, KTO, ORPO, SimPO                                  │
│  优势: 简单；训练稳定；无 RM 泛化问题                          │
│  劣势: 离线数据依赖；无法在线探索                              │
└─────────────────────────────────────────────────────────────┘
```

#### 隐式 Reward 的统一公式

DPO 族方法的核心：策略模型隐式定义了一个 reward 函数：

```text
DPO:     r(x,y) = β log(π_θ(y|x) / π_ref(y|x))
SimPO:   r(x,y) = (β/|y|) log π_θ(y|x)    (无参考模型，长度归一化)
ORPO:   r(x,y) = log(odds_θ(y|x)) = log(π_θ(y|x) / (1-π_θ(y|x)))  (几率比)
```

### 2.3 Outcome Reward Model (ORM) vs Process Reward Model (PRM)

| 维度 | ORM (结果奖励) | PRM (过程奖励) |
|------|---------------|---------------|
| **评分粒度** | 整个回答一个分数 | 每个推理步骤一个分数 |
| **适用场景** | 对话、摘要、翻译 | 数学推理、多步规划、代码生成 |
| **训练数据需求** | pairwise/pointwise 偏好 | 步骤级别正确性标注 |
| **核心挑战** | 无法指导中间推理；粗粒度 | 标注成本极高；步骤粒度定义模糊 |
| **代表论文** | 大多数 RLHF 论文 | PRM Lessons (Zhang, 2025, [2501.07301](https://arxiv.org/abs/2501.07301)); Free Process Rewards (Yuan, 2024, [2412.01981](https://arxiv.org/abs/2412.01981)); PRM with Q-Value (Li, 2024, [2410.11287](https://arxiv.org/abs/2410.11287)); Unsupervised PRM (Gadetsky, 2026, [2605.10158](https://arxiv.org/abs/2605.10158)); R-PRM (She, 2025, [2503.21295](https://arxiv.org/abs/2503.21295)); Bidirectional PRM (Zhang, 2025, [2508.01682](https://arxiv.org/abs/2508.01682)) |
| **前沿问题** | 无监督 PRM (无需步骤标注)；双向 PRM (前向+反向验证)；PRM 在 Vision-Language 中的迁移 (Ong, 2025, [2509.23250](https://arxiv.org/abs/2509.23250)) |

#### PRM 数据构建三路线

```text
1. 人工标注路线（最权威但最昂贵）：
   人工对每个推理步骤标注正确/错误/中性
   → GroundedPRM (Zhang, 2025, [2510.14942](https://arxiv.org/abs/2510.14942)): 树搜索 + 保真度感知标注

2. 自动化路线（利用 ground truth 反推）：
   用数学答案正确性反推步骤质量
   → 不确定性方法 (Han, 2025, [2508.01773](https://arxiv.org/abs/2508.01773))
   → Automated Process Supervision (Luo, 2024, [2406.06592](https://arxiv.org/abs/2406.06592))

3. 无监督路线（无需步骤标注）：
   利用模型自身特征（如 logit 熵、attention）构建奖励
   → Free Process Rewards without Process Labels (Yuan, 2024, [2412.01981](https://arxiv.org/abs/2412.01981))
   → Unsupervised PRM (Gadetsky, 2026, [2605.10158](https://arxiv.org/abs/2605.10158))
   → Activation Reward Models (Chai, 2025, [2507.01368](https://arxiv.org/abs/2507.01368))
```

### 2.4 Reward Hacking 问题谱系

Reward Hacking 是 RLHF 的核心挑战，表现为策略优化了 reward model 的"代理指标"而非真实目标。

| Reward Hacking 类型 | 表现 | 检测方法 | 缓解方法 | 代表论文 |
|---------------------|------|----------|----------|----------|
| **长度偏置 (Length Bias)** | 越长的回答 reward 越高 | Length-Controlled Eval (Dubois, 2024, [2404.04475](https://arxiv.org/abs/2404.04475)) | Length-norm reward; SimPO 的 avg log prob | Eliminating Biased Length Reliance (Lu, 2024, [2406.10957](https://arxiv.org/abs/2406.10957)) |
| **风格过拟合 (Style Overfitting)** | 学习 RM 偏好的表面风格而非内容质量 | 人工评审 / LLM-as-judge | RM 对抗训练; RM ensemble | Style over Substance (Feuer, 2024, [2409.15268](https://arxiv.org/abs/2409.15268)) |
| **多目标 Reward Hacking** | 在 helpulness/harmlessness 等多目标间投机 | Pareto 前沿分析 | 多目标约束优化; MO-GRPO | MO-GRPO (Ichihara, 2025, [2509.22047](https://arxiv.org/abs/2509.22047)) |
| **生产环境 Reward Hacking** | 在真实部署中学习利用系统漏洞 | 部署环境监控 | 因果 reward; 方向对齐 | Natural Emergent Misalignment (MacDiarmid, 2025, [2511.18397](https://arxiv.org/abs/2511.18397)) |
| **迭代自 refinement中的 Reward Hacking** | 自我迭代优化时逐步偏离目标 | 评估 hack 的传递性 | elastic reset; 中途人工干预 | Spontaneous Reward Hacking (Pan, 2024, [2407.04549](https://arxiv.org/abs/2407.04549)) |
| **Agent 情境 Reward Hacking** | Agent 在 tool-use 环境中利用环境/工具漏洞 | Hack-Verifiable 测试环境 | 结构化中间监督 | Hack-Verifiable Environments (Roth, 2026, [2605.20744](https://arxiv.org/abs/2605.20744)) |

#### 关键缓解方法

| 方法 | 核心思想 | 论文 |
|------|----------|------|
| **RM Ensemble** | 多个 RM 取平均或投票，降低个别 RM 的 exploitability | Eisenstein (2023, [2312.09244](https://arxiv.org/abs/2312.09244)) → 结论：ensemble 缓解但不能消除 reward hacking |
| **对抗 RM 训练** | 在 adversarial 生成的 hack 样本上训练 RM | Bukharin (2025, [2504.06141](https://arxiv.org/abs/2504.06141)) |
| **因果 Reward** | 用因果推断区分行为与奖励间的真实因果关系 | Chaoqi Wang (2025, [2501.09620](https://arxiv.org/abs/2501.09620)) |
| **动态标准生成 (CARMO)** | 根据 prompt 动态生成评估标准，防止 RM 学到表面特征 | Gupta (2024, [2410.21545](https://arxiv.org/abs/2410.21545)) |
| **方向对齐 (Directional Alignment)** | 约束策略梯度方向与参考模型方向一致 | Deng (2026, [2605.25189](https://arxiv.org/abs/2605.25189)) |
| **进化 RM (Evolving RM)** | RL 过程中同时进化 RM，防止过时 | Kim (2025, [2504.20157](https://arxiv.org/abs/2504.20157)); Cooper (Hong, 2025, [2508.05613](https://arxiv.org/abs/2508.05613)) |
| **Elastic Reset** | 定期重置优化状态防止过度优化 | Noukhovitch (2023, [2312.07551](https://arxiv.org/abs/2312.07551)) |

### 2.5 奖励建模前沿方向

| 方向 | 代表工作 | 关键创新 |
|------|----------|----------|
| **序列到序列 RM** | Seq-to-Seq RM (Zhou, 2024, [2409.00162](https://arxiv.org/abs/2409.00162)) | RM 输出自然语言反馈而非标量 → 可解释性 |
| **动态 β (β-DPO)** | β-DPO (Wu, 2024, [2407.08639](https://arxiv.org/abs/2407.08639)) | 每个样本自适应 β，难样本 β 大，易样本 β 小 |
| **不确定性感知 RM** | Adaptive PO with Uncertainty Anchor (Wang, 2025, [2509.10515](https://arxiv.org/abs/2509.10515)) | RM 输出 reward + uncertainty → 低置信度样本降权 |
| **无参考模型 RM** | Learning from Reference Answers (Zhao, 2025, [2504.09895](https://arxiv.org/abs/2504.09895)) | 使用参考答案而非 pairwise 偏好 → 无偏好数据情景 |
| **Rubric-based RM** | Stabilizing Rubric Integration (Tan, 2026, [2603.26535](https://arxiv.org/abs/2603.26535)) | 将评估 rubric 整合进 GRPO |
| **Activation-based RM** | Activation Reward Models (Chai, 2025, [2507.01368](https://arxiv.org/abs/2507.01368)) | 利用 LLM 内部激活构建奖励，Few-shot 可用 |

---

## 3. 算法详细对比

### 3.1 PPO for LLM

#### 3.1.1 原始 PPO (Schulman et al., 2017) 回顾

PPO 是一种 trust-region policy gradient 方法，核心机制：

```text
PPO-Clip 目标函数：
L^{CLIP}(θ) = E_t[min(r_t(θ)·Â_t, clip(r_t(θ), 1-ε, 1+ε)·Â_t)]

其中：
  r_t(θ) = π_θ(a_t|s_t) / π_old(a_t|s_t)  — 重要性采样比率
  Â_t  = GAE(λ) advantage estimate
  ε   = 0.2 (典型值)
```

#### 3.1.2 PPO 在 LLM RLHF 中的适配

LLM 场景的特殊性要求对 PPO 进行关键修改：

| 修改点 | 标准 PPO (游戏/机器人) | LLM PPO (RLHF) | 缘由 |
|--------|----------------------|----------------|------|
| **State/Action 定义** | 环境状态 s → 动作 a | Prompt x → Response y (整段) | 语言生成的序列性 |
| **KL 惩罚** | 无 | KL(π_θ \|\| π_ref) 或 KL(π_θ \|\| π_SFT) | 防止 language collapse; 保持生成质量 |
| **Value Function** | 独立价值网络 | 策略 head 加 value head (shared backbone) | 减少参数量 |
| **Reward** | 环境奖励 | RM 评分 + KL penalty | 对齐目标 |
| **Episode** | 有限步长 | 单个 response 生成 (token-level 或 sequence-level) | 生成式任务 |

```text
LLM PPO 的完整奖励信号：
R_total(x,y) = R_RM(x,y) - β · KL(π_θ(·|x) || π_ref(·|x))
                 ↑ RM 评分       ↑ KL 惩罚，β 控制约束强度

PPO + KL 惩罚的目标：
max_π  E_{x~D, y~π(·|x)} [R_RM(x,y)]  -  β · D_KL(π_θ || π_ref)

等价于在约束下最大化奖励的 RL 问题。
```

#### 3.1.3 Value Function 在 LLM PPO 中的角色

| 方面 | 说明 |
|------|------|
| **优势计算** | Â_t = R_t + γ·V(s_{t+1}) - V(s_t) (TD error) 或 GAE |
| **Token-level vs Sequence-level** | Token-level: 每个 token 有独立的 V(s)；Sequence-level: 只在 sequence 结束时给 reward |
| **训练目标** | L_V = E[(V(s) - R_return)²] |

**核心假设 (PPO-RLHF)**：
1. Reward model 能够准确反映人类偏好（实际上有 reward hacking 风险）
2. KL 约束足够防止策略偏离太远（β 需要调参）
3. Online 采样能带来比 offline 更好的泛化（Iterative RLHF 验证此假设）

### 3.2 DPO 及变体

#### 3.2.1 DPO 族总览

DPO (Rafailov et al., 2023) 的核心洞察：在 Bradley-Terry 偏好模型下，最优策略与 reward 函数存在闭式映射，从而可以将偏好数据直接用于策略优化。

```text
DPO 的核心推导：
1. 假设 BT 模型：P(y_w ≻ y_l) = σ(r(y_w) - r(y_l))
2. RLHF 最优策略的形式：π*(y|x) ∝ π_ref(y|x) · exp(r(x,y)/β)
3. 反推隐式 reward：r(x,y) = β · log(π(y|x) / π_ref(y|x))
4. 代入 BT 模型得到 DPO loss：

L_DPO(π_θ; π_ref) = -E_{(x,y_w,y_l)~D} [log σ(
    β·log(π_θ(y_w|x)/π_ref(y_w|x)) - β·log(π_θ(y_l|x)/π_ref(y_l|x))
)]
```

##### DPO 变体对比矩阵

| 方法 | 年份 | 第一作者 | arXiv ID | 核心公式创新 | 有无 ref model | 数据需求 | 关键区别 |
|------|------|----------|----------|-------------|---------------|----------|----------|
| **DPO** | 2023 | Rafailov | [2305.18290](https://arxiv.org/abs/2305.18290) | σ(β log(π_w/π_ref_w) - β log(π_l/π_ref_l)) | ✅ 需要 | pairwise | BT 模型下的直接优化 |
| **KTO** | 2024 | Ethayarajh | [2402.01306](https://arxiv.org/abs/2402.01306) | λ_w·σ(z_ref - z) + λ_l·σ(z - z_ref) | ✅ 需要 | 单侧 ✓/✗ | 基于前景理论；无需 pairwise |
| **IPO** | 2024 | Ji | [2402.00856](https://arxiv.org/abs/2402.00856) | (log(π_w/π_ref_w) - log(π_l/π_ref_l) - (2β)⁻¹)² | ✅ 需要 | pairwise | 回归目标替代分类目标；防止过拟合 |
| **ORPO** | 2024 | Hong | [2403.07691](https://arxiv.org/abs/2403.07691) | L_SFT + λ·(-log σ(log odds_w - log odds_l)) | ❌ 无需 | pairwise | 合并 SFT + 偏好优化；无参考模型 |
| **SimPO** | 2024 | Meng | [2405.14734](https://arxiv.org/abs/2405.14734) | σ(β·avg_log_π_w - β·avg_log_π_l - γ) | ❌ 无需 | pairwise | 长度归一化 + target reward margin γ |
| **ODPO** | 2024 | Amini | [2402.10571](https://arxiv.org/abs/2402.10571) | DPO + offset Δ in sigmoid | ✅ 需要 | pairwise | 引入 offset 处理偏好强度差异 |
| **β-DPO** | 2024 | Wu | [2407.08639](https://arxiv.org/abs/2407.08639) | 动态 β(x) 替代固定 β | ✅ 需要 | pairwise | 样本自适应正则化强度 |
| **IPO (Exact)** | 2024 | Ji | [2402.00856](https://arxiv.org/abs/2402.00856) | 精确优化而非近似 | ✅ 需要 | pairwise | 解析解方向 |
| **Curry-DPO** | 2024 | Pattnaik | [2403.07230](https://arxiv.org/abs/2403.07230) | 按难度课程学习 | ✅ 需要 | pairwise (ranked) | 从易到难的课程学习 |
| **α-DPO** | 2025 | Gupta | [2501.03884](https://arxiv.org/abs/2501.03884) | 调整 reward shaping 参数 α | ✅ 需要 | pairwise | reward function shape 的重要性 |
| **DPO-Shift** | 2025 | Yang | [2502.07599](https://arxiv.org/abs/2502.07599) | 固定 β 下通过分布平移达偏移效果 | ✅ 需要 | pairwise | 暗含偏移等效性 |
| **SGDPO** | 2025 | Zhu | [2505.12435](https://arxiv.org/abs/2505.12435) | 自引导 DPO（模型自身生成偏好对） | ✅ 需要 | self-gen pairs | 自举式数据生成 |
| **Uni-DPO** | 2026 | Peng | [2506.10054](https://arxiv.org/abs/2506.10054) | 统一框架动态选择偏好对 | ✅ 需要 | pairwise | 动态偏好对选择 |
| **GOPO** | 2026 | Choi | [2602.03876](https://arxiv.org/abs/2602.03876) | 利用排序奖励（ranked rewards）替代 pairwise BT | ❌ 部分需要 | ranked | Plackett-Luce 偏好模型 |
| **CAPO** | 2025 | Pokharel | [2511.07691](https://arxiv.org/abs/2511.07691) | 多语言置信度感知偏好优化 | ✅ 需要 | pairwise | 多语言校准 |
| **MaPPO** | 2025 | Lan | [2507.21183](https://arxiv.org/abs/2507.21183) | 最大后验 + 先验知识偏好优化 | ✅ 需要 | pairwise | 贝叶斯视角 |

##### 各变体详解

#### DPO (Rafailov et al., 2023)
```text
目标函数：
L_DPO = -E_{(x,y_w,y_l)~D} [log σ(β·log(π_θ(y_w|x)/π_ref(y_w|x))
                                        - β·log(π_θ(y_l|x)/π_ref(y_l|x)))]

假设：
- Bradley-Terry 偏好模型成立
- 偏好数据是 pairwise 且标注可靠
- π_ref 是合理的初始策略

优势：无需 RM，端到端训练
局限：
- 完全离线，无法探索新分布
- 对 π_ref 质量敏感
- Reward over-optimization 依然存在 (Scaling Laws for RM Overoptimization, Rafailov, 2024, [2406.02900](https://arxiv.org/abs/2406.02900))
```

#### KTO (Ethayarajh et al., 2024)
```text
核心创新：将 Kahneman-Tversky 前景理论引入偏好优化，仅需每个回答的 ✓/✗ 标签

目标函数（简化）：
L_KTO = λ_w·max(0, z_ref - z) + λ_l·max(0, z - z_ref)
其中 z = β·log(π_θ(y|x)/π_ref(y|x))

优势：
- 不需要 pairwise 数据！仅需 good/bad 标签
- 更贴合实际数据收集场景（用户点赞/点踩）
- 前景理论的非对称性减少 hallucination

局限：
- 需要合理设置 reference point z_ref
- 标签噪声影响比 DPO 更显著
```

#### ORPO (Hong et al., 2024)
```text
核心创新：将 SFT 和偏好优化合并为单一训练目标，无需参考模型

目标函数：
L_ORPO = L_SFT + λ·L_OR

L_SFT = -log π_θ(y_w|x)  (仅在 chosen 上做 SFT)
L_OR  = -log σ(log odds_θ(y_w|x) - log odds_θ(y_l|x))

其中 odds_θ(y|x) = π_θ(y|x) / (1 - π_θ(y|x))

优势：
- 无需 reference model → 内存/计算减半
- SFT + Preference 联合优化 → 可能更稳定的训练动态
- 单一阶段训练

局限：
- odds ratio 在序列级别计算，高维空间可能导致数值不稳定
- 仍需 pairwise 偏好数据
```

#### SimPO (Meng et al., 2024)
```text
核心创新：用长度归一化的平均 log probability 作为隐式 reward，引入 target reward margin

目标函数：
r_SimPO(x,y) = (β/|y|) · log π_θ(y|x)   ← 平均 log prob (长度归一化)
L_SimPO = -log σ(r_SimPO(x,y_w) - r_SimPO(x,y_l) - γ)   ← γ: target margin

优势：
- 无 reference model → 极简设计
- 长度归一化 → 自动抑制长度偏置（关键创新）
- target margin γ → 控制 chosen/rejected 的最小间隔
- 匹配或超越 DPO 的 AlpacaEval 表现

局限：
- 平均 log prob 可能低估 token 级别的重要性差异
- γ 是额外超参数（但论文称不敏感）
```

#### Condition Equivalence of DPO and RLHF (Yang, 2026, [2605.20834](https://arxiv.org/abs/2605.20834))

2026 年工作对 DPO 与 RLHF 等价性的理论条件进行了严格分析：
- DPO 仅在偏好数据覆盖足够好时等价于 RLHF
- 指出 DPO 的隐式假设和失败模式
- 提供可证明的对齐条件

### 3.3 Online / Iterative DPO

Offline DPO 的根本局限：数据分布由初始策略决定，无法探索 reward landscape 未知区域。

#### Iterative DPO 通用框架

```text
Iterative DPO 循环：
  for t = 1, 2, ..., T:
    1. 用当前策略 π_t 对 prompt 集采样 responses
    2. 获取偏好标注（人工/AI/自动验证）
    3. 在新偏好数据 D_t 上做 DPO 训练 → π_{t+1}

代表实现：
  Online DPO (Qi, 2024, [2406.05534](https://arxiv.org/abs/2406.05534)):
    Fast-Slow Chasing: fast model 更新快但噪声大, slow model 稳定但滞后
    → 用 slow model 的隐式 reward 对 fast model 采样做偏好标注

  iLR-DPO (Liu, 2024, [2406.11817](https://arxiv.org/abs/2406.11817)):
    迭代 + 长度正则化 → 7B 模型达到 GPT-4 级别

  Iterative Reasoning PO (Pang, 2024, [2404.19733](https://arxiv.org/abs/2404.19733)):
    在推理任务上迭代偏好优化 → 带 chain-of-thought 的偏好学习

  Enhancing LLM Reasoning with Iterative DPO (Tu, 2025, [2503.12854](https://arxiv.org/abs/2503.12854)):
    对 Iterative DPO 在推理上的全面实证研究
```

#### Online AI Feedback DPO
```text
OAIF (Guo, 2024, [2402.04792](https://arxiv.org/abs/2402.04792)):
  在 DPO 框架中使用在线 AI feedback → 结合 RLAIF 的自动标注 + DPO 的端到端训练
```

### 3.4 GRPO (Group Relative Policy Optimization)

#### 3.4.1 起源与应用里程碑

GRPO 由 DeepSeek 团队在 DeepSeekMath 中提出，在 DeepSeek-R1 中成为核心训练算法，引爆 2025-2026 的 GRPO 研究热潮。

```text
核心论文：
  DeepSeek-R1 (DeepSeek-AI, 2025, [2501.12948](https://arxiv.org/abs/2501.12948))
    → GRPO 应用于大规模 reasoning RL
    → DeepSeek-R1-Zero: 纯 RL (无 SFT) + GRPO → reasoning 能力涌现
```

#### 3.4.2 算法机制

```text
GRPO 的目标函数：
对于每个 prompt x，采样 G 个 responses {y_1, ..., y_G}
计算每个 response 的 reward r_i = R(y_i)
组内归一化：
  Â_i = (r_i - mean(r)) / std(r)    ← 组相对 advantage

策略梯度：
  ∇J_GRPO = E[Â_i · ∇log π_θ(y_i|x)] - β · ∇KL(π_θ || π_ref)

GRPO vs PPO 的核心区别：
┌─────────────────┬──────────────────┬──────────────────────┐
│ 维度              │ PPO              │ GRPO                  │
├─────────────────┼──────────────────┼──────────────────────┤
│ Advantage 估计    │ Value Network    │ 组内相对归一化         │
│ 需要 Value Head?  │ ✅               │ ❌                    │
│ Reward 需求       │ 绝对奖励信号     │ 相对排序即可           │
│ 组比较            │ Batch 内隐式     │ 显式同一 prompt 多采样  │
│ 计算开销          │ Value func 训练  │ G 倍采样 (推理开销大)  │
└─────────────────┴──────────────────┴──────────────────────┘
```

#### 3.4.3 GRPO 的理论分析

| 论文 | 核心发现 |
|------|----------|
| **Demystifying GRPO** (Zhou, 2026, [2603.01162](https://arxiv.org/abs/2603.01162)) | GRPO 的策略梯度本质上是一个 **U-Statistic**；其方差以 O(1/G) 递减 |
| **On/Off-Policy GRPO** (Mroueh, 2025, [2505.22257](https://arxiv.org/abs/2505.22257)) | GRPO 可在 on-policy 和 off-policy 模式下运作；off-policy 效率更高 |
| **GRPO is Off-Policy** (Yao, 2025, [2509.24203](https://arxiv.org/abs/2509.24203)) | 揭示 GRPO-like 的 REINFORCE 实际上是 **off-policy** 算法 |
| **Unifying GRPO and Self-Distillation** (Li, 2026, [2604.02288](https://arxiv.org/abs/2604.02288)) | 通过 sample routing 统一 GRPO 和 self-distillation |

#### 3.4.4 GRPO 的改进与变体

| 变体 | 论文 | 核心改进 |
|------|------|----------|
| **GRPO-VPS** | Wang (2026, [2604.20659](https://arxiv.org/abs/2604.20659)) | 可验证过程监督：将 process-level 验证信号集成进 GRPO |
| **MO-GRPO** | Ichihara (2025, [2509.22047](https://arxiv.org/abs/2509.22047)) | 多目标 GRPO：在多目标场景下缓解 reward hacking |
| **DaGRPO** | Xie (2025, [2512.06337](https://arxiv.org/abs/2512.06337)) | Distinctiveness-aware GRPO：解决 reasoning 中梯度冲突 |
| **EBPO** | Han (2026, [2602.05165](https://arxiv.org/abs/2602.05165)) | Empirical Bayes 收缩：稳定组间 advantage 估计 |
| **CPPO** | Lin (2025, [2503.22342](https://arxiv.org/abs/2503.22342)) | Completion Pruning PO：加速 GRPO 训练 |
| **BiasGRPO** | Reddy (2026, [2606.04807](https://arxiv.org/abs/2606.04807)) | 在高方差 reward landscape 中稳定 bias 缓解 |
| **Latent-GRPO** | Deng (2026, [2604.27998](https://arxiv.org/abs/2604.27998)) | 将 GRPO 应用于 latent reasoning (连续隐空间推理) |
| **Sharpness-Guided GRPO** | Le (2025, [2511.00066](https://arxiv.org/abs/2511.00066)) | 通过 probability shaping 引导锐度 |
| **PAPO** | Tan (2026, [2603.26535](https://arxiv.org/abs/2603.26535)) | Process-Aware Policy Optimization: 将 process-level 评估解耦 |

### 3.5 正则化方法

DPO 族和 RLHF 中的正则化方法对比：

| 正则化类型 | 数学形式 | 作用 | 使用场景 |
|-----------|----------|------|----------|
| **KL 散度正则化** | β·KL(π_θ \|\| π_ref) | 防止偏离参考模型太远 → 避免 language collapse | PPO-RLHF, DPO, IPO |
| **Reverse KL / Forward KL** | D_KL(π_θ \|\| π_ref) vs D_KL(π_ref \|\| π_θ) | Reverse KL = mode-seeking; Forward KL = mean-seeking | DPO uses Reverse KL implicitly |
| **f-Divergence** | 泛化 KL 到任意 f-divergence | 更灵活的分布约束 | Beyond Reverse KL (Wang, 2023, [2309.16240](https://arxiv.org/abs/2309.16240)) |
| **Likelihood Displacement** | DPO 中 chosen prob 增加时 rejected 未充分减少的现象 | 分析 DPO 的一种失败模式 | Unintentional Unalignment (Razin, 2024, [2410.08847](https://arxiv.org/abs/2410.08847)) |
| **长度归一化** | r(x,y) = β·avg_log_π 而非 β·sum_log_π | 消除长度偏置 | SimPO; Length-Reliance Elimination (Lu, 2024, [2406.10957](https://arxiv.org/abs/2406.10957)) |
| **Target Reward Margin (γ)** | min_{margin} r(y_w) - r(y_l) ≥ γ | 确保 chosen 显著优于 rejected | SimPO |
| **参考策略理解** | 分析 π_ref 选择的影响 | 解耦 reference policy 的作用 | Understanding Reference Policies (Liu, 2024, [2407.13709](https://arxiv.org/abs/2407.13709)) |

### 3.6 其他重要算法

| 方法 | 核心思想 | 论文 |
|------|----------|------|
| **Self-Play Preference Optimization (SPPO)** | 策略自我对弈生成偏好数据 → 不依赖人工标注 | Wu (2024, [2405.00675](https://arxiv.org/abs/2405.00675)) |
| **SPPO (Self-supervised PO)** | 利用偏好程度感知的自监督信号 | Li (2024, [2409.17791](https://arxiv.org/abs/2409.17791)) |
| **Extensive Self-Contrast** | 无需反馈的自对比对齐 | Liu (2024, [2404.00604](https://arxiv.org/abs/2404.00604)) |
| **Weighted PO (WPO)** | 在 RLHF 中加权偏好优化 | Zhou (2024, [2406.11827](https://arxiv.org/abs/2406.11827)) |
| **Multi-Objective DPO (MODPO)** | 多目标偏好：不同标注者的偏好不一定一致 | Zhou (2023, [2310.03708](https://arxiv.org/abs/2310.03708)) |
| **Reward-Aware PO (RAPO)** | 统一数学框架连接多种 PO 方法 | Sun (2025, [2502.00203](https://arxiv.org/abs/2502.00203)) |
| **Pre-DPO** | 用 guiding reference model 改进 DPO 数据利用率 | Pan (2025, [2504.15843](https://arxiv.org/abs/2504.15843)) |
| **DPO Kernels** | 核方法增强 DPO 的语义感知和散度丰富性 | Das (2025, [2501.03271](https://arxiv.org/abs/2501.03271)) |
| **SimPER** | 无超参数的极简偏好对齐 | Xiao (2025, [2502.00883](https://arxiv.org/abs/2502.00883)) |
| **MIPO** | 调制干预偏好优化：保持简单，精炼困难 | Jang (2024, [2409.17545](https://arxiv.org/abs/2409.17545)) |
| **Active Learning for DPO** | 主动学习选择最有信息量的偏好数据 | Kveton (2025, [2503.01076](https://arxiv.org/abs/2503.01076)) |
| **AMPO** | 主动多偏好优化：对比多组 helpful/undesired responses | Gupta (2025, [2502.18293](https://arxiv.org/abs/2502.18293)) |
| **Entropy Controllable DPO** | 控制生成熵，防止过拟合单一模式 | Omura (2024, [2411.07595](https://arxiv.org/abs/2411.07595)) |

### 3.7 Agentic RL 中的偏好优化

当 RL/偏好优化应用于 multi-turn tool-use / agent 场景时，产生新的方法需求：

| 方法 | 场景 | 核心贡献 | 论文 |
|------|------|----------|------|
| **Multi-Turn DPO** | Agent 多轮交互 | 整个交互轨迹级别的偏好优化 | Shi (2024, [2406.14868](https://arxiv.org/abs/2406.14868)) |
| **Step-Level Value PO** | 数学推理 | 步骤级 value 偏好优化 | Chen (2024, [2406.10858](https://arxiv.org/abs/2406.10858)) |
| **Iterative Preference Learning for Math Agents** | 数学 Agent | 多轮迭代偏好学习 + tool use | Xiong (2024, [2409.02392](https://arxiv.org/abs/2409.02392)) |
| **SLEA-RL** | 多轮 Agentic 训练 | 步骤级经验增强 RL | Wang (2026, [2603.18079](https://arxiv.org/abs/2603.18079)) |
| **Information Gain-based PO** | Multi-turn LLM Agent | 基于信息增益的策略优化 | Wang (2025, [2510.14967](https://arxiv.org/abs/2510.14967)) |
| **Agent-R1** | 端到端 Agent RL | 端到端强化学习训练 tool-using agent | Cheng (2025, [2511.14460](https://arxiv.org/abs/2511.14460)) |
| **SCRIBE** | Tool-Using Agent | 结构化中间监督解决 credit assignment | Jiang (2026, [2601.03555](https://arxiv.org/abs/2601.03555)) |
| **AgentFly** | LM Agent 扩展框架 | 可扩展的 LM Agent RL 框架 | Wang (2025, [2507.14897](https://arxiv.org/abs/2507.14897)) |

---

## 4. 数据策略

### 4.1 数据类型与构建方法

```text
LLM 后训练数据谱系：

                    ┌── 人类比较对 (Pairwise Human Pref)
                    │   来源：众包标注 (InstructGPT, Llama 2)
                    │   成本：高 ($$$ per pair)
    偏好数据 ───────┤
                    ├── AI 反馈 (RLAIF)
                    │   来源：LLM-as-judge, Constitutional AI
                    │   成本：低 (compute only)
                    │
                    ├── 合成偏好数据
                    │   来源：模型自举 (SPPO, SGDPO)
                    │         多智能体模拟 (Synthesizing Post-Training Data)
                    │   成本：低-中
                    │
                    └── 可验证信号 (Verifiable Rewards)
                        来源：代码执行结果、数学答案、单元测试
                        成本：极低 (自动)
```

#### 4.1.1 人类偏好数据 (Human Preference Data)

| 来源 | 数据类型 | 规模 | 代表工作 |
|------|----------|------|----------|
| **InstructGPT** | 比较对 + 排序 | ~33K prompts | Ouyang (2022, [2203.02155](https://arxiv.org/abs/2203.02155)) |
| **Anthropic Helpful/Harmless** | pairwise 偏好 | ~161K | Bai (2022, [2204.05862](https://arxiv.org/abs/2204.05862)) |
| **Llama 2** | 比较对 + 安全标注 | ~1M+ | Touvron (2023, [2307.09288](https://arxiv.org/abs/2307.09288)) |
| **UltraFeedback** | 高质量多维度评分 | ~64K prompts | Cui (2023, [2310.01377](https://arxiv.org/abs/2310.01377)) |
| **West-of-N** | 合成偏好 + 最佳选择 | - | Pace (2024, [2401.12086](https://arxiv.org/abs/2401.12086)) |

#### 4.1.2 AI 反馈 (RLAIF)

| 方法 | 核心思想 | 论文 |
|------|----------|------|
| **Constitutional AI** | 用宪法原则指导 AI 自我 critique 和 revision | Bai (2022, [2212.08073](https://arxiv.org/abs/2212.08073)) |
| **RLAIF** | 用 LLM 替代人类做偏好标注 → 规模扩展 | Lee (2023, [2309.00267](https://arxiv.org/abs/2309.00267)) |
| **Self-Rewarding** | 同一模型生成 + 评判 → 自举 | 多个 self-rewarding 变体 |
| **Magpie** | 无提示从对齐 LLM 合成指令数据 | Xu (2024, [2406.08464](https://arxiv.org/abs/2406.08464)) |
| **Arena Learning** | 模拟 Chatbot Arena → pairwise battle → 数据飞轮 | Luo (2024, [2407.10627](https://arxiv.org/abs/2407.10627)) |
| **Critical Evaluation of AI Feedback** | RLAIF 效果 vs 人类反馈的严格对比 | Sharma (2024, [2402.12366](https://arxiv.org/abs/2402.12366)) |

#### 4.1.3 合成偏好数据生成

| 方法 | 生成方式 | 论文 |
|------|----------|------|
| **Synthesizing Post-Training Data** | 多智能体模拟生成指令数据 | Tang (2024, [2410.14251](https://arxiv.org/abs/2410.14251)) |
| **Icon²** | 自合成偏好数据 + 内在正则化 | Chen (2025, [2509.05605](https://arxiv.org/abs/2509.05605)) |
| **ASTRA** | 自动合成 agentic 轨迹和 RL arena | Tian (2026, [2601.21558](https://arxiv.org/abs/2601.21558)) |
| **Tool-R0** | 从零数据自演进 tool-learning agent | Acikgoz (2026, [2602.21320](https://arxiv.org/abs/2602.21320)) |
| **PromptCoT 2.0** | 大规模 prompt 合成为推理任务 | Zhao (2025, [2509.19894](https://arxiv.org/abs/2509.19894)) |

### 4.2 数据质量与选择

| 论文 | 关键洞察 |
|------|----------|
| **Clean First, Align Later** (Yeh, 2025, [2509.23564](https://arxiv.org/abs/2509.23564)) | 偏好数据清洗对对齐质量影响显著；噪声数据的危害>数据量不足 |
| **Less is More** (Deng, 2025, [2502.14560](https://arxiv.org/abs/2502.14560)) | 通过数据选择改进 DPO：少量精选数据 > 大量低质数据 |
| **Principled Data Selection** (Gao, 2025, [2502.09650](https://arxiv.org/abs/2502.09650)) | "困难样本"可能有隐藏风险；模型能力与数据难度需要匹配 |
| **Not All Preference Pairs Are Created Equal** (Yang, 2024, [2406.17312](https://arxiv.org/abs/2406.17312)) | 标注高效迭代偏好学习：如何选择最有价值的偏好对 |
| **Annotation-Efficient PO** (Jinnai, 2024, [2405.13541](https://arxiv.org/abs/2405.13541)) | 标注预算有限时的偏好优化策略 |
| **ALMA** (Yasunaga, 2024, [2412.04305](https://arxiv.org/abs/2412.04305)) | 最小标注对齐：仅需少量人工标注 |

### 4.3 Data Scaling Laws for RLHF

| 论文 | 核心发现 |
|------|----------|
| **Scaling Laws for RM Overoptimization** (Rafailov, 2024, [2406.02900](https://arxiv.org/abs/2406.02900)) | RM size ↑ → overoptimization 出现更晚；KL budget ↑ → 可达更高真实 reward 但过拟合风险 ↑；DPO 的 overoptimization 特征类似 RLHF |

---

## 5. 评估方法论

### 5.1 评估框架总览

| 评估平台 | 类型 | 指标 | 论文 | 关键特点 |
|----------|------|------|------|----------|
| **AlpacaEval** | LLM-as-judge (自动) | Win Rate, Length-Controlled WR | - | 对标 GPT-4；简单 prompt |
| **AlpacaEval 2.0** | LLM-as-judge (自动) | LC Win Rate | Dubois (2024, [2404.04475](https://arxiv.org/abs/2404.04475)) | 长度受控 → 消除长度偏置 |
| **MT-Bench** | LLM-as-judge (自动) | 多轮对话评分 (1-10) | Zheng (2023, [2306.05685](https://arxiv.org/abs/2306.05685)) | 多轮对话 + 8 类任务 |
| **Chatbot Arena** | 人类投票 (众包) | Elo Score | Zheng (2023, [2306.05685](https://arxiv.org/abs/2306.05685)); Chiang (2024, [2403.04132](https://arxiv.org/abs/2403.04132)) | 盲测配对比较；真实用户 |
| **Arena-Hard** | LLM-as-judge (自动) | Win Rate | Li (2024, [2406.11939](https://arxiv.org/abs/2406.11939)) | 筛选 Arena 中最难的问题 |
| **MixEval** | 混合评估 | 多维得分 | Ni (2024, [2406.06565](https://arxiv.org/abs/2406.06565)) | 混合多个 benchmark 提取智慧 |
| **Varco Arena** | 锦标赛自动评估 | Elo | Son (2024, [2411.01281](https://arxiv.org/abs/2411.01281)) | 无参考基准；锦标赛式 |
| **JudgeBench** | Meta-评估 | Judge 准确率 | Tan (2024, [2410.12784](https://arxiv.org/abs/2410.12784)) | 评估 LLM-judge 本身 |
| **AlignBench** | LLM-as-judge (中文) | 多维度评分 | Liu (2023, [2311.18743](https://arxiv.org/abs/2311.18743)) | 中文对齐评估 |
| **PRMBench** | PRM 评估 | PRM 准确率 | Song (2025, [2501.03124](https://arxiv.org/abs/2501.03124)) | 细粒度过程奖励模型评估 |

### 5.2 LLM-as-Judge 的局限与批评

| 局限 | 论文 | 核心发现 |
|------|------|----------|
| **长度偏置 (Length Bias)** | Dubois (2024, [2404.04475](https://arxiv.org/abs/2404.04475)) | LLM judge 系统性偏好更长回答；LC 可修正但不能消除 |
| **风格优于实质** | Feuer (2024, [2409.15268](https://arxiv.org/abs/2409.15268)) | LLM judges 偏好风格（格式、礼貌）超过内容质量 |
| **Cheating 可能** | Zheng (2024, [2410.07137](https://arxiv.org/abs/2410.07137)) | Null models (始终输出固定文本) 在某些 benchmark 上获得高 win rate |
| **非传递性** | Xu (2025, [2502.14074](https://arxiv.org/abs/2502.14074)) | LLM-as-judge 存在非传递性：A > B, B > C 但 C > A |
| **Benchmark 过拟合** | Singh (2025, [2504.20879](https://arxiv.org/abs/2504.20879)) | "Leaderboard Illusion"：benchmark 进步的幻觉 |
| **认知偏置** | Koo (2023, [2309.17012](https://arxiv.org/abs/2309.17012)) | LLM evaluator 存在类似人类的认知偏置（如位置偏置） |

### 5.3 评估指标对比

| 指标 | 定义 | 优势 | 局限 |
|------|------|------|------|
| **Win Rate** | baseline model 对比胜率 | 直观；可比 | 受 judge 偏置影响；无法反映绝对能力 |
| **Elo Score** | 基于 Bradley-Terry 的评分 | 多人/模型可比；动态更新 | 需足够对战数据；新模型冷启动问题 |
| **LC Win Rate** | 长度回归后 win rate | 消除长度混淆 | 可能过度修正 |
| **Human Eval** | 人工评审 | 金标准 | 昂贵、慢、不可规模化 |
| **Automatic Metrics** (ROUGE, BLEU) | 字面匹配 | 快速、可复现 | 与人类偏好相关性极低 |
| **PRM Accuracy** | 步骤正确性判别 | 细粒度 | 需步骤级别标注 |

### 5.4 评估的实验范式

```text
标准对齐评估流程：
1. 在 AlpacaEval / MT-Bench / Arena-Hard 上评估
2. 报告 Win Rate (vs baseline) 和/或 Elo Score
3. 如果有条件，补充 Human Eval（通常仅在重要论文中）
4. 消融实验：超参数 (β, γ, G)、数据量、model size

标准实验设置约定：
- Baseline：通常为 SFT model 或 Llama-3-Instruct / GPT-4 级别模型
- Temperature：0 用于评估（确定性生成）
- Judge：GPT-4 / GPT-4-Turbo 最常用
- 评测 prompt：参考 AlpacaEval / MT-Bench 标准模板
```

---

## 6. 方法演化关系图

### 6.1 时间线演化

```text
2017 ─── PPO (Schulman et al.)                    [策略基础]
          │
2020 ─── GPT-3 / Scaling Laws                     [模型基础]
          │
2022 ─── InstructGPT (PPO-RLHF 范式)               [RLHF 范式确立]
          │
          ├── Constitutional AI (RLAIF)            [AI 反馈路线]
          │
2023 ─── Llama 2 (工业级 RLHF 开源)                [开源工程化]
          │
          ├──★ DPO (直接偏好优化革命)              [范式转折点]
          │    ├── 隐式 reward 统一论
          │    └── 开启 DPO 变体爆发
          │
          ├── UltraFeedback (高质量 AI 偏好数据)
          ├── RLAIF: Scaling RLHF with AI Feedback
          ├── MT-Bench & Chatbot Arena
          │
2024 ─── DPO 变体爆发年:
          │   KTO (前景理论) ── 仅需单侧标签
          │   ORPO (无参考模型) ── SFT+偏好联合
          │   SimPO (无参考模型+长度归一化) ── 极简
          │   IPO (回归目标) ── 防止过拟合
          │   Online DPO ── 在线采样+离线优化
          │   Iterative DPO ── 自举循环
          │   SPPO ── 自博弈
          │   Multi-Objective DPO ── 多偏好
          │
          ├── PRM 方法爆发:
          │   自动过程监督 (无步骤标注)
          │   Q-Value PRM
          │   Free Process Rewards
          │
          ├── Reward Hacking 系统研究:
          │   RM Ensemble 效果有限
          │   Causal Rewards
          │   CARMO (动态标准)
          │
          ├── AlpacaEval 2.0 (长度受控评估)
          ├── Arena-Hard
          │
2025 ───★ DeepSeek-R1 / GRPO 革命:
          │   GRPO → reasoning RL 新范式
          │   DeepSeek-R1-Zero: 纯 RL 涌现推理
          │
          ├── GRPO 变体爆发:
          │   MO-GRPO, DaGRPO, EBPO, CPPO, BiasGRPO
          │   GRPO-VPS (过程监督)
          │   Latent-GRPO (隐空间推理)
          │
          ├── Agentic RL 爆发:
          │   Agent-R1, Tool-R1, SLEA-RL
          │   Multi-turn DPO, Step-level PO
          │
          ├── SFT-RL 关系再定义:
          │   状态分布视角
          │   Non-decoupling SFT/RL
          │   隐式 Reward 统一论
          │
2026 ─── 理论深化与统一:
          │   DPO-RLHF 等价性条件
          │   GRPO 的 U-Statistic 性质
          │   On/Off-Policy 统一视角
          │   Reward Hacking 系统综述
          │   Directional Alignment
          │   Sample Routing 统一 GRPO/蒸馏
```

### 6.2 方法家族树

```text
                        ┌─────────────────────┐
                        │   LLM 对齐训练       │
                        └──────────┬──────────┘
                                   │
            ┌──────────────────────┼──────────────────────┐
            │                      │                      │
   ┌────────▼────────┐   ┌────────▼────────┐   ┌────────▼────────┐
   │  RL-based       │   │  DPO Family     │   │  Group-wise     │
   │  (需要 RM)      │   │  (隐式 reward)  │   │  (组相对)       │
   └────────┬────────┘   └────────┬────────┘   └────────┬────────┘
            │                      │                      │
   ┌────────┼────────┐    ┌───────┼───────┐      ┌───────┼───────┐
   │        │        │    │       │       │      │       │       │
PPO      Robust   Offline  DPO   KTO    ORPO   GRPO   GRPO-  PAPO
-RLHF    RLHF      RLHF          (单侧) (无ref)        VPS
           │                          │                     │
      MaxMin-RLHF                   SimPO             MO-GRPO
      Online Mirror                  (无ref,          DaGRPO
      Descent                      长度归一化)         EBPO
                                                        CPPO
```

### 6.3 关键转折点

| 时间 | 转折事件 | 影响 |
|------|----------|------|
| **2022** | InstructGPT 发布 | RLHF 范式确立：SFT → RM → PPO 三阶段 |
| **2023.05** | DPO 发布 | 范式革命：去 RM 化 → 端到端偏好优化 |
| **2024** | DPO 变体爆发 (KTO/ORPO/SimPO/IPO) | 细化数据需求 (KTO)、简化架构 (ORPO/SimPO) |
| **2025.01** | DeepSeek-R1 发布 | GRPO + reasoning RL 引领新潮；组相对优化实用化 |
| **2025-2026** | Agentic RL 爆发 | RL 从"对齐"走向"能力增强" |工具使用、多步推理 |

---

## 7. 未解决问题

### 7.1 方法层面

| 问题 | 现状 | 挑战 |
|------|------|------|
| **DPO vs RLHF 何时等价** | Yang (2026) 给出条件但实践困难 | 偏好数据充分覆盖条件难以满足 |
| **无参考模型的代价** | SimPO/ORPO 去掉了 π_ref 但有自身局限 | 训练不稳定、分布塌缩风险 |
| **GRPO 的偏差-方差权衡** | 组大小 G 越大方差越小但采样成本高 | 最优 G 的理论指导缺失 |
| **Online vs Offline 的最优混合** | Iterative DPO 已证明优于纯 offline | 混合比例、采样策略缺乏理论 |
| **多轮交互中的信用分配** | SCRIBE 等方法尝试结构化监督 | Agent RL 的 credit assignment 远未解决 |

### 7.2 数据层面

| 问题 | 现状 | 挑战 |
|------|------|------|
| **Human vs AI Feedback 差距** | RLAIF 在某些场景接近 human feedback | RLAIF 的 scale 上限和偏置传播 |
| **合成数据的质量退化** | 多轮自举可能导致质量退化 | 检测和防止"数据近亲繁殖" |
| **偏好数据的普适性** | 偏好高度依赖标注者群体 | 跨文化、跨语言偏好对齐 |
| **PRM 数据瓶颈** | 无监督 PRM 兴起但仍不如监督 | 自动标注精度 vs 人类标注精度差距 |

### 7.3 评估层面

| 问题 | 现状 | 挑战 |
|------|------|------|
| **LLM-judge 偏置无法根除** | LC 修正了长度但风格偏置仍在 | 如何设计 unbiased auto-evaluator |
| **Chatbot Arena 的时效性** | 新模型需要大量对战才能稳定 Elo | 冷启动加速方法 |
| **Reasoning 评估缺少标准** | 数学/代码可用答案验证，开放领域无标准 | 如何评估开放领域推理质量 |
| **安全对齐的评估困境** | 安全性难以量化为单一指标 | 多维度安全评估的统一 |

### 7.4 理论层面

| 问题 | 现状 | 挑战 |
|------|------|------|
| **Reward Hacking 的理论边界** | 多种缓解方法但无法根除 | 是否存在根本上可避免 reward hacking 的框架 |
| **KL 约束的理论基础** | 实践经验丰富但理论薄弱 | 最优 KL 约束形式（reverse vs forward vs f-divergence） |
| **Scaling Laws 的普适性** | Overoptimization scaling law 已提出 | 不同方法/数据/模型的 scaling 行为差异 |
| **对齐税 (Alignment Tax)** | RLHF 可能降低某些能力 | 如何量化和对冲对齐税 |

---

## 附录：方法命名索引

| 缩写 | 全称 | 论文 |
|------|------|------|
| RLHF | Reinforcement Learning from Human Feedback | InstructGPT (2022) |
| RLAIF | RL from AI Feedback | Lee (2023, [2309.00267](https://arxiv.org/abs/2309.00267)); CAI (Bai, 2022) |
| RLVR | RL with Verifiable Rewards | DeepSeek-R1 (2025) |
| SFT | Supervised Fine-Tuning | 通用 |
| PPO | Proximal Policy Optimization | Schulman (2017) |
| DPO | Direct Preference Optimization | Rafailov (2023, [2305.18290](https://arxiv.org/abs/2305.18290)) |
| KTO | Kahneman-Tversky Optimization | Ethayarajh (2024, [2402.01306](https://arxiv.org/abs/2402.01306)) |
| ORPO | Odds Ratio Preference Optimization | Hong (2024, [2403.07691](https://arxiv.org/abs/2403.07691)) |
| SimPO | Simple Preference Optimization | Meng (2024, [2405.14734](https://arxiv.org/abs/2405.14734)) |
| IPO | Identity Preference Optimization | Ji (2024, [2402.00856](https://arxiv.org/abs/2402.00856)) |
| ODPO | DPO with an Offset | Amini (2024, [2402.10571](https://arxiv.org/abs/2402.10571)) |
| GRPO | Group Relative Policy Optimization | DeepSeek-R1 (2025, [2501.12948](https://arxiv.org/abs/2501.12948)) |
| ORM | Outcome Reward Model | 通用 |
| PRM | Process Reward Model | 多篇 |
| SPPO | Self-Play Preference Optimization | Wu (2024, [2405.00675](https://arxiv.org/abs/2405.00675)) |
| WPO | Weighted Preference Optimization | Zhou (2024, [2406.11827](https://arxiv.org/abs/2406.11827)) |
| MODPO | Multi-Objective DPO | Zhou (2023, [2310.03708](https://arxiv.org/abs/2310.03708)) |
| CARMO | Context-Aware Reward Modelling | Gupta (2024, [2410.21545](https://arxiv.org/abs/2410.21545)) |
| PAPO | Process-Aware Policy Optimization | Tan (2026, [2603.26535](https://arxiv.org/abs/2603.26535)) |
| CPPO | Completion Pruning Policy Optimization | Lin (2025, [2503.22342](https://arxiv.org/abs/2503.22342)) |
| EBPO | Empirical Bayes Policy Optimization | Han (2026, [2602.05165](https://arxiv.org/abs/2602.05165)) |

---

*本文件基于 paper_inventory.md 中实际存在的 280 篇论文构建。所有引用均可追溯到 paper_inventory.md 中的具体条目。未编造的因果关系或实验结果。推断标注为推断。*
