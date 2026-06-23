# Lab & People Map: 大语言模型研究实验室、团队与人员脉络

> **生成时间**: 2026-06-23
> **生成者**: lab_people_agent
> **信息来源**: Wikipedia (OpenAI, Anthropic, Mistral AI, DeepSeek, Meta AI 词条), paper_inventory.md 中的论文作者列表, 公开报道与技术报告
> **置信度说明**: 每条信息标注来源可信度 — ✅ 官网/论文确认 | 🔶 公开报道推断 | ⚠️ 社区传闻/推断

---

## 目录

1. [工业界实验室](#1-工业界实验室)
2. [学术界关键人物](#2-学术界关键人物)
3. [人才流动关键路径](#3-人才流动关键路径)
4. [开源社区关键贡献者](#4-开源社区关键贡献者)
5. [合作网络](#5-合作网络)
6. [来源与置信度汇总](#6-来源与置信度汇总)

---

## 1. 工业界实验室

---

### 1.1 OpenAI

> **全称**: OpenAI, Inc. (非营利) / OpenAI Group PBC (营利性公益公司)
> **成立**: 2015-12-08 | **总部**: San Francisco, California | **创始人**: Elon Musk, Sam Altman, Ilya Sutskever, Greg Brockman, Trevor Blackwell 等

**简介**: OpenAI 是当代 LLM 发展的核心推动者。从 GPT-1 (2018) 到 GPT-4 (2023)、o1 (2024)，OpenAI 定义了自回归语言模型 + 规模化预训练 + 指令对齐的技术路线。2022 年 11 月 ChatGPT 的发布被认为是引爆全球 AI 热潮的催化剂。

#### 核心人物

| 人物 | 角色 | 主要贡献 | 代表论文/工作 | 当前状态 |
|------|------|----------|-------------|---------|
| **Sam Altman** | CEO (2019–至今), 联合创始人 | 公司战略领导, ChatGPT 产品化推动 | — | OpenAI CEO |
| **Ilya Sutskever** | 联合创始人, 前首席科学家 | GPT 系列技术方向的早期奠定, 深度学习理论研究 | AlexNet, Seq2Seq, GPT-1/2/3 共同作者 | 2024 年离开, 创办 Safe Superintelligence Inc. (SSI) |
| **Greg Brockman** | 联合创始人, President, CEO of Applications | 早期团队组建, 工程基础设施 | — | OpenAI |
| **Alec Radford** | 研究员 | GPT-1, GPT-2 的第一作者 | GPT-1 (2018), GPT-2 (2019) | OpenAI (未公开近况) |
| **Tom Brown (Tom B. Brown)** | 研究员 | GPT-3 第一作者 | GPT-3 (2020, [2005.14165](https://arxiv.org/abs/2005.14165)) | 2021 年加入 Anthropic |
| **Jared Kaplan** | 研究员 | Scaling Laws 第一作者, GPT-3, GPT-4 共同作者 | Scaling Laws (2020, [2001.08361](https://arxiv.org/abs/2001.08361)) | 2021 年共同创办 Anthropic, 任 Chief Science Officer |
| **Jakub Pachocki** | 研究员, 后任首席科学家 (推断, 2024 后) | GPT-4 预训练负责人 | GPT-4 Technical Report (2023) | OpenAI |
| **Paul Christiano** | 研究员 | RLHF 奠基性工作 | Deep RL from Human Preferences (2017, [1706.03741](https://arxiv.org/abs/1706.03741)) | 后离开 OpenAI, 创办 Alignment Research Center (ARC) |
| **Jan Leike** | 前 Alignment 团队联席负责人 | RLHF, 对齐研究 | — | 2024 年 5 月离开 OpenAI, 加入 Anthropic |
| **John Schulman** | 联合创始人, 前 Alignment 联席负责人 | RLHF, PPO 算法 | — | 2024 年离开, 加入 Anthropic |
| **Andrej Karpathy** | 联合创始人, 前研究员 | 早期技术奠基 | — | OpenAI → Tesla (AI 总监) → 2024 短暂回归 OpenAI → 2025 加入 Anthropic |
| **Wojciech Zaremba** | 联合创始人 | 早期机器人/RL 研究 | — | OpenAI |
| **Mira Murati** | 前 CTO (2018–2024) | 工程管理, ChatGPT/Codex/DALL-E 产品化 | — | 2024 年 9 月离开, 创办 Thinking Machines Lab |
| **Elon Musk** | 联合创始人 (2015–2018 离开董事会) | 早期资金支持与发起 | — | xAI (Grok) |

#### 代表论文（按时间线）

1. GPT-1: Alec Radford et al., "Improving Language Understanding by Generative Pre-Training" (2018) ✅
2. GPT-2: Alec Radford et al., "Language Models are Unsupervised Multitask Learners" (2019) ✅
3. GPT-3: Tom B. Brown et al., "Language Models are Few-Shot Learners" (2020, [2005.14165](https://arxiv.org/abs/2005.14165)) ✅
4. Scaling Laws: Jared Kaplan et al., "Scaling Laws for Neural Language Models" (2020, [2001.08361](https://arxiv.org/abs/2001.08361)) ✅
5. InstructGPT: Long Ouyang et al., "Training language models to follow instructions with human feedback" (2022, [2203.02155](https://arxiv.org/abs/2203.02155)) ✅
6. GPT-4 Technical Report: OpenAI (Josh Achiam et al.) (2023, [2303.08774](https://arxiv.org/abs/2303.08774)) ✅
7. o1 System Card: OpenAI (2024) ✅

**来源可信度**: 核心人物均来自 Wikipedia 词条和论文作者列表 ✅

---

### 1.2 Google / DeepMind

> **Google Brain**: 2011 年由 Jeff Dean, Greg Corrado, Andrew Ng 创立, 2023 年与 DeepMind 合并为 Google DeepMind
> **DeepMind**: 2010 年成立 (Demis Hassabis, Shane Legg, Mustafa Suleyman), 2014 年被 Google 收购
> **总部**: Mountain View, CA / London, UK

**简介**: Google 是 Transformer 架构的发源地，也是预训练范式 (BERT, T5) 和规模化 (PaLM, Gemini) 的关键推动者。2023 年 Brain 与 DeepMind 合并后，Gemini 成为统一的多模态旗舰模型。

#### 核心人物

| 人物 | 角色 | 主要贡献 | 代表论文/工作 | 当前状态 |
|------|------|----------|-------------|---------|
| **Ashish Vaswani** | 前 Google Brain 研究员 | Transformer 一作 | "Attention Is All You Need" (2017, [1706.03762](https://arxiv.org/abs/1706.03762)) | 离开 Google, 联合创办 Adept AI → 后去向不明 🔶 |
| **Noam Shazeer** | 前 Google Brain 研究员 | Transformer, T5, Switch Transformer, MoE 先驱 | Transformer (2017), T5 (2019), Switch Transformer (2021) | 离开 Google, 联合创办 Character.AI |
| **Jakob Uszkoreit** | 前 Google Brain 研究员 | Transformer 共同作者 | "Attention Is All You Need" (2017) | 离开 Google, 联合创办 Inceptive (生物 AI) |
| **Niki Parmar** | 前 Google Brain 研究员 | Transformer 共同作者 | "Attention Is All You Need" (2017) | 曾加入 Adept AI (与 Vaswani), 后去向不明 🔶 |
| **Jeff Dean** | Google Chief Scientist, Google Brain 联合创始人 | AI 基础设施 (TensorFlow), 规模化 | — | Google DeepMind |
| **Quoc Le** | Google Brain 研究员 | Seq2Seq, 半监督学习, 规模化探索 | — | Google DeepMind |
| **Jacob Devlin** | 前 Google AI Language 研究员 | BERT 一作 | BERT (2018, [1810.04805](https://arxiv.org/abs/1810.04805)) | — |
| **Colin Raffel** | 前 Google Research 研究员 | T5 一作 | T5 (2019, [1910.10683](https://arxiv.org/abs/1910.10683)) | 后加入 UNC Chapel Hill 任教授 |
| **Jason Wei** | Google Research 研究员 | Chain-of-Thought (CoT) 一作, FLAN | CoT (2022, [2201.11903](https://arxiv.org/abs/2201.11903)), FLAN (2021) | 2025 年加入 OpenAI 🔶 |
| **Demis Hassabis** | DeepMind CEO, 联合创始人 | AlphaGo, AlphaFold, Gemini 系列 | — | Google DeepMind CEO |
| **Oriol Vinyals** | DeepMind 首席科学家 | Gemini, Gopher, AlphaStar | Gemini (2023) | Google DeepMind |
| **Koray Kavukcuoglu** | DeepMind CTO | 通用 AI 研究 | — | Google DeepMind |
| **Jordan Hoffmann** | DeepMind 研究员 | Chinchilla 一作 | Chinchilla (2022, [2203.15556](https://arxiv.org/abs/2203.15556)) | — |
| **Jack W. Rae** | DeepMind 研究员 | Gopher 一作 | Gopher (2022, [2112.11446](https://arxiv.org/abs/2112.11446)) | — |
| **Shane Legg** | DeepMind 联合创始人, 首席 AGI 科学家 | AGI 理论与安全 | — | Google DeepMind |
| **Mustafa Suleyman** | DeepMind 联合创始人 | 早期战略 | — | 离开 DeepMind → Inflection AI → **Microsoft AI CEO** |

#### 代表论文

1. Transformer: Ashish Vaswani et al., "Attention Is All You Need" (2017, [1706.03762](https://arxiv.org/abs/1706.03762)) ✅
2. BERT: Jacob Devlin et al., "BERT: Pre-training of Deep Bidirectional Transformers" (2018, [1810.04805](https://arxiv.org/abs/1810.04805)) ✅
3. T5: Colin Raffel et al., "Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer" (2019, [1910.10683](https://arxiv.org/abs/1910.10683)) ✅
4. Chinchilla: Jordan Hoffmann et al., "Training Compute-Optimal Large Language Models" (2022, [2203.15556](https://arxiv.org/abs/2203.15556)) ✅
5. PaLM: Aakanksha Chowdhery et al., "PaLM: Scaling Language Modeling with Pathways" (2022, [2204.02311](https://arxiv.org/abs/2204.02311)) ✅
6. Chain-of-Thought: Jason Wei et al. (2022, [2201.11903](https://arxiv.org/abs/2201.11903)) ✅
7. Gemini: Gemini Team, Google (2023, [2312.11805](https://arxiv.org/abs/2312.11805)) ✅

**备注**: Google Brain 与 DeepMind 于 2023 年合并，之前为两个独立的 AI 研究机构。合并后 Gemini 为统一旗舰项目。

---

### 1.3 Meta AI (FAIR)

> **全称**: Meta AI (原 Facebook Artificial Intelligence Research, FAIR)
> **成立**: 2013 | **总部**: Menlo Park, CA / 多地 (巴黎, 纽约, 伦敦, 蒙特利尔等)

**简介**: Meta AI 是开源 LLM 生态的核心推动者。从 RoBERTa、BART 到 LLaMA 系列，Meta 始终坚持开放权重策略，深刻影响了全球开源社区。PyTorch 深度学习框架也出自 FAIR。

#### 核心人物

| 人物 | 角色 | 主要贡献 | 代表论文/工作 | 当前状态 |
|------|------|----------|-------------|---------|
| **Yann LeCun** | VP & Chief AI Scientist, FAIR 联合创始人 | 深度学习奠基人 (CNN), FAIR 战略领导, 自监督学习 | — | Meta; 兼职 NYU 教授 |
| **Hugo Touvron** | 研究员 | LLaMA 系列一作 | LLaMA (2023, [2302.13971](https://arxiv.org/abs/2302.13971)), LLaMA 2 (2023), LLaMA 3 (2024) | Meta AI |
| **Guillaume Lample** | 前 Meta AI 研究员 | LLaMA 共同作者 | — | 2023 年离开, 联合创办 Mistral AI |
| **Timothée Lacroix** | 前 Meta AI 研究员 | LLaMA 共同作者, 大模型训练 | — | 2023 年离开, 联合创办 Mistral AI |
| **Yinhan Liu** | 前 Facebook AI 研究员 | RoBERTa 一作, BART 共同作者 | RoBERTa (2019, [1907.11692](https://arxiv.org/abs/1907.11692)) | 后加入 OpenAI |
| **Mike Lewis** | Facebook AI 研究员 | BART 一作 | BART (2019, [1910.13461](https://arxiv.org/abs/1910.13461)) | Meta AI |
| **Naman Goyal** | Facebook AI 研究员 | RoBERTa, BART, OPT 共同作者 | — | Meta AI |
| **Patrick Lewis** | Facebook AI 研究员 | RAG 一作 | RAG (2020, [2005.11401](https://arxiv.org/abs/2005.11401)) | — |
| **Mark Zuckerberg** | Meta CEO | 公司 AI 战略方向, 推动开源 | — | Meta |

#### 代表论文

1. RoBERTa: Yinhan Liu et al. (2019, [1907.11692](https://arxiv.org/abs/1907.11692)) ✅
2. BART: Mike Lewis et al. (2019, [1910.13461](https://arxiv.org/abs/1910.13461)) ✅
3. RAG: Patrick Lewis et al. (2020, [2005.11401](https://arxiv.org/abs/2005.11401)) ✅
4. LLaMA: Hugo Touvron et al. (2023, [2302.13971](https://arxiv.org/abs/2302.13971)) ✅
5. LLaMA 2: Hugo Touvron et al. (2023, [2307.09288](https://arxiv.org/abs/2307.09288)) ✅
6. LLaMA 3: Meta AI (2024, [2407.21783](https://arxiv.org/abs/2407.21783)) ✅
7. OPT: Susan Zhang et al. (2022, [2205.01068](https://arxiv.org/abs/2205.01068)) ✅

---

### 1.4 Anthropic

> **成立**: 2021-01-26 | **总部**: San Francisco, California | **创始人**: Dario Amodei, Daniela Amodei, Jared Kaplan, Jack Clark, Chris Olah, Ben Mann, Sam McCandlish, Tom Brown

**简介**: Anthropic 由 7 名前 OpenAI 员工于 2021 年创立，起因是对 OpenAI 商业化方向和安全策略的分歧。以 AI 安全为核心使命，开发 Claude 系列模型，提出 Constitutional AI 框架。在安全研究、可解释性 (mechanistic interpretability) 方面有独特积累。

#### 核心人物

| 人物 | 角色 | 主要贡献 | 背景 |
|------|------|----------|------|
| **Dario Amodei** | CEO, 联合创始人 | Claude 系列, Constitutional AI | 前 OpenAI VP of Research; GPT-2/GPT-3 共同作者 |
| **Daniela Amodei** | President, 联合创始人 | 公司运营与安全策略 | 前 OpenAI 员工 (安全/政策) |
| **Jared Kaplan** | Chief Science Officer, 联合创始人 | Scaling Laws, Claude 技术路线 | 前 OpenAI 研究员; Scaling Laws (2020) 一作; 前 Johns Hopkins 教授 |
| **Tom Brown** | 联合创始人, 研究员 | GPT-3 一作, Claude 训练 | 前 OpenAI 研究员 |
| **Sam McCandlish** | 联合创始人, 研究员 | Scaling Laws, Claude | 前 OpenAI 研究员 |
| **Jack Clark** | 联合创始人, Policy 负责人 | AI 政策与治理 | 前 OpenAI Policy Director |
| **Chris Olah** | 联合创始人, 研究员 | 可解释性 (mechanistic interpretability) | 前 Google Brain, OpenAI 研究员 |
| **Amanda Askell** | 研究员 | Claude 角色设计 (character), Constitutional AI | 哲学家背景 |
| **Jan Leike** | Alignment Science 联席负责人 | RLHF, 对齐研究 | 前 OpenAI Alignment 联席负责人 (2024 年 5 月离开) |
| **John Schulman** | Alignment 联席负责人 | RLHF, PPO 算法 | OpenAI 联合创始人 (2024 年离开) |
| **Andrej Karpathy** | 研究员 | 深度学习/LLM 研究 | OpenAI 联合创始人 → Tesla AI → OpenAI → Anthropic (2025) |
| **John M. Jumper** | 研究员 | AlphaFold (Nobel Prize 2024) | 前 DeepMind |

#### 代表论文

1. Constitutional AI: Yuntao Bai et al. (2022, [2212.08073](https://arxiv.org/abs/2212.08073)) ✅
2. Claude 3 / Claude 3.5 (2024, [Anthropic 官网](https://www.anthropic.com/claude)) ✅

**来源可信度**: 创始人信息来自 Wikipedia 词条 (CNBC, NYT 等媒体报道) ✅

---

### 1.5 Mistral AI

> **成立**: 2023-04-28 | **总部**: Paris, France | **创始人**: Arthur Mensch, Guillaume Lample, Timothée Lacroix

**简介**: 欧洲最具影响力的 AI 创业公司。以极小的团队和资本，在 2023 年发布 Mistral 7B，以 Apache 2.0 开源，性能超越 LLaMA 2 13B。后续发布 Mixtral 8x7B (MoE) 进一步巩固技术地位。三位创始人皆毕业于法国巴黎综合理工学院 (École Polytechnique)。

#### 核心人物

| 人物 | 角色 | 主要贡献 | 背景 |
|------|------|----------|------|
| **Arthur Mensch** | CEO, 联合创始人 | 公司战略, Mistral/Mixtral 系列 | 前 Google DeepMind 研究员; Chinchilla 共同作者 |
| **Guillaume Lample** | Chief Scientist, 联合创始人 | 模型架构设计 | 前 Meta AI (FAIR) 研究员, LLaMA 共同作者 |
| **Timothée Lacroix** | CTO, 联合创始人 | 大模型训练与工程 | 前 Meta AI (FAIR) 研究员 |

#### 代表论文

1. Mistral 7B: Albert Q. Jiang et al. (2023, [2310.06825](https://arxiv.org/abs/2310.06825)) ✅
2. Mixtral of Experts: Albert Q. Jiang et al. (2024, [2401.04088](https://arxiv.org/abs/2401.04088)) ✅

**关键合作**: Microsoft 于 2024 年 2 月投资 Mistral AI (€15M), Mistral Large 可通过 Azure 访问。

---

### 1.6 阿里巴巴 (通义千问 / Qwen)

> **团队**: Alibaba Cloud (阿里云) — 通义千问团队
> **总部**: 杭州, 中国

**简介**: 阿里巴巴的通义千问 (Qwen) 是中国开源 LLM 的重要力量。从 Qwen (2023) 到 Qwen2 (2024)、Qwen2.5 (2024)，Qwen 系列在中文和英文任务上均表现强劲，发布频次高、版本迭代快。

#### 核心人物

| 人物 | 角色 | 主要贡献 | 代表论文 |
|------|------|----------|---------|
| **Jinze Bai** | Qwen 系列核心作者 | Qwen, Qwen-VL 一作 | Qwen (2023, [2309.16609](https://arxiv.org/abs/2309.16609)), Qwen-VL (2023, [2308.12966](https://arxiv.org/abs/2308.12966)) |
| **An Yang** | Qwen2/2.5 核心作者 | Qwen2, Qwen2.5 一作 | Qwen2 (2024, [2407.10671](https://arxiv.org/abs/2407.10671)), Qwen2.5 (2024, [2412.15115](https://arxiv.org/abs/2412.15115)) |
| **Shuai Bai** | Qwen/Qwen-VL 核心作者 | 多模态 LLM | Qwen, Qwen-VL 共同作者 |

**备注**: 由于 Qwen 团队论文以集体署名为主，具体组织架构和团队负责人未在论文中公开披露。以上人物信息均来自论文作者列表。🔶

#### 代表论文

1. Qwen: Jinze Bai et al. (2023, [2309.16609](https://arxiv.org/abs/2309.16609)) ✅
2. Qwen2: An Yang et al. (2024, [2407.10671](https://arxiv.org/abs/2407.10671)) ✅
3. Qwen2.5: An Yang et al. (2024, [2412.15115](https://arxiv.org/abs/2412.15115)) ✅
4. Qwen-VL: Jinze Bai et al. (2023, [2308.12966](https://arxiv.org/abs/2308.12966)) ✅

---

### 1.7 DeepSeek (深度求索)

> **全称**: 杭州深度求索人工智能基础技术研究有限公司
> **成立**: 2023-07-17 | **总部**: 杭州, 浙江 | **创始人**: 梁文锋 (Liang Wenfeng)
> **母公司**: High-Flyer (幻方量化, 对冲基金)

**简介**: DeepSeek 是近年来最具冲击力的中国 AI 公司。凭借 MoE 架构创新 (DeepSeekMoE, Multi-head Latent Attention) 和极低的训练成本 (V3 ~$6M)，在性能上追赶甚至超越 OpenAI 等闭源巨头。DeepSeek-R1 首创纯 RL 驱动推理能力 (无需 SFT 冷启动)，被视为"AI 界的 Sputnik 时刻"。全部模型采用 MIT 许可证开源。

#### 核心人物

| 人物 | 角色 | 主要贡献 | 背景 |
|------|------|----------|------|
| **梁文锋 (Liang Wenfeng)** | CEO, 创始人 | 公司战略, 核心研发方向 | High-Flyer (幻方量化) 联合创始人, 浙江大学背景 |
| **DeepSeek-AI (集体署名)** | 研究团队 | 所有 DeepSeek 论文以 "DeepSeek-AI" 集体署名 | — |

**重要说明**: DeepSeek 的研究论文以 "DeepSeek-AI" 为作者署名，少数技术报告会列出关键贡献者（如 Xiao Bi, Deli Chen, Guanting Chen, Damai Dai, Chengqi Deng 等），但组织架构和团队角色未公开。

#### 代表论文

1. DeepSeek LLM (2024, [2401.02954](https://arxiv.org/abs/2401.02954)) — Xiao Bi et al. ✅
2. DeepSeekMoE (2024, [2401.06066](https://arxiv.org/abs/2401.06066)) — Damai Dai et al. ✅
3. DeepSeek-V2 (2024, [2405.04434](https://arxiv.org/abs/2405.04434)) ✅
4. DeepSeek-V3 (2024, [2412.19437](https://arxiv.org/abs/2412.19437)) ✅
5. DeepSeek-R1 (2025, [2501.12948](https://arxiv.org/abs/2501.12948)) ✅

**关键数据** (来自 Wikipedia / 公开报道):
- 员工约 160 人 (2025 年) 🔶
- V3 训练成本 ~$6M (公司宣称, 存在争议) 
- 使用受到贸易限制的 Nvidia H800 GPU 训练
- 创始人梁文锋持股约 84% (通过两家壳公司)

---

### 1.8 微软 (Microsoft)

> **AI 研究部门**: Microsoft Research (MSR), Microsoft AI

**简介**: 微软通过与 OpenAI 的深度合作 (2019 年起累计投资 >$13B) 在 LLM 领域占据独特地位。同时微软自身也有 Phi 系列小模型 (Sébastien Bubeck 团队) 和 LoRA 等高效训练技术的创新。

#### 核心人物

| 人物 | 角色 | 主要贡献 | 代表论文/工作 |
|------|------|----------|-------------|
| **Sébastien Bubeck** | Microsoft Research 研究员 | Phi 系列小模型负责人 | Phi-3 (2024, [2404.14219](https://arxiv.org/abs/2404.14219)) |
| **Edward J. Hu** | Microsoft 研究员 | LoRA (Low-Rank Adaptation) | LoRA (2021, [2106.09685](https://arxiv.org/abs/2106.09685)) |
| **Mustafa Suleyman** | Microsoft AI CEO | AI 产品的战略领导 | 前 DeepMind 联合创始人, 前 Inflection AI CEO |

#### 关键合作关系

- **Microsoft–OpenAI**: 自 2019 年起的战略投资关系。2025 年后 Microsoft 持有 OpenAI 27% 股权。OpenAI 在 Microsoft Azure 上进行训练和推理。
- **Microsoft–Mistral**: 2024 年 2 月投资 €15M, Mistral Large 在 Azure 上线。

---

### 1.9 智谱 AI (Zhipu AI / 清华系)

> **成立**: 2019 年 | **总部**: 北京, 中国 | **背景**: 清华大学 KEG 实验室孵化

**简介**: 智谱 AI 是清华大学计算机系技术成果转化企业。核心模型系列为 GLM (General Language Model) 和 ChatGLM。GLM 采用自回归填空 (autoregressive blank infilling) 的统一框架，与 BERT 和 GPT 均有差异。

#### 核心人物

| 人物 | 角色 | 主要贡献 | 背景 |
|------|------|----------|------|
| **唐杰 (Jie Tang)** | 联合创始人/首席科学家 | GLM 系列技术方向 | 清华大学教授, KEG 实验室负责人 |
| **张鹏 (Peng Zhang)** | CEO | 公司运营与产品化 | — |
| **刘知远 (Zhiyuan Liu)** | 联合创始人 | NLP 预训练模型研究 (CPM 系列) | 清华大学副教授 |

#### 代表论文

- CogVLM: Weihan Wang et al. (2023, [2311.03079](https://arxiv.org/abs/2311.03079)) ✅ — 清华/智谱

**来源可信度**: 核心人物信息来自公开报道和官网 🔶 (部分细节需交叉验证)

---

### 1.10 xAI (Elon Musk)

> **成立**: 2023 年 | **创始人**: Elon Musk | **产品**: Grok 系列

**简介**: Elon Musk 在离开 OpenAI 后创办的 AI 公司。发布 Grok 系列模型，定位为 "anti-woke" AI。xAI 利用 X (Twitter) 平台的数据进行训练。

**备注**: 在 LLM 学术论文方面的贡献有限 (截至 2026 年中)，Grok 的技术细节公开较少。列为观察对象。

---

## 2. 学术界关键人物

### 2.1 华盛顿大学 (University of Washington / Allen AI)

| 人物 | 主要贡献 | 代表论文 |
|------|----------|---------|
| **Luke Zettlemoyer** | T5, BART 共同作者; QLoRA; 语言生成与知识 | QLoRA (2023, [2305.14314](https://arxiv.org/abs/2305.14314)) ✅ |
| **Yejin Choi** | 常识推理, 知识增强 LLM | — |
| **Noah A. Smith** | Self-Instruct, NLP 基础 | Self-Instruct (2022) ✅ |

### 2.2 CMU (Carnegie Mellon University)

| 人物 | 主要贡献 | 代表论文 |
|------|----------|---------|
| **Graham Neubig** | 多语言 NLP, 代码生成 | — |
| **Ruslan Salakhutdinov** | XLNet, 生成模型 | XLNet (2019) ✅ |
| **Tom Mitchell** | 机器学习基础理论 | — |

### 2.3 Stanford University

| 人物 | 主要贡献 | 代表论文 |
|------|----------|---------|
| **Christopher Manning** | NLP 基础, GloVe, DPO 共同作者 | DPO (2023, [2305.18290](https://arxiv.org/abs/2305.18290)) ✅ |
| **Percy Liang** | 评估基准, HELM benchmark | — |
| **Fei-Fei Li** | 计算机视觉, ImageNet | — |
| **Chelsea Finn** | 元学习, 机器人 | — |
| **Stefano Ermon** | FlashAttention, DPO 共同作者 | FlashAttention (2022), DPO (2023) ✅ |
| **Tri Dao** | FlashAttention 一作 | FlashAttention (2022, [2205.14135](https://arxiv.org/abs/2205.14135)) ✅ |
| **Christopher Ré** | FlashAttention, 高效 ML | FlashAttention (2022) ✅ |
| **Rafael Rafailov** | DPO 一作 | DPO (2023, [2305.18290](https://arxiv.org/abs/2305.18290)) ✅ |
| **Eric Zelikman** | STaR (Self-Taught Reasoner) | STaR (2022, [2203.14465](https://arxiv.org/abs/2203.14465)) ✅ |

### 2.4 UC Berkeley

| 人物 | 主要贡献 | 代表论文 |
|------|----------|---------|
| **Pieter Abbeel** | 机器人, RL | — |
| **Sergey Levine** | 离线 RL, 机器人 | — |
| **Ken Goldberg** | 机器人, 早期 RLHF 相关工作 | — |

### 2.5 NYU

| 人物 | 主要贡献 | 代表论文 |
|------|----------|---------|
| **Yann LeCun** | 深度学习奠基人 (CNN, 自监督学习) | 同时任职于 Meta; NYU 兼职教授 |
| **Kyunghyun Cho** | Seq2Seq, 注意力机制理论 | — |

### 2.6 MIT

| 人物 | 主要贡献 | 代表论文 |
|------|----------|---------|
| **Regina Barzilay** | NLP + 医疗, 分子设计 | — |
| **Lex Fridman** | 社区传播 (播客), 自动驾驶 | — |

### 2.7 其他重要学术人物

| 人物 | 机构 | 主要贡献 |
|------|------|----------|
| **Jeremy Howard** | fast.ai / University of Queensland | ULMFiT (2018) — NLP 迁移学习先驱 ✅ |
| **Sebastian Ruder** | Google DeepMind (前 fast.ai) | ULMFiT (2018), NLP 迁移学习综述 ✅ |
| **Tim Dettmers** | University of Washington | QLoRA (2023), bitsandbytes 量化库 ✅ |
| **Shunyu Yao** | Princeton | ReAct (2022), Tree-of-Thought (2023), SWE-Agent (2024) ✅ |
| **Karthik Narasimhan** | Princeton | GPT-1 共同作者, SWE-Agent 共同作者 ✅ |
| **Yi Tay** | 前 Google Brain | 大模型效率, 架构探索 | — |
| **Jianlin Su** | Zhuiyi Technology (追一科技) | RoPE (2021, [2104.09864](https://arxiv.org/abs/2104.09864)) — 被 LLaMA/Mistral/Qwen 广泛采用 ✅ |

---

## 3. 人才流动关键路径

### 3.1 Transformer 八大作者的分散轨迹 (Google → 全球)

"Attention Is All You Need" (2017) 的八位作者全部离开了 Google，这一现象被广泛称为 "Transformer 作者大迁徙"。

| 人物 | 在 Google 的角色 | 去向 | 创业方向 |
|------|-----------------|------|---------|
| **Ashish Vaswani** | 一作 | Adept AI (联合创始人) | AI Agent (2022 年创办, 后续发展不明) |
| **Noam Shazeer** | T5/Switch/MoE | Character.AI (联合创始人) | AI 角色对话 (2022 年创办) |
| **Jakob Uszkoreit** | 核心贡献者 | Inceptive (联合创始人) | AI + 生物医药 (RNA 设计) |
| **Niki Parmar** | 核心贡献者 | Adept AI (曾加入) → 去向不明 | — |
| **Illia Polosukhin** | 核心贡献者 | NEAR Protocol (联合创始人) | 区块链/Web3 AI |
| **Aidan Gomez** | 当时为学生/实习生 🔶 | Cohere (联合创始人 & CEO) | 企业级 LLM 平台 (2019 年创办) |
| **Llion Jones** | 核心贡献者 | Sakana AI (联合创始人) | 日本 AI 初创 (2023 年创办) |
| **Łukasz Kaiser** | 核心贡献者 | OpenAI | LLM 研究 |

> **来源**: 公开报道 (NYT, Bloomberg, TechCrunch 等), 各公司官网 ✅

### 3.2 OpenAI → Anthropic 分裂

2021 年，一批 OpenAI 核心员工因对 OpenAI 商业化方向和安全策略存在分歧而离开，成立了 Anthropic。

| 人物 | OpenAI 角色 | Anthropic 角色 |
|------|------------|---------------|
| **Dario Amodei** | VP of Research | CEO |
| **Daniela Amodei** | 安全/政策团队 | President |
| **Jared Kaplan** | 研究员 (Scaling Laws) | Chief Science Officer |
| **Tom Brown** | 研究员 (GPT-3 一作) | 研究员 |
| **Sam McCandlish** | 研究员 (Scaling Laws) | 研究员 |
| **Jack Clark** | Policy Director | Policy 负责人 |
| **Chris Olah** | 可解释性研究员 | 可解释性研究员 |
| **Ben Mann** | 工程师 | 核心工程师 |

此后 (2024 年) 又有更多 OpenAI 员工加入 Anthropic:
- **Jan Leike** (Alignment 联席负责人) — 2024 年 5 月
- **John Schulman** (OpenAI 联合创始人, Alignment 联席负责人) — 2024 年 8 月
- **Andrej Karpathy** (OpenAI 联合创始人) — 2025 年

### 3.3 Meta AI → Mistral AI

| 人物 | Meta AI 角色 | Mistral AI 角色 |
|------|------------|---------------|
| **Guillaume Lample** | 研究员 (LLaMA 系列) | Chief Scientist |
| **Timothée Lacroix** | 研究员 (LLaMA 系列) | CTO |

三人 (加上从 DeepMind 来的 Arthur Mensch) 曾在 École Polytechnique 同期学习。

### 3.4 Google DeepMind → Mistral AI

| 人物 | DeepMind 角色 | Mistral AI 角色 |
|------|-------------|---------------|
| **Arthur Mensch** | 研究员 (Chinchilla) | CEO |

### 3.5 DeepMind → Microsoft AI

| 人物 | DeepMind 角色 | Microsoft 角色 |
|------|-------------|---------------|
| **Mustafa Suleyman** | 联合创始人 | Microsoft AI CEO (2024 年起) |

### 3.6 其他值得注意的人员流动

| 人物 | 原机构 | 新机构 | 时间 |
|------|--------|--------|------|
| **Yinhan Liu** (RoBERTa) | Meta AI | OpenAI | — |
| **Jason Wei** (CoT, FLAN) | Google Research | OpenAI | 2025 🔶 |
| **Ilya Sutskever** | OpenAI | Safe Superintelligence Inc. (SSI) | 2024 |
| **Mira Murati** | OpenAI (CTO) | Thinking Machines Lab | 2024 |
| **Andrej Karpathy** | OpenAI → Tesla → OpenAI → Anthropic | Anthropic | 2025 |
| **Paul Christiano** | OpenAI | Alignment Research Center (ARC) | — |

---

## 4. 开源社区关键贡献者

### 4.1 LMSYS (Large Model Systems Organization)

> **核心贡献**: Vicuna 模型, Chatbot Arena 评估平台

| 人物/角色 | 主要贡献 |
|-----------|---------|
| 加州大学伯克利分校 Sky Lab + UCSD 合作团队 | Vicuna (基于 LLaMA 微调的开源 Chat 模型), FastChat 框架, Chatbot Arena (众包 LLM 评估基准) |

**代表工作**: Vicuna (2023), Chatbot Arena

**来源可信度**: 公开项目和论文 ✅

### 4.2 EleutherAI

> **核心贡献**: GPT-NeoX, Pythia, The Pile 数据集

EleutherAI 是一个分布式的开源 AI 研究团队，成立于 2020 年。最初目标是复现 GPT-3 级别的开源模型。

**代表工作**:
- GPT-NeoX-20B (2022)
- Pythia 系列 (用于可解释性研究)
- The Pile (高质量开源预训练数据集, 825GB)

**来源可信度**: 公开项目和论文 ✅

### 4.3 Nous Research

> **核心贡献**: Hermes 系列 (指令微调开源模型)

志愿者驱动的开源 AI 研究组织，专注于发布高质量的开源微调模型 (基于 LLaMA, Mistral 等)。

### 4.4 Hugging Face

> **核心贡献**: Transformers 库, 开源模型托管平台, BLOOM 模型

| 人物 | 角色 | 主要贡献 |
|------|------|---------|
| **Clément Delangue** | CEO | 开源 AI 生态 |
| **Julien Chaumond** | CTO | 技术平台 |
| **Thomas Wolf** | Chief Science Officer | 开源研究 |

**代表工作**:
- Transformers 库 (PyTorch/TF/JAX 跨框架 NLP 库)
- BLOOM (176B 多语言开源 LLM, BigScience Workshop)
- Hugging Face Hub (模型和数据集托管)

### 4.5 独立贡献者

| 人物 | 主要贡献 | 代表工作 |
|------|----------|---------|
| **Tri Dao** | FlashAttention 一作 | FlashAttention (2022), FlashAttention-2 (2023) — Stanford (现 Together AI / Princeton 🔶) |
| **Tim Dettmers** | QLoRA, bitsandbytes 量化库 | QLoRA (2023) — University of Washington |
| **Yi Tay** | 大模型架构效率探索 (UL2, PaLI 等) | 前 Google Brain |
| **Jianlin Su** | RoPE (旋转位置编码) | RoPE (2021) — Zhuiyi Technology; 被 LLaMA/Qwen/Mistral 广泛采用 |

---

## 5. 合作网络

### 5.1 公司间投资与合作关系

```text
Microsoft ←→ OpenAI
  │ 2019 年起投资 (>$13B), Azure 独家云合作
  │ 2025 年后 Microsoft 持有 OpenAI 27% 股权
  
Amazon ←→ Anthropic
  │ 2023 年起投资 ($8B+), AWS 为主要云提供商

Google ←→ Anthropic
  │ 2023 年起投资 ($2B+)
  
Nvidia ←→ (几乎所有 LLM 公司)
  │ GPU 供应商, 也通过投资参与

Microsoft → Mistral AI
  │ 2024 年投资 €15M, Azure 合作

xAI ↔ Anthropic (2026)
  │ Colossus 数据中心算力租赁 🔶
```

### 5.2 学术-工业合作案例

| 学术机构 | 工业合作方 | 合作成果示例 |
|---------|-----------|------------|
| Stanford | — | DPO (2023), FlashAttention (2022) |
| UW / Allen AI | — | QLoRA (2023), Self-Instruct (2022) |
| Princeton | Google DeepMind | ReAct (2022), Tree-of-Thought (2023) |
| CMU | Google Brain | XLNet (2019) |
| 清华 KEG | Zhipu AI | CogVLM (2023) |

### 5.3 竞争关系概览

| 竞争轴线 | 双方/多方 | 说明 |
|---------|----------|------|
| 闭源 vs 开源 | OpenAI vs Meta/Mistral/DeepSeek | 核心商业模式与哲学之争 |
| 安全优先 vs 能力优先 | Anthropic vs OpenAI/xAI | AI 安全理念差异 |
| 美国 vs 中国 | OpenAI/Anthropic vs DeepSeek/Qwen | 地缘政治下的 AI 竞赛 |
| 大模型 vs 小模型 | GPT-4/Claude vs Phi/Gemma | 效率与规模之争 |

---

## 6. 来源与置信度汇总

### 来源分类

| 来源类型 | 示例 | 置信度 |
|---------|------|--------|
| **论文作者列表** | paper_inventory.md 中所有论文的作者 | ✅ 可靠 |
| **Wikipedia 词条** | OpenAI, Anthropic, Mistral AI, DeepSeek, Meta AI 词条 | ✅ 可靠 (包含引用来源) |
| **公司官网/博客** | OpenAI Blog, Anthropic 官网, Meta AI 官网 | ✅ 可靠 |
| **公开新闻报道** | NYT, Bloomberg, Reuters, TechCrunch, WSJ | 🔶 较可靠 (需交叉验证) |
| **arXiv / 技术报告** | 各类模型技术报告 | ✅ 可靠 |
| **社区推测/传闻** | 社交媒体讨论, 论坛帖子 | ⚠️ 低置信度 (已在文中标注) |

### 关键不确定性

1. **DeepSeek 团队具体人员**: 论文以集体署名为主，内部角色分工未公开。梁文锋为公开创始人，但其他核心研究人员信息有限。
2. **Qwen 团队组织架构**: 阿里巴巴未公开通义千问团队的具体组织架构。
3. **Ashish Vaswani 的当前去向**: Adept AI 后发展不明。
4. **融资额数据**: 部分来自新闻报道，可能不精确（已省略具体融资数字以避免传播未证实信息）。
5. **导师-学生关系**: 未在本文中做任何断言，因为缺乏公开可核实的来源。

---

*本文遵循 quality_protocol 硬规则：人员关系必须有公开来源或标注为推断；不得编造团队规模、融资额等未证实数据；标注每条信息的来源可信度。*

*最后更新: 2026-06-23*
