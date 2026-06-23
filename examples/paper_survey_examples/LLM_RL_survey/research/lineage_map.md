# LLM 强化学习后训练 - 演进脉络

> **生成时间**: 2026-06-23
> **生成 Agent**: lineage_mapping_agent
> **数据来源**: research/paper_inventory.md (280 篇)、research/query_plan.md
> **分析方法**: 以时间线、问题定义、方法突破、实验范式、影响力路径五轴梳理

---

## 1. 时间线

| 时期 | 关键问题 | 代表性论文 (含 arXiv ID) | 主要转变 |
|------|----------|------------------------|---------|
| **奠基期 (2017-2020)** | 通用 RL 算法能否用于语言模型？如何从人类偏好中学习？ | PPO (Schulman et al., 2017) `1707.06347`; [RLHF 早期探索](https://arxiv.org/abs/1706.03741) (Christiano et al., 2017 方向锚定) | PPO 作为通用策略优化算法确立；RLHF 概念从机器人控制迁移至语言任务 |
| **成型期 (2021-2022)** | 如何将 RLHF 系统化应用于 LLM 对齐？如何平衡 helpfulness 和 harmlessness？ | InstructGPT (Ouyang et al., 2022) `2203.02155`; Constitutional AI / Training a Helpful and Harmless Assistant (Bai et al., 2022) `2204.05862`; Constitutional AI (Bai et al., 2022) `2212.08073` | **SFT → RM → PPO 三阶段范式确立**；RLAIF (AI 反馈替代人工反馈) 提出；多目标对齐 (helpful + harmless) 成为设计原则 |
| **爆发期 (2023)** | 能否绕过显式 Reward Model？DPO 能否替代 PPO？开源社区如何复现 RLHF？ | **DPO** (Rafailov et al., 2023) `2305.18290`; Llama 2 (Touvron et al., 2023) `2307.09288`; UltraFeedback (Cui et al., 2023) `2310.01377`; RLAIF (Lee et al., 2023) `2309.00267`; MT-Bench/Chatbot Arena (Zheng et al., 2023) `2306.05685`; ToolLLM (Qin et al., 2023) `2307.16789` | **从在线 RL 到离线偏好优化的范式转变**；工业级 RLHF 开源 (Llama 2)；AI 反馈规模化 (RLAIF)；Agent 训练的 RL 方法萌芽 (ToolLLM)；Evaluation 标准化 |
| **深化期前期 (2024)** | DPO 有哪些变体？能否摆脱参考模型？在线 vs 离线 DPO？偏好数据质量如何影响对齐？ | **ORPO** (Hong et al., 2024) `2403.07691`; **SimPO** (Meng et al., 2024) `2405.14734`; **KTO** (Ethayarajh et al., 2024) `2402.01306`; Online DPO (Qi et al., 2024) `2406.05534`; **Self-Play PO** (Wu et al., 2024) `2405.00675`; Iterative RPO (Pang et al., 2024) `2404.19733`; Direct Multi-Turn PO for Agents (Shi et al., 2024) `2406.14868`; Chatbot Arena (Chiang et al., 2024) `2403.04132`; Arena-Hard (Li et al., 2024) `2406.11939` | **DPO 变体爆发 (ORPO/SimPO/KTO/SPPO 等)**；无参考模型优化 (ORPO/SimPO)；在线/迭代 DPO 出现；Agent 场景的偏好优化开始；Evaluation 方法论深化 (Arena-Hard, Length-Controlled AlpacaEval) |
| **深化期后期 (2025-2026)** | GRPO 如何革新推理能力训练？Agentic RL 如何规模化？RLVR 的统一框架是什么？SFT vs RL 的本质关系？ | **DeepSeek-R1** (DeepSeek-AI, 2025) `2501.12948`; **Demystifying GRPO** (Zhou et al., 2026) `2603.01162`; Agent-R1 (Cheng et al., 2025) `2511.14460`; Tool-R1 (Zhang et al., 2025) `2509.12867`; MO-GRPO (Ichihara et al., 2025) `2509.22047`; Conditional Equivalence of DPO and RLHF (Yang et al., 2026) `2605.20834`; Post-Training is About States (Nie et al., 2026) `2605.22731`; Mechanistic Analysis (Sinha et al., 2026) `2606.09850` | **RLVR (Reinforcement Learning with Verifiable Rewards) 范式兴起**；GRPO 取代 PPO 成为推理训练主力；Agentic RL 系统化 (Tool-R1, Agent-R1)；理论反思 (DPO⇔RLHF 等价性、SFT 与 RL 不可解耦)；可解释性视角介入 (Mechanistic Analysis) |

---

## 2. 问题-方法矩阵

| 问题定义 | 方法族 | 代表论文 (arXiv ID) | 优势 | 局限 |
|----------|--------|---------------------|------|------|
| **对齐人类偏好 — 在线 RL** | PPO + Reward Model (经典 RLHF) | InstructGPT `2203.02155`; Llama 2 `2307.09288`; Training Helpful & Harmless Assistant `2204.05862` | 成熟训练流程；可在线采样探索；RM 可复用 | 需训练独立的 Reward Model；训练不稳定 (KL 惩罚调参)；Reward Hacking 风险 |
| **对齐人类偏好 — 离线偏好优化** | DPO 及变体 | DPO `2305.18290`; ORPO `2403.07691`; SimPO `2405.14734`; KTO `2402.01306`; IPO/CPO (方向锚定) | 无需训练 RM；训练简单稳定；计算开销低 | 依赖优质偏好数据；离线数据分布偏移；可能退化为 SFT (Likelihood Displacement) |
| **对齐人类偏好 — 在线/迭代 DPO** | Online DPO / Iterative DPO | Online DPO `2406.05534`; Iterative RPO `2404.19733`; Self-Exploring LM `2405.19332`; Iterative Length-Regularized DPO `2406.11817` | 突破离线数据瓶颈；模型自我采样探索；理论上接近 RLHF | 需要在线标注或自标注；迭代成本高 |
| **推理能力训练 — RLVR (可验证奖励)** | GRPO + Rule-based Reward | DeepSeek-R1 `2501.12948`; Demystifying GRPO `2603.01162`; GRPO-VPS `2604.20659`; CPPO `2503.22342` | 奖励信号无歧义 (数学/代码)；组内归一化降低方差；不需 RM | 仅适用于可验证域 (math/code)；非可验证域需 PRM 或新范式；训练方差大 |
| **推理能力训练 — 过程监督** | Process Reward Model (PRM) | Free Process Rewards `2412.01981`; The Lessons of Developing PRMs `2501.07301`; PRMBench `2501.03124`; GroundedPRM `2510.14942` | 细粒度步骤级监督；与 test-time scaling 协同 | 过程标签获取困难；PRM 自身可能被 hacking；与 ORM 复杂交互 |
| **Agent 能力训练** | Tool-Augmented RL / Multi-Turn RL | ToolLLM `2307.16789`; Agent-R1 `2511.14460`; Tool-R1 `2509.12867`; Direct Multi-Turn PO for Agents `2406.14868`; SLEA-RL `2603.18079`; SCRIBE `2601.03555` | 端到端优化 Agent 行为；处理多步交互 | 奖励信号稀疏 (credit assignment)；环境交互成本高；工具可靠性依赖 |
| **安全对齐** | Constitutional AI / RLAIF | Constitutional AI `2212.08073`; RLAIF `2309.00267`; Inverse Constitutional AI `2406.06560`; Reflect `2601.18730` | 可扩展的 AI 反馈替代人工；原则可解释 | AI 反馈自身偏差；原则制定主观性；Emergent Misalignment |
| **多目标对齐** | Multi-Objective RLHF / MODPO | MODPO `2310.03708`; MaxMin-RLHF `2402.08925`; Aligning to Thousands of Preferences `2405.17977` | 满足多样化用户偏好；避免单一化对齐 | 目标间可能存在冲突；权重调参复杂 |
| **评估体系** | LLM-as-Judge / Arena / Benchmark | MT-Bench/Chatbot Arena `2306.05685`; Chatbot Arena `2403.04132`; Arena-Hard `2406.11939`; Length-Controlled AlpacaEval `2404.04475`; JudgeBench `2410.12784` | 可扩展自动评估；接近人类判断 | 长度偏差、位置偏差、非传递性 (Non-Transitivity)；LLM-judge 自身偏好偏见 |

---

## 3. 关键转折点

### 3.1 从 SFT 到 RLHF 的转变 (2021-2022)

**触发性论文**:
- InstructGPT (Ouyang et al., 2022) `2203.02155` — 确立了 SFT → RM → PPO 三级流水线
- Training a Helpful and Harmless Assistant (Bai et al., 2022) `2204.05862` — 引入多目标 RLHF (helpfulness + harmlessness)

**转变本质**: 
纯 SFT (行为克隆) 受限于示范数据分布，模型缺乏对未见过输入的对齐能力。RLHF 通过奖励模型将人类偏好编码为可微分信号，使模型可以在超越示范数据的空间中进行优化。

**后续影响**:
- 2026 年出现反思：SFT 和 RL 在 post-training 中实际上不可解耦 (Niu et al., `2601.07389`)；两类方法共享相似的 state distribution 优化目标 (Nie et al., `2605.22731`)

---

### 3.2 从 PPO 到 DPO 的转变 — 离线偏好优化 (2023)

**触发性论文**:
- Direct Preference Optimization (Rafailov et al., 2023) `2305.18290` — 核心洞察：**语言模型自身隐式包含了奖励函数**，偏好优化可通过简单的分类损失实现，无需显式训练 RM

**转变本质**:
传统 RLHF 需要：(a) 训练 Reward Model → (b) 用 PPO 优化策略 → (c) 维护 reference model + 计算 KL 惩罚。DPO 通过 Bradley-Terry 偏好模型下的闭式解，将偏好数据直接映射为策略参数的梯度更新，极大地简化了训练流程。

**分叉路径**:
- **DPO 正统派**: 保留参考模型，改进损失函数 (β-DPO `2407.08639`; DPO with Offset `2402.10571`; Curry-DPO `2403.07230`)
- **无参考模型派**: ORPO (合并 SFT+PO, `2403.07691`); SimPO (使用平均 log probability, `2405.14734`)
- **非成对偏好派**: KTO (基于前景理论，无需 chosen/rejected 对, `2402.01306`)
- **理论统一派**: Conditional Equivalence of DPO and RLHF (Yang et al., 2026, `2605.20834`) — 揭示 DPO 与 RLHF 在隐式假设下的等价性及其失效模式

**被高估的论文 / 争议**:
- DPO 在实践中存在 Likelihood Displacement 问题 (Razin et al., `2410.08847`)：DPO 可能只降低 rejected 响应的概率而不提升 chosen 响应质量，与预期行为不符
- DPO 在长度上有系统性偏差 (Lu et al., `2406.10957`)
- Or DPO 综述 (Xiao et al., `2410.15595`) 指出 DPO 方法族缺乏统一的理论框架

---

### 3.3 从单一对齐到 Agentic RL (2024-2026)

**触发性论文**:
- ToolLLM (Qin et al., 2023) `2307.16789` — 将工具使用能力纳入 LLM RL 训练
- DeepSeek-R1 (DeepSeek-AI, 2025) `2501.12948` — RLVR 范式 + GRPO 在推理任务上的突破
- Agent-R1 (Cheng et al., 2025) `2511.14460`; Tool-R1 (Zhang et al., 2025) `2509.12867`

**转变本质**:
对齐的目标从"生成符合人类偏好的文本"扩展为"在环境中完成多步交互任务"。这引入了全新的挑战：
1. **奖励稀疏性**: 多步 agent 任务只在最终有成功/失败信号
2. **Credit Assignment**: 哪个中间步骤导致了最终失败？
3. **环境交互成本**: 真实 API 调用、代码执行、网络浏览成本高

**方法路线分叉**:
- **RLVR 路线** (DeepSeek-R1 → GRPO 系列): 用于有明确 ground-truth 可验证的推理任务 (数学证明、代码正确性)
- **Process Supervision 路线** (PRM → GroundedPRM → SCRIBE): 为中间步骤提供细粒度奖励
- **Multi-Turn PO 路线** (Direct Multi-Turn PO `2406.14868` → SLEA-RL `2603.18079`): 将 DPO 扩展到多轮交互
- **Self-Play 路线** (SPPO `2405.00675` → Arena Learning `2407.10627`): 用模型自身生成的数据进行迭代优化

---

### 3.4 从在线到离线再到迭代/在线循环 (2023-2026)

**演进路径**:

```
Online RLHF (PPO) [2022]
    ↓ 简化训练流程
Offline DPO [2023] — 但面临分布外泛化问题
    ↓ 引入在线采样
Online DPO [2024] — 恢复在线探索能力
    ↓ 迭代自改进
Iterative DPO / Self-Play [2024-2025]
    ↓ 绕过偏好数据需求
RLVR + GRPO [2025-2026] — 用可验证信号替代偏好
```

**关键论文**:
- Online DPO (Qi et al., 2024) `2406.05534` — Fast-Slow Chasing 机制实现在线采样与离线优化的解耦
- Self-Exploring LMs (Zhang et al., 2024) `2405.19332` — 主动偏好获取，模型主动选择不确定样本进行标注
- Iterative Preference Learning (Xiong et al., 2023) `2312.11456` — 系统化迭代 RLHF 的理论基础
- RLHF Workflow (Dong et al., 2024) `2405.07863` — 完整在线迭代 RLHF 工程实践报告

---

## 4. 论文影响路径图说明

### 路径 A: PPO → DPO → GRPO (核心算法主线)

```
PPO (Schulman, 2017) [1707.06347]
    │  作为 RLHF 的优化器
    ▼
InstructGPT (Ouyang, 2022) [2203.02155]
    │  确立 SFT→RM→PPO 三阶段范式
    ▼
Llama 2 (Touvron, 2023) [2307.09288]
    │  工业级 RLHF 实践 + 开源
    ├──────────────────────────────────────┐
    ▼                                      ▼
DPO (Rafailov, 2023) [2305.18290]      RLAIF (Lee, 2023) [2309.00267]
    │  绕过 RM 的直接偏好优化               AI 反馈替代人工反馈
    ├──────────────┬──────────────┐
    ▼              ▼              ▼
ORPO (2024)    SimPO (2024)    KTO (2024)
[2403.07691]   [2405.14734]    [2402.01306]
无参考模型      无参考模型       非成对偏好
    │              │              │
    ▼              ▼              ▼
Online DPO (2024) ← Iterative RPO (2024) ← Self-Play PO (2024)
[2406.05534]       [2404.19733]            [2405.00675]
    │
    ▼
DeepSeek-R1 (2025) [2501.12948]  ←  RLVR + GRPO
    │
    ▼
GRPO 变体爆发 (2025-2026):
├── Demystifying GRPO [2603.01162] (理论分析：U-Statistic)
├── MO-GRPO [2509.22047] (多目标)
├── GRPO-VPS [2604.20659] (可验证过程监督)
├── CPPO [2503.22342] (加速训练)
├── Unifying GRPO & Self-Distillation [2604.02288]
└── Group-Relative REINFORCE [2509.24203] (off-policy 视角)
```

### 路径 B: Reward Modeling (支撑性技术线)

```
Preference Model / Bradley-Terry (基础)
    │
    ▼
Training Helpful & Harmless Assistant (Bai, 2022) [2204.05862]
    │  多目标 RM
    ▼
UltraFeedback (Cui, 2023) [2310.01377]
    │  高质量偏好数据构建
    ├──────────────────────────┐
    ▼                          ▼
Reward Hacking 研究            Process Reward Models
├── RM Ensembles (2023)       ├── Free Process Rewards (2024)
│   [2312.09244]              │   [2412.01981]
├── Causal Rewards (2025)     ├── PRMBench (2025) [2501.03124]
│   [2501.09620]              ├── GroundedPRM (2025)
├── Beyond Reward Hacking     │   [2510.14942]
│   (2026) [2604.13602]       ├── Bidirectional PRM (2025)
├── Directional Alignment     │   [2508.01682]
│   (2026) [2605.25189]       └── Unsupervised PRMs (2026)
├── Hack-Verifiable Envs          [2605.10158]
│   (2026) [2605.20744]
└── The Flip Side of RLHF
    (2026) [2605.30888]
```

### 路径 C: Agentic RL (新兴前沿线)

```
WebGPT (OpenAI, 2021 方向锚定)
    │
    ▼
ToolLLM (Qin, 2023) [2307.16789]
    │  16K API 工具使用训练
    ├─────────────────────────────┐
    ▼                             ▼
RLVR 方向                        Multi-Turn RL 方向
├── DeepSeek-R1 (2025)          ├── Direct Multi-Turn PO
│   [2501.12948]                │   (2024) [2406.14868]
├── Agent-R1 (2025)             ├── Building Math Agents
│   [2511.14460]                │   (2024) [2409.02392]
├── Tool-R1 (2025)              ├── Multi-Agent Tool-Integrated
│   [2509.12867]                │   PO (2025) [2510.04678]
├── SFR-DeepResearch (2025)     ├── SLEA-RL (2026)
│   [2509.06283]                │   [2603.18079]
├── Stable RL for Reasoning     ├── ASTRA (2026)
│   (2025) [2505.18086]         │   [2601.21558]
├── DINO-R1 (2025) [2505.24025] └── Information Gain-based PO
└── SCRIBE (2026) [2601.03555]      (2025) [2510.14967]
```

### 路径 D: Benchmark & Evaluation (评估体系线)

```
MT-Bench / Chatbot Arena (Zheng, 2023) [2306.05685]
    │  确立 LLM-as-Judge 评估范式
    ├──────────────────────────────┐
    ▼                              ▼
AlpacaEval 系列                  Arena-Hard (Li, 2024)
├── Length-Controlled (2024)     [2406.11939]
│   [2404.04475]                    │
├── Cheating Benchmarks (2024)      ▼
│   [2410.07137]                 JudgeBench (Tan, 2024)
│   (Null model 高 win rate)     [2410.12784]
│                                  │
├── Chatbot Arena paper (2024)     ▼
│   [2403.04132]                Non-Transitivity in
│                                LLM-as-Judge (Xu, 2025)
├── AlignBench (2023)            [2502.14074]
│   [2311.18743] (中文)
│                                  ▼
└── Varco Arena (2024)          The Leaderboard Illusion
    [2411.01281]                (Singh, 2025) [2504.20879]
```

---

## 5. 各阶段核心问题和代表论文

### 奠基期 (2017-2020): PPO 算法基础与 RLHF 概念萌芽

**核心问题**: 策略梯度方法能否在保持训练稳定性的同时，在复杂策略空间中优化？人类偏好能否作为语言模型的奖励信号？

| 论文 | arXiv ID | 贡献 | 地位 |
|------|----------|------|------|
| PPO (Schulman et al., 2017) | `1707.06347` | 提出 Proximal Policy Optimization，通过 clip 机制实现稳定在线策略优化 | **开创性** — 方法基石 |
| Deep reinforcement learning from human preferences (Christiano et al., 2017) | (检索计划锚点) `1706.03741` | RLHF 概念：从人类偏好中学习奖励函数 | **开创性** — 概念先驱 |

> **注意**: 此阶段论文因 HuggingFace API 搜索的时间覆盖限制，主要出现在检索计划中作为锚点。PPO `1707.06347` 已被 HuggingFace API 确认存在。Christiano et al. 2017 作为 RLHF 概念先驱在 query_plan 中列出。

---

### 成型期 (2021-2022): RLHF 工业化范式建立

**核心问题**: 如何系统化地将 RLHF 应用于大规模语言模型？如何同时对齐 helpfulness 和 harmlessness？

| 论文 | arXiv ID | 贡献 | 地位 |
|------|----------|------|------|
| InstructGPT (Ouyang et al., 2022) | `2203.02155` | 确立 SFT → RM → PPO 三阶段 RLHF 范式；首次证明 RLHF 在 175B 模型上的有效性 | **开创性** — 范式定义者 |
| Training a Helpful and Harmless Assistant (Bai et al., 2022) | `2204.05862` | 引入 helpfulness 和 harmlessness 双目标 RLHF；多目标偏好学习 | **开创性** — 多目标对齐先驱 |
| Constitutional AI (Bai et al., 2022) | `2212.08073` | 提出 RLAIF：用 AI 反馈替代人工反馈；宪法式原则引导对齐 | **开创性** — RLAIF 范式开创 |

---

### 爆发期 (2023): DPO 革命 + 开源 RLHF + 评估标准化

**核心问题**: DPO 能否替代 PPO？开源社区如何实现工业级 RLHF？如何系统性评估 LLM 对齐效果？

| 论文 | arXiv ID | 贡献 | 地位 |
|------|----------|------|------|
| DPO (Rafailov et al., 2023) | `2305.18290` | 发现 LM 隐式包含奖励函数；通过 Bradley-Terry 闭式解实现无需 RM 的偏好优化 | **开创性** — 方向转折点 |
| Llama 2 (Touvron et al., 2023) | `2307.09288` | 首个开源工业级 RLHF 训练的 LLM；提供完整 RLHF 训练方法论 | **代表性** — 开源社区基石 |
| UltraFeedback (Cui et al., 2023) | `2310.01377` | 大规模高质量偏好数据集构建方法论；社区广泛使用的 RM 训练数据 | **代表性** — 数据基础设施 |
| RLAIF (Lee et al., 2023) | `2309.00267` | 系统化验证 AI 反馈可替代人工反馈进行 RLHF 训练 | **代表性** — RLAIF 走向实用 |
| MT-Bench / Chatbot Arena (Zheng et al., 2023) | `2306.05685` | 首次提出 LLM-as-Judge 评估范式和多模型竞技场平台 | **开创性** — 评估范式定义者 |
| ToolLLM (Qin et al., 2023) | `2307.16789` | 将 16000+ API 的工具使用能力纳入 LLM 训练，开 Agentic RL 先河 | **开创性** — Agent RL 先驱 |
| Iterative Preference Learning (Xiong et al., 2023) | `2312.11456` | 迭代 RLHF 的理论框架，连接理论与实践 | **代表性** — 理论桥梁 |
| MODPO (Zhou et al., 2023) | `2310.03708` | 多目标直接偏好优化，避免单一偏好覆盖多样化需求 | **代表性** — 多目标对齐 |

---

### 深化期前期 (2024): DPO 变体爆发 + Agent 偏好优化 + Online DPO

**核心问题**: DPO 有哪些核心变体？能否摆脱参考模型？离线偏好数据的分布偏移如何解决？如何将偏好优化扩展到 Agent 多轮场景？

| 论文 | arXiv ID | 贡献 | 地位 |
|------|----------|------|------|
| ORPO (Hong et al., 2024) | `2403.07691` | 合并 SFT 和偏好优化为单一训练阶段，无需参考模型 | **代表性** — 架构简化 |
| SimPO (Meng et al., 2024) | `2405.14734` | 使用平均对数概率作为隐式奖励，以长度归一化替代参考模型 | **代表性** — 简洁高效 |
| KTO (Ethayarajh et al., 2024) | `2402.01306` | 基于 Kahneman-Tversky 前景理论，无需成对偏好数据即可优化 | **开创性** — 非成对偏好 |
| Online DPO (Qi et al., 2024) | `2406.05534` | Fast-Slow Chasing 实现在线 DPO，突破离线数据分布限制 | **代表性** — 在线化先驱 |
| Self-Play PO (Wu et al., 2024) | `2405.00675` | 自博弈偏好优化，无需 Bradley-Terry 假设，适用于非传递性偏好 | **代表性** — 博弈论视角 |
| Iterative RPO (Pang et al., 2024) | `2404.19733` | 迭代推理偏好优化，针对推理任务改进迭代优化方法 | **代表性** — 推理专项 |
| Iterative Length-Regularized DPO (Liu et al., 2024) | `2406.11817` | 证明迭代 DPO 可将 7B 模型性能提升至接近 GPT-4 水平 | **代表性** — 实证威力 |
| Direct Multi-Turn PO for Agents (Shi et al., 2024) | `2406.14868` | 将 DPO 扩展至多轮 Agent 交互场景 | **开创性** — Agent PO 先驱 |
| Self-Exploring LMs (Zhang et al., 2024) | `2405.19332` | 主动偏好获取策略，模型自主选择不确定样本 | **代表性** — 数据效率 |
| Chatbot Arena (Chiang et al., 2024) | `2403.04132` | 大规模众包平台论文，系统验证 Elo 评分对 LLM 评估的有效性 | **代表性** — 评估平台 |
| Arena-Hard (Li et al., 2024) | `2406.11939` | 从 Arena 数据中自动构建高难度 benchmark | **代表性** — 动态 benchmark |
| MaxMin-RLHF (Chakraborty et al., 2024) | `2402.08925` | 公平导向的 RLHF，最大化最差群体的偏好满意度 | **代表性** — 公平对齐 |
| Free Process Rewards (Yuan et al., 2024) | `2412.01981` | 无需过程标注即可训练 PRM | **代表性** — PRM 自动化 |
| Scaling Laws for RM Overoptimization (Rafailov et al., 2024) | `2406.02900` | 量化 Direct Alignment 算法中 RM 过度优化的 scaling 规律 | **代表性** — 理论分析 |
| Cheating LLM Benchmarks (Zheng et al., 2024) | `2410.07137` | 暴露 LLM 自动 benchmark 可被 null model 轻易欺骗 | **争议/重要** — benchmark 可信度危机 |

---

### 深化期后期 (2025-2026): GRPO + Agentic RL + 理论反思

**核心问题**: GRPO 为何有效？RLVR 如何统一可验证推理训练？Agent 能力如何通过 RL 系统化提升？DPO 与 RLHF 的本质关系？SFT 与 RL 是否可解耦？

| 论文 | arXiv ID | 贡献 | 地位 |
|------|----------|------|------|
| DeepSeek-R1 (DeepSeek-AI, 2025) | `2501.12948` | R1-Zero: 纯 RL 无 SFT 推理涌现；R1: 冷启动 SFT + RL；引入 GRPO 替代 PPO | **开创性** — 新范式定义者 |
| Demystifying GRPO (Zhou et al., 2026) | `2603.01162` | 揭示 GRPO 策略梯度本质为 U-Statistic；建立理论分析框架 | **代表性** — 理论奠基 |
| Conditional Equivalence of DPO and RLHF (Yang et al., 2026) | `2605.20834` | 证明 DPO 和 RLHF 在隐式假设下的有条件等价性及失效模式 | **代表性** — 统一理论 |
| Agent-R1 (Cheng et al., 2025) | `2511.14460` | 端到端 RL 训练 Agent；将 R1 范式迁移至 Agent 场景 | **开创性** — Agent RL 系统化 |
| Tool-R1 (Zhang et al., 2025) | `2509.12867` | 样本高效的 Agent 工具使用 RL 训练 | **代表性** — 数据效率 |
| SFR-DeepResearch (Nguyen et al., 2025) | `2509.06283` | 面向深度研究场景的单 Agent RL 训练 | **代表性** — 复杂推理 |
| MO-GRPO (Ichihara et al., 2025) | `2509.22047` | 多目标 GRPO，缓解 GRPO 在多目标场景下的 Reward Hacking | **代表性** — 多目标扩展 |
| GRPO-VPS (Wang et al., 2026) | `2604.20659` | 将可验证过程监督与 GRPO 结合，提升推理训练质量 | **代表性** — 过程监督融合 |
| Unifying GRPO & Self-Distillation (Li et al., 2026) | `2604.02288` | 通过样本路由统一 GRPO 和自蒸馏方法 | **最新** — 统一框架 |
| Post-Training is About States (Nie et al., 2026) | `2605.22731` | 从状态分布视角统一 SFT/RL/Distillation；post-training 本质是 state distribution 优化 | **最新** — 理论统一 |
| Mechanistic Analysis (Sinha et al., 2026) | `2606.09850` | 从可解释性视角分析 DPO/RLHF 如何重塑模型内部计算 | **最新** — 新视角 |
| On the Non-decoupling of SFT and RL (Niu et al., 2026) | `2601.07389` | 揭示 SFT 与 RL 在 post-training 中不可解耦的内在联系 | **代表性** — 方法关系澄清 |
| Supervised Fine-Tuning vs RL (Jiang et al., 2026) | `2603.13985` | 系统对比 SFT 与 RL 在 post-training 中的效果差异及适用场景 | **代表性** — 实证对比 |
| The Flip Side of RLHF (Wang et al., 2026) | `2605.30888` | On-policy 反馈用于 RM 自监督改进 | **最新** — RM 自我进化 |
| SLEA-RL (Wang et al., 2026) | `2603.18079` | 步骤级经验增强的 Agent RL 训练 | **最新** — Agent RL 前沿 |
| ASTRA (Tian et al., 2026) | `2601.21558` | 自动化 Agent 轨迹合成和 RL 训练环境构建 | **最新** — Agent RL 基础设施 |
| SCRIBE (Jiang et al., 2026) | `2601.03555` | 结构化中层监督用于工具使用 LLM 训练 | **最新** — Credit Assignment |
| Understanding R1-Zero-Like Training (Liu et al., 2025) | `2503.20783` | 对 R1-Zero 类纯 RL 训练提供批判性视角 | **最新** — 反思性 |
| The Leaderboard Illusion (Singh et al., 2025) | `2504.20879` | 系统性揭示 benchmark 排行榜的误导性 | **争议/重要** — 评估生态批评 |
| Investigating Non-Transitivity in LLM-as-a-Judge (Xu et al., 2025) | `2502.14074` | 发现 LLM 评判存在非传递性问题，动摇 Elo 评分基础 | **争议/重要** — 评估方法论危机 |

---

## 6. 未解决问题

### 6.1 理论与方法层面

| 问题 | 严重程度 | 说明 |
|------|----------|------|
| **DPO 与 RLHF 的真实性能差距** | 高 | DPO 是否在所有场景下都能匹配或超越 RLHF？Conditional Equivalence 论文 (`2605.20834`) 揭示二者等价需要严格假设，实证中 DPO 在分布外泛化上可能弱于在线 RLHF |
| **Reward Hacking 的系统性解决方案** | 高 | 从 PPO 时代的 RM overoptimization 到 GRPO 时代的 Reward Hacking (`2509.22047`; `2604.13602`)，至今缺乏通用解决方案。Emergent Misalignment (`2511.18397`) 表明生产环境中 reward hacking 会自发出现 |
| **非可验证域的 RLVR** | 高 | GRPO/R1 范式强烈依赖 ground-truth 可验证奖励 (数学、代码)，在创意写作、对话、道德判断等主观领域缺乏有效方法。References Improve LLM Alignment (`2602.16802`) 试图使用 reference 替代 verifiable reward，但仍处早期 |
| **过程监督 vs 结果监督的本质权衡** | 中 | PRM 提供细粒度信号但获取成本高且自身可被 hacking (`2501.07301`)；ORM 简单但奖励稀疏。二者的实际效果差异在不同任务上不一致 |
| **SFT 与 RL 的解耦性** | 中 | `2601.07389` 和 `2605.22731` 从不同角度论证 SFT 与 RL 共享底层机制，这对未来 post-training pipeline 设计有深远影响，但尚未形成操作共识 |
| **GRPO 的理论完备性** | 中 | 虽然 Demystifying GRPO (`2603.01162`) 提供了 U-Statistic 视角，但 GRPO 的收敛性、最优性、与 PPO 的理论关系仍有待完善 |

### 6.2 评估与 benchmark 层面

| 问题 | 严重程度 | 说明 |
|------|----------|------|
| **LLM-as-Judge 的可靠性** | 高 | 长度偏差 (`2404.04475`)、位置偏差、非传递性 (`2502.14074`) 和 null model 攻击 (`2410.07137`) 持续挑战自动评估的可信度 |
| **Benchmark 排行榜的生态危害** | 中 | The Leaderboard Illusion (`2504.20879`) 揭示排行榜已成为优化目标而非科学测量工具 |
| **对齐效果的长期稳定性** | 中 | 现有评估均为静态快照，缺乏对模型在持续交互中 alignment drift 的监测 |

### 6.3 Agentic RL 特有挑战

| 问题 | 严重程度 | 说明 |
|------|----------|------|
| **Credit Assignment in Multi-Step Tasks** | 高 | 多步 Agent 任务中，最终失败难以归因到具体步骤。SCRIBE (`2601.03555`) 和 SLEA-RL (`2603.18079`) 提供了部分方案，但远未解决 |
| **训练-部署分布偏移** | 高 | Agent 在训练环境中接触的 API/工具与部署时不同；工具可用性、API 行为变化导致训练失效 |
| **Agent 训练的可扩展性** | 中 | 环境交互成本随任务复杂度增长，Tool-R1 (`2509.12867`) 从数据效率角度缓解但未根本解决 |

---

## 7. 未来方向

### 7.1 短期方向 (1-2 年，已有初步探索)

1. **RLVR → 通用对齐的统一框架**
   - 将 GRPO/RLVR 从可验证域扩展到非可验证域（如用 AI 反馈或弱监督信号替代 ground-truth reward）
   - 代表性探索: References Improve LLM Alignment (`2602.16802`), The Flip Side of RLHF (`2605.30888`)

2. **在线 + 离线混合偏好优化**
   - 结合离线 DPO 的高效性和在线 RL 的探索能力
   - 代表性探索: Online DPO (`2406.05534`), Self-Exploring LMs (`2405.19332`)

3. **Agent RL 的方法论固化**
   - 将 RLVR 范式中验证的方法 (GRPO, PRM) 系统化迁移至 Agent 训练
   - 代表性探索: Agent-R1 (`2511.14460`), Tool-R1 (`2509.12867`), SLEA-RL (`2603.18079`)

4. **评估基础设施的修复**
   - 解决 LLM-as-Judge 的非传递性、偏差和可欺骗性问题
   - 代表性探索: Non-Transitivity (`2502.14074`), JudgeBench (`2410.12784`)

### 7.2 中期方向 (2-4 年，需要基础突破)

5. **自演化对齐 (Self-Improving Alignment)**
   - 模型在部署后持续通过自身经验改进对齐质量，无需人工介入
   - 挑战: 如何防止自我强化导致的 alignment drift / emergent misalignment

6. **多智能体对齐 (Multi-Agent Alignment)**
   - 多 LLM Agent 系统中的对齐问题：协作、竞争、博弈均衡
   - 挑战: 宪法的多智能体扩展、协调中的 emergent 行为

7. **Post-Training 的统一理论**
   - 将 SFT、RLHF、DPO、GRPO 统一到同一理论框架下
   - 早期探索: Post-Training is About States (`2605.22731`), Conditional Equivalence (`2605.20834`)

### 7.3 长期方向 (4-6 年，需要范式突破)

8. **超越偏好的对齐信号**
   - 当前所有方法依赖偏好信号 (人类偏好、AI 偏好、ground-truth 奖励)。是否存在更根本的对齐信号？
   - 可能方向: Causal Rewards (`2501.09620`), 信息论对齐, 博弈论对齐

9. **对齐与能力获取的统一**
   - 当前 pre-training、post-training (SFT+RL)、inference 三阶段分离。未来可能融合为端到端的能力获取 + 对齐过程

---

## 8. 有待验证的关键假设

根据 query_plan 记录的检索假设，结合 paper_inventory 分析结果：

| 假设 | 验证状态 | 证据 |
|------|----------|------|
| **假设 2**: DPO 出现后基于 RM 的 RLHF 工作大幅减少 | **部分成立** | Paper inventory 显示 Q3 (PPO-RLHF) 仍有 42 篇，Q4 (DPO 变体) 80 篇。DPO 流行但 PPO-RLHF 未消失，而是向 Online RLHF、Iterative RLHF 方向演化 |
| **假设 3**: GRPO 和 Agentic RL 是 2024-2026 新兴方向 | **成立** | GRPO 31 篇（全部 2025-2026），Agentic RL 64 篇（集中 2024-2026）。增速极快 |
| **假设 4**: 2024 后 SFT 研究更多关注数据质量而非方法创新 | **成立** | Q1 (SFT) 中 2025-2026 论文多关注 SFT 与 RL 的关系 (`2601.07389`, `2603.13985`, `2605.22731`)，而非新的 SFT 方法 |
| **假设 5**: 工业界论文技术细节不完整 | **推断 (未充分验证)** | Llama 2 (`2307.09288`) 提供了详细细节；但 OpenAI 的 InstructGPT `2203.02155` 和 DeepSeek-R1 `2501.12948` 的技术报告质量较高；需社区复现验证 |

---

## 9. 论文影响力标注说明

本文使用以下标签区分论文地位：

- **开创性 (Pioneering)**: 定义新方向或新范式的论文。如 DPO `2305.18290`、DeepSeek-R1 `2501.12948`、InstructGPT `2203.02155`
- **代表性 (Representative)**: 体现某方向标准方法的论文。如 ORPO `2403.07691`、UltraFeedback `2310.01377`
- **最新 (Recent/Frontier)**: 2025-2026 年前沿工作，影响力待验证。如 ASTRA `2601.21558`
- **争议/重要 (Controversial/Important)**: 挑战主流观点的论文。如 Cheating Benchmarks `2410.07137`、The Leaderboard Illusion `2504.20879`
- **推断关系**: 本文中论文之间的派生、影响关系基于引用模式和方法相似性推断，非正式学术谱系

---

*生成时间: 2026-06-23 | 数据源: research/paper_inventory.md (280 篇), research/query_plan.md*
