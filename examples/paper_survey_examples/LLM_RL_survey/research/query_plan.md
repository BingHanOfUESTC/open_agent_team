# 检索计划：LLM 强化学习后训练 (LLM RL Post-Training)

> **生成时间**: 2026-06-23
> **生成 Agent**: query_planning_agent
> **目标**: 将「LLM 强化学习后训练」拆解为可执行、可复现的系统化检索计划

---

## 1. 任务类型

**Systematic Literature Review / 系统性文献综述**

覆盖从基础 SFT、RLHF 到最新偏好优化方法的完整演进路径。

---

## 2. 研究问题拆解

主问题：**LLM 强化学习后训练方法论全景** 拆解为以下 7 个子问题（每个可独立检索）：

| 编号 | 子问题 | 描述 | 典型论文锚点（仅作方向锚定，非预判结论） |
|------|--------|------|------------------------------------------|
| Q1 | **SFT 基础** | 监督微调在 LLM 后训练中的角色、数据构建策略、与 RL 的关系 | InstructGPT SFT 阶段、Self-Instruct、LIMA |
| Q2 | **Reward Modeling** | 奖励模型的设计、训练、泛化性、Reward Hacking 问题 | InstructGPT RM、Constitutional AI 的 RLAIF、reward over-optimization |
| Q3 | **PPO-based RLHF** | PPO 在 LLM 对齐中的算法改进、训练稳定性、scaling 特性 | InstructGPT PPO、Llama 2 RLHF、RL4LMs |
| Q4 | **DPO 及变体** | 直接偏好优化的方法族：DPO、KTO、ORPO、SimPO、CPO 等 | DPO (NeurIPS 2023)、及其后续变体 |
| Q5 | **GRPO 及 Group-wise 方法** | 基于组相对策略优化的方法，包括与 PPO 的对比 | GRPO 论文及其拓展 |
| Q6 | **Agentic RL** | 用于 Agent 能力训练的 RL 方法：tool use、multi-step reasoning、code generation | WebGPT、Toolformer、ReAct + RL |
| Q7 | **评估与 Benchmark** | 对齐评估框架、benchmark、human evaluation 方法论 | AlpacaEval、MT-Bench、Chatbot Arena |

---

## 3. 核心关键词

### 3.1 一级关键词（统领全局）

**中文**：
- 大语言模型 强化学习 后训练
- 人类反馈强化学习
- 偏好对齐 偏好优化
- 直接偏好优化
- 奖励建模
- LLM 对齐训练

**English**：
- LLM post-training, LLM alignment
- Reinforcement Learning from Human Feedback (RLHF)
- Preference Optimization
- Reward Modeling
- Language Model Alignment
- Instruction Tuning

### 3.2 二级关键词（按子方向）

#### Q1 — SFT 基础
| English | 中文 / 同义词 |
|---------|-------------|
| Supervised Fine-Tuning | 监督微调、指令微调 |
| Instruction Tuning | 指令调优 |
| Self-Instruct | 自指令生成 |
| SFT data curation | SFT 数据构建 |
| Instruction following | 指令遵循 |
| Demonstration data | 示范数据 |

#### Q2 — Reward Modeling
| English | 中文 / 同义词 |
|---------|-------------|
| Reward Model (RM) | 奖励模型 |
| Preference Model | 偏好模型 |
| Bradley-Terry model | Bradley-Terry 偏好模型 |
| Reward hacking / over-optimization | 奖励破解、过度优化 |
| RLAIF (RL from AI Feedback) | AI 反馈强化学习 |
| Constitutional AI | 宪法式 AI |

#### Q3 — PPO-based RLHF
| English | 中文 / 同义词 |
|---------|-------------|
| Proximal Policy Optimization | 近端策略优化 |
| PPO in LLM | PPO 大模型应用 |
| KL penalty / KL divergence | KL 散度惩罚 |
| Policy gradient | 策略梯度 |
| Actor-critic | 演员-评论家 |
| RL4LMs | 语言模型强化学习框架 |

#### Q4 — DPO 及变体
| English | 中文 / 同义词 |
|---------|-------------|
| Direct Preference Optimization (DPO) | 直接偏好优化 |
| Kahneman-Tversky Optimization (KTO) | KTO 优化 |
| Odds Ratio Preference Optimization (ORPO) | ORPO 优化 |
| Simple Preference Optimization (SimPO) | SimPO 优化 |
| Contrastive Preference Optimization (CPO) | CPO 对比偏好优化 |
| Identity Preference Optimization (IPO) | IPO |
| Iterative DPO | 迭代 DPO |
| Offline / Online DPO | 离线/在线 DPO |
| Reference-free / length-normalized | 无参考模型、长度归一化 |

#### Q5 — GRPO 及 Group-wise 方法
| English | 中文 / 同义词 |
|---------|-------------|
| Group Relative Policy Optimization (GRPO) | 组相对策略优化 |
| Group-wise comparison | 组内比较 |
| Multi-sample evaluation | 多样本评估 |
| Outcome reward model (ORM) | 结果奖励模型 |
| Process reward model (PRM) | 过程奖励模型 |

#### Q6 — Agentic RL
| English | 中文 / 同义词 |
|---------|-------------|
| Agentic RL / LLM Agents | Agent 强化学习 |
| Tool use / tool calling | 工具调用 |
| Multi-step reasoning RL | 多步推理强化学习 |
| WebGPT / WebAgent | 网络 Agent |
| Code generation RL | 代码生成 RL |
| Reinforcement learning for reasoning | 推理增强 RL |
| Grounding / environment interaction | 环境交互 |

#### Q7 — 评估与 Benchmark
| English | 中文 / 同义词 |
|---------|-------------|
| AlpacaEval | 羊驼评估 |
| MT-Bench | 多轮对话基准 |
| Chatbot Arena / Elo rating | 聊天竞技场、Elo 评分 |
| Human evaluation | 人工评估 |
| Win rate / preference rate | 胜率 / 偏好率 |
| Alignment benchmark | 对齐基准 |

---

## 4. 同义词和相关术语（扩展检索用）

```text
# 概念等价组
"RLHF" ≈ "reinforcement learning from human feedback" ≈ "human preference alignment"
"DPO" ≈ "direct preference optimization" ≈ "offline preference learning"
"PPO" ≈ "proximal policy optimization" ≈ "trust region policy optimization variant"
"SFT" ≈ "supervised fine-tuning" ≈ "instruction tuning" ≈ "behavior cloning"
"Reward Model" ≈ "preference predictor" ≈ "scoring model"
"Alignment" ≈ "value alignment" ≈ "preference alignment" ≈ "safety tuning"

# 方法边界
- DPO 及其变体 ≠ 传统 RL（无需显式奖励模型）
- GRPO ≠ PPO（组相对 vs. 绝对奖励）
- SFT 单独使用 ≠ RLHF/DPO（但常作为前置步骤，需在检索时区分）
```

---

## 5. 领域边界

### 明确纳入
- LLM（参数量 > 1B）的后训练阶段方法
- 基于人类偏好或 AI 反馈的对齐方法
- 在线 RL（PPO 类）和离线偏好优化（DPO 类）
- 用于 Agent 场景的 RL 后训练
- Reward Modeling 方法

### 明确排除
- 预训练阶段的 RL 方法（如 expert iteration for pretraining）
- 纯视觉或多模态模型的对齐（除非方法可迁移到 LLM）
- 传统 NLP 任务中的 RL（非生成式 LLM 场景）
- 纯推理时对齐（如 prompt engineering、decoding strategies，除非与训练协同）
- 联邦学习、隐私保护等与后训练正交的方向
- 纯哲学/伦理讨论无具体算法的论文

### 边界模糊需人工判断
- Small LM（<1B）的 RLHF 实验（如有方法论贡献可纳入）
- Diffusion LLM 的偏好优化（新兴方向，视发展程度决定）
- RL for reasoning（如 DeepSeek-R1 类 o1 风格训练，若涉及 RL 后训练可纳入）

---

## 6. 时间范围

| 阶段 | 时间窗口 | 重点 | 策略 |
|------|----------|------|------|
| **奠基期** | 2017–2020 | PPO 原始论文、RLHF 概念萌芽、GPT-2/3 发布 | 仅纳入里程碑论文（3–5 篇） |
| **成型期** | 2021–2022 | InstructGPT、Constitutional AI、RL4LMs、WebGPT | 核心方法论文全覆盖 |
| **爆发期** | 2023 | DPO 提出、Llama 2 RLHF、开源 RLHF 框架 | 高密度检索，DPO 为转折点 |
| **深化期** | 2024–2026 | DPO 变体爆发 (KTO/ORPO/SimPO/CPO)、GRPO、Agentic RL | 全量跟踪，关注对比实验 |

**检索优先级**：2023–2026 > 2021–2022 > 2017–2020

**特殊规则**：
- PPO 原始论文 (Schulman et al., 2017) 作为背景方法，必须纳入
- 任何 2025–2026 的 DPO 新变体论文，优先检索最新 arxiv 版本
- 2024–2026 GRPO 和 Agentic RL 方向需以月为单位追踪

---

## 7. 来源优先级

| 优先级 | 来源 | 用途 | 说明 |
|--------|------|------|------|
| **P0** | **arXiv API** (`cs.CL`, `cs.LG`, `cs.AI`) | 主检索源，覆盖所有预印本 | 速度最快、覆盖面最广 |
| **P0** | **Papers with Code** | 获取 SOTA 榜单、benchmark 结果、代码链接 | 验证论文实际影响力 |
| **P1** | **HuggingFace Papers** | 获取论文元数据、关联模型/Dataset/Space | 社区精选，信息结构化 |
| **P1** | **Semantic Scholar API** | 获取引用关系、影响力指标 | 发现经典论文和引用脉络 |
| **P1** | **OpenReview** | 获取 NeurIPS/ICML/ICLR 同行评审 | 了解方法争议和审稿人评价 |
| **P2** | **Google Scholar** | 补充引用追踪、发现灰色文献 | 作为交叉验证 |
| **P2** | **Conference Proceedings** (NeurIPS, ICML, ICLR, ACL, EMNLP) | 确认正式发表版本 | 与 arXiv 版本对比，关注修改 |
| **P3** | **Twitter/X / Reddit / 知乎** | 发现社区热点和最新 pre-print | 仅作发现渠道，不作为事实源 |
| **P3** | **GitHub Trending** | 发现高星开源 RLHF 框架 | 反映工程落地热度 |

**检索流程**：
```
arXiv API 初筛 → Papers with Code 验证影响力 → HuggingFace 获取元数据
→ Semantic Scholar 追踪引用 → OpenReview 查看评审（如适用）
```

---

## 8. 纳入标准

一篇论文必须满足以下**至少 3 项**才能纳入：

1. **方法贡献**：提出新的 RLHF/偏好优化方法或对现有方法的实质性改进
2. **实证规模**：在 ≥7B 参数 LLM 上有实验验证（奠基性方法论文可放宽）
3. **引用影响力**：发表后 1 年内引用 > 50（新论文可放宽，以社区讨论度替代）
4. **开源可复现**：提供代码或权重（纯理论论文需方法足够清晰可复现）
5. **benchmark 验证**：在 AlpacaEval / MT-Bench / Chatbot Arena 等标准 benchmark 上有结果
6. **里程碑意义**：被领域综述引用或被视为某子方向的奠基工作（如 InstructGPT, DPO）

**特别纳入**（不满足数量要求但必须纳入）：
- PPO 原始论文 (Schulman et al., 2017) — 方法基础
- InstructGPT (Ouyang et al., 2022) — RLHF 范式确立
- DPO (Rafailov et al., 2023) — 偏好优化转折点
- Llama 2 (Touvron et al., 2023) — 工业级 RLHF 实践

---

## 9. 排除标准

以下类型论文应**排除**：

1. **纯应用无方法贡献**：仅将现有 RLHF 方法应用于特定领域（如医疗、法律）而无方法改进
2. **实验薄弱的宣传性论文**：方案描述为主，缺少严格消融或对比实验
3. **未经验证的纯理论**：仅在 toy setting 上验证的纯理论分析（除非有领域公认的理论贡献）
4. **低质量预印本**：无作者机构信息、无实验、格式混乱的 arXiv 预印本
5. **重复发表**：同一方法的多版本预印本，仅保留最新或会议版本
6. **非 LLM 场景**：将 PPO/DPO 用于非语言场景（如 robotic control）但未讨论 LLM 迁移性
7. **语言障碍**：非中英文且无英文版本的主要论文

**降级观察（暂不纳入，但标记跟踪）**：
- arXiv 新论文（< 3 个月）且无引用、无代码、无社区讨论
- 仅在中文预印本平台发布、未被国际社区关注的方法

---

## 10. 检索式

### 10.1 arXiv API 检索式

#### 通用检索（宽覆盖，后续人工筛选）

```text
# 检索式 1：RLHF 核心检索
cat:cs.CL OR cat:cs.LG OR cat:cs.AI
AND (all:"reinforcement learning from human feedback" OR all:"RLHF" OR all:"human feedback" AND all:"language model")

# 检索式 2：偏好优化（避开纯 RL 论文）
cat:cs.CL OR cat:cs.LG OR cat:cs.AI
AND (all:"preference optimization" OR all:"preference learning")
AND (all:"large language model" OR all:"LLM" OR all:"language model alignment")

# 检索式 3：DPO 及变体
cat:cs.CL OR cat:cs.LG
AND (all:"direct preference optimization" OR all:"KTO" OR all:"ORPO" OR all:"SimPO" OR all:"CPO" OR all:"contrastive preference optimization" OR all:"odds ratio preference optimization")
```

#### 子方向专项检索

```text
# 检索式 4：PPO in LLM
cat:cs.CL OR cat:cs.LG
AND (all:"proximal policy optimization" OR all:"PPO")
AND (all:"language model" OR all:"LLM" OR all:"RLHF")
AND NOT (all:"robotics" OR all:"game" OR all:"Atari")

# 检索式 5：Reward Modeling
cat:cs.CL OR cat:cs.LG
AND (all:"reward model" OR all:"reward modeling" OR all:"reward hacking")
AND (all:"language model" OR all:"LLM" OR all:"alignment")

# 检索式 6：RLAIF / Constitutional AI
cat:cs.CL OR cat:cs.AI
AND (all:"RLAIF" OR all:"constitutional AI" OR all:"AI feedback" OR all:"synthetic feedback")
AND (all:"language model" OR all:"alignment")

# 检索式 7：GRPO
cat:cs.CL OR cat:cs.LG
AND (all:"group relative policy optimization" OR all:"GRPO" OR all:"group-wise" AND all:"preference")

# 检索式 8：Agentic RL
cat:cs.CL OR cat:cs.AI
AND (all:"reinforcement learning" OR all:"RL")
AND (all:"agent" OR all:"tool use" OR all:"tool calling" OR all:"reasoning")
AND (all:"language model" OR all:"LLM")
AND NOT (all:"multi-agent" AND all:"game")

# 检索式 9：SFT / Instruction Tuning
cat:cs.CL OR cat:cs.LG
AND (all:"supervised fine-tuning" OR all:"instruction tuning" OR all:"SFT")
AND (all:"language model" OR all:"LLM")
AND NOT (all:"pre-training" AND NOT all:"post-training")

# 检索式 10：评估 Benchmark
cat:cs.CL
AND (all:"AlpacaEval" OR all:"MT-Bench" OR all:"chatbot arena" OR all:"LLM evaluation" OR all:"alignment evaluation")
```

### 10.2 组合检索策略

```text
Phase 1 — 广度优先（用检索式 1+2+3）
  目标：获取所有 LLM RLHF 相关论文，建立 paper_inventory
  预计论文量：300–500 篇 → 去重后约 200–300 篇

Phase 2 — 专项补充（用检索式 4–10）
  目标：填补各子方向的论文
  预计各子方向增量：20–50 篇

Phase 3 — 引用追踪
  用 Semantic Scholar API 追踪里程碑论文的被引和引用关系
  发现遗漏的高影响力论文

Phase 4 — 人工筛选
  按纳入/排除标准过滤，形成最终 paper_inventory
  预计最终纳入：60–100 篇核心论文
```

### 10.3 经典论文固定检索（不依赖 API，直接验证）

| 论文 | 检索方式 | 验证点 |
|------|----------|--------|
| PPO (Schulman et al., 2017) | arXiv ID: `1707.06347` | 确认原始方法 |
| InstructGPT (Ouyang et al., 2022) | arXiv ID: `2203.02155` | RLHF 范式确立 |
| DPO (Rafailov et al., 2023) | arXiv ID: `2305.18290` | 偏好优化转折点 |
| Llama 2 (Touvron et al., 2023) | arXiv ID: `2307.09288` | 工业级 RLHF |
| Constitutional AI (Bai et al., 2022) | arXiv ID: `2212.08073` | RLAIF 方法 |
| Training language models to follow instructions (Christiano et al., 2017 / OpenAI) | arXiv 检索 | RLHF 早期探索 |

---

## 11. 潜在偏差

### 11.1 检索偏差
- **arXiv 偏差**：arXiv 以英文学术界为主，可能遗漏中文社区的重要工作（如 DeepSeek 系列的技术报告）
  - **缓解**：补充检索 DeepSeek、Qwen、ChatGLM 等中文团队的技术报告
- **关键词偏差**：不同子方向使用不同术语描述相似概念（如 "alignment" vs "preference optimization"）
  - **缓解**：已在第 4 节记录同义词等价组
- **时间窗口偏差**：2017–2020 的论文可能未被 arXiv 分类标签准确覆盖
  - **缓解**：对经典论文使用固定 ID 检索

### 11.2 选择偏差
- **高引论文优先**：可能遗漏被低估的新方法
  - **缓解**：Phase 2 专项补充不依赖引用量筛选
- **英文优先**：可能遗漏中文技术报告
  - **缓解**：明确将中文重要工作纳入检索
- **明星团队偏差**：OpenAI / Anthropic / Meta / Google 的论文更容易被发现
  - **缓解**：检索时不过滤作者/机构，Phase 4 人工筛选时关注独立团队工作

### 11.3 评估偏差
- **Benchmark 偏差**：AlpacaEval / MT-Bench 等基准本身存在局限性（如长度偏差、位置偏差）
  - **缓解**：检索时同时纳入对 benchmark 的批评性论文
- **Self-reported 偏差**：论文自报的 win rate 可能不可比
  - **缓解**：优先纳入有独立评估或多 benchmark 对比的论文

### 11.4 检索假设记录（必填）
```text
假设 1：LLM RLHF 的核心工作集中在 arXiv cs.CL 和 cs.LG 分类下，cs.AI 作为补充
假设 2：DPO 出现后（2023+），基于奖励模型的 RLHF 工作大幅减少——需验证此趋势是否真实
假设 3：GRPO 和 Agentic RL 是 2024–2026 的新兴方向，论文总量较少但增速快——检索时应降低引用量门槛
假设 4：SFT 作为独立研究方向的论文大部分在 2022–2023，2024 后更关注 SFT 数据质量而非方法创新
假设 5：工业界论文（OpenAI, Anthropic, Meta, Google DeepMind）的技术细节可能不完整，需结合社区复现版本
```

---

## 12. 检索执行计划

```text
Step 1: 执行 Phase 1 检索式（1+2+3），生成 paper_inventory_draft_1.md
Step 2: 执行 Phase 2 检索式（4–10），生成 paper_inventory_draft_2.md
Step 3: 去重、合并，生成 paper_inventory.md
Step 4: 对里程碑论文执行引用追踪（Semantic Scholar）
Step 5: 按纳入/排除标准过滤，标注 confidence level
Step 6: 对每篇纳入论文补充元数据（作者、年份、会议、引用量、代码链接）
Step 7: 输出最终 paper_inventory.md 并进入 lineage_mapping 阶段
```

---

## 附录 A：arXiv 分类标签参考

| 标签 | 全称 | 相关性 |
|------|------|--------|
| `cs.CL` | Computation and Language | **最高** — LLM 对齐论文主力分类 |
| `cs.LG` | Machine Learning | **高** — RL 方法论论文 |
| `cs.AI` | Artificial Intelligence | **中** — Agent / 通用 AI 方法 |
| `stat.ML` | Machine Learning (Statistics) | **低** — 理论分析方法 |

## 附录 B：会议/期刊映射

| 会议 | 偏好优化相关 Session |
|------|---------------------|
| NeurIPS | Oral/Spotlight: Alignment, RL |
| ICML | RL for LLMs, Preference Learning |
| ICLR | LLM alignment, post-training |
| ACL/EMNLP | Instruction tuning, human evaluation |
| COLM | 新兴会议，对齐方向覆盖好 |
