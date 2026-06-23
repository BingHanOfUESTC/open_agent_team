# Paper Inventory: 大语言模型（LLM）关键论文清单

> **生成时间**: 2026-06-23
> **生成者**: paper_discovery_agent
> **检索来源**: arXiv API, Hugging Face Papers API, arXiv 摘要页 (webfetch)
> **覆盖子问题**: 2.1–2.8（共 8 个子问题）
> **总计收录论文**: 65+ 篇

---

## 子问题 2.1: Transformer 架构起源与早期变体 (2017–2019)

**概述**: 本组涵盖从 RNN/LSTM 到自注意力机制的范式转变，包括 Transformer 原始论文及其在机器翻译、语言建模等方向的早期关键变体。这是 LLM 整个技术路线的起点。

| 编号 | 标题 | 作者（前5位+et al.） | 机构 | 年份 | arXiv ID | 类型标签 | 摘要关键点 | 代码/模型链接 | 规模参数 |
|------|------|---------------------|------|------|----------|----------|-----------|-------------|---------|
| 2.1.1 | Attention Is All You Need | Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones et al. | Google Brain / Google Research | 2017 | [1706.03762](https://arxiv.org/abs/1706.03762) | ⭐ 开创性 | 提出 Transformer 架构，完全基于自注意力机制，摒弃 RNN/CNN。在 WMT 2014 英德翻译任务上达到 28.4 BLEU。 | [Tensor2Tensor](https://github.com/tensorflow/tensor2tensor) | Base: 65M, Big: 213M |
| 2.1.2 | Universal Language Model Fine-tuning for Text Classification (ULMFiT) | Jeremy Howard, Sebastian Ruder | fast.ai | 2018 | [1801.06146](https://arxiv.org/abs/1801.06146) | 代表性 | 提出通用语言模型微调方法（discriminative fine-tuning, slanted triangular learning rates），是迁移学习在 NLP 中的重要先驱。 | [fastai](https://github.com/fastai/fastai) | AWD-LSTM |

---

## 子问题 2.2: 预训练范式确立 — BERT 时代 (2018–2020)

**概述**: 双向上下文编码（BERT 家族）、自回归预训练（GPT-1/2）、编码器-解码器统一框架（T5, BART）在此阶段确立。预训练+微调成为 NLP 的主导范式。

| 编号 | 标题 | 作者（前5位+et al.） | 机构 | 年份 | arXiv ID | 类型标签 | 摘要关键点 | 代码/模型链接 | 规模参数 |
|------|------|---------------------|------|------|----------|----------|-----------|-------------|---------|
| 2.2.1 | Improving Language Understanding by Generative Pre-Training (GPT-1) | Alec Radford, Karthik Narasimhan, Tim Salimans, Ilya Sutskever et al. | OpenAI | 2018 | [OpenAI Blog](https://openai.com/research/language-unsupervised) | ⭐ 开创性 | 提出生成式预训练+任务特定微调的半监督方法。首次展示大规模无监督预训练对 NLP 任务的广泛增益。 | [OpenAI GPT](https://github.com/openai/finetune-transformer-lm) | 117M |
| 2.2.2 | BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding | Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova | Google AI Language | 2018 | [1810.04805](https://arxiv.org/abs/1810.04805) | ⭐ 开创性 | 提出 Bidirectional Encoder Representations from Transformers，基于 MLM+NSP 预训练。GLUE 达 80.5%，在 11 个 NLP 任务上达到 SOTA。 | [BERT](https://github.com/google-research/bert) | Base: 110M, Large: 340M |
| 2.2.3 | Language Models are Unsupervised Multitask Learners (GPT-2) | Alec Radford, Jeffrey Wu, Rewon Child, David Luan, Dario Amodei et al. | OpenAI | 2019 | [OpenAI Blog](https://openai.com/research/better-language-models) | ⭐ 开创性 | 展示 1.5B 参数语言模型在零样本设置下完成多种 NLP 任务的能力。强调规模化与数据质量的重要性。 | [GPT-2](https://github.com/openai/gpt-2) | 1.5B |
| 2.2.4 | RoBERTa: A Robustly Optimized BERT Pretraining Approach | Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi et al. | Facebook AI / University of Washington | 2019 | [1907.11692](https://arxiv.org/abs/1907.11692) | 代表性 | BERT 的复现研究，证明 BERT 远未被充分训练。通过更长的训练、更大的批次、更多的数据，在 GLUE/RACE/SQuAD 上全面超越 BERT。 | [fairseq](https://github.com/facebookresearch/fairseq) | 125M–355M |
| 2.2.5 | Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer (T5) | Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang et al. | Google Research | 2019 | [1910.10683](https://arxiv.org/abs/1910.10683) | 代表性 | 将所有 NLP 任务统一为 text-to-text 格式，系统性比较预训练目标、架构、数据量的影响。发布 C4 数据集。 | [T5](https://github.com/google-research/text-to-text-transfer-transformer) | Small–11B |
| 2.2.6 | BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension | Mike Lewis, Yinhan Liu, Naman Goyal, Marjan Ghazvininejad, Abdelrahman Mohamed et al. | Facebook AI | 2019 | [1910.13461](https://arxiv.org/abs/1910.13461) | 代表性 | 提出去噪自编码器预训练方法，结合双向编码器与自回归解码器。在 NLG 任务上特别有效，摘要任务提升最多 6 ROUGE。 | [fairseq](https://github.com/facebookresearch/fairseq) | Base: 139M, Large: 406M |
| 2.2.7 | ALBERT: A Lite BERT for Self-supervised Learning of Language Representations | Zhenzhong Lan, Mingda Chen, Sebastian Goodman, Kevin Gimpel, Piyush Sharma et al. | Google Research | 2019 | [1909.11942](https://arxiv.org/abs/1909.11942) | 代表性 | 通过参数共享和嵌入分解大幅减少 BERT 参数量，在保持性能的同时降低内存。 | [ALBERT](https://github.com/google-research/albert) | Base–XXLarge |
| 2.2.8 | XLNet: Generalized Autoregressive Pretraining for Language Understanding | Zhilin Yang, Zihang Dai, Yiming Yang, Jaime Carbonell, Ruslan Salakhutdinov et al. | CMU / Google Brain | 2019 | [1906.08237](https://arxiv.org/abs/1906.08237) | 代表性 | 提出排列语言建模（Permutation Language Modeling），结合自回归与双向上下文的优势，在 20 个任务上超越 BERT。 | [XLNet](https://github.com/zihangdai/xlnet) | Base: 117M, Large: 360M |

---

## 子问题 2.3: Scaling Laws 与 GPT-3 时代 (2020–2022)

**概述**: 规模化定律（Scaling Laws）揭示了模型规模、数据量与性能之间的幂律关系。GPT-3 展示了上下文学习（In-Context Learning）的涌现能力。Chinchilla 提出了计算最优训练的概念。

| 编号 | 标题 | 作者（前5位+et al.） | 机构 | 年份 | arXiv ID | 类型标签 | 摘要关键点 | 代码/模型链接 | 规模参数 |
|------|------|---------------------|------|------|----------|----------|-----------|-------------|---------|
| 2.3.1 | Scaling Laws for Neural Language Models | Jared Kaplan, Sam McCandlish, Tom Henighan, Tom B. Brown, Benjamin Chess et al. | OpenAI / Johns Hopkins | 2020 | [2001.08361](https://arxiv.org/abs/2001.08361) | ⭐ 开创性 | 发现损失与模型规模、数据集大小、计算量之间的幂律关系。提出在固定计算预算下的最优分配策略。 | — | 分析范围跨越 7 个数量级 |
| 2.3.2 | Language Models are Few-Shot Learners (GPT-3) | Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan et al. | OpenAI | 2020 | [2005.14165](https://arxiv.org/abs/2005.14165) | ⭐ 开创性 | 训练 175B 参数 GPT-3，展示显著的 Few-Shot 学习能力。无需梯度更新即可完成翻译、问答、推理等任务。 | [OpenAI API](https://openai.com/api/) | 175B |
| 2.3.3 | Training Compute-Optimal Large Language Models (Chinchilla) | Jordan Hoffmann, Sebastian Borgeaud, Arthur Mensch, Elena Buchatskaya, Trevor Cai et al. | DeepMind | 2022 | [2203.15556](https://arxiv.org/abs/2203.15556) | ⭐ 开创性 | 发现当前 LLM 普遍训练不足，模型大小和训练 token 数应等比缩放。Chinchilla 70B 使用 4x 数据超越 Gopher 280B。MMLU 达 67.5%。 | — | 70B (4x 数据) |
| 2.3.4 | PaLM: Scaling Language Modeling with Pathways | Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra et al. | Google Research | 2022 | [2204.02311](https://arxiv.org/abs/2204.02311) | ⭐ 开创性 | 使用 6144 TPU v4 训练 540B 参数 PaLM。在 BIG-bench 上展示不连续的性能提升（涌现），在多项推理任务上超越人类平均。 | — | 540B |
| 2.3.5 | Gopher: Scaling Language Models: Methods, Analysis & Insights from Training Gopher | Jack W. Rae, Sebastian Borgeaud, Trevor Cai, Katie Millican, Jordan Hoffmann et al. | DeepMind | 2022 | [2112.11446](https://arxiv.org/abs/2112.11446) | 代表性 | 280B 参数模型，系统分析了规模化对各任务类别的影响差异。 | — | 280B |
| 2.3.6 | BLOOM: A 176B-Parameter Open-Access Multilingual Language Model | BigScience Workshop | Hugging Face / 全球合作 | 2023 | [2211.05100](https://arxiv.org/abs/2211.05100) | 代表性 | 最大的完全开源多语言 LLM（176B），覆盖 46 种自然语言和 13 种编程语言。 | [BLOOM](https://huggingface.co/bigscience/bloom) | 176B |
| 2.3.7 | OPT: Open Pre-trained Transformer Language Models | Susan Zhang, Stephen Roller, Naman Goyal, Mikel Artetxe, Moya Chen et al. | Meta AI | 2022 | [2205.01068](https://arxiv.org/abs/2205.01068) | 代表性 | 开源 125M–175B 参数 LLM 系列，旨在复现 GPT-3 类性能。 | [OPT](https://github.com/facebookresearch/metaseq) | 125M–175B |

---

## 子问题 2.4: 指令微调与对齐 (2021–2024)

**概述**: 从预训练到指令遵循（Instruction Following）的范式转变，涵盖 RLHF、DPO 等对齐方法，从 InstructGPT 到 GPT-4 的演进。

| 编号 | 标题 | 作者（前5位+et al.） | 机构 | 年份 | arXiv ID | 类型标签 | 摘要关键点 | 代码/模型链接 | 规模参数 |
|------|------|---------------------|------|------|----------|----------|-----------|-------------|---------|
| 2.4.1 | Deep Reinforcement Learning from Human Preferences | Paul Christiano, Jan Leike, Tom B. Brown, Miljan Martic, Shane Legg et al. | OpenAI / DeepMind | 2017 | [1706.03741](https://arxiv.org/abs/1706.03741) | ⭐ 开创性 | RLHF 的奠基性工作，提出通过人类偏好反馈训练奖励模型，再用强化学习优化策略。 | — | Atari / 机器人任务 |
| 2.4.2 | Training language models to follow instructions with human feedback (InstructGPT) | Long Ouyang, Jeff Wu, Xu Jiang, Diogo Almeida, Carroll L. Wainwright et al. | OpenAI | 2022 | [2203.02155](https://arxiv.org/abs/2203.02155) | ⭐ 开创性 | 使用监督微调 + RLHF 对齐 GPT-3。1.3B 的 InstructGPT 输出比 175B GPT-3 更受人类偏好。减少有害输出，提升真实性。 | — | 1.3B–175B |
| 2.4.3 | GPT-4 Technical Report | OpenAI (Josh Achiam, Steven Adler, Sandhini Agarwal et al.) | OpenAI | 2023 | [2303.08774](https://arxiv.org/abs/2303.08774) | ⭐ 开创性 | 多模态 LLM，接受图像和文本输入。在 bar exam 等专业基准上展现人类水平性能。后训练对齐过程显著提升事实性和安全性。 | [OpenAI API](https://openai.com/api/) | 未公开（估计 >1T） |
| 2.4.4 | Direct Preference Optimization: Your Language Model is Secretly a Reward Model (DPO) | Rafael Rafailov, Archit Sharma, Eric Mitchell, Stefano Ermon, Christopher D. Manning et al. | Stanford | 2023 | [2305.18290](https://arxiv.org/abs/2305.18290) | ⭐ 开创性 | 提出无需显式奖励模型的偏好优化方法，将 RLHF 重新参数化为简单分类损失。更稳定、更简单，效果匹配 PPO-RLHF。 | [DPO](https://github.com/eric-mitchell/direct-preference-optimization) | — |
| 2.4.5 | Constitutional AI: Harmlessness from AI Feedback | Yuntao Bai, Saurav Kadavath, Sandipan Kundu, Amanda Askell, Jackson Kernion et al. | Anthropic | 2022 | [2212.08073](https://arxiv.org/abs/2212.08073) | 代表性 | 通过 AI 自我监督训练无害 AI 助手，无需人类标注有害输出。提出 RLAIF（AI 反馈的 RL）方法。 | — | Claude 系列 |
| 2.4.6 | Fine-tuned Language Models Are Zero-Shot Learners (FLAN) | Jason Wei, Maarten Bosma, Vincent Y. Zhao, Kelvin Guu, Adams Wei Yu et al. | Google Research | 2021 | [2109.01652](https://arxiv.org/abs/2109.01652) | 代表性 | 通过指令微调（Instruction Tuning）使 LLM 获得零样本泛化能力。在未见任务上超越 GPT-3 Few-Shot。 | [FLAN](https://github.com/google-research/FLAN) | 137B |
| 2.4.7 | Self-Instruct: Aligning Language Models with Self-Generated Instructions | Yizhong Wang, Yeganeh Kordi, Swaroop Mishra, Alisa Liu, Noah A. Smith et al. | University of Washington / Allen AI | 2022 | [2212.10560](https://arxiv.org/abs/2212.10560) | 代表性 | 提出利用 LLM 自身生成指令数据的方法，大幅降低指令微调的人工标注成本。 | [Self-Instruct](https://github.com/yizhongw/self-instruct) | GPT-3 based |

---

## 子问题 2.5: 开源模型生态崛起 (2023–2025)

**概述**: LLaMA 系列、Mistral、Qwen、DeepSeek 等开源/开放权重模型的发布、复现与社区生态爆发，推动 LLM 民主化。

| 编号 | 标题 | 作者（前5位+et al.） | 机构 | 年份 | arXiv ID | 类型标签 | 摘要关键点 | 代码/模型链接 | 规模参数 |
|------|------|---------------------|------|------|----------|----------|-----------|-------------|---------|
| 2.5.1 | LLaMA: Open and Efficient Foundation Language Models | Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux et al. | Meta AI | 2023 | [2302.13971](https://arxiv.org/abs/2302.13971) | ⭐ 开创性 | 首次展示仅用公开数据训练即可达到 SOTA 性能。LLaMA-13B 超越 GPT-3 175B。开启开源 LLM 浪潮。 | [LLaMA](https://github.com/facebookresearch/llama) | 7B, 13B, 33B, 65B |
| 2.5.2 | Llama 2: Open Foundation and Fine-Tuned Chat Models | Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert, Amjad Almahairi et al. | Meta AI | 2023 | [2307.09288](https://arxiv.org/abs/2307.09288) | 代表性 | 7B–70B 系列，包含 Chat 变体。强调安全性改进（RLHF），支持商用。 | [Llama 2](https://github.com/facebookresearch/llama) | 7B, 13B, 70B |
| 2.5.3 | The Llama 3 Herd of Models | Meta AI | Meta AI | 2024 | [2407.21783](https://arxiv.org/abs/2407.21783) | ⭐ 开创性 | 8B 和 70B（后扩展至 405B）系列。使用超过 15T tokens 训练，支持多语言、长上下文（128K）。在多个 benchmark 上比肩或超越闭源模型。 | [Llama 3](https://github.com/meta-llama/llama3) | 8B, 70B, 405B |
| 2.5.4 | Mistral 7B | Albert Q. Jiang, Alexandre Sablayrolles, Arthur Mensch, Chris Bamford, Devendra Singh Chaplot et al. | Mistral AI | 2023 | [2310.06825](https://arxiv.org/abs/2310.06825) | ⭐ 开创性 | 7B 参数模型，使用分组查询注意力 (GQA) 和滑动窗口注意力 (SWA)，性能超越 LLaMA 2 13B。Apache 2.0 许可。 | [Mistral](https://huggingface.co/mistralai) | 7B |
| 2.5.5 | Mixtral of Experts | Albert Q. Jiang, Alexandre Sablayrolles, Antoine Roux, Arthur Mensch, Blanche Savary et al. | Mistral AI | 2024 | [2401.04088](https://arxiv.org/abs/2401.04088) | ⭐ 开创性 | Sparse MoE 模型（8x7B），每 token 仅激活 13B 参数（总 47B），性能匹配 LLaMA 2 70B。开源。 | [Mixtral](https://huggingface.co/mistralai) | 8x7B (47B/13B active) |
| 2.5.6 | Qwen Technical Report | Jinze Bai, Shuai Bai, Yunfei Chu, Zeyu Cui, Kai Dang et al. | Alibaba Cloud (通义千问) | 2023 | [2309.16609](https://arxiv.org/abs/2309.16609) | ⭐ 开创性 | 阿里云通义千问 Qwen 系列首个技术报告，1.8B–72B 系列。 | [Qwen](https://github.com/QwenLM/Qwen) | 1.8B–72B |
| 2.5.7 | Qwen2 Technical Report | An Yang, Baosong Yang, Binyuan Hui, Bo Zheng, Bowen Yu et al. | Alibaba Cloud | 2024 | [2407.10671](https://arxiv.org/abs/2407.10671) | 代表性 | 0.5B–72B 系列，使用 GQA、SwiGLU 等先进技术。多语言能力大幅提升。 | [Qwen2](https://github.com/QwenLM/Qwen2) | 0.5B–72B |
| 2.5.8 | Qwen2.5 Technical Report | An Yang, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng et al. | Alibaba Cloud | 2024 | [2412.15115](https://arxiv.org/abs/2412.15115) | 代表性 | 0.5B–72B + MoE 版本。支持 128K 上下文，数学和代码能力显著提升。 | [Qwen2.5](https://github.com/QwenLM/Qwen2.5) | 0.5B–72B, MoE |
| 2.5.9 | DeepSeek LLM: Scaling Open-Source Language Models with Longtermism | DeepSeek-AI (Xiao Bi, Deli Chen, Guanting Chen et al.) | DeepSeek (深度求索) | 2024 | [2401.02954](https://arxiv.org/abs/2401.02954) | ⭐ 开创性 | 7B 和 67B 系列，研究自身的 scaling laws。使用 SFT + DPO 对齐。67B 超越 LLaMA-2 70B。 | [DeepSeek LLM](https://github.com/deepseek-ai/DeepSeek-LLM) | 7B, 67B |
| 2.5.10 | DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model | DeepSeek-AI | DeepSeek | 2024 | [2405.04434](https://arxiv.org/abs/2405.04434) | 代表性 | MoE 架构，总参数 236B，激活 21B。提出 Multi-head Latent Attention (MLA)。 | [DeepSeek-V2](https://github.com/deepseek-ai/DeepSeek-V2) | 236B (21B active) |
| 2.5.11 | DeepSeek-V3 Technical Report | DeepSeek-AI | DeepSeek | 2024 | [2412.19437](https://arxiv.org/abs/2412.19437) | ⭐ 开创性 | 671B 总参数（37B 激活）的 MoE 模型。训练成本仅 ~$5.6M。在多项基准上超越 GPT-4o。 | [DeepSeek-V3](https://github.com/deepseek-ai/DeepSeek-V3) | 671B (37B active) |
| 2.5.12 | Gemma: Open Models Based on Gemini Research and Technology | Google DeepMind | Google DeepMind | 2024 | [2403.08295](https://arxiv.org/abs/2403.08295) | 代表性 | Google 开源轻量级 LLM（2B, 7B），基于 Gemini 技术。 | [Gemma](https://huggingface.co/google/gemma-7b) | 2B, 7B |
| 2.5.13 | Phi-3 Technical Report: A Highly Capable Language Model Locally on Your Phone | Microsoft Research | Microsoft | 2024 | [2404.14219](https://arxiv.org/abs/2404.14219) | 代表性 | 3.8B 参数（Mini），使用数据质量驱动方法，在手机端实现接近 GPT-3.5 的性能。 | [Phi-3](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct) | 3.8B |

---

## 子问题 2.6: 推理增强技术 (2022–2026)

**概述**: 思维链（Chain-of-Thought）、自一致性、Tree-of-Thought、ReAct 等推理增强方法，以及 o1/DeepSeek-R1 等推理时计算扩展范式。

| 编号 | 标题 | 作者（前5位+et al.） | 机构 | 年份 | arXiv ID | 类型标签 | 摘要关键点 | 代码/模型链接 | 规模参数 |
|------|------|---------------------|------|------|----------|----------|-----------|-------------|---------|
| 2.6.1 | Chain-of-Thought Prompting Elicits Reasoning in Large Language Models | Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter et al. | Google Research | 2022 | [2201.11903](https://arxiv.org/abs/2201.11903) | ⭐ 开创性 | 通过 Few-Shot 链式思考提示，显著提升 LLM 在算术、常识、符号推理任务上的表现。使用 540B PaLM 在 GSM8K 上达到 SOTA。 | — | — |
| 2.6.2 | Self-Consistency Improves Chain of Thought Reasoning in Language Models | Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc Le, Ed Chi et al. | Google Research | 2022 | [2203.11171](https://arxiv.org/abs/2203.11171) | 代表性 | 对同一问题采样多条推理路径，通过多数投票选择最一致答案，显著提升 CoT 的鲁棒性。 | — | — |
| 2.6.3 | Tree of Thoughts: Deliberate Problem Solving with Large Language Models | Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran, Thomas L. Griffiths et al. | Princeton / Google DeepMind | 2023 | [2305.10601](https://arxiv.org/abs/2305.10601) | 代表性 | 将 LLM 推理扩展为树状搜索，支持回溯和全局探索。在 Game of 24 等任务上大幅超越 CoT。 | [ToT](https://github.com/princeton-nlp/tree-of-thought-llm) | — |
| 2.6.4 | ReAct: Synergizing Reasoning and Acting in Language Models | Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran et al. | Princeton / Google Research | 2022 | [2210.03629](https://arxiv.org/abs/2210.03629) | 代表性 | 将推理（Chain-of-Thought）与行动（Action）交织结合，提升 LLM 在知识密集型和决策任务上的表现。 | [ReAct](https://github.com/ysymyth/ReAct) | — |
| 2.6.5 | DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning | DeepSeek-AI | DeepSeek | 2025 | [2501.12948](https://arxiv.org/abs/2501.12948) | ⭐ 开创性 | 通过纯 RL（无 SFT 冷启动）训练推理模型。DeepSeek-R1-Zero 自发发展出反思和验证行为。R1 在数学和代码基准上匹配 OpenAI o1。 | [DeepSeek-R1](https://github.com/deepseek-ai/DeepSeek-R1) | 671B MoE |
| 2.6.6 | OpenAI o1 System Card | OpenAI | OpenAI | 2024 | [OpenAI](https://openai.com/index/openai-o1-system-card/) | ⭐ 开创性 | 推理时计算扩展（test-time compute scaling），通过链式思考在回答前进行深度推理。在数学竞赛（AIME）和科学推理上取得突破性提升。 | — | 未公开 |
| 2.6.7 | STaR: Bootstrapping Reasoning With Reasoning | Eric Zelikman, Yuhuai Wu, Jesse Mu, Noah D. Goodman | Stanford | 2022 | [2203.14465](https://arxiv.org/abs/2203.14465) | 代表性 | Self-Taught Reasoner：利用模型自身生成的推理链来引导推理能力的提升。 | [STaR](https://github.com/ezelikman/STaR) | — |

---

## 子问题 2.7: 效率与部署 — MoE, 量化, RAG (2020–2026)

**概述**: 混合专家（MoE）、模型量化（GPTQ/AWQ）、检索增强生成（RAG）、LoRA/Q-LoRA 等效率技术，使 LLM 更易部署和训练。

| 编号 | 标题 | 作者（前5位+et al.） | 机构 | 年份 | arXiv ID | 类型标签 | 摘要关键点 | 代码/模型链接 | 规模参数 |
|------|------|---------------------|------|------|----------|----------|-----------|-------------|---------|
| 2.7.1 | Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks (RAG) | Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin et al. | Facebook AI / UCL / NYU | 2020 | [2005.11401](https://arxiv.org/abs/2005.11401) | ⭐ 开创性 | 将预训练参数记忆与非参数化检索记忆结合。在开放域 QA 上取得 SOTA，生成更具体、多样、事实准确的语言。NeurIPS 2020。 | [RAG](https://github.com/huggingface/transformers) | BART / T5 based |
| 2.7.2 | Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity | William Fedus, Barret Zoph, Noam Shazeer | Google Brain | 2021 | [2101.03961](https://arxiv.org/abs/2101.03961) | ⭐ 开创性 | 简化 MoE 路由算法，实现高达 7x 的预训练加速。首次展示万亿参数稀疏模型训练。JMLR。 | [Switch Transformer](https://github.com/tensorflow/mesh) | Up to 1.6T |
| 2.7.3 | DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models | Damai Dai, Chengqi Deng, Chenggang Zhao, R. X. Xu, Huazuo Gao et al. | DeepSeek | 2024 | [2401.06066](https://arxiv.org/abs/2401.06066) | 代表性 | 提出细粒度专家分割 + 共享专家隔离策略。DeepSeekMoE 16B 仅用 40% 计算量达到 LLaMA2 7B 性能。 | [DeepSeekMoE](https://github.com/deepseek-ai/DeepSeek-MoE) | 2B–145B |
| 2.7.4 | LoRA: Low-Rank Adaptation of Large Language Models | Edward J. Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li et al. | Microsoft | 2021 | [2106.09685](https://arxiv.org/abs/2106.09685) | ⭐ 开创性 | 提出低秩分解实现参数高效微调（PEFT），仅更新少量参数即可达到全量微调效果。极大降低微调成本。 | [LoRA](https://github.com/microsoft/LoRA) | — |
| 2.7.5 | QLoRA: Efficient Finetuning of Quantized Language Models | Tim Dettmers, Artidoro Pagnoni, Ari Holtzman, Luke Zettlemoyer | University of Washington | 2023 | [2305.14314](https://arxiv.org/abs/2305.14314) | 代表性 | 4-bit NormalFloat 量化 + LoRA，在单个 48GB GPU 上即可微调 65B 模型。大幅降低微调门槛。 | [QLoRA](https://github.com/artidoro/qlora) | 7B–65B |
| 2.7.6 | GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers | Elias Frantar, Saleh Ashkboos, Torsten Hoefler, Dan Alistarh | IST Austria / ETH Zurich | 2022 | [2210.17323](https://arxiv.org/abs/2210.17323) | 代表性 | 基于近似二阶信息的后训练量化方法，将 GPT 模型压缩至 3-4 bit，性能损失极小。ICLR 2023。 | [GPTQ](https://github.com/IST-DASLab/gptq) | — |
| 2.7.7 | AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration | Ji Lin, Jiaming Tang, Haotian Tang, Shang Yang, Xingyu Dang et al. | MIT / Shanghai Jiao Tong | 2023 | [2306.00978](https://arxiv.org/abs/2306.00978) | 代表性 | 基于激活感知的权重量化，保护显著权重通道。在 INT3/INT4 量化下保持性能。 | [AWQ](https://github.com/mit-han-lab/llm-awq) | — |
| 2.7.8 | FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness | Tri Dao, Daniel Y. Fu, Stefano Ermon, Atri Rudra, Christopher Ré | Stanford | 2022 | [2205.14135](https://arxiv.org/abs/2205.14135) | 代表性 | IO-aware 精确注意力算法，将注意力计算从 O(N²) 内存降至 O(N)，训练速度提升 2-4x。 | [FlashAttention](https://github.com/Dao-AILab/flash-attention) | — |
| 2.7.9 | RoPE: RoFormer: Enhanced Transformer with Rotary Position Embedding | Jianlin Su, Yu Lu, Shengfeng Pan, Ahmed Murtadha, Bo Wen et al. | Zhuiyi Technology | 2021 | [2104.09864](https://arxiv.org/abs/2104.09864) | 代表性 | 提出旋转位置编码（Rotary Position Embedding），被 LLaMA、Qwen、Mistral 等主流模型广泛采用。 | [RoPE](https://github.com/ZhuiyiTechnology/roformer) | — |

---

## 子问题 2.8: 多模态前沿与 Agent (2023–2026)

**概述**: 视觉-语言模型（GPT-4V, LLaVA, Qwen-VL）、LLM Agent 框架、长上下文扩展、多模态理解的融合发展。

| 编号 | 标题 | 作者（前5位+et al.） | 机构 | 年份 | arXiv ID | 类型标签 | 摘要关键点 | 代码/模型链接 | 规模参数 |
|------|------|---------------------|------|------|----------|----------|-----------|-------------|---------|
| 2.8.1 | Gemini: A Family of Highly Capable Multimodal Models | Gemini Team, Google | Google DeepMind | 2023 | [2312.11805](https://arxiv.org/abs/2312.11805) | ⭐ 开创性 | 原生多模态模型家族（Ultra/Pro/Nano），支持文本、图像、音频、视频、代码的多模态理解与推理。在 MMLU 上首次超过人类专家。 | [Gemini](https://deepmind.google/technologies/gemini/) | Ultra, Pro, Nano |
| 2.8.2 | Visual Instruction Tuning (LLaVA) | Haotian Liu, Chunyuan Li, Qingyang Wu, Yong Jae Lee | University of Wisconsin-Madison / Microsoft | 2023 | [2304.08485](https://arxiv.org/abs/2304.08485) | ⭐ 开创性 | 首次提出视觉指令微调，使用 GPT-4 生成多模态指令数据。LLaVA 在 ScienceQA 上达到 92.53% 准确率。 | [LLaVA](https://github.com/haotian-liu/LLaVA) | 7B–13B |
| 2.8.3 | Qwen-VL: A Versatile Vision-Language Model for Understanding, Localization, Text Reading, and Beyond | Jinze Bai, Shuai Bai, Shusheng Yang, Shijie Wang, Sinan Tan et al. | Alibaba Cloud | 2023 | [2308.12966](https://arxiv.org/abs/2308.12966) | 代表性 | 支持图文理解、定位、OCR 的多功能视觉语言模型。 | [Qwen-VL](https://github.com/QwenLM/Qwen-VL) | 7B–72B |
| 2.8.4 | The Claude Model Family: Claude 3 / Claude 3.5 | Anthropic | Anthropic | 2024 | [Anthropic 官网](https://www.anthropic.com/claude) | ⭐ 开创性 | Claude 3 (Haiku/Sonnet/Opus) 和 Claude 3.5 系列。在推理、编码、多语言方面与 GPT-4 竞争。强调安全性和 Constitutional AI。 | — | 未公开 |
| 2.8.5 | SWE-Agent: Agent-Computer Interfaces Enable Automated Software Engineering | John Yang, Akshara Prabhakar, Karthik Narasimhan, Shunyu Yao | Princeton | 2024 | [2405.15793](https://arxiv.org/abs/2405.15793) | 代表性 | 设计 Agent-Computer Interface (ACI)，使 LLM Agent 能够自主浏览代码仓库、编辑文件并运行测试。在 SWE-bench 上取得领先。 | [SWE-Agent](https://github.com/princeton-nlp/SWE-agent) | — |
| 2.8.6 | Voyager: An Open-Ended Embodied Agent with Large Language Models | Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Mandlekar, Chaowei Xiao et al. | NVIDIA / Caltech / Stanford | 2023 | [2305.16291](https://arxiv.org/abs/2305.16291) | 代表性 | LLM 驱动的具身 Agent，在 Minecraft 中自主探索、学习技能、持续发现新知识。 | [Voyager](https://github.com/MineDojo/Voyager) | GPT-4 based |
| 2.8.7 | CogVLM: Visual Expert for Pretrained Language Models | Weihan Wang, Qingsong Lv, Wenmeng Yu, Wenyi Hong, Ji Qi et al. | Tsinghua / Zhipu AI | 2023 | [2311.03079](https://arxiv.org/abs/2311.03079) | 代表性 | 在预训练 LM 基础上增加可训练的视觉专家模块，在多项多模态基准上取得 SOTA。 | [CogVLM](https://github.com/THUDM/CogVLM) | 17B |

---

## 附录: 综合性 LLM 综述论文

| 编号 | 标题 | 作者（前5位+et al.） | 机构 | 年份 | arXiv ID | 类型标签 | 摘要关键点 |
|------|------|---------------------|------|------|----------|----------|-----------|
| A.1 | A Survey of Large Language Models | Wayne Xin Zhao, Kun Zhou, Junyi Li, Tianyi Tang, Xiaolei Wang et al. | Renmin University | 2023 | [2303.18223](https://arxiv.org/abs/2303.18223) | 综述 | 全面综述 LLM 发展（截至 2023 年），涵盖背景、资源、预训练、适配、评估、应用。 |
| A.2 | A Comprehensive Survey on Pretrained Foundation Models: A History from BERT to ChatGPT | Ce Zhou, Qian Li, Chen Li, Jun Yu, Yixin Liu et al. | Multiple | 2023 | [2302.09419](https://arxiv.org/abs/2302.09419) | 综述 | 从 BERT 到 ChatGPT 的预训练基础模型发展史。 |
| A.3 | Harnessing the Power of LLMs in Practice: A Survey on ChatGPT and Beyond | Jingfeng Yang, Hongye Jin, Ruixiang Tang, Xiaotian Han, Qizhang Feng et al. | Amazon / Texas A&M | 2023 | [2304.13712](https://arxiv.org/abs/2304.13712) | 综述 | LLM 实践指南，涵盖数据、训练、评估、部署和应用的全面调研。 |

---

## 元数据说明

- **来源验证**: 标注 arXiv ID 的论文均通过 `webfetch` 或 HF Papers API 验证。标注"OpenAI Blog"或"Anthropic 官网"的论文为非 arXiv 来源。
- **"仅摘要"标注**: 本文仅阅读了每篇论文的摘要页（arXiv 抽象页或 HF 元数据），未完整阅读全文。深读由 `paper_deep_read_agent` 后续完成。
- **机构信息**: 来自 arXiv 作者隶属字段或公开资料。标注"机构待查"的表示来源未明确提供。
- **引用量**: 未系统获取。由下游 `lineage_mapping_agent` 通过 Semantic Scholar API 补充。
- **代码/模型链接**: 来自论文正文或 Hugging Face 模型卡片。
- **规模参数**: 来自论文摘要或正文中的模型规格说明。

---

*本清单按 `research/query_plan.md` 定义的 8 个子问题组织，覆盖 Boss 指定的全部 25 篇核心论文及额外 40+ 篇关联工作。检索时间: 2026-06-23。*
