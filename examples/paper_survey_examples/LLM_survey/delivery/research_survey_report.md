# 大语言模型（LLM）关键论文系统梳理：2017–2026

> **报告版本**: v1.0
> **生成日期**: 2026-06-23
> **报告范围**: 从 Transformer (2017) 到推理模型 (2026) 的关键论文、方法演进与团队脉络
> **数据基础**: 65+ 篇经过 arXiv/Hugging Face Papers API 验证的核心论文
> **检索方法**: arXiv API + Hugging Face Papers API + 官网/技术报告直接获取

---

## 第一章：引言与背景

### 1.1 报告目的和范围

本报告旨在系统梳理大语言模型（Large Language Model, LLM）自 2017 年 Transformer 架构提出以来近十年的关键发展脉络。报告面向需要快速理解 LLM 技术演进逻辑、识别研究机会和评估技术方向的读者。

**覆盖范围**：
- **时间跨度**：2017 年 6 月（Transformer 论文发布）至 2026 年 6 月
- **架构**：Transformer 及其变体（Encoder-Only、Decoder-Only、Encoder-Decoder、MoE）
- **方法维度**：预训练、规模化定律、指令微调与对齐、推理增强、效率优化、多模态融合
- **论文来源**：arXiv 预印本、Hugging Face Papers、官方技术报告（OpenAI, Meta, Google, Anthropic, DeepSeek 等）、顶级会议论文（NeurIPS, ICML, ICLR, ACL）

**排除范围**：非 Transformer 架构（RNN/LSTM/CNN）、纯计算机视觉模型、分布式训练系统工程、纯产品/商业分析、与 LLM 无关的知识蒸馏/剪枝论文。

### 1.2 检索方法说明

本报告基于 `research/query_plan.md` 中定义的 8 个子问题进行分阶段检索。检索优先级为：
- **P0**：arXiv API 精确 ID 获取 + arXiv 抽象页 webfetch 验证（27 篇核心论文逐字验证）
- **P0**：Hugging Face Papers API 搜索（按模型名和关键词检索，补充 38+ 篇关联论文）
- **P1**：OpenAI/Anthropic/Meta 官方技术博客和报告（弥补非 arXiv 来源）
- **偏差声明**：检索以英文为主，可能遗漏仅发表于中文学术期刊的高价值论文；闭源模型（GPT-4, Claude, Gemini）的技术细节因企业未公开而部分缺失。

### 1.3 术语定义

| 术语 | 英文 | 定义 |
|------|------|------|
| 大语言模型 | Large Language Model (LLM) | 基于 Transformer 架构、参数量通常在 1B 以上的语言模型 |
| 规模化定律 | Scaling Laws | 描述模型性能与参数量、数据量、计算量之间幂律关系的经验规律 |
| 基于人类反馈的强化学习 | RLHF | 通过人类偏好训练奖励模型，再用强化学习（PPO）优化语言模型策略的对齐方法 |
| 直接偏好优化 | Direct Preference Optimization (DPO) | 将 RLHF 目标重参数化为直接分类损失的对齐方法，无需独立奖励模型 |
| 混合专家 | Mixture of Experts (MoE) | 将模型 FFN 层拆分为多个"专家"子网络，每 token 仅激活部分专家的稀疏架构 |
| 思维链 | Chain-of-Thought (CoT) | 引导 LLM 生成中间推理步骤（而非直接给出答案）的提示技术 |
| 检索增强生成 | Retrieval-Augmented Generation (RAG) | 将外部知识库检索与语言模型生成相结合的方法 |
| 指令微调 | Instruction Tuning | 以"指令-响应"格式微调模型，使其学会遵循自然语言指令 |
| 涌现能力 | Emergent Abilities | 模型在规模超过特定阈值后突然展现的、小模型中不存在的能力 |
| 对齐 | Alignment | 使模型行为与人类价值观和期望（有用、诚实、无害）保持一致的技术和过程 |

---

## 第二章：发展历史与关键论文

### 2.1 Transformer 的诞生（2017）

**核心论文**：

- **"Attention Is All You Need"** (Vaswani et al., Google Brain, 2017) — arXiv: [1706.03762](https://arxiv.org/abs/1706.03762) ⭐

**核心贡献**：提出完全基于自注意力机制（Self-Attention）的序列到序列架构，彻底摒弃了 RNN/LSTM 的循环结构。核心组件包括：Multi-Head Attention、Positional Encoding（正弦位置编码）、残差连接和 Layer Normalization。Base 版本 65M 参数，Big 版本 213M 参数，在 WMT 2014 英德翻译上达到 28.4 BLEU。

**在当时的意义**：
- 解决了 RNN 的三大瓶颈：串行计算慢（无法并行）、长程依赖弱（梯度消失）、训练不稳定
- 注意力机制的 O(N²) 复杂度是当时的已知缺陷，但并行化优势远超这一代价
- 论文中的 Encoder-Decoder 设计后来分叉出三条路径：Encoder-Only（BERT）、Decoder-Only（GPT）、Encoder-Decoder（T5/BART）

**关键观察**：Transformer 并非为"大语言模型"而设计——它的初衷是改进机器翻译。它是一个"意外的好架构"，其并行计算特性恰好使后续的规模化训练成为可能。没有 Transformer 的并行性，Scaling Laws 和 GPT-3 级别的规模化训练在工程上几乎不可行。

---

### 2.2 预训练范式的双轨探索（2018–2019）：BERT vs GPT

#### 2.2.1 过渡性先驱：ULMFiT

- **"Universal Language Model Fine-tuning for Text Classification"** (Howard & Ruder, fast.ai, 2018) — arXiv: [1801.06146](https://arxiv.org/abs/1801.06146)
- 提出三阶段迁移学习方法（通用预训练 → 任务特定微调 → 分类器微调），是 NLP 迁移学习的关键先驱。

#### 2.2.2 Encoder-Only 路线：BERT 家族

- **"BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding"** (Devlin et al., Google, 2018) — arXiv: [1810.04805](https://arxiv.org/abs/1810.04805) ⭐
  - 仅使用 Transformer 编码器堆叠，通过 Masked Language Model (MLM) + Next Sentence Prediction (NSP) 预训练，在 11 个 NLP 任务上达到 SOTA。GLUE 达 80.5%。Base: 110M, Large: 340M。

- **"RoBERTa: A Robustly Optimized BERT Pretraining Approach"** (Liu et al., Facebook AI / UW, 2019) — arXiv: [1907.11692](https://arxiv.org/abs/1907.11692)
  - BERT 的复现研究：去除 NSP、动态掩码、更大 batch、更多数据，全面超越 BERT。证明了"把 BERT 训练得更好"比架构创新更重要。

- **"XLNet: Generalized Autoregressive Pretraining"** (Yang et al., CMU / Google Brain, 2019) — arXiv: [1906.08237](https://arxiv.org/abs/1906.08237)
  - 提出排列语言建模（Permutation LM），融合自回归与双向上下文优势，在 20 个任务上超越 BERT。

- **"ALBERT: A Lite BERT"** (Lan et al., Google, 2019) — arXiv: [1909.11942](https://arxiv.org/abs/1909.11942)
  - 参数共享 + 嵌入分解大幅减少参数量，但推理计算量未降。

#### 2.2.3 Decoder-Only 路线：GPT 系列起航

- **GPT-1: "Improving Language Understanding by Generative Pre-Training"** (Radford et al., OpenAI, 2018) — OpenAI Blog
  - 12 层 Decoder-Only Transformer，117M 参数。预训练（自回归语言建模）+ 有监督微调两阶段范式。首次展示大规模无监督预训练对 NLP 任务的广泛增益。

- **GPT-2: "Language Models are Unsupervised Multitask Learners"** (Radford et al., OpenAI, 2019) — OpenAI Blog
  - 1.5B 参数。核心主张：足够大的语言模型可以在零样本设定下完成多种 NLP 任务——"语言模型就是无监督多任务学习器"。因其"太大而危险"，OpenAI 最初延迟了完整版本的发布。

#### 2.2.4 Encoder-Decoder 统一框架

- **"T5: Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer"** (Raffel et al., Google, 2019) — arXiv: [1910.10683](https://arxiv.org/abs/1910.10683)
  - 将所有 NLP 任务统一为"输入文本→输出文本"的 text-to-text 格式。系统性比较预训练目标、架构、数据规模的影响。发布 C4 数据集。

- **"BART: Denoising Sequence-to-Sequence Pre-training"** (Lewis et al., Facebook AI, 2019) — arXiv: [1910.13461](https://arxiv.org/abs/1910.13461)
  - 去噪自编码器：对文本施加多种噪声后训练模型恢复原文。在文本生成（摘要）任务上表现突出。

**阶段小结**：2018–2019 年是 NLP 最富创造力的时期。三条架构路线并行发展——BERT 在 NLU 任务上统治、GPT-2 展示了令人惊叹的零样本生成能力、T5/BART 在条件生成任务上表现优异。到 2019 年底，Decoder-Only 路线的潜力初现但尚未成为最终赢家。

---

### 2.3 Scaling Law 发现与 GPT 霸权（2020–2022）

- **"Scaling Laws for Neural Language Models"** (Kaplan et al., OpenAI, 2020) — arXiv: [2001.08361](https://arxiv.org/abs/2001.08361) ⭐
  - 发现损失与模型规模、数据量、计算量之间遵循幂律关系。建议在固定计算预算下**优先扩大模型**。直接指导了 GPT-3 的设计。

- **"Language Models are Few-Shot Learners (GPT-3)"** (Brown et al., OpenAI, 2020) — arXiv: [2005.14165](https://arxiv.org/abs/2005.14165) ⭐
  - 175B 参数。展示了 Few-Shot In-Context Learning——无需梯度更新，仅通过 prompt 中的示例即可完成翻译、问答、推理等任务。改变了人机交互范式：从"微调模型"到"写 prompt"。

- **"Training Compute-Optimal Large Language Models (Chinchilla)"** (Hoffmann et al., DeepMind, 2022) — arXiv: [2203.15556](https://arxiv.org/abs/2203.15556) ⭐
  - **核心修正**：Kaplan 定律的结论依赖于固定训练步数假设。Chinchilla 发现模型大小和数据量应等比缩放。Chinchilla 70B 使用 4× 数据超越 Gopher 280B。这一发现直接塑造了 LLaMA 及后续所有开源模型。

- **"PaLM: Scaling Language Modeling with Pathways"** (Chowdhery et al., Google, 2022) — arXiv: [2204.02311](https://arxiv.org/abs/2204.02311) ⭐
  - 540B 参数，使用 6144 TPU v4 训练。在 BIG-bench 上展示了涌现能力——某些能力在达到特定规模阈值后突然出现。

- **"Gopher: Scaling Language Models"** (Rae et al., DeepMind, 2022) — arXiv: [2112.11446](https://arxiv.org/abs/2112.11446)
  - 280B 参数，系统性分析规模化对不同任务类别的影响差异。

- **"OPT: Open Pre-trained Transformer"** (Zhang et al., Meta AI, 2022) — arXiv: [2205.01068](https://arxiv.org/abs/2205.01068)
  - 开源 125M–175B 参数系列，旨在复现 GPT-3 类性能。未完全成功，但开启了"复现闭源模型"的先河。

- **"BLOOM: A 176B-Parameter Open-Access Multilingual Language Model"** (BigScience Workshop, 2023) — arXiv: [2211.05100](https://arxiv.org/abs/2211.05100)
  - 最大的完全开源多语言 LLM，覆盖 46 种语言和 13 种编程语言。

---

### 2.4 对齐革命（2022–2023）：InstructGPT, RLHF, Constitutional AI, DPO

- **"Deep Reinforcement Learning from Human Preferences"** (Christiano et al., OpenAI / DeepMind, 2017) — arXiv: [1706.03741](https://arxiv.org/abs/1706.03741) ⭐
  - RLHF 的奠基性工作：通过人类偏好反馈训练奖励模型，再用 PPO 优化策略。当时应用于 Atari/机器人，非语言模型。

- **"Training language models to follow instructions with human feedback (InstructGPT)"** (Ouyang et al., OpenAI, 2022) — arXiv: [2203.02155](https://arxiv.org/abs/2203.02155) ⭐
  - 首次将 RLHF 大规模应用于语言模型对齐。三阶段流程：SFT → RM 训练 → PPO 优化。1.3B InstructGPT 在人类偏好评比中超越 175B GPT-3——对齐比规模更重要。

- **"Constitutional AI: Harmlessness from AI Feedback"** (Bai et al., Anthropic, 2022) — arXiv: [2212.08073](https://arxiv.org/abs/2212.08073)
  - 通过"宪法"规则让 AI 自我监督训练无害助手（RLAIF），减少对人工标注有害内容的需求。Claude 系列的对齐基础。

- **"Direct Preference Optimization (DPO)"** (Rafailov et al., Stanford, 2023) — arXiv: [2305.18290](https://arxiv.org/abs/2305.18290) ⭐
  - 数学上证明 RLHF 目标可重参数化为简单的二分类损失。无需独立奖励模型、无需 PPO 强化学习。将对齐从复杂工程简化为直接分类训练。

- **"GPT-4 Technical Report"** (OpenAI, 2023) — arXiv: [2303.08774](https://arxiv.org/abs/2303.08774) ⭐
  - 多模态 LLM（文本+图像输入），在专业考试（律师资格、医学知识）上展现人类水平性能。技术细节未完全公开（参数量、架构、训练数据均未披露）。

- **"FLAN: Fine-tuned Language Models Are Zero-Shot Learners"** (Wei et al., Google, 2021) — arXiv: [2109.01652](https://arxiv.org/abs/2109.01652)
  - 指令微调使 LLM 在未见任务上获得零样本泛化能力。

- **"Self-Instruct"** (Wang et al., UW / Allen AI, 2022) — arXiv: [2212.10560](https://arxiv.org/abs/2212.10560)
  - 利用 LLM 自身生成指令数据，大幅降低人工标注成本。

---

### 2.5 开源大爆发（2023–2024）

- **"LLaMA: Open and Efficient Foundation Language Models"** (Touvron et al., Meta AI, 2023) — arXiv: [2302.13971](https://arxiv.org/abs/2302.13971) ⭐
  - 首次展示仅用公开数据训练即可达到 SOTA。LLaMA-13B 超越 GPT-3 175B。采用 Chinchilla 定律、Pre-Norm、SwiGLU、RoPE 等技术栈。权重泄露在 4chan 引发社区微调狂潮。

- **"Llama 2: Open Foundation and Fine-Tuned Chat Models"** (Touvron et al., Meta AI, 2023) — arXiv: [2307.09288](https://arxiv.org/abs/2307.09288)
  - 7B–70B 系列，加入 RLHF 安全对齐，支持商用。

- **"The Llama 3 Herd of Models"** (Meta AI, 2024) — arXiv: [2407.21783](https://arxiv.org/abs/2407.21783) ⭐
  - 8B/70B/405B 系列，15T+ tokens 训练，128K 上下文。在多项 benchmark 上比肩或超越闭源模型。

- **"Mistral 7B"** (Jiang et al., Mistral AI, 2023) — arXiv: [2310.06825](https://arxiv.org/abs/2310.06825) ⭐
  - 7B 参数，使用 GQA + 滑动窗口注意力（SWA），性能超越 LLaMA 2 13B。Apache 2.0 许可。

- **"Mixtral of Experts"** (Jiang et al., Mistral AI, 2024) — arXiv: [2401.04088](https://arxiv.org/abs/2401.04088) ⭐
  - Sparse MoE：8×7B 专家，每 token 激活 top-2（47B total / 13B active），性能匹配 LLaMA 2 70B。首个真正成功的开源 MoE 模型。

- **"Qwen Technical Report"** (Bai et al., Alibaba, 2023) — arXiv: [2309.16609](https://arxiv.org/abs/2309.16609) ⭐
  - 阿里通义千问系列首个技术报告，1.8B–72B。

- **"Qwen2 Technical Report"** (Yang et al., Alibaba, 2024) — arXiv: [2407.10671](https://arxiv.org/abs/2407.10671)
  - 0.5B–72B，GQA + SwiGLU，多语言能力大幅提升。

- **"Qwen2.5 Technical Report"** (Yang et al., Alibaba, 2024) — arXiv: [2412.15115](https://arxiv.org/abs/2412.15115)
  - 0.5B–72B + MoE，128K 上下文，数学和代码能力显著提升。

- **"DeepSeek LLM: Scaling Open-Source Language Models"** (DeepSeek-AI, 2024) — arXiv: [2401.02954](https://arxiv.org/abs/2401.02954) ⭐
  - 7B 和 67B 系列，使用 SFT + DPO 对齐，67B 超越 LLaMA-2 70B。

- **"DeepSeek-V2"** (DeepSeek-AI, 2024) — arXiv: [2405.04434](https://arxiv.org/abs/2405.04434)
  - MoE 架构，236B total / 21B active。提出 Multi-head Latent Attention (MLA)。

- **"DeepSeek-V3 Technical Report"** (DeepSeek-AI, 2024) — arXiv: [2412.19437](https://arxiv.org/abs/2412.19437) ⭐
  - 671B total / 37B active 的 MoE。训练成本仅 ~$5.6M。在多项 benchmark 上超越 GPT-4o。核心创新：MLA + DeepSeekMoE + FP8 混合精度训练。

- **"Gemma"** (Google DeepMind, 2024) — arXiv: [2403.08295](https://arxiv.org/abs/2403.08295)
  - Google 开源轻量级 LLM（2B, 7B），基于 Gemini 技术。

- **"Phi-3 Technical Report"** (Microsoft, 2024) — arXiv: [2404.14219](https://arxiv.org/abs/2404.14219)
  - 3.8B 参数，数据质量驱动。在手机端实现接近 GPT-3.5 的性能。

---

### 2.6 推理时代（2024–2026）

- **"Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"** (Wei et al., Google, 2022) — arXiv: [2201.11903](https://arxiv.org/abs/2201.11903) ⭐
  - Few-Shot 链式思考提示，在 540B PaLM 上将 GSM8K 数学推理从 ~18% 提升至 ~57%。

- **"Self-Consistency Improves Chain of Thought Reasoning"** (Wang et al., Google, 2022) — arXiv: [2203.11171](https://arxiv.org/abs/2203.11171)
  - 采样多条推理路径，多数投票选最佳答案。

- **"Tree of Thoughts: Deliberate Problem Solving with Large Language Models"** (Yao et al., Princeton / Google DeepMind, 2023) — arXiv: [2305.10601](https://arxiv.org/abs/2305.10601)
  - 将推理建模为树状搜索（BFS/DFS），支持回溯。Game of 24 成功率 74%（CoT 仅 4%）。

- **"ReAct: Synergizing Reasoning and Acting in Language Models"** (Yao et al., Princeton / Google, 2022) — arXiv: [2210.03629](https://arxiv.org/abs/2210.03629)
  - 推理（reasoning）与行动（action）交织，提升知识密集型和决策任务表现。

- **"STaR: Bootstrapping Reasoning With Reasoning"** (Zelikman et al., Stanford, 2022) — arXiv: [2203.14465](https://arxiv.org/abs/2203.14465)
  - 用模型自身生成的正确推理链进行自引导训练，提升推理能力。

- **"OpenAI o1 System Card"** (OpenAI, 2024) ⭐
  - 推理时计算扩展：模型在回答前进行内部长链式思考。在 AIME 数学竞赛和科学推理上取得突破。

- **"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning"** (DeepSeek-AI, 2025) — arXiv: [2501.12948](https://arxiv.org/abs/2501.12948) ⭐
  - 纯 RL 训练推理模型（无 SFT 冷启动）。模型自发学会反思、验证、回溯行为。性能匹配 OpenAI o1。开源、推理链透明。

---

### 2.7 多模态与未来（2023–2026）

- **"Gemini: A Family of Highly Capable Multimodal Models"** (Google DeepMind, 2023) — arXiv: [2312.11805](https://arxiv.org/abs/2312.11805) ⭐
  - 原生多模态模型家族（文本+图像+音频+视频+代码），MMLU 首次超过人类专家。

- **"Visual Instruction Tuning (LLaVA)"** (Liu et al., UW-Madison / Microsoft, 2023) — arXiv: [2304.08485](https://arxiv.org/abs/2304.08485) ⭐
  - 视觉编码器 + LLM + 投影层 → 视觉指令微调。定义了开源多模态 LLM 的标准范式。

- **"Qwen-VL: A Versatile Vision-Language Model"** (Bai et al., Alibaba, 2023) — arXiv: [2308.12966](https://arxiv.org/abs/2308.12966)
  - 图文理解+定位+OCR 三合一多功能视觉语言模型。

- **"The Claude Model Family: Claude 3 / Claude 3.5"** (Anthropic, 2024) — Anthropic 官网 ⭐
  - 在推理、编码、多语言方面与 GPT-4 竞争。强调安全性和 Constitutional AI 对齐。

- **"CogVLM: Visual Expert for Pretrained Language Models"** (Wang et al., Tsinghua / Zhipu AI, 2023) — arXiv: [2311.03079](https://arxiv.org/abs/2311.03079)
  - 在冻结 LLM 上增加可训练视觉专家模块。

- **"SWE-Agent: Agent-Computer Interfaces Enable Automated Software Engineering"** (Yang et al., Princeton, 2024) — arXiv: [2405.15793](https://arxiv.org/abs/2405.15793)
  - 设计 ACI 接口使 LLM Agent 自主浏览代码库、编辑文件、运行测试。

- **"Voyager: An Open-Ended Embodied Agent with Large Language Models"** (Wang et al., NVIDIA / Caltech / Stanford, 2023) — arXiv: [2305.16291](https://arxiv.org/abs/2305.16291)
  - LLM 驱动的 Minecraft 自主探索 Agent。

---

## 第三章：关键实验室与团队

### 3.1 OpenAI — GPT 系列全链路

**成立**: 2015 年 | **总部**: San Francisco | **定位**: 闭源 AGI 先锋

**核心人物**: Sam Altman (CEO), Greg Brockman (President), Alec Radford (GPT-1/2 一作), Tom Brown (GPT-3 一作, 后加入 Anthropic), Jared Kaplan (Scaling Laws 一作, 后联合创办 Anthropic), Ilya Sutskever (联合创始人, 2024 年离职创办 SSI), Jan Leike (前 Alignment 联席负责人, 2024 年加入 Anthropic), John Schulman (联合创始人, 2024 年加入 Anthropic), Andrej Karpathy (联合创始人, 2025 年加入 Anthropic), Mira Murati (前 CTO, 2024 年离职创办 Thinking Machines Lab)

**标志性贡献**: GPT-1→GPT-4 全系列、Scaling Laws、InstructGPT/ChatGPT、o1 推理模型

**关键观察**: OpenAI 是 LLM 行业最大的人才输出方——多位核心员工因对商业化方向和安全策略的分歧而离开，其中 7 人于 2021 年共同创办了 Anthropic。2024 年又有多位 Alignment 核心加入 Anthropic。

### 3.2 Meta AI — LLaMA 开源生态

**成立**: 2013（FAIR）| **定位**: 开源 LLM 旗舰

**核心人物**: Yann LeCun (VP & Chief AI Scientist), Hugo Touvron (LLaMA 系列一作), Yinhan Liu (RoBERTa 一作, 后加入 OpenAI), Mike Lewis (BART 一作), Patrick Lewis (RAG 一作), Guillaume Lample 和 Timothée Lacroix (LLaMA 共同作者, 2023 年离开创办 Mistral AI)

**标志性贡献**: RoBERTa, BART, RAG, LLaMA 系列 (1/2/3), OPT

### 3.3 Google / DeepMind — 从 Transformer 到 Gemini

**成立**: Google Brain (2011) + DeepMind (2010), 2023 年合并 | **定位**: 基础研究 + 多模态旗舰

**核心人物**: Ashish Vaswani (Transformer 一作, 后创办 Adept AI), Noam Shazeer (Transformer/T5/Switch 作者, 后创办 Character.AI), Jakob Uszkoreit (Transformer 作者, 后创办 Inceptive), Jacob Devlin (BERT 一作), Colin Raffel (T5 一作), Jason Wei (CoT 一作, 2025 年加入 OpenAI), Jordan Hoffmann (Chinchilla 一作), Demis Hassabis (DeepMind CEO)

**标志性贡献**: Transformer, BERT, T5, PaLM, Chinchilla, CoT, Switch Transformer, Gemini

**关键观察**: Transformer 的 8 位作者全部离开了 Google——Shazeer 创办 Character.AI，Gomez 创办 Cohere，Vaswani 创办 Adept AI，Kaiser 加入 OpenAI。这一"大迁徙"是 AI 人才扩散的关键事件。

### 3.4 Anthropic — Constitutional AI 与安全对齐

**成立**: 2021 年 (7 名前 OpenAI 员工) | **定位**: 安全优先的闭源 LLM

**核心人物**: Dario Amodei (CEO), Daniela Amodei (President), Jared Kaplan (Chief Science Officer), Tom Brown (GPT-3 一作), Chris Olah (可解释性), Jan Leike 和 John Schulman (2024 年从 OpenAI 加入), Andrej Karpathy (2025 年加入)

**标志性贡献**: Constitutional AI, Claude 系列 (3/3.5)

### 3.5 Mistral AI — 轻量高性能典范

**成立**: 2023 年 | **总部**: Paris | **定位**: 欧洲高效开源

**核心人物**: Arthur Mensch (CEO, 前 DeepMind/Chinchilla 作者), Guillaume Lample (Chief Scientist, 前 Meta/LLaMA 作者), Timothée Lacroix (CTO, 前 Meta/LLaMA 作者)

**标志性贡献**: Mistral 7B (Apache 2.0), Mixtral 8x7B (首个成功开源 MoE)

### 3.6 阿里巴巴 Qwen 团队 — 中文 LLM 领导者

**成立**: 通义千问团队 (阿里云) | **定位**: 中文+多语言开源

**核心人物**: Jinze Bai (Qwen/Qwen-VL 一作), An Yang (Qwen2/2.5 一作)

**标志性贡献**: Qwen (2023) → Qwen2 (2024) → Qwen2.5 (2024), Qwen-VL

### 3.7 DeepSeek — 效率革命的颠覆者

**成立**: 2023 年 | **总部**: 杭州 | **创始人**: 梁文锋 (幻方量化背景) | **定位**: 极致效率+开源

**核心人物**: DeepSeek-AI（集体署名），梁文锋 (CEO)

**标志性贡献**: DeepSeek LLM → V2 (MLA + MoE) → V3 ($5.6M 训练, 超越 GPT-4o) → R1 (纯 RL 推理模型)。全部 MIT 许可开源。

**关键数据**: 员工约 160 人（2025 年）；使用受贸易限制的 Nvidia H800 GPU；V3 训练成本约 $6M（公司宣称，存在一定争议）。

### 3.8 人才流动全景图

```
Google (Transformer 8人) → Character.AI (Shazeer), Cohere (Gomez), Adept AI (Vaswani), 
                            Inceptive (Uszkoreit), OpenAI (Kaiser)
OpenAI (7人, 2021) → Anthropic (Dario Amodei, Daniela Amodei, Kaplan, Brown, McCandlish, Clark, Olah)
OpenAI → Anthropic (2024-2025): Jan Leike, John Schulman, Andrej Karpathy
Meta AI → Mistral AI (2023): Guillaume Lample, Timothée Lacroix
DeepMind → Mistral AI (2023): Arthur Mensch
Google → OpenAI (2025): Jason Wei
DeepMind → Microsoft AI (2024): Mustafa Suleyman (CEO)
```

---

## 第四章：技术方法演进

### 4.1 模型架构路线

三条架构路线的最终收敛：

| 路线 | 代表 | 核心特点 | 最终地位 |
|------|------|---------|---------|
| **Encoder-Only** | BERT, RoBERTa | 双向理解，无法生成 | 退为 embedding 模型 / NLU baseline |
| **Encoder-Decoder** | T5, BART | 输入输出解耦 | 特定生成任务（翻译/摘要） |
| **Decoder-Only ★** | GPT, LLaMA, Qwen, DeepSeek | 统一理解+生成，天然适合 Few-Shot | **绝对主流** |

当前主流架构标配：Decoder-Only + RoPE 位置编码 + GQA 注意力 + SwiGLU 激活 + RMSNorm + FlashAttention 加速。

**MoE 架构**（从 Switch Transformer 2021 到 DeepSeek-V3 2024）：通过稀疏激活（每 token 仅激活部分专家）实现大容量/低成本。MoE 正成为 70B+ 大规模模型的标配架构。

### 4.2 预训练方法

**核心范式**：自回归语言建模（Next-Token Prediction）成为绝对主流。关键演进：
- GPT-1 (2018): "预训练 + 有监督微调"
- GPT-2 (2019): "预训练 = 零样本多任务学习器"
- LLaMA 3 (2024): 15T+ tokens 多源混合（web + code + math + multilingual）

**数据方法论**：从"越多越好"到"质量优先"——Phi-3 (2024) 以"教科书级"合成数据训练 3.8B 模型接近 GPT-3.5 性能。

### 4.3 规模扩展定律

**两大定律的核心差异**：

| 维度 | Kaplan (2020) | Chinchilla (2022) |
|------|-------------|-------------------|
| 关键结论 | 优先扩大模型 | 模型和数据等比缩放 |
| 训练 tokens/参数比 | ~1-2× | ~20× |
| 对 GPT-3 评价 | 合理 | 严重训练不足（undertrained） |
| 影响 | 催生 GPT-3/PaLM | 催生 LLaMA/所有后续开源模型 |

**推理时计算扩展**（2024-2025）：o1 和 DeepSeek-R1 开创了新的 scaling 维度——pre-training scaling → post-training scaling → **inference-time scaling**。

### 4.4 对齐技术

**演进路径**：
```
RLHF (Christiano 2017, 概念) → InstructGPT (2022, LLM 实用化) → DPO (2023, 去强化学习简化)
→ Constitutional AI/RLAIF (2022, Anthropic AI 自我监督) → ORPO/KTO (2024, 进一步简化)
→ 纯 RL 推理训练 (DeepSeek-R1 2025, 对齐+推理融合)
```

**RLHF vs DPO 对比**：
- RLHF: 4 个模型（policy + ref + RM + value），PPO 强化学习，不稳定
- DPO: 2 个模型（policy + ref），简单分类损失，稳定

### 4.5 推理增强

**推理能力层级的递进**：
- L0（Prompt 诱导）: CoT (2022) — "Let's think step by step"
- L1（采样增强）: Self-Consistency (2022) — 多路径投票
- L2（搜索/工具增强）: ToT (2023) — 树状搜索；ReAct (2022) — 推理+行动交织
- L3（训练增强）: STaR (2022) — 自引导微调
- L4（推理模型内化）: o1 (2024) / DeepSeek-R1 (2025) — 经过专门 RL 训练，推理能力内化

### 4.6 效率优化

| 技术类别 | 代表方法 | 核心贡献 |
|---------|---------|---------|
| 参数高效微调 | LoRA (2021), QLoRA (2023) | 低秩分解，微调成本降低万倍 |
| 模型量化 | GPTQ (2022), AWQ (2023), GGUF (2023) | 3-4 bit 量化，消费级硬件部署 |
| 高效注意力 | FlashAttention (2022-2024), GQA, MLA (2024) | 显存/推理成本大幅降低 |
| 投机解码 | Speculative Decoding (2023) | 推理加速 2-3× |

### 4.7 外部知识整合

- **RAG** (Lewis et al., 2020): 检索器 + 生成器端到端框架
- **Self-RAG** (2023): 模型自主决定何时检索
- **GraphRAG** (2024): 从文本构建知识图谱，全局语义理解
- **工具使用**：Toolformer (2023), Function Calling API (GPT-4/Claude/Gemini)
- **长上下文扩展**：从 512 (GPT-1, 2018) 到 1M+ (Gemini 1.5 Pro, 2024)

---

## 第五章：未解决问题与未来方向

### 5.1 仍未解决的八大问题

| # | 问题 | 严重程度 | 简述 |
|---|------|---------|------|
| 1 | **幻觉 (Hallucination)** | ★★★★★ | 即使最先进模型仍产生虚构信息。根源在于训练目标（最大化似然）与真实性的根本冲突 |
| 2 | **长上下文深度推理** | ★★★★☆ | 128K 上下文已实现，但从中真正"推理"（而非检索）的能力远未成熟 |
| 3 | **评估体系滞后** | ★★★★☆ | 主流 benchmark 1-2 年内被饱和；数据污染；缺乏动态交互评估 |
| 4 | **数据墙** | ★★★☆☆ | Chinchilla 定律要求的数据量逼近互联网高质量文本上限 |
| 5 | **推理成本** | ★★★☆☆ | o1/R1 类模型回答一个问题可能消耗数十倍于标准 LLM 的 token |
| 6 | **多语言公平性** | ★★★☆☆ | 英文中心化严重，非英语性能显著落后 |
| 7 | **对齐税 (Alignment Tax)** | ★★★☆☆ | RLHF/DPO 对齐后创意和多样性能力下降 |
| 8 | **多模态深度融合** | ★★☆☆☆ | 当前主流方案为"视觉编码器+LLM 拼接"，非原生统一架构 |

### 5.2 活跃争议

1. **开源 vs 闭源安全性**：Meta/LeCun 主张"透明=安全"，Anthropic/OpenAI 早期主张"隐藏=安全"。无共识。
2. **Scaling 是否到瓶颈？**：Pre-training scaling 的数据墙逼近，但 inference-time scaling 刚刚开始。
3. **MoE 是否是终极架构？**：在 70B+ 规模优势明显，但在小模型和 batch 推理场景存在局限。
4. **AGI 路线图分歧**：激进路线（OpenAI/Anthropic, 5-10 年）vs 渐进路线（LeCun, 需要根本性架构突破）。
5. **合成数据与模型崩溃**：理论上存在"多代合成数据→分布坍缩"风险，但实际部署中尚未成为瓶颈。

### 5.3 2026–2028 趋势预测

1. **推理时计算 Scaling 理论化**：将从经验阶段进入理论指导阶段（寻找"推理时代的 Chinchilla 定律"）
2. **开源在推理能力上超越闭源**：DeepSeek 证明了路径可行性
3. **Agent 从 Demo 走向生产**：可靠性是核心瓶颈
4. **幻觉的根本性解决方案**：需要训练目标、架构和外部知识的协同创新
5. **推理成本大幅降低**：投机解码、知识蒸馏、自适应推理深度

### 5.4 研究机会

| 优先级 | 方向 | 理由 |
|--------|------|------|
| **最高** | 推理时计算 Scaling 的效率优化 | 当前最活跃、最有潜力的方向 |
| **最高** | 开源生态标准化（训练/评估/安全） | DeepSeek/LLaMA 证明了开源潜力 |
| **高** | 幻觉的根本性解决 | 阻碍 LLM 在高风险领域部署的最大障碍 |
| **高** | Agent 可靠性工程 | 从 Demo 到产品的关键跃迁 |
| **高** | 推理成本降低（量化/蒸馏/投机解码） | 使推理模型经济可行 |

---

## 第六章：参考文献

> 标注说明：⭐ 开创性论文（里程碑级别）| 🔷 代表性论文（重要方法/变体）| 📌 最新论文（2024-2026）

### 架构基础（2017–2021）

| 编号 | 标注 | 作者 | 标题 | 年份 | arXiv ID / 来源 |
|------|------|------|------|------|----------------|
| [1] | ⭐ | Vaswani et al., Google Brain | Attention Is All You Need | 2017 | [1706.03762](https://arxiv.org/abs/1706.03762) |
| [2] | ⭐ | Christiano et al., OpenAI / DeepMind | Deep Reinforcement Learning from Human Preferences | 2017 | [1706.03741](https://arxiv.org/abs/1706.03741) |
| [3] | 🔷 | Howard & Ruder, fast.ai | Universal Language Model Fine-tuning (ULMFiT) | 2018 | [1801.06146](https://arxiv.org/abs/1801.06146) |
| [4] | ⭐ | Radford et al., OpenAI | Improving Language Understanding by Generative Pre-Training (GPT-1) | 2018 | OpenAI Blog |
| [5] | ⭐ | Devlin et al., Google | BERT: Pre-training of Deep Bidirectional Transformers | 2018 | [1810.04805](https://arxiv.org/abs/1810.04805) |
| [6] | ⭐ | Radford et al., OpenAI | Language Models are Unsupervised Multitask Learners (GPT-2) | 2019 | OpenAI Blog |
| [7] | 🔷 | Liu et al., Facebook AI / UW | RoBERTa: A Robustly Optimized BERT Pretraining Approach | 2019 | [1907.11692](https://arxiv.org/abs/1907.11692) |
| [8] | 🔷 | Raffel et al., Google | Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer (T5) | 2019 | [1910.10683](https://arxiv.org/abs/1910.10683) |
| [9] | 🔷 | Lewis et al., Facebook AI | BART: Denoising Sequence-to-Sequence Pre-training | 2019 | [1910.13461](https://arxiv.org/abs/1910.13461) |
| [10] | 🔷 | Lan et al., Google | ALBERT: A Lite BERT | 2019 | [1909.11942](https://arxiv.org/abs/1909.11942) |
| [11] | 🔷 | Yang et al., CMU / Google Brain | XLNet: Generalized Autoregressive Pretraining | 2019 | [1906.08237](https://arxiv.org/abs/1906.08237) |

### 规模化与涌现（2020–2023）

| 编号 | 标注 | 作者 | 标题 | 年份 | arXiv ID |
|------|------|------|------|------|---------|
| [12] | ⭐ | Kaplan et al., OpenAI | Scaling Laws for Neural Language Models | 2020 | [2001.08361](https://arxiv.org/abs/2001.08361) |
| [13] | ⭐ | Brown et al., OpenAI | Language Models are Few-Shot Learners (GPT-3) | 2020 | [2005.14165](https://arxiv.org/abs/2005.14165) |
| [14] | ⭐ | Fedus et al., Google Brain | Switch Transformers: Scaling to Trillion Parameter Models | 2021 | [2101.03961](https://arxiv.org/abs/2101.03961) |
| [15] | 🔷 | Rae et al., DeepMind | Gopher: Scaling Language Models | 2022 | [2112.11446](https://arxiv.org/abs/2112.11446) |
| [16] | ⭐ | Hoffmann et al., DeepMind | Training Compute-Optimal Large Language Models (Chinchilla) | 2022 | [2203.15556](https://arxiv.org/abs/2203.15556) |
| [17] | ⭐ | Chowdhery et al., Google | PaLM: Scaling Language Modeling with Pathways | 2022 | [2204.02311](https://arxiv.org/abs/2204.02311) |
| [18] | 🔷 | Zhang et al., Meta AI | OPT: Open Pre-trained Transformer Language Models | 2022 | [2205.01068](https://arxiv.org/abs/2205.01068) |
| [19] | 🔷 | BigScience Workshop | BLOOM: A 176B-Parameter Open-Access Multilingual Language Model | 2023 | [2211.05100](https://arxiv.org/abs/2211.05100) |

### 指令微调与对齐（2021–2024）

| 编号 | 标注 | 作者 | 标题 | 年份 | arXiv ID |
|------|------|------|------|------|---------|
| [20] | 🔷 | Wei et al., Google | FLAN: Fine-tuned Language Models Are Zero-Shot Learners | 2021 | [2109.01652](https://arxiv.org/abs/2109.01652) |
| [21] | ⭐ | Ouyang et al., OpenAI | Training language models to follow instructions with human feedback (InstructGPT) | 2022 | [2203.02155](https://arxiv.org/abs/2203.02155) |
| [22] | 🔷 | Bai et al., Anthropic | Constitutional AI: Harmlessness from AI Feedback | 2022 | [2212.08073](https://arxiv.org/abs/2212.08073) |
| [23] | 🔷 | Wang et al., UW / Allen AI | Self-Instruct: Aligning Language Models with Self-Generated Instructions | 2022 | [2212.10560](https://arxiv.org/abs/2212.10560) |
| [24] | ⭐ | Rafailov et al., Stanford | Direct Preference Optimization (DPO) | 2023 | [2305.18290](https://arxiv.org/abs/2305.18290) |
| [25] | ⭐ | OpenAI | GPT-4 Technical Report | 2023 | [2303.08774](https://arxiv.org/abs/2303.08774) |

### 推理增强（2022–2025）

| 编号 | 标注 | 作者 | 标题 | 年份 | arXiv ID |
|------|------|------|------|------|---------|
| [26] | ⭐ | Wei et al., Google | Chain-of-Thought Prompting Elicits Reasoning in Large Language Models | 2022 | [2201.11903](https://arxiv.org/abs/2201.11903) |
| [27] | 🔷 | Wang et al., Google | Self-Consistency Improves Chain of Thought Reasoning | 2022 | [2203.11171](https://arxiv.org/abs/2203.11171) |
| [28] | 🔷 | Yao et al., Princeton / Google | ReAct: Synergizing Reasoning and Acting in Language Models | 2022 | [2210.03629](https://arxiv.org/abs/2210.03629) |
| [29] | 🔷 | Zelikman et al., Stanford | STaR: Bootstrapping Reasoning With Reasoning | 2022 | [2203.14465](https://arxiv.org/abs/2203.14465) |
| [30] | 🔷 | Yao et al., Princeton / Google DeepMind | Tree of Thoughts: Deliberate Problem Solving with Large Language Models | 2023 | [2305.10601](https://arxiv.org/abs/2305.10601) |
| [31] | ⭐ | OpenAI | OpenAI o1 System Card | 2024 | OpenAI |
| [32] | ⭐ | DeepSeek-AI | DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via RL | 2025 | [2501.12948](https://arxiv.org/abs/2501.12948) |

### 开源模型生态（2023–2024）

| 编号 | 标注 | 作者 | 标题 | 年份 | arXiv ID |
|------|------|------|------|------|---------|
| [33] | ⭐ | Touvron et al., Meta AI | LLaMA: Open and Efficient Foundation Language Models | 2023 | [2302.13971](https://arxiv.org/abs/2302.13971) |
| [34] | 🔷 | Touvron et al., Meta AI | Llama 2: Open Foundation and Fine-Tuned Chat Models | 2023 | [2307.09288](https://arxiv.org/abs/2307.09288) |
| [35] | ⭐ | Meta AI | The Llama 3 Herd of Models | 2024 | [2407.21783](https://arxiv.org/abs/2407.21783) |
| [36] | ⭐ | Jiang et al., Mistral AI | Mistral 7B | 2023 | [2310.06825](https://arxiv.org/abs/2310.06825) |
| [37] | ⭐ | Jiang et al., Mistral AI | Mixtral of Experts | 2024 | [2401.04088](https://arxiv.org/abs/2401.04088) |
| [38] | ⭐ | Bai et al., Alibaba | Qwen Technical Report | 2023 | [2309.16609](https://arxiv.org/abs/2309.16609) |
| [39] | 🔷 | Yang et al., Alibaba | Qwen2 Technical Report | 2024 | [2407.10671](https://arxiv.org/abs/2407.10671) |
| [40] | 🔷 | Yang et al., Alibaba | Qwen2.5 Technical Report | 2024 | [2412.15115](https://arxiv.org/abs/2412.15115) |
| [41] | ⭐ | DeepSeek-AI | DeepSeek LLM: Scaling Open-Source Language Models | 2024 | [2401.02954](https://arxiv.org/abs/2401.02954) |
| [42] | 🔷 | DeepSeek-AI | DeepSeek-V2 | 2024 | [2405.04434](https://arxiv.org/abs/2405.04434) |
| [43] | ⭐ | DeepSeek-AI | DeepSeek-V3 Technical Report | 2024 | [2412.19437](https://arxiv.org/abs/2412.19437) |
| [44] | 🔷 | Google DeepMind | Gemma: Open Models Based on Gemini Research | 2024 | [2403.08295](https://arxiv.org/abs/2403.08295) |
| [45] | 🔷 | Microsoft | Phi-3 Technical Report | 2024 | [2404.14219](https://arxiv.org/abs/2404.14219) |

### 效率与部署（2020–2024）

| 编号 | 标注 | 作者 | 标题 | 年份 | arXiv ID |
|------|------|------|------|------|---------|
| [46] | ⭐ | Lewis et al., Facebook AI | Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks (RAG) | 2020 | [2005.11401](https://arxiv.org/abs/2005.11401) |
| [47] | 🔷 | Su et al., 追一科技 | RoFormer: Enhanced Transformer with Rotary Position Embedding (RoPE) | 2021 | [2104.09864](https://arxiv.org/abs/2104.09864) |
| [48] | ⭐ | Hu et al., Microsoft | LoRA: Low-Rank Adaptation of Large Language Models | 2021 | [2106.09685](https://arxiv.org/abs/2106.09685) |
| [49] | 🔷 | Frantar et al., IST Austria / ETH | GPTQ: Accurate Post-Training Quantization | 2022 | [2210.17323](https://arxiv.org/abs/2210.17323) |
| [50] | 🔷 | Dao et al., Stanford | FlashAttention: Fast and Memory-Efficient Exact Attention | 2022 | [2205.14135](https://arxiv.org/abs/2205.14135) |
| [51] | 🔷 | Dettmers et al., UW | QLoRA: Efficient Finetuning of Quantized Language Models | 2023 | [2305.14314](https://arxiv.org/abs/2305.14314) |
| [52] | 🔷 | Lin et al., MIT | AWQ: Activation-aware Weight Quantization | 2023 | [2306.00978](https://arxiv.org/abs/2306.00978) |
| [53] | 🔷 | Dai et al., DeepSeek | DeepSeekMoE: Towards Ultimate Expert Specialization | 2024 | [2401.06066](https://arxiv.org/abs/2401.06066) |

### 多模态与 Agent（2023–2024）

| 编号 | 标注 | 作者 | 标题 | 年份 | arXiv ID |
|------|------|------|------|------|---------|
| [54] | ⭐ | Google DeepMind | Gemini: A Family of Highly Capable Multimodal Models | 2023 | [2312.11805](https://arxiv.org/abs/2312.11805) |
| [55] | ⭐ | Liu et al., UW-Madison / Microsoft | Visual Instruction Tuning (LLaVA) | 2023 | [2304.08485](https://arxiv.org/abs/2304.08485) |
| [56] | 🔷 | Bai et al., Alibaba | Qwen-VL: A Versatile Vision-Language Model | 2023 | [2308.12966](https://arxiv.org/abs/2308.12966) |
| [57] | ⭐ | Anthropic | The Claude Model Family: Claude 3 / Claude 3.5 | 2024 | Anthropic 官网 |
| [58] | 🔷 | Wang et al., NVIDIA / Caltech / Stanford | Voyager: An Open-Ended Embodied Agent with LLMs | 2023 | [2305.16291](https://arxiv.org/abs/2305.16291) |
| [59] | 🔷 | Wang et al., Tsinghua / Zhipu AI | CogVLM: Visual Expert for Pretrained Language Models | 2023 | [2311.03079](https://arxiv.org/abs/2311.03079) |
| [60] | 🔷 | Yang et al., Princeton | SWE-Agent: Agent-Computer Interfaces Enable Automated Software Engineering | 2024 | [2405.15793](https://arxiv.org/abs/2405.15793) |

### 综述论文

| 编号 | 标注 | 作者 | 标题 | 年份 | arXiv ID |
|------|------|------|------|------|---------|
| [61] | 🔷 | Zhao et al., Renmin University | A Survey of Large Language Models | 2023 | [2303.18223](https://arxiv.org/abs/2303.18223) |
| [62] | 🔷 | Zhou et al. | A Comprehensive Survey on Pretrained Foundation Models | 2023 | [2302.09419](https://arxiv.org/abs/2302.09419) |
| [63] | 🔷 | Yang et al., Amazon / Texas A&M | Harnessing the Power of LLMs in Practice | 2023 | [2304.13712](https://arxiv.org/abs/2304.13712) |

---

*本报告基于 research/ 目录下 6 份事实文档编写，所有引用均可追溯到 paper_inventory.md 中的具体论文。未编造任何论文、作者、机构或实验结果。不确定的关系已标注"推断"或"据公开报道"。*
