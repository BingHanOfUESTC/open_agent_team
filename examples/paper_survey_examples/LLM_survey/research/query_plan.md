# Query Plan: 大语言模型（LLM）关键论文系统梳理 (2017–2026)

> **Plan 版本**: v1.0
> **生成时间**: 2026-06-23
> **Plan 作者**: query_planning_agent
> **适用范围**: 本计划供 paper_discovery_agent、lineage_mapping_agent、method_taxonomy_agent 等下游 agent 执行检索与筛选。

---

## 1. 任务类型

- **类型**: 系统性文献综述 (Systematic Literature Review)
- **目标**: 梳理自 Transformer (2017) 以来大语言模型发展的关键论文，按时间线和技术路线组织，形成可追溯的发展脉络。
- **交付形式**: 最终产出 `research/paper_inventory.md`（论文清单）+ `research/lineage_map.md`（发展轨迹）+ `research/method_taxonomy.md`（方法分类），为 `delivery/research_survey_report.md` 提供事实基础。

---

## 2. 研究问题拆解

将 Boss 的总体任务分解为 **8 个子问题**，每个子问题对应独立的检索路径：

### 子问题 2.1: Transformer 架构起源与早期变体 (2017–2019)

**核心关注**：从 RNN/LSTM 到自注意力机制的范式转变，Transformer 原始论文及其在 NLP 各任务上的早期适配。

| 维度 | 内容 |
|------|------|
| 必收论文 | "Attention Is All You Need" (Vaswani et al., 2017) |
| 关联论文 | Transformer 在机器翻译、语言建模、文本生成等方向的早期变体 |
| 注意边界 | **不包括** CNN/RNN 架构本身的改进论文；**不包括**图神经网络中的 attention 机制 |

### 子问题 2.2: 预训练范式确立 — BERT 时代 (2018–2020)

**核心关注**：双向上下文编码（BERT 家族）、自回归预训练（GPT-1/2）、编码器-解码器统一框架（T5, BART）。

| 维度 | 内容 |
|------|------|
| 必收论文 | BERT (Devlin et al., 2018), GPT-1 (Radford et al., 2018), GPT-2 (Radford et al., 2019), RoBERTa (Liu et al., 2019), T5 (Raffel et al., 2019), BART (Lewis et al., 2019) |
| 关联论文 | ALBERT, DistilBERT, XLNet, ERNIE 等典型变体 |
| 注意边界 | **不包括**纯任务特定微调技巧论文（如特定 NER/情感分类的微调），除非涉及关键方法创新 |

### 子问题 2.3: Scaling Laws 与 GPT-3 时代 (2020–2022)

**核心关注**：规模化定律（Scaling Laws）、涌现能力、GPT-3 的上下文学习（In-Context Learning）、计算最优训练（Chinchilla）。

| 维度 | 内容 |
|------|------|
| 必收论文 | GPT-3 (Brown et al., 2020), Scaling Laws (Kaplan et al., 2020), Chinchilla (Hoffmann et al., 2022), PaLM (Chowdhery et al., 2022) |
| 关联论文 | Gopher, Megatron-LM, OPT, BLOOM 等大模型训练 |
| 注意边界 | **不包括**纯分布式训练系统论文（如 DeepSpeed/FSDP 底层优化） |

### 子问题 2.4: 指令微调与对齐 (2021–2024)

**核心关注**：从预训练到指令遵循（Instruction Following），RLHF、DPO 等对齐方法，从 InstructGPT 到 GPT-4 的对齐演进。

| 维度 | 内容 |
|------|------|
| 必收论文 | InstructGPT (Ouyang et al., 2022), RLHF (Christiano et al., 2017; Stiennon et al., 2020), DPO (Rafailov et al., 2023), Constitutional AI (Bai et al., 2022), GPT-4 Technical Report (OpenAI, 2023) |
| 关联论文 | FLAN, T0, Self-Instruct, Alpaca, Vicuna, ORCA 等指令数据集与方法 |
| 注意边界 | **不包括**纯强化学习理论论文；**不包括**与 LLM 无关的 preference learning |

### 子问题 2.5: 开源模型生态崛起 (2023–2025)

**核心关注**：LLaMA 系列、Mistral、Qwen、DeepSeek 等开源/开放权重模型的发布、复现与社区生态。

| 维度 | 内容 |
|------|------|
| 必收论文 | LLaMA (Touvron et al., 2023), LLaMA 2 (Touvron et al., 2023), LLaMA 3 (Meta, 2024), LLaMA 3.1 (Meta, 2024), Mistral 7B (Jiang et al., 2023), Mixtral (Jiang et al., 2024), Qwen (Bai et al., 2023), Qwen 2 (Yang et al., 2024), Qwen 2.5 (Yang et al., 2024), DeepSeek-V2/V3 (DeepSeek-AI, 2024) |
| 关联论文 | Yi, Falcon, Gemma, Phi, DBRX, Command R 等 |
| 注意边界 | **不包括**仅基于开源模型微调但无方法创新的衍生模型论文；**不包括**纯模型部署/推理优化论文 |

### 子问题 2.6: 推理增强技术 (2022–2026)

**核心关注**：思维链（Chain-of-Thought）、自一致性、Tree-of-Thought、规划推理、o1/o3 等推理时计算增强。

| 维度 | 内容 |
|------|------|
| 必收论文 | Chain-of-Thought (Wei et al., 2022), Self-Consistency (Wang et al., 2022), Tree-of-Thought (Yao et al., 2023), ReAct (Yao et al., 2022), o1 System Card (OpenAI, 2024), DeepSeek-R1 (DeepSeek-AI, 2025) |
| 关联论文 | Least-to-Most, Program-of-Thought, Graph-of-Thought, STaR, Quiet-STaR |
| 注意边界 | **不包括**纯符号推理/定理证明系统；**不包括**非 LLM-based 的规划算法 |

### 子问题 2.7: 效率与部署 — MoE, 量化, RAG (2021–2026)

**核心关注**：混合专家（MoE）、模型量化（GPTQ/AWQ/GGUF）、检索增强生成（RAG）、KV-cache 压缩、蒸馏等效率技术。

| 维度 | 内容 |
|------|------|
| 必收论文 | Switch Transformer (Fedus et al., 2021), RAG (Lewis et al., 2020), GPTQ (Frantar et al., 2022), AWQ (Lin et al., 2023), Mixtral (Jiang et al., 2024), DeepSeekMoE (Dai et al., 2024) |
| 关联论文 | QLoRA, GGML/GGUF, Sliding Window Attention, FlashAttention, Grouped Query Attention |
| 注意边界 | **不包括**非 LLM 的通用模型压缩论文；**不包括**不涉及 LLM 的信息检索系统 |

### 子问题 2.8: 多模态前沿与 Agent (2023–2026)

**核心关注**：视觉-语言模型（GPT-4V, LLaVA, Qwen-VL）、LLM Agent 框架（AutoGPT, MetaGPT）、长上下文扩展（Long Context）。

| 维度 | 内容 |
|------|------|
| 必收论文 | GPT-4V (OpenAI, 2023), LLaVA (Liu et al., 2023), Gemini (Google, 2023), Claude 3 (Anthropic, 2024), Qwen-VL (Bai et al., 2023) |
| 关联论文 | CogVLM, InternVL, MiniCPM-V, Voyager, SWE-Agent, Gemini 2.0 |
| 注意边界 | **不包括**纯计算机视觉模型（ViT, DETR 等）；**不包括**与语言模型无关的具身智能 |

---

## 3. 核心关键词

### 3.1 一级关键词（方向锚定词）

> 这些词是检索的"锚"，必须出现在检索式中，用于划定方向边界。

| 英文主关键词 | 说明 |
|-------------|------|
| `large language model` / `LLM` | 最通用的锚定词 |
| `transformer` | 架构层面的核心词 |
| `language model pre-training` | 预训练范式 |
| `instruction tuning` | 指令微调范式 |
| `reinforcement learning from human feedback` / `RLHF` | 对齐方法 |
| `chain-of-thought` | 推理方法 |
| `mixture of experts` / `MoE` | 效率架构 |
| `retrieval augmented generation` / `RAG` | 检索增强 |
| `model quantization` | 量化压缩 |
| `open-source LLM` | 开源生态 |

### 3.2 二级关键词（模型/技术名）

> 按子问题分组，用于精准定位具体论文。

**模型系列**：
| 类别 | 关键词 |
|------|--------|
| Transformer 起源 | `Vaswani`, `attention mechanism`, `self-attention`, `multi-head attention` |
| GPT 系列 | `GPT`, `GPT-2`, `GPT-3`, `GPT-4`, `InstructGPT`, `ChatGPT`, `generative pre-trained transformer`, `OpenAI` |
| BERT 家族 | `BERT`, `RoBERTa`, `ALBERT`, `DistilBERT`, `bidirectional encoder`, `masked language model` |
| LLaMA 系列 | `LLaMA`, `LLaMA 2`, `LLaMA 3`, `LLaMA 3.1`, `Meta AI`, `open weights` |
| Qwen 系列 | `Qwen`, `Qwen 2`, `Qwen 2.5`, `Qwen-VL`, `Tongyi Qianwen`, `Alibaba` |
| 其他大模型 | `Mistral`, `Mixtral`, `DeepSeek`, `Chinchilla`, `PaLM`, `Gemini`, `Claude`, `BLOOM`, `OPT`, `Falcon`, `Phi`, `Gemma`, `Yi` |
| 编码器-解码器 | `T5`, `BART`, `text-to-text transfer`, `denoising autoencoder` |

**技术方法**：
| 类别 | 关键词 |
|------|--------|
| 对齐 | `RLHF`, `DPO`, `direct preference optimization`, `PPO`, `constitutional AI`, `alignment tax`, `reward model` |
| 推理 | `chain-of-thought`, `CoT`, `zero-shot CoT`, `self-consistency`, `tree-of-thought`, `ReAct`, `reasoning`, `o1`, `test-time compute` |
| 效率 | `MoE`, `mixture of experts`, `quantization`, `GPTQ`, `AWQ`, `GGUF`, `QLoRA`, `LoRA`, `distillation`, `pruning`, `KV cache` |
| 检索 | `RAG`, `retrieval augmented`, `dense retrieval`, `hybrid search` |
| 长上下文 | `long context`, `RoPE`, `position interpolation`, `context window extension` |

### 3.3 中文对照关键词

> 用于中文数据库（知网、万方）辅助检索，标注英文对应关系。

| 中文术语 | 对应英文 |
|---------|---------|
| 大语言模型 | Large Language Model (LLM) |
| 预训练语言模型 | Pre-trained Language Model (PLM) |
| 自注意力机制 | Self-Attention Mechanism |
| 指令微调 | Instruction Tuning / Instruction Fine-tuning |
| 基于人类反馈的强化学习 | RLHF (Reinforcement Learning from Human Feedback) |
| 思维链 | Chain-of-Thought (CoT) |
| 混合专家 | Mixture of Experts (MoE) |
| 检索增强生成 | Retrieval-Augmented Generation (RAG) |
| 模型量化 | Model Quantization |
| 涌现能力 | Emergent Abilities |
| 规模化定律 | Scaling Laws |
| 上下文学习 | In-Context Learning |

---

## 4. 同义词和相关术语

> 下表定义不同表述之间的等价/近似关系，防止因用词不同而漏检。

| 标准术语 | 同义词 / 等价表述 | 注意区分 |
|---------|------------------|---------|
| `Large Language Model` (LLM) | `foundation model`, `large pre-trained language model`, `large-scale language model` | **不等于** Small Language Model (SLM)；**不等于** general "Neural Language Model" (2017 前) |
| `Transformer` | `self-attention network`, `attention-based architecture` | **不等于** "attention mechanism" (1980s 概念)；**不等于** "Graph Attention Network" (GAT) |
| `GPT` | `Generative Pre-trained Transformer`, `GPT-N` | **不等于** "GPT" as GUID Partition Table；**不等于** "ChatGPT" (产品名而非模型论文) |
| `Instruction Tuning` | `instruction fine-tuning`, `supervised fine-tuning (SFT)`, `prompt-based fine-tuning` | **不等于** general `fine-tuning` (BERT 时代的 fine-tuning)；**不等于** `prompt engineering` |
| `RLHF` | `reinforcement learning from human feedback`, `RL from human preferences`, `preference-based RL` | **不等于** `DPO` (替代方法, 非强化学习)；**不等于** generic `RL` in games/robotics |
| `Chain-of-Thought` | `CoT`, `reasoning chain`, `step-by-step reasoning`, `intermediate reasoning steps` | **不等于** `scratchpad` (更早期的概念)；**不等于** `self-explanation` |
| `RAG` | `retrieval-augmented generation`, `retrieval-enhanced LM`, `grounded generation` | **不等于** `open-book QA` (任务而非方法)；**不等于** `knowledge-enhanced LM` (不涉及实时检索) |
| `MoE` | `mixture of experts`, `sparsely-gated MoE`, `conditional computation` | **不等于** `ensemble` (集成学习)；**不等于** `multi-task learning` |
| `Quantization` | `model compression`, `weight quantization`, `PTQ` (post-training quantization), `QAT` (quantization-aware training) | **不等于** `pruning` (剪枝)；**不等于** `knowledge distillation` (蒸馏) |
| `Open-source LLM` | `open-weight model`, `publicly available LLM`, `community model` | **不等于** `open-source` in strict OSI sense (多数开放模型仅开放权重)；**不等于** `open data` |

---

## 5. 领域边界

> 明确「研究什么」和「不研究什么」，防止检索范围漂移。

### 5.1 包含范围 (In-scope)

- **架构**: Transformer 及其变体 (encoder-only, decoder-only, encoder-decoder)
- **模型规模**: 从 millions 到 trillions 参数的语言模型
- **任务**: 自然语言生成、理解、推理（核心 NLP 任务 + 涌现能力）
- **方法**: 预训练、微调、对齐、推理增强、效率优化
- **时间**: 2017-06（Transformer 论文发布）至 2026-06（当前）
- **来源类型**: 正式发表论文、arXiv 预印本、技术报告、会议论文 (NeurIPS, ICML, ICLR, ACL, EMNLP, NAACL 等)

### 5.2 排除范围 (Out-of-scope)

- **非 Transformer 架构**: RNN/LSTM/CNN 语言模型改进（2017 年前已进入成熟期）
- **纯视觉模型**: ViT (Vision Transformer) 本身属于 CV 方向，除非与语言模型有直接交叉（如多模态 LLM）
- **非语言大模型**: 蛋白质折叠、气象预测、分子生成等领域的 foundation model（即使使用 Transformer）
- **纯系统工程**: 分布式训练框架（DeepSpeed/FSDP）、推理引擎（vLLM/TGI）的纯系统论文
- **纯产品/商业**: ChatGPT 产品迭代、API 定价策略、用户体验研究
- **纯教育/评测**: 仅评测 LLM 在某任务上的表现但无方法创新
- **纯社会科学**: LLM 的社会影响、伦理、法规（除非是技术层面 bias/fairness 方法）

### 5.3 边界案例处理规则

| 边界论文类型 | 判定规则 |
|------------|---------|
| Diffusion Language Models | 若持续被社区关注且有与 autoregressive 对比 → **纳入** |
| State Space Models (Mamba, etc.) | 若作为 Transformer 替代方案有重要影响 → **纳入**作为对比 |
| Code Generation Models (Codex, StarCoder) | 若对 LLM 训练方法论有贡献 → **纳入**；纯代码评测 → **排除** |
| Speech/Music LLMs | 仅纳入对 NLP LLM 有直接技术回馈的 → 否则 **排除** |
| Small Language Models (<1B) | 若有方法创新（如 Phi 系列的数据质量方法） → **纳入**；纯模型发布 → **排除** |

---

## 6. 时间范围

### 6.1 阶段划分

| 阶段 | 时间 | 标签 | 关键事件与检索重心 |
|------|------|------|-------------------|
| **Phase 0: 前奏** | 2017-06 ~ 2017-12 | Transformer 诞生 | Transformer 原始论文及其首次引用；关注 encoder-decoder 架构 |
| **Phase 1: 预训练萌芽** | 2018-01 ~ 2019-06 | BERT + GPT 范式确立 | BERT 系列 (encoder-only)、GPT-1/GPT-2 (decoder-only) 奠定两个流派；ELMo, ULMFiT 等过渡性工作 |
| **Phase 2: 大一统与规模化** | 2019-06 ~ 2020-12 | T5 统一 + GPT-3 震撼 | T5/BART 统一框架；GPT-3 展示 in-context learning；Scaling Laws 提出 |
| **Phase 3: 对齐与推理** | 2021-01 ~ 2022-12 | InstructGPT + CoT | 指令微调 (FLAN, T0)、RLHF (InstructGPT)、思维链 (CoT)；Chinchilla 最优计算；PaLM 涌现 |
| **Phase 4: 开源爆发** | 2023-01 ~ 2023-12 | LLaMA 效应 | LLaMA 1 泄露引发开源浪潮；Mistral, Qwen, DeepSeek 纷纷入局；GPT-4 发布；DPO 提出 |
| **Phase 5: 多模态与推理深化** | 2024-01 ~ 2024-12 | 视觉语言 + o1 推理 | GPT-4V/GPT-4o、LLaMA 3、Mixtral、Qwen 2/2.5、Claude 3/3.5、Gemini 2；o1 推理范式；长上下文 |
| **Phase 6: 前沿** | 2025-01 ~ 2026-06 | Agent + DeepSeek 突破 | DeepSeek-R1/V3、Agent 框架、推理时计算、开源追赶闭源、超长上下文 |

### 6.2 各子问题的时间范围

| 子问题 | 主检索窗口 | 备注 |
|--------|----------|------|
| 2.1 Transformer 起源 | 2017-06 ~ 2019-12 | 早期变体可在 2019 前截断 |
| 2.2 BERT 时代 | 2018-01 ~ 2020-12 | 可放宽至 2021 用于 ALBERT 等后续工作 |
| 2.3 Scaling Laws + GPT-3 | 2020-01 ~ 2022-12 | Kaplan (2020) 为起点 |
| 2.4 指令微调与对齐 | 2021-01 ~ 2024-12 | RLHF 起源可上溯至 2017 (Christiano) |
| 2.5 开源生态 | 2023-01 ~ 2025-12 | 核心爆发在 2023-2024 |
| 2.6 推理增强 | 2022-01 ~ 2026-06 | CoT (2022) 为起点 |
| 2.7 效率与部署 | 2020-01 ~ 2026-06 | RAG (2020), Switch Transformer (2021) |
| 2.8 多模态 + Agent | 2023-01 ~ 2026-06 | 2023 为主起点 |

---

## 7. 来源优先级

### 7.1 来源分级

| 优先级 | 来源 | 用途 | 说明 |
|--------|------|------|------|
| **P0 (第一优先)** | arXiv (arxiv.org) | 论文元数据、全文预印本 | ML/NLP 领域的事实标准预印本平台；覆盖 95%+ 目标论文；`cs.CL`, `cs.LG`, `cs.AI` 类别 |
| **P0** | Hugging Face Papers | 论文元数据、模型卡片、关联模型 | 与 arXiv 互补，提供模型/数据集/代码链接；适合开源模型追踪 |
| **P1 (第二优先)** | Papers with Code | 论文-任务-代码关联、benchmark 排名 | 用于验证论文影响力（SOTA 声明）、发现同类方法 |
| **P1** | OpenReview | 会议论文评审意见 | 用于读 NeurIPS/ICML/ICLR 论文时获取同行评议 |
| **P2 (第三优先)** | Semantic Scholar / Google Scholar | 引用图、作者影响力 | 辅助构建 lineage_map；不可作为唯一来源 |
| **P2** | 官方技术报告 (OpenAI, Meta, Google, Anthropic, DeepSeek 等) | 获取未发表于会议的模型细节 | GPT-4/Gemini/Claude 等闭源模型的主要信息来源 |
| **P3 (补充)** | 中文来源 (知网 CNKI, 万方) | 中文语境下的 LLM 综述 | 仅用于补充视角，非主要来源 |
| **P3** | GitHub / Hugging Face Hub | 代码、模型权重 | 用于验证开源论文的可复现性 |

### 7.2 来源使用规则

1. **主体检索**必须走 arXiv API（`systematic-literature-review` skill 内置脚本）。
2. Hugging Face Papers 用于补充模型元数据和发现"非 arXiv 首发"的技术报告。
3. Papers with Code 用于交叉验证 benchmark 声明和发现遗漏论文。
4. **不得**使用百度学术、ResearchGate 等非结构化来源作为主检索工具。
5. 中文数据库仅作为 Qwen/DeepSeek 等中国团队工作的中文补充材料来源。

---

## 8. 纳入标准

> 符合以下任一条件 + 不在排除标准内 → 纳入。

### 8.1 必须纳入 (MUST include)

| 条件 | 说明 |
|------|------|
| **里程碑论文** | Boss 明确列名的论文（Transformer, GPT 系列, LLaMA 系列, Qwen 系列, BERT, RoBERTa, T5, BART, Chinchilla, PaLM, Gemini, Claude, Mistral, DeepSeek 等）；无论引用量高低 |
| **方法创新论文** | 提出关键训练技术的论文（RLHF, DPO, CoT, RAG, MoE 等），即使并非所有都被 Boss 逐一点名 |
| **高引用基准论文** | 在 Semantic Scholar / Google Scholar 上引用量 > 500 的 LLM 相关论文 |
| **高社区影响力论文** | Hugging Face 上 `likes` > 200 或 Papers with Code 上有显著 benchmark 提升的论文 |
| **领域综述** | 高质量 LLM survey 论文，用于校验覆盖完整性 |

### 8.2 附加纳入 (SHOULD include if found)

| 条件 | 说明 |
|------|------|
| **重要变体** | 对里程碑方法有显著改进的后续工作（如 RoBERTa 对 BERT、Mixtral 对 Mistral） |
| **竞争性工作** | 与必收论文同期、解决同一问题但方法不同的重要工作 |
| **"负结果"或反思类论文** | 揭露 LLM 评估缺陷、揭示 scaling 瓶颈的工作（如"On the Dangers of Stochastic Parrots"、"Inverse Scaling"） |

---

## 9. 排除标准

> 检索命中的论文若满足以下任一条件 → 排除。

| 条件 | 说明 | 示例 |
|------|------|------|
| **与 LLM 无关** | 论文虽提及 "transformer" 或 "attention" 但用于非语言领域且对 NLP 无回馈 | 用 Transformer 做蛋白质预测的论文 |
| **非 Transformer 架构** | 纯 RNN/CNN 语言模型论文（2017 后仍有发布） | RNN-based 语言建模的改进 |
| **纯应用/无方法** | 仅将现有 LLM 应用于特定领域但无方法贡献 | "Using ChatGPT for medical Q&A" |
| **纯工程/部署** | 推理引擎实现、分布式训练框架论文（除非提出新的量化/压缩方法） | vLLM 系统论文 |
| **无全文/过期预印本** | arXiv 预印本超过 2 年未更新且未被正式发表/引用极少 | 2019 年的某个从未更新、从未被引的预印本 |
| **语言不匹配** | 全文非英文且非中文（检索工具支持有限） | 日文/韩文/俄文的 LLM 论文 |
| **重复/冗余** | 同一工作的多版本（保留最新/最完整版本） | arXiv v1 v2 v3 |
| **数据质量低** | 明显的水文：无实验、无对比、无消融研究 | 仅提出 idea 未验证的 "position paper" |
| **完全被替代** | 方法的已被后续论文完全超越且无独特历史价值 | 早期某个已被 BERT 完全超越的 embedding 方法 |

---

## 10. 检索式模板

> 以下检索式格式适配 `arxiv_search.py` 脚本。所有检索默认 `--sort-by relevance`。

### 10.1 按子问题的检索式

#### 子问题 2.1: Transformer 起源与早期变体

```bash
# 检索式 T1: Transformer 原始论文精确检索
python arxiv_search.py "Attention Is All You Need" --max-results 5 --sort-by relevance

# 检索式 T2: Transformer 架构在 NLP 中的早期应用
python arxiv_search.py "transformer" AND "machine translation" --max-results 20 --sort-by relevance --start-date 2017-06-01 --end-date 2019-12-31

# 检索式 T3: 自注意力机制早期探索
python arxiv_search.py "self-attention" AND "language model" --max-results 15 --sort-by relevance --start-date 2017-01-01 --end-date 2019-12-31
```

#### 子问题 2.2: BERT 时代

```bash
# 检索式 B1: BERT 及相关变体
python arxiv_search.py "BERT" AND "pre-trained language model" --max-results 20 --sort-by relevance --start-date 2018-01-01 --end-date 2020-12-31

# 检索式 B2: GPT 早期 (GPT-1, GPT-2)
python arxiv_search.py "generative pre-trained transformer" OR "GPT-2" --max-results 15 --sort-by relevance --start-date 2018-01-01 --end-date 2020-12-31

# 检索式 B3: 编码器-解码器统一框架
python arxiv_search.py "T5" OR "BART" AND "text-to-text" --max-results 15 --sort-by relevance --start-date 2019-01-01 --end-date 2020-12-31
```

#### 子问题 2.3: Scaling Laws + GPT-3

```bash
# 检索式 S1: GPT-3 与大规模预训练
python arxiv_search.py "GPT-3" OR "language models are few-shot learners" --max-results 20 --sort-by relevance --start-date 2020-01-01 --end-date 2022-12-31

# 检索式 S2: Scaling Laws
python arxiv_search.py "scaling laws" AND "neural language models" --max-results 15 --sort-by relevance --start-date 2020-01-01 --end-date 2022-12-31

# 检索式 S3: 计算最优训练 (Chinchilla)
python arxiv_search.py "Chinchilla" OR "compute-optimal" AND "large language model" --max-results 15 --sort-by relevance --start-date 2021-01-01 --end-date 2022-12-31

# 检索式 S4: PaLM / Gopher / 大模型训练
python arxiv_search.py "PaLM" OR "Gopher" OR "large language model training" --max-results 15 --sort-by relevance --start-date 2021-01-01 --end-date 2022-12-31
```

#### 子问题 2.4: 指令微调与对齐

```bash
# 检索式 A1: RLHF + InstructGPT
python arxiv_search.py "RLHF" OR "reinforcement learning from human feedback" AND "language model" --max-results 20 --sort-by relevance --start-date 2021-01-01 --end-date 2024-12-31

# 检索式 A2: DPO
python arxiv_search.py "direct preference optimization" OR "DPO" AND "language model" --max-results 15 --sort-by relevance --start-date 2023-01-01 --end-date 2024-12-31

# 检索式 A3: 指令微调方法
python arxiv_search.py "instruction tuning" OR "instruction fine-tuning" AND "large language model" --max-results 20 --sort-by relevance --start-date 2021-01-01 --end-date 2024-12-31

# 检索式 A4: GPT-4 技术报告
python arxiv_search.py "GPT-4" AND "technical report" --max-results 5 --sort-by relevance

# 检索式 A5: Constitutional AI 及替代对齐方法
python arxiv_search.py "constitutional AI" OR "safe RLHF" AND "language model" --max-results 15 --sort-by relevance --start-date 2021-01-01 --end-date 2024-12-31
```

#### 子问题 2.5: 开源模型生态

```bash
# 检索式 O1: LLaMA 系列
python arxiv_search.py "LLaMA" AND "large language model" AND "Meta" --max-results 20 --sort-by relevance --start-date 2023-01-01 --end-date 2025-12-31

# 检索式 O2: Mistral / Mixtral
python arxiv_search.py "Mistral" OR "Mixtral" AND "language model" --max-results 15 --sort-by relevance --start-date 2023-01-01 --end-date 2025-12-31

# 检索式 O3: Qwen 系列
python arxiv_search.py "Qwen" AND "language model" --max-results 20 --sort-by relevance --start-date 2023-01-01 --end-date 2025-12-31

# 检索式 O4: DeepSeek 系列
python arxiv_search.py "DeepSeek" AND "language model" --max-results 20 --sort-by relevance --start-date 2023-01-01 --end-date 2025-12-31

# 检索式 O5: 其他开源大模型
python arxiv_search.py "open-source" AND "large language model" --max-results 20 --sort-by relevance --start-date 2023-01-01 --end-date 2025-12-31

# 检索式 O6: Gemma / Phi / Falcon 等
python arxiv_search.py "Gemma" OR "Phi-3" OR "Falcon" AND "language model" --max-results 15 --sort-by relevance --start-date 2023-01-01 --end-date 2025-12-31
```

#### 子问题 2.6: 推理增强

```bash
# 检索式 R1: Chain-of-Thought
python arxiv_search.py "chain-of-thought" OR "chain of thought" AND "reasoning" AND "large language model" --max-results 20 --sort-by relevance --start-date 2022-01-01 --end-date 2026-06-23

# 检索式 R2: 高级推理 (ToT, ReAct, etc.)
python arxiv_search.py "tree-of-thought" OR "ReAct" OR "self-consistency" AND "reasoning" --max-results 15 --sort-by relevance --start-date 2022-01-01 --end-date 2026-06-23

# 检索式 R3: o1 / o3 推理时计算
python arxiv_search.py "test-time compute" OR "reasoning model" AND "large language model" --max-results 15 --sort-by relevance --start-date 2024-01-01 --end-date 2026-06-23

# 检索式 R4: DeepSeek-R1 及其他推理模型
python arxiv_search.py "DeepSeek-R1" OR "reasoning with reinforcement learning" --max-results 15 --sort-by relevance --start-date 2024-01-01 --end-date 2026-06-23
```

#### 子问题 2.7: 效率与部署

```bash
# 检索式 E1: MoE
python arxiv_search.py "mixture of experts" OR "MoE" AND "language model" --max-results 20 --sort-by relevance --start-date 2021-01-01 --end-date 2026-06-23

# 检索式 E2: 量化
python arxiv_search.py "quantization" AND "large language model" --max-results 20 --sort-by relevance --start-date 2022-01-01 --end-date 2026-06-23

# 检索式 E3: RAG
python arxiv_search.py "retrieval augmented generation" OR "RAG" AND "language model" --max-results 20 --sort-by relevance --start-date 2020-01-01 --end-date 2026-06-23

# 检索式 E4: LoRA / QLoRA / 高效微调
python arxiv_search.py "LoRA" OR "QLoRA" OR "parameter efficient fine-tuning" AND "large language model" --max-results 15 --sort-by relevance --start-date 2021-01-01 --end-date 2026-06-23

# 检索式 E5: 长上下文 / KV-cache
python arxiv_search.py "long context" OR "context window" AND "large language model" --max-results 15 --sort-by relevance --start-date 2023-01-01 --end-date 2026-06-23
```

#### 子问题 2.8: 多模态与 Agent

```bash
# 检索式 M1: 多模态 LLM
python arxiv_search.py "multimodal large language model" OR "vision language model" --max-results 20 --sort-by relevance --start-date 2023-01-01 --end-date 2026-06-23

# 检索式 M2: LLM Agent
python arxiv_search.py "LLM agent" OR "language model agent" --max-results 15 --sort-by relevance --start-date 2023-01-01 --end-date 2026-06-23

# 检索式 M3: Claude / Gemini (Anthropic/Google)
python arxiv_search.py "Gemini" OR "Claude" AND "large language model" --max-results 15 --sort-by relevance --start-date 2023-01-01 --end-date 2026-06-23
```

### 10.2 综合检索式

> 当需要"捞底"覆盖时使用的宽泛检索式。

```bash
# 综合检索 C1: LLM 综述论文
python arxiv_search.py "survey" AND "large language model" --max-results 30 --sort-by relevance --start-date 2022-01-01 --end-date 2026-06-23

# 综合检索 C2: 高引 LLM 论文（通过 relevence + 时间窗口）
python arxiv_search.py "large language model" --max-results 50 --sort-by relevance --start-date 2023-01-01 --end-date 2025-12-31
```

### 10.3 Hugging Face Papers 补充检索

> 对于 HF Papers 上有专门页面的模型系列，直接搜索模型名：

```
HF Papers 精确搜索:
  - "Llama 3" (Meta)
  - "Qwen2.5" (Alibaba)
  - "DeepSeek V3" (DeepSeek-AI)
  - "Mistral 7B" (Mistral AI)
  - "Mixtral 8x7B" (Mistral AI)
  - "Gemma 2" (Google)
  - "Phi-4" (Microsoft)
  - "Claude" (Anthropic) — 注意: Claude 无 arXiv 论文，需走 Anthropic 官网
```

---

## 11. 潜在偏差

> 记录检索过程中的已知偏差、假设和局限性，帮助下游 agent 和最终读者理解本计划的覆盖范围。

### 11.1 检索偏差

| 偏差类型 | 描述 | 缓解措施 |
|---------|------|---------|
| **英文中心偏差** | 检索式以英文为主；可能遗漏仅发表在中文学术期刊上的高价值论文 | 补充中文检索式（见 10.3 待开发）；标记语言来源 |
| **arXiv 覆盖偏差** | 闭源模型（GPT-4, Claude, Gemini）的技术报告可能不在 arXiv 上，或仅在 arXiv 上为精简版 | 使用 Hugging Face Papers + 官网直接抓取补充 |
| **关键词漏检** | 某些论文使用非标准术语（如 "generative model" 而不提 "LLM"） | 启用滚雪球检索（追踪已纳入论文的引用和参考文献） |
| **时间窗口截断** | Phase 0 起始于 2017-06，可能遗漏 2017 上半年发表的 attention 相关关键前驱工作 | 将 attention mechanism 时间窗口前移 6 个月 |
| **相关性排序偏差** | `--sort-by relevance` 依赖 arXiv BM25 排序，可能偏向标题含精确关键词的论文而非实质内容最重要的论文 | 对每个子问题检索后，额外做一次按引用量筛选（Semantic Scholar API） |

### 11.2 筛选偏差

| 偏差类型 | 描述 | 缓解措施 |
|---------|------|---------|
| **确认偏差** | 倾向于纳入"已知重要"的论文，忽略与主流叙事不符但重要的异见论文 | 明确保留"负结果和反思"纳入条件；检索时不做主观关键词过滤 |
| **实验室/团队偏差** | Boss 列名的模型以西方大厂（OpenAI, Meta, Google）和中国大厂（阿里, DeepSeek）为主，可能遗漏其他地区的重要工作 | 专门设置开源生态子问题（2.5），覆盖全球开源模型；检索时不设机构过滤 |
| **近期偏差 (Recency Bias)** | 2023-2024 的论文更容易被检索和纳入，早期论文可能因表述过时而漏检 | 分阶段设置时间窗口，对 2017-2022 做专项检索 |
| **语言模型规模偏差** | 倾向关注大型模型（>7B），忽略小型但方法创新的模型 | 在纳入标准中明确以方法创新而非模型大小为判断依据 |
| **技术报告 vs 经过同行评议偏差** | 许多重要 LLM 仅以技术报告形式发布，未经过同行评议 | 标记论文发表类型（preprint/tech-report/conference/journal）；不在质量维度上区别对待 |

### 11.3 假设记录

> 以下假设是本检索计划的基础，如假设不成立，需重新评估计划。

| # | 假设内容 | 影响范围 |
|---|---------|---------|
| H1 | arXiv 上预印本足以覆盖 90%+ 的 LLM 关键论文 | 全计划 |
| H2 | 以英文论文为主、中文论文为辅的策略不会遗漏重大技术突破 | 来源优先级 |
| H3 | Boss 列名的模型系列代表了 LLM 发展的主流路线，不需要额外补充非主流架构 | 子问题分解 |
| H4 | 2017-06 之前的 attention/NLP 工作对理解 LLM 发展脉络并非必需（仅需背景了解） | 时间范围 |
| H5 | 一篇论文的"重要性"可以通过引用量 + 社区热度 + 方法创新度来近似评估 | 纳入/排除标准 |
| H6 | 技术报告（如 GPT-4 Technical Report）和正式会议论文在信息可信度上等价 | 来源处理 |
| H7 | Qwen, DeepSeek 等中国团队的技术报告英文版是主要信息来源，中文版本仅作补充 | 语言策略 |
| H8 | `systematic-literature-review` skill 的 arXiv 搜索足以获取所需论文，不需要额外爬取第三方数据库 | 工具依赖 |

### 11.4 缺口声明

> 以下方面本计划明确**不覆盖**，是已知缺口：

| 缺口 | 原因 | 对最终报告的影响 |
|------|------|----------------|
| 非 arXiv/学术来源的工业技术博客 | 结构化检索困难，质量参差不齐 | 可能遗漏 OpenAI/Anthropic 博客中未形成论文的重要发现 |
| 中文非学术来源（知乎、微信公众号技术文章） | 非结构化、未经验证 | 补充性信息缺失，不影响核心脉络 |
| 商业闭源模型的详细训练细节 | 企业未公开 | GPT-4/Claude/Gemini 的部分技术细节将标记为"未公开" |
| 专利文献 | 检索工具不支持 | 不影响学术脉络；LLM 领域的核心创新主要通过论文公开 |
| 代码/模型权重的实际可用性 | 超出文献调研范围 | 标记为"未验证开源状态" |

---

## 12. 执行建议

### 12.1 检索执行顺序

建议按以下顺序分轮次执行检索，每轮完成后与 downstream agent 同步结果：

| 轮次 | 子问题 | 检索式 | 预计论文数 | 优先级 |
|------|--------|--------|----------|--------|
| 1 | 2.1 Transformer 起源 | T1, T2, T3 | 5-15 | P0 |
| 2 | 2.2 BERT 时代 | B1, B2, B3 | 15-30 | P0 |
| 3 | 2.3 Scaling + GPT-3 | S1, S2, S3, S4 | 15-30 | P0 |
| 4 | 2.4 指令微调与对齐 | A1, A2, A3, A4, A5 | 20-40 | P0 |
| 5 | 2.5 开源生态 | O1-O6 | 20-50 | P0 |
| 6 | 2.6 推理增强 | R1, R2, R3, R4 | 15-30 | P1 |
| 7 | 2.7 效率与部署 | E1-E5 | 15-30 | P1 |
| 8 | 2.8 多模态 + Agent | M1, M2, M3 | 10-25 | P2 |
| 9 | 综合补充 | C1, C2 | 10-30 | P2 |

### 12.2 下游 Agent 分工

| Agent | 输入 | 任务 |
|-------|------|------|
| paper_discovery_agent | 本查询计划 | 执行上述检索式，填充 `paper_inventory.md` |
| lineage_mapping_agent | paper_inventory.md | 构建论文间引用与影响关系 |
| method_taxonomy_agent | paper_inventory.md | 按方法学分类组织论文 |
| synthesis_insight_agent | 以上所有中间产出 | 跨论文综合分析 |

---

## 附录 A: arXiv 类别参考

| 类别 | 全称 | 预期覆盖 |
|------|------|---------|
| `cs.CL` | Computation and Language | 核心类别，NLP/LLM 论文主要归属 |
| `cs.LG` | Machine Learning | LLM 训练方法、优化相关 |
| `cs.AI` | Artificial Intelligence | Agent、推理相关 |
| `cs.CV` | Computer Vision | 多模态 LLM 可能归属 |
| `cs.IR` | Information Retrieval | RAG 相关论文 |
| `stat.ML` | Machine Learning (Statistics) | 理论 scaling laws 相关 |

## 附录 B: 已知关键论文 arXiv ID 速查

> 供 paper_discovery_agent 做`--id`精确获取时使用。非完整清单，仅列出确认 ID 的核心论文。

| 论文 | arXiv ID | 备注 |
|------|----------|------|
| Attention Is All You Need | `1706.03762` | Transformer |
| BERT | `1810.04805` | |
| GPT-1 | 未在 arXiv 以独立论文发表 | 参考 OpenAI blog |
| GPT-2 | `1907.09217` (不准确, 需检索确认) | Language Models are Unsupervised Multitask Learners |
| GPT-3 | `2005.14165` | |
| InstructGPT | `2203.02155` | |
| GPT-4 Technical Report | `2303.08774` | |
| RoBERTa | `1907.11692` | |
| T5 | `1910.10683` | |
| BART | `1910.13461` | |
| Scaling Laws | `2001.08361` | |
| Chinchilla | `2203.15556` | |
| PaLM | `2204.02311` | |
| LLaMA | `2302.13971` | |
| LLaMA 2 | `2307.09288` | |
| DPO | `2305.18290` | |
| Chain-of-Thought | `2201.11903` | |
| RAG | `2005.11401` | |
| Switch Transformer | `2101.03961` | |
| Constitutional AI | `2212.08073` | |

---

*本查询计划按 quality_protocol 要求编写，所有假设、偏差和缺口均已记录，下游 agent 可据此进行可复现的检索。*
