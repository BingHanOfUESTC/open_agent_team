# Method Taxonomy: 大语言模型（LLM）方法分类脉络

> **生成时间**: 2026-06-23
> **生成者**: method_taxonomy_agent
> **数据基础**: `research/paper_inventory.md`（65+ 篇论文）、`research/query_plan.md`（8 个子问题范围）
> **组织原则**: 按"问题如何被定义 → 方法如何解决 → 方法间如何演化"组织，而非按论文标题罗列。
> **标注规则**: 标注 `[PI-X.X.X]` 的论文引用自 paper_inventory.md 对应编号。

---

## 0. 总览：七个方法维度及其内在关系

本分类体系将 LLM 研究的方法论组织为 **7 个核心维度**。这 7 个维度并非独立并列，而是构成一个层次化的"问题-方法-优化"关系网：

```
维度 A: 模型架构 ← 基础骨架，"用什么结构建模"
   ├─ 决定能力天花板
   └─ 演化驱动维度 B（预训练目标）和维度 C（规模扩展）

维度 B: 预训练方法 ← 学习范式，"如何从数据中学习"
   ├─ 与维度 A 耦合：不同架构需要不同的预训练目标
   └─ 为维度 D（对齐）提供基础模型

维度 C: 规模扩展 ← 工程科学，"多大算够、怎么分配算好"
   ├─ 回答维度 A+B 的"乘数效应"问题
   └─ 催生维度 F（效率优化）的需求

维度 D: 对齐方法 ← 价值规约，"让模型做人类想要的"
   ├─ 维度 B 预训练模型 → 维度 D 后训练对齐
   └─ 维度 E 推理时的行为受对齐约束

维度 E: 推理增强 ← 认知策略，"让模型想得更深"
   ├─ 维度 D 对齐模型 → 维度 E 推理策略
   └─ 与维度 G（外部知识）协作用于复杂任务

维度 F: 效率优化 ← 工程约束，"又好又快又省"
   ├─ 服务于维度 A（架构效率）+ 维度 C（训练效率）+ 维度 E（推理效率）
   └─ 使大规模模型（维度 C）可部署

维度 G: 外部知识 ← 知识边界，"模型记不住、需要查"
   ├─ 弥补维度 B 参数记忆的局限
   └─ 与维度 E（推理增强）协同工作
```

---

## 维度 A: 模型架构 (Model Architecture)

### A.1 编码器-解码器架构 (Encoder-Decoder)

**问题定义**: 如何在统一的序列到序列框架中同时实现双向理解和自回归生成？

| 节点 | 年份 | 代表论文 | 核心思想 | 演化关系 |
|------|------|----------|----------|----------|
| **A.1.1** Transformer (原版) | 2017 | `Attention Is All You Need` (Vaswani et al., Google Brain) [PI-2.1.1] | 完全基于自注意力机制的序列到序列架构。6层编码器 + 6层解码器，无 RNN/CNN。多头注意力 (MHA) + 位置编码 + 残差连接 + Layer Norm。在 WMT 2014 英德翻译 BLEU 28.4。参数量 Base: 65M, Big: 213M。 | 整个 LLM 领域的架构起点。编码器 → BERT 路线；解码器 → GPT 路线；编码器-解码器 → T5/BART 路线。 |
| **A.1.2** T5 | 2019 | `Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer` (Raffel et al., Google) [PI-2.2.5] | 将所有 NLP 任务统一为 text-to-text 格式（输入文本 → 输出文本）。Encoder-decoder Transformer 架构。系统性比较预训练目标、架构变体、数据量和模型规模的影响。发布 C4 数据集。Scale: Small ~ 11B。 | 统一了编码器-解码器范式的预训练方式。后训练的 text-to-text 思想影响指令微调。不如 decoder-only 在语言生成上高效。 |
| **A.1.3** BART | 2019 | `BART: Denoising Sequence-to-Sequence Pre-training` (Lewis et al., Facebook AI) [PI-2.2.6] | 去噪自编码器预训练：对文本施加多种噪声（token 掩码、删除、文本填充、句子重排），训练模型恢复原文本。双向编码器 + 自回归解码器。在摘要生成任务上提升最多 6 ROUGE。Scale: Base 139M, Large 406M。 | 与 T5 同期，但更侧重 NLG 任务（文本生成/摘要）。去噪思路启发了后续 UL2。在纯理解任务上弱于 BERT，在纯生成任务上弱于 GPT。 |

**优劣对比**:
- **Encoder-Decoder 优势**: 输入和输出解耦，适合翻译/摘要等输入输出长度不对称的任务；编码器提供双向上下文，解码器保持因果性。
- **劣势**: 参数量是 decoder-only 的两倍（同样性能下）；架构不够统一，逐渐被 decoder-only 在大部分场景中替代。
- **代表性应用**: T5 和 BART 至今仍是 NLP 学术实验的重要 baseline。

---

### A.2 仅编码器架构 (Encoder-only)

**问题定义**: 如何在无生成需求时最大化对文本的双向理解能力？

| 节点 | 年份 | 代表论文 | 核心思想 | 演化关系 |
|------|------|----------|----------|----------|
| **A.2.1** BERT | 2018 | `BERT: Pre-training of Deep Bidirectional Transformers` (Devlin et al., Google) [PI-2.2.2] | 仅使用 Transformer 编码器堆叠。双向自注意力，可同时看到左右上下文。预训练：MLM（Masked Language Model）+ NSP（下一句预测）。GLUE 达 80.5%，在 11 个 NLP 任务 SOTA。Scale: Base 110M, Large 340M。 | 开启了"预训练+微调"时代。NSP 后被证实非必要（RoBERTa 弃之）。架构上限受限于仅编码器（无法生成），LLM 时代被 decoder-only 替代。 |
| **A.2.2** RoBERTa | 2019 | `RoBERTa: A Robustly Optimized BERT Pretraining Approach` (Liu et al., Facebook AI / UW) [PI-2.2.4] | BERT 的严格复现研究。关键改进：更长的训练、更大的 batch size、更多数据、去掉 NSP 任务、使用动态掩码。证明 BERT 远未被充分训练。在 GLUE/RACE/SQuAD 上全面超越 BERT。 | 揭示了预训练方法论比架构创新更重要的规律——"把 BERT 训练得更好"即可显著超越 BERT。这一发现影响了后续所有预训练研究。 |
| **A.2.3** ALBERT | 2019 | `ALBERT: A Lite BERT` (Lan et al., Google) [PI-2.2.7] | 通过参数共享（跨层共享注意力参数和前馈参数）和嵌入矩阵分解大幅减少参数量。在保持性能的同时降低内存占用。 | 面向部署场景的效率优化，但推理速度并未因参数减少而提升（因为计算量未减少）。适合内存受限场景。 |
| **A.2.4** XLNet | 2019 | `XLNet: Generalized Autoregressive Pretraining` (Yang et al., CMU / Google Brain) [PI-2.2.8] | 排列语言建模 (Permutation LM)：对所有可能的 token 排列进行自回归建模，实现双向上下文的利用，同时避免 MLM 的 [MASK] 符号问题（预训练-微调不一致）。在 20 个任务上超越 BERT。 | 试图解决 MLM 的核心缺陷（预训练时有 [MASK]，微调时没有），但排列操作的计算开销大。后续被 DeBERTa 在 NLP 理解任务上超越。 |

**优劣对比**:
- **Encoder-only 优势**: 双向上下文理解充分，适合分类、序列标注、句子对匹配等 NLU 任务。训练效率高（无自回归解码）。
- **劣势**: 无法进行文本生成；需要下游任务的特定头（task-specific head），泛化性不如 decoder-only；在 LLM 时代基本被 decoder-only 替代（即使是理解任务，也可以通过 prompt 实现）。
- **现状**: 主要作为 embedding 模型使用（如 BGE, E5），或作为轻量级 NLU baseline。

---

### A.3 仅解码器架构 (Decoder-only)

**问题定义**: 如何用单一自回归架构统一所有语言任务（理解 + 生成），并通过规模扩展获取泛化能力？

| 节点 | 年份 | 代表论文 | 核心思想 | 演化关系 |
|------|------|----------|----------|----------|
| **A.3.1** GPT-1 | 2018 | `Improving Language Understanding by Generative Pre-Training` (Radford et al., OpenAI) [PI-2.2.1] | 第一代生成式预训练 Transformer。12层 decoder-only 架构。预训练（自回归语言建模）+ 有监督微调两阶段。117M 参数。首次展示无监督预训练 + 任务特定微调的范式。 | 与 BERT 同期但方向不同：GPT 走生成路线，BERT 走理解路线。微调范式与 BERT 相同，但架构是 decoder-only（因果注意力掩码）。 |
| **A.3.2** GPT-2 | 2019 | `Language Models are Unsupervised Multitask Learners` (Radford et al., OpenAI) [PI-2.2.3] | 1.5B 参数。提出语言模型是"无监督多任务学习器"。零样本（zero-shot）完成翻译、问答、摘要等多种任务，无需微调。强调数据质量和规模的重要性。 | 范式转变：从"预训练+微调"到"预训练+提示"。不再需要任务特定的微调。奠定了"Few-Shot / Zero-Shot 提示"的路线。但因规模限制（1.5B），实际 zero-shot 效果有限。 |
| **A.3.3** GPT-3 | 2020 | `Language Models are Few-Shot Learners` (Brown et al., OpenAI) [PI-2.3.2] | 175B 参数。核心发现：通过上下文学习 (In-Context Learning)，无需梯度更新即可完成翻译、问答、推理等任务。模型的元学习能力在规模达到一定阈值后涌现。 | 将 decoder-only 架构推到极致规模。Few-Shot 学习能力成为了 LLM 定义的标志。但其上下文学习能力远不如后续的指令微调模型。 |
| **A.3.4** LLaMA 系列 | 2023-2024 | LLaMA (Meta, 2023) [PI-2.5.1], LLaMA 2 [PI-2.5.2], LLaMA 3 [PI-2.5.3] | 证明仅使用公开数据即可训练 SOTA decoder-only 模型。LLaMA-13B 超越 GPT-3 175B。LLaMA 3 使用 >15T tokens 训练，支持 128K 上下文。LLaMA 3.1 最高到 405B。核心技术创新：Pre-Norm (RMSNorm)、SwiGLU 激活、RoPE 位置编码。 | 开启了开源 LLM 时代。RoPE + SwiGLU + RMSNorm 成为开源 decoder-only 的事实标准配置。LLaMA 3 在多个 benchmark 上比肩或超越闭源模型。 |
| **A.3.5** Mistral 7B | 2023 | `Mistral 7B` (Jiang et al., Mistral AI) [PI-2.5.4] | 7B decoder-only，使用分组查询注意力 (GQA)、滑动窗口注意力 (SWA)。性能超越 LLaMA 2 13B。Apache 2.0 许可。 | 展示了高效的注意力机制（GQA + SWA）在较小模型中也能取得出色性能。SWA 使长序列推理内存线性增长。 |
| **A.3.6** Qwen 系列 | 2023-2024 | Qwen [PI-2.5.6], Qwen2 [PI-2.5.7], Qwen2.5 [PI-2.5.8] | 阿里通义千问 decoder-only 系列。Qwen2: GQA + SwiGLU + 多语言；Qwen2.5: 128K 上下文、数学/代码能力突出、含 MoE 版本。Scale: 0.5B~72B。 | 中文 LLM 的代表性工作之一。规模覆盖广泛（从边缘部署到云端），Qwen2.5 在代码和数学上达到开源领先水平。 |
| **A.3.7** DeepSeek 系列 | 2024 | DeepSeek LLM [PI-2.5.9], DeepSeek-V2/V3 [PI-2.5.10, PI-2.5.11] | 中国深度求索团队。DeepSeek-V3: 671B 总参数 MoE (37B 激活)，使用 Multi-head Latent Attention (MLA) + DeepSeekMoE。训练成本仅 ~$5.6M。在多项基准上超越 GPT-4o。 | MLA 是 DeepSeek 原创的高效注意力机制（通过低维潜在空间压缩 KV cache）。极低的训练成本改写了"大模型必定高成本"的叙事。 |
| **A.3.8** Phi-3 | 2024 | `Phi-3 Technical Report` (Microsoft) [PI-2.5.13] | 3.8B 参数 decoder-only，使用数据质量驱动方法（"教科书级"合成数据训练）。在手机端实现接近 GPT-3.5 的性能。 | 证明数据质量可以补偿模型规模不足。小模型 + 极高质量数据是可行的路线。 |
| **A.3.9** Gemma | 2024 | `Gemma: Open Models Based on Gemini Research` (Google DeepMind) [PI-2.5.12] | Google 开源轻量级 decoder-only 系列（2B, 7B），基于 Gemini 同源技术。 | Google 对开源生态的回应。技术细节有限（源自闭源 Gemini 体系）。 |

**优劣对比**:
- **Decoder-only 优势**: 架构统一（理解+生成同一目标）；无编码器-解码器的输入输出不对称问题；可无缝用于 Few-Shot / Zero-Shot / 对话 / 代码生成；推理时只需要维护 KV cache（无需编码器输出缓存）。
- **劣势**: 训练效率低于 encoder-only（相同参数量下，自回归训练需串行）；短文本分类等纯 NLU 任务上不一定优于同等规模的 encoder-only；存在 exposure bias（训练时 teacher-forcing vs 推理时自回归的不一致）。
- **现状**: Decoder-only 是当前 LLM 的绝对主流架构（GPT, LLaMA, Qwen, DeepSeek, Mistral, Gemma, Phi 等）。

---

### A.4 混合专家架构 (Mixture of Experts, MoE)

**问题定义**: 如何在增加模型总参数量的同时控制每 token 的推理计算量？

| 节点 | 年份 | 代表论文 | 核心思想 | 演化关系 |
|------|------|----------|----------|----------|
| **A.4.1** Switch Transformer | 2021 | `Switch Transformers: Scaling to Trillion Parameter Models` (Fedus et al., Google Brain) [PI-2.7.2] | 简化 MoE 路由算法：每个 token 只路由到 top-1 专家（而非 top-k）。实现高达 7x 的预训练加速。首次展示 1.6T 参数稀疏模型训练。 | 将 MoE 从理论变为可工程化的大规模方案。top-1 路由牺牲了部分精度但极大简化了负载均衡。 |
| **A.4.2** Mixtral 8x7B | 2024 | `Mixtral of Experts` (Jiang et al., Mistral AI) [PI-2.5.5] | Sparse MoE: 8 个 7B 专家，每 token 激活 top-2 专家（13B 激活 / 47B 总参数）。性能匹配 LLaMA 2 70B，推理成本接近 13B 模型。Apache 2.0 开源。 | 首个真正成功的开源 MoE LLM。证明了 MoE 在性价比上的巨大优势。top-2 路由平衡了多专家协同与计算效率。 |
| **A.4.3** DeepSeekMoE | 2024 | `DeepSeekMoE: Towards Ultimate Expert Specialization` (Dai et al., DeepSeek) [PI-2.7.3] | 细粒度专家分割 + 共享专家隔离策略。将每个 FFN 进一步拆分为更小的专家，并设置一些"共享专家"（常激活）。DeepSeekMoE 16B 仅用 40% 计算量达到 LLaMA2 7B 性能。 | 解决了传统 MoE 的知识冗余问题（多个专家学到相似知识）。细粒度专家 + 共享专家是 MoE 设计的重要创新。 |
| **A.4.4** DeepSeek-V2/V3 | 2024 | DeepSeek-V2 [PI-2.5.10], DeepSeek-V3 [PI-2.5.11] | V2: 236B 总参数 / 21B 激活；V3: 671B 总参数 / 37B 激活。均结合 DeepSeekMoE + Multi-head Latent Attention (MLA)。V3 训练成本 ~$5.6M，超越 GPT-4o。 | DeepSeek 将 MoE + 高效注意力（MLA）做到了极致。V3 的性价比颠覆了行业认知，使"民间复现 GPT-4 级别模型"成为可能。 |

**优劣对比**:
- **MoE 优势**: 总参数量大（知识容量大），激活参数量小（推理成本低）；训练效率高（计算量远小于同性能的 dense 模型）；专家可并行分布训练。
- **劣势**: 路由策略复杂（负载不均衡、专家坍塌）；推理时需要加载全部专家权重（即使只有部分激活），内存占用大；微调/部署的工程复杂度高；batch 推理时可能无法充分利用所有专家。
- **适用场景**: 大规模模型部署（追求知识容量/成本比）；云端推理服务（高吞吐场景）；不适合极致低延迟场景或少专家场景。

---

### A.5 状态空间模型 (State Space Model / Mamba)

**问题定义**: Transformer 的 O(N²) 注意力复杂度在处理超长序列时存在瓶颈。是否存在 O(N) 复杂度的替代架构？

| 节点 | 年份 | 代表论文 | 核心思想 | 演化关系 |
|------|------|----------|----------|----------|
| **A.5.1** Mamba | 2023 | `Mamba: Linear-Time Sequence Modeling with Selective State Spaces` (Gu & Dao, CMU / Princeton) | 提出选择性状态空间模型 (S6)，使 SSM 的参数能够依赖于输入（类似注意力机制的选择性）。训练和推理均为线性复杂度 O(N)。在语言建模等任务上匹配或超越同规模 Transformer。 | 作为 Transformer 替代路线引起广泛关注。线性复杂度对超长序列（>100K tokens）有天然优势。但在短序列和小模型上优势不明显，生态系统远不如 Transformer 成熟。 |
| **A.5.2** Mamba-2 | 2024 | `Transformers are SSMs` (Dao & Gu, Princeton) | 统一了状态空间模型和结构化掩码注意力 (Structured Masked Attention)。证明 SSM 可以看作是半可分离矩阵上的结构化注意力。架构更简洁，支持 FlashAttention 加速。 | 从理论层面架起了 SSM 和 Transformer 的桥梁。暗示两者不是替代关系，而是连续频谱上的不同设计点。 |

**现状与展望**: Mamba/Mamba-2 在超长序列（DNA 建模、长文档）和线性推理场景有优势，但在通用 LLM 领域尚未替代 Transformer 成为主流。Jamba 等混合架构（Mamba + Transformer 层）探索了两者的融合。**暂未纳入本文核心路线图**（边界外，按 query_plan §5.3 边界处理规则）。

---

### A.6 Transformer 关键子组件技术创新

**问题定义**: Transformer 的哪些子组件可被改进以提升性能或效率？

| 组件 | 年份 | 代表工作 | 核心思想 | 演化 / 影响 |
|------|------|----------|----------|------------|
| **位置编码: RoPE** | 2021 | `RoFormer: Enhanced Transformer with Rotary Position Embedding` (Su et al., 追一科技) [PI-2.7.9] | 通过旋转矩阵将位置信息编码到注意力计算中，实现相对位置编码。具有长期衰减性、可外推性。 | 被 LLaMA、Qwen、Mistral、DeepSeek 等几乎所有主流开源模型采用。是当前最成功的位置编码方案。 |
| **注意力: GQA / MQA** | GQA: 2023 (LLaMA 2) | LLaMA 2 [PI-2.5.2] | Multi-Query Attention (MQA): 所有头共享一组 K/V。Grouped-Query Attention (GQA): 分组共享 K/V，平衡效率与质量。大幅减少 KV cache 占用。 | GQA 成为大模型标配（Mistral, Qwen2, LLaMA 3 等均采用）。 |
| **注意力: FlashAttention** | 2022-2024 | FlashAttention (Dao et al., Stanford) [PI-2.7.8] | IO-aware 精确注意力算法。通过 tiling 和 recomputation 将注意力计算从 O(N²) 内存降至 O(N)，训练速度 2-4x。v2/v3 持续优化。 | 已成为 Transformer 训练的基建。几乎所有主流模型训练都使用 FlashAttention。 |
| **注意力: MLA** | 2024 | DeepSeek-V2 [PI-2.5.10] | Multi-head Latent Attention: 将 K/V 矩阵映射到低维潜在空间压缩 KV cache，大幅减少推理时的 KV cache 内存。 | DeepSeek 原创，是目前最高效的注意力机制之一。推理内存成本降至传统 MHA 的 1/5-1/10。 |
| **激活函数: SwiGLU** | 2022 (PaLM) | PaLM (Google) [PI-2.3.4] | 使用 SwiGLU 激活函数替代标准 ReLU/GELU FFN。在同等训练 FLOPs 下提升模型质量。 | 被几乎所有新一代开源模型采用。与 RMSNorm + RoPE 组成开源 LLM 的"标准三件套"。 |
| **归一化: RMSNorm** | 2019 (T5) / 2023 (LLaMA) | T5 [PI-2.2.5]; LLaMA [PI-2.5.1] | RMSNorm 替代 LayerNorm（去掉均值的减法和偏置），训练更稳定、速度更快。Pre-Norm（LLaMA 采用 norm 在 attention/FFN 之前）替代 Post-Norm。 | 当前 decoder-only 模型的标配。Pre-Norm 比 Post-Norm 更有利于大规模训练稳定性。 |

---

## 维度 B: 预训练方法 (Pre-training Methods)

### B.1 预训练目标分类树

```
B. 预训练方法
├─ B.1 自回归语言建模 (AR LM)
│   ├─ B.1.1 GPT 式 next-token prediction (GPT-1/2/3)
│   ├─ B.1.2 前缀语言建模 (Prefix LM) — 部分双向
│   └─ B.1.3 自回归扩展: 代码预训练、多语言预训练
│
├─ B.2 自编码语言建模 (Denoising / AE)
│   ├─ B.2.1 掩码语言建模 (MLM, BERT)
│   │   ├─ 全词掩码 (Whole Word Masking)
│   │   ├─ 动态掩码 (Dynamic Masking, RoBERTa)
│   │   └─ 跨度掩码 (Span Masking, T5)
│   ├─ B.2.2 去噪自编码 (Denoising, BART)
│   └─ B.2.3 文本填充 (Text Infilling, T5)
│
├─ B.3 置换语言建模 (PLM, XLNet)
│
├─ B.4 统一预训练范式
│   └─ B.4.1 UL2: Mixture-of-Denoisers
│
└─ B.5 预训练数据方法论
    ├─ B.5.1 数据规模演进
    ├─ B.5.2 数据质量方法论
    └─ B.5.3 代表性数据集
```

---

### B.1 自回归语言建模 (Autoregressive LM)

**问题定义**: 给定前文 token 序列 $x_{<t}$，预测下一个 token $x_t$ 的概率分布 $P(x_t | x_{<t})$。

| 节点 | 年份 | 代表论文 | 核心思想 | 优劣 |
|------|------|----------|----------|------|
| **B.1.1** GPT 式 Next-Token Prediction | 2018 | GPT-1 [PI-2.2.1] | 标准 causal LM 目标: $L(\theta) = -\sum_i \log P(x_i | x_{<i})$。单向的（只能看到上文）。训练简单、与推理一致（inference 也是逐 token 生成）。 | **优势**: 训练和推理目标一致；天然适合生成任务；可无缝扩展到 Few-Shot / Zero-Shot。**劣势**: 无法利用下文信息，纯理解任务（分类/匹配）不如双向模型。 |
| **B.1.2** 大规模 AR LM | 2019-2020 | GPT-2 [PI-2.2.3], GPT-3 [PI-2.3.2] | 大规模 AR LM 在 zero-shot/few-shot 设定下展现出元学习能力。核心发现："语言建模客观函数本身即包含了多任务学习的信号"。 | **优势**: 规模扩展后涌现上下文学习能力（无需微调）。**劣势**: 预训练 compute 巨大（GPT-3 175B 训练成本数百万美元）。 |
| **B.1.3** 现代 AR LM 实践 | 2023-2024 | LLaMA [PI-2.5.1], LLaMA 3 [PI-2.5.3] | 可混合多种语料（代码、数学、多语言）。LLaMA 3 使用了 >15T tokens 的混合数据（web + code + math + multilingual）。高质量数据过滤和去重至关重要。 | AR LM 是当前 decoder-only LLM 的绝对主流预训练目标。几乎所有开源/闭源 LLM（除 T5/BART 系列外）均采用此范式。 |

---

### B.2 自编码语言建模 (Autoencoding LM / MLM)

**问题定义**: 如何使模型同时利用上文和下文信息（双向上下文）进行文本理解？

| 节点 | 年份 | 代表论文 | 核心思想 | 优劣 |
|------|------|----------|----------|------|
| **B.2.1** Masked Language Modeling (MLM) | 2018 | BERT [PI-2.2.2] | 随机遮蔽 15% 的输入 token，训练模型预测被遮蔽的 token。配合 NSP（下一句预测）辅助任务。利用了双向上下文。 | **优势**: 充分利用左右上下文，NLU 性能强；训练效率高（每个样本预测多个 masked token）。**劣势**: 预训练-微调不一致（微调时没有 [MASK]）；无法用于文本生成。 |
| **B.2.2** NSP 的消亡 | 2019 | RoBERTa [PI-2.2.4] | 通过消融实验证明 NSP 对下游任务没有帮助，甚至可能有害。移除 NSP、使用动态掩码、更大 batch、更多数据是 RoBERTa 超越 BERT 的关键。 | NSP 被证伪，此后几乎无新模型使用。 |
| **B.2.3** Span Masking | 2019 | T5 [PI-2.2.5] | 遮蔽连续的 token span（如一个命名实体或短语），而非独立的随机 token。训练模型生成整个被遮蔽 span 的文本。 | Span masking 更符合自然语言的语义单元遮蔽方式。比 MLM 更适用于 text-to-text 生成任务。 |
| **B.2.4** 去噪自编码 (Denoising) | 2019 | BART [PI-2.2.6] | 对原始文本施加多种破坏操作（token 删除、masking、句子置换、文本填充），训练模型恢复原文。基于 Seq2Seq 架构。 | 比 MLM 更灵活（多种噪声类型），在 NLG 任务上表现突出。但本质上仍是降噪 → 生成的范式。 |

---

### B.3 置换语言建模 (Permutation LM)

| 节点 | 年份 | 代表论文 | 核心思想 | 优劣 |
|------|------|----------|----------|------|
| **B.3.1** XLNet | 2019 | XLNet [PI-2.2.8] | 对所有可能的输入排列进行自回归建模，使每个 token 在所有排列中都能"看到"其他 token（包括"未来"的）。既保留了自回归的因子分解优势，又实现了双向上下文的利用。 | **优势**: 避免 MLM 的预训练-微调不一致；理论优雅。**劣势**: 排列操作计算开销大；输入序列顺序信息部分丢失（需额外的位置编码补偿）；实现复杂；最终性能提升不如 RoBERTa 的"更好训练"来得显著。 |

---

### B.4 统一预训练范式

| 节点 | 年份 | 代表论文 | 核心思想 | 优劣 |
|------|------|----------|----------|------|
| **B.4.1** UL2 | 2022 | `UL2: Unifying Language Learning Paradigms` (Tay et al., Google) | 提出 Mixture-of-Denoisers (MoD) 框架：将 AR、MLM、prefix LM 等不同预训练目标统一为"不同噪声类型 + span 长度"的去噪任务。通过特殊的"mode token"控制行为。 | 统一了预训练范式，但实现复杂。在学术界有理论价值，工业界采用有限（decoder-only + AR LM 的简洁性难以撼动）。 |

---

### B.5 预训练数据方法论

**问题定义**: 预训练数据怎么选、怎么处理，对模型能力有何影响？

| 节点 | 年份 | 代表论文 / 数据集 | 核心思想 |
|------|------|-------------------|----------|
| **B.5.1** C4 (Colossal Clean Crawled Corpus) | 2019 | T5 [PI-2.2.5] | 从 Common Crawl 中过滤、去重、清洗得到的 750GB 英文文本数据集。引入了系统的数据清洗 pipeline（丢弃非英文、低质量、重复文本）。 |
| **B.5.2** The Pile | 2020 | `The Pile: An 800GB Dataset of Diverse Text for Language Modeling` (EleutherAI) | 22 个高质量、多样化的子集组成（学术论文、书籍、代码、论坛等）。强调数据多样性对模型能力的重要性。成为开源 LLM 训练的事实标准基准数据。 |
| **B.5.3** RefinedWeb | 2023 | `The RefinedWeb Dataset for Falcon LLM` (TII) | 大规模、高质量 Web 数据过滤方法。从 CommonCrawl 中使用启发式 + 模型辅助过滤，获得 5T tokens 高质量数据。训练出的 Falcon 模型在同等规模下表现出色。 |
| **B.5.4** LLaMA 数据配方 | 2023 | LLaMA [PI-2.5.1] | 仅使用公开数据（CommonCrawl + C4 + GitHub + Wikipedia + Books + ArXiv + StackExchange）。LLaMA-65B 使用 ~1.4T tokens 训练。证明了公开数据 + 合理混合可以匹敌使用私有大数据的模型。 |
| **B.5.5** 数据质量 > 数据量 | 2024 | Phi-3 [PI-2.5.13] | "教科书级"合成数据：使用 LLM 生成高质量、逐步推理的教科书式文本训练小模型。3.8B 参数小模型的性能接近 GPT-3.5（175B）。挑战了"规模决定一切"的假设。 |
| **B.5.6** FineWeb | 2024 | `FineWeb: Decanting the Web for the Highest Quality Text Data` (Hugging Face) | 开源的大规模高质量 web 数据过滤 pipeline，15T tokens。使用了先进的去重、质量评分和过滤策略。 |

**数据方法论总结**:
```
数据量 (Quantity) 路径: GPT-3 → Chinchilla → LLaMA → LLaMA 3 (>15T tokens)
数据质量 (Quality) 路径: Phi-3 → FineWeb → 合成数据
最优实践: 两者结合 — 大规模 + 高质量过滤 + 多样化的数据混合
```

---

## 维度 C: 规模扩展方法 (Scaling Methods)

### C.1 规模化定律 (Scaling Laws)

**问题定义**: 模型性能（loss）与模型参数量 $N$、训练数据量 $D$、计算量 $C$ 之间存在怎样的函数关系？在固定计算预算下，如何分配模型大小和数据量？

| 节点 | 年份 | 代表论文 | 核心发现 | 启示 / 影响 |
|------|------|----------|----------|------------|
| **C.1.1** Kaplan Scaling Laws | 2020 | `Scaling Laws for Neural Language Models` (Kaplan et al., OpenAI) [PI-2.3.1] | 损失与模型规模、数据集大小、计算量之间呈幂律关系。在固定计算预算下，**模型规模应比数据量增长更快**（$N \propto C^{0.73}, D \propto C^{0.27}$）。架构超参数（深度/宽度）的影响远小于模型规模。 | 直接驱动了 GPT-3 (175B) 的构建，以及"砸更多参数"的风潮。但后来被 Chinchilla 修正。 |
| **C.1.2** Chinchilla 最优计算定律 | 2022 | `Training Compute-Optimal Large Language Models` (Hoffmann et al., DeepMind) [PI-2.3.3] | **核心修正**: Kaplan 定律依赖于固定训练步数的假设，导致低估数据的重要性。Chinchilla 发现：在固定计算预算下，**模型大小和数据量应等比增长**（约1:1）。当前 LLM 普遍训练不足（undertrained）。Chinchilla 70B 使用 4x 数据超越 Gopher 280B。 | "小模型 + 更多数据"优于"大模型 + 更少数据"。直接催生了 LLaMA 系列的策略（在相对较小的模型上使用极大量数据训练）。MMLU 67.5%。 |
| **C.1.3** DeepSeek 的 Scaling Laws | 2024 | `DeepSeek LLM: Scaling Open-Source Language Models` [PI-2.5.9] | DeepSeek 对 batch size 扩展进行了专门实验。发现：在给定模型大小和数据量下，存在最优 batch size；batch size 过大反而有害。提出 batch size 调度策略（训练过程中动态增大 batch size）。 | 补充了 scaling laws 在训练超参数层面的细节。 |

**两大定律的核心差异**:
| 维度 | Kaplan (OpenAI, 2020) | Chinchilla (DeepMind, 2022) |
|------|----------------------|---------------------------|
| 关键结论 | 模型规模更重要 | 数据规模同等重要 |
| 最优分配 | 大模型 + 少量数据 | 数据与模型等比增长 |
| 训练 tokens/参数比 | ~1-2x | ~20x |
| 对 GPT-3 的评价 | 合理 | **严重 undertrained** |
| 对 LLaMA 的影响 | — | LLaMA 采用 Chinchilla-optimal 策略 |

---

### C.2 涌现能力 (Emergent Abilities)

**问题定义**: 为何某些能力（如多步推理、上下文学习）在模型规模达到某个阈值后突然出现？

**关键证据来源**:
- **PaLM** [PI-2.3.4]: 540B 参数下在 BIG-bench 上观察到"不连续的、突然的性能飞跃"。例如，可解释多步推理在 ~100B 以下几乎为 0，在 540B 时跃升至人类水平。
- **GPT-3** [PI-2.3.2]: 175B 参数下 Few-Shot ICL 能力显著优于小规模模型。
- **CoT** [PI-2.6.1]: 思维链提示仅在足够大的模型上有效（约 >100B）。

**方法论争议**（2023-2024）**:
- 涌现是否真实存在，还是评估指标（非线性指标如 EM/Accuracy）的 artifact？(`Schaeffer et al., 2023, "Are Emergent Abilities of Large Language Models a Mirage?"` — 未收入本清单但在社区引起重大讨论)
- 部分研究认为：如果使用连续指标（如 token-level loss），能力提升是平滑的，不存在突变。

---

### C.3 推理时的计算扩展 (Test-time Compute Scaling)

**问题定义**: 如果推理时允许模型"多想一会儿"（更多计算），性能能否继续提升？

| 节点 | 年份 | 代表论文 | 核心思想 |
|------|------|----------|----------|
| **C.3.1** o1 推理模型 | 2024 | `OpenAI o1 System Card` [PI-2.6.6] | 推理时计算扩展：模型在回答前进行长链式思考（chain-of-thought），不限定思考步数。在数学竞赛（AIME）和科学推理上取得突破。性能随推理时计算的增加而持续提升。 |
| **C.3.2** DeepSeek-R1 | 2025 | `DeepSeek-R1: Incentivizing Reasoning via RL` [PI-2.6.5] | 通过纯 RL（无 SFT 冷启动）训练出推理能力。模型自发学会分配更多"思考 token"、自我验证和回溯。性能匹配 o1。 |
| **C.3.3** Scaling for Inference | 2025 | o1/o3 相关报告 | 推理时的 compute scaling 成为一种新的 scaling 范式：pre-training scaling → post-training scaling → **inference-time scaling**。 |

**核心范式转变**:
- 传统: 预训练时投入更多 compute → 更好的模型 → 推理时单次前向传播
- 新范式: 预训练 compute + 推理时 compute → 双维度扩展 → 推理时可用可变计算量换取更高质量

---

## 维度 D: 对齐方法 (Alignment Methods)

### D.1 问题定义

**核心问题**: 预训练模型（next-token prediction）的行为目标（最大化似然）与人类期望（有用、诚实、无害）之间存在根本性的"对齐鸿沟"（alignment gap）。如何弥补？

**对齐三目标** (HHH):
- **Helpful** (有用): 遵循指令，提供准确、相关的信息
- **Honest** (诚实): 不编造信息，承认不确定性
- **Harmless** (无害): 不生成有害、歧视、暴力内容

---

### D.2 基于人类反馈的强化学习 (RLHF)

| 节点 | 年份 | 代表论文 | 核心思想 | 演化关系 |
|------|------|----------|----------|----------|
| **D.2.1** RLHF 奠基 | 2017 | `Deep RL from Human Preferences` (Christiano et al., OpenAI / DeepMind) [PI-2.4.1] | 通过人类对轨迹对的偏好反馈训练奖励模型，再用 PPO 强化学习优化策略。在 Atari 和机器人控制中验证。 | RLHF 的理论基础。将偏好学习从 Atari 迁移到语言模型是后人的贡献。 |
| **D.2.2** InstructGPT | 2022 | `Training language models to follow instructions with human feedback` (Ouyang et al., OpenAI) [PI-2.4.2] | 首次将 RLHF 大规模应用于语言模型对齐。三阶段流程：(1) 监督微调（SFT）— 人工标注的 prompt-response 对；(2) 奖励模型（RM）训练 — 人工对多个响应排序；(3) PPO 优化 — 用 RM 作为奖励函数，PPO 优化策略。1.3B InstructGPT 输出被偏好 > 175B GPT-3。 | 奠定了 RLHF 的标准流程。对 ChatGPT 和 GPT-4 有直接贡献。但其对数据和人工标注的依赖很高，且 PPO 训练不稳定。 |
| **D.2.3** Constitutional AI / RLAIF | 2022 | `Constitutional AI: Harmlessness from AI Feedback` (Bai et al., Anthropic) [PI-2.4.5] | 不依赖人类标注有害输出，而是用 AI 自我监督。核心思想：(1) 使用"宪法"（一组原则）让模型批判自己的输出；(2) 用 AI 反馈替代人类反馈（RLAIF: RL from AI Feedback）。 | 减少了对有害内容人工标注的需求（降低了标注者的心理伤害风险）。Claude 系列模型的对齐基础。但宪法设计本身依赖人类先验。 |

**RLHF 核心流程**:
```
Step 1: SFT — 收集 prompt 和高质量人工响应 → 微调基础模型
Step 2: RM — 收集 prompt 和多个模型响应 → 人工排序 → 训练奖励模型
Step 3: PPO — 用 RM 作为奖励信号 → PPO 优化策略 → 加上 KL 正则化（防止偏离 SFT 太远）
```

---

### D.3 直接偏好优化 (Direct Preference Optimization, DPO)

**问题定义**: RLHF 需要训练独立的奖励模型 + PPO 强化学习，流程复杂、训练不稳定。能否更简洁地实现偏好对齐？

| 节点 | 年份 | 代表论文 | 核心思想 | 演化关系 |
|------|------|----------|----------|----------|
| **D.3.1** DPO | 2023 | `Direct Preference Optimization` (Rafailov et al., Stanford) [PI-2.4.4] | 数学上证明 RLHF 的优化目标可以重参数化为一个简单的二分类损失函数。无需显式训练奖励模型，无需强化学习。将偏好学习转化为：最大化偏好响应相对于非偏好响应的对数概率比。 | ⭐ 方法创新里程碑。更简单、更稳定，效果匹配 PPO-RLHF。大幅降低了对齐的门槛。但 DPO 的效果对偏好数据质量敏感。 |
| **D.3.2** DPO 变体 | 2024 | ORPO, KTO, SimPO, RSO | ORPO: 将偏好对齐和 SFT 融合为一个损失函数；KTO: 不需要成对偏好数据，仅需二元反馈；SimPO: 使用序列平均对数概率作为隐式奖励；RSO: 从统计角度重新推导偏好优化。 | DPO 方法族的快速繁荣期。不同变体针对数据收集成本、偏好信号质量、训练稳定性等不同问题进行改良。 |

**RLHF vs DPO 对比**:
| 维度 | RLHF (PPO-based) | DPO |
|------|-----------------|-----|
| 需要 RM? | 是（需单独训练） | 否（隐式） |
| 训练算法 | PPO 强化学习 | 简单分类损失 |
| 训练稳定性 | 不稳定（需要 KL 正则化等技巧） | 稳定 |
| 是否需要在线采样 | PPO 需要 | DPO 使用静态数据集 |
| 计算成本 | 高（4 个模型：policy + ref + RM + value） | 低（2 个模型：policy + ref） |
| 灵活性 | 可用于迭代式在线学习 | 离线方法，可能有分布偏移 |
| 适用场景 | 大规模在线对齐（如 ChatGPT） | 学术研究和资源受限场景 |

---

### D.4 指令微调 (Instruction Tuning)

**问题定义**: 如何让预训练模型学会"遵循指令"而不是"补全文本"？如何以最低成本获得指令遵循能力？

| 节点 | 年份 | 代表论文 | 核心思想 |
|------|------|----------|----------|
| **D.4.1** FLAN | 2021 | `Fine-tuned Language Models Are Zero-Shot Learners` (Wei et al., Google) [PI-2.4.6] | 在多种 NLP 任务上以指令格式微调模型，使模型在**未见过的**任务上获得零样本泛化能力。使用 62 个任务的数据集，137B 模型。指令微调后的模型在未见任务上超越 GPT-3 Few-Shot。 |
| **D.4.2** Self-Instruct | 2022 | `Self-Instruct: Aligning Language Models with Self-Generated Instructions` (Wang et al., UW / Allen AI) [PI-2.4.7] | 利用 LLM 自身生成指令数据：给定少量种子任务 → LLM 生成新任务指令 → LLM 生成输入输出对 → 过滤低质量数据 → 微调模型。大幅降低人工标注成本。 |
| **D.4.3** Alpaca | 2023 | `Alpaca: A Strong, Replicable Instruction-Following Model` (Stanford) | 使用 GPT-3.5 (text-davinci-003) 生成 52K 指令数据，微调 LLaMA 7B。仅 $600 训练成本获得接近 text-davinci-003 的性能。激发社区广泛复现和创新。 |
| **D.4.4** Vicuna | 2023 | `Vicuna: An Open-Source Chatbot` (LMSYS) | 从 ShareGPT 收集真实用户对话数据，微调 LLaMA 13B。训练成本 $300。社区评估认为其达到了 ChatGPT 90% 的质量。 |

---

### D.5 对齐方法演化总结

```
2017: Christiano et al. — 提出 RLHF 概念 (Atari/机器人)
  ↓
2021: FLAN — 指令微调使模型获得零样本泛化
  ↓
2022: InstructGPT — RLHF 首次大规模应用于语言模型
  ├─ 2022: Constitutional AI / RLAIF — 用 AI 替代人类标注
  ↓
2023: DPO — 去强化学习化，简化对齐流程
  ├─ 2023-2024: ORPO / KTO / SimPO — DPO 变体繁荣
  ↓
2024: GPT-4 — 大规模后训练对齐 + 多模态
2025: DeepSeek-R1 — RL 驱动推理能力，开辟对齐新维度（推理对齐）
```

---

## 维度 E: 推理增强方法 (Reasoning Enhancement)

### E.1 问题定义

**核心问题**: LLM 在需要多步逻辑推理的任务（数学、代码、规划）上表现不佳。如何让模型"慢下来思考"而不是"快速猜测"？

---

### E.2 思维链 (Chain-of-Thought, CoT)

| 节点 | 年份 | 代表论文 | 核心思想 | 演化关系 |
|------|------|----------|----------|----------|
| **E.2.1** Few-Shot CoT | 2022 | `Chain-of-Thought Prompting Elicits Reasoning` (Wei et al., Google) [PI-2.6.1] | 在 prompt 中提供少量包含推理步骤的示例（"让我们一步步思考"），诱导模型生成中间推理链。在 540B PaLM 上，GSM8K 数学推理从 ~18%（标准提示）提升到 ~57%。 | ⭐ 开创性发现：LLM 具备"潜在"推理能力，通过合适的提示可以"解锁"。但需要人工编写 CoT 示例。 |
| **E.2.2** Zero-Shot CoT | 2022 | `Large Language Models are Zero-Shot Reasoners` (Kojima et al.) | 仅需在 prompt 末尾添加 "Let's think step by step"（让我们一步步思考），无需 Few-Shot 示例，即可触发 CoT 推理。 | 更简洁。证明 CoT 能力是模型内在的，不需要示例中的推理模式。 |
| **E.2.3** 自一致性 (Self-Consistency) | 2022 | `Self-Consistency Improves Chain of Thought Reasoning` (Wang et al., Google) [PI-2.6.2] | 对同一问题采样多条推理路径（通过调整 temperature），对最终答案进行多数投票（majority voting）。显著提升 CoT 的鲁棒性和准确性。 | "采样+投票"范式简单但有效。本质是利用推理路径的多样性，边际收益递减（通常 5-10 条采样即可）。 |
| **E.2.4** STaR (Self-Taught Reasoner) | 2022 | `STaR: Bootstrapping Reasoning With Reasoning` (Zelikman et al., Stanford) [PI-2.6.7] | 利用模型自身生成的推理链来训练模型提升推理能力。流程：(1) 模型对问题生成推理链；(2) 筛选出导致正确答案的推理链；(3) 用这些"成功"推理链微调模型；(4) 迭代。 | 推理能力"自举"的先驱。启发了后续的 Self-Improving 方法（如 ReST, RL from Execution Feedback）。 |

---

### E.3 搜索引导推理 (Search-based Reasoning)

**问题定义**: CoT 是"线性"的一路走到黑，缺乏回溯和探索多种可能性的能力。如何让模型像人类一样"深思熟虑"？

| 节点 | 年份 | 代表论文 | 核心思想 | 演化关系 |
|------|------|----------|----------|----------|
| **E.3.1** Tree-of-Thought (ToT) | 2023 | `Tree of Thoughts: Deliberate Problem Solving` (Yao et al., Princeton / Google DeepMind) [PI-2.6.3] | 将推理过程建模为树状搜索。在每一步生成多个可能的"思维"（thought），使用 BFS/DFS 搜索最优路径。支持回溯和全局探索。在 Game of 24 问题上，ToT 成功率达 74%（CoT 仅 4%）。 | 推理策略的重大创新。但计算开销大（每步需要多次 LLM 调用）。实用性受限于需要明确定义"思维"粒度和评估函数的任务。 |
| **E.3.2** Graph-of-Thought | 2023-2024 | `Graph of Thoughts: Solving Elaborate Problems with Large Language Models` (Besta et al.) | 将推理建模为有向无环图（DAG），允许多个思维节点合并、分支和循环。比 ToT 的树结构更灵活。 | 继续泛化推理结构。但实现复杂度上升，收益递减。 |
| **E.3.3** ReAct | 2022 | `ReAct: Synergizing Reasoning and Acting` (Yao et al., Princeton / Google) [PI-2.6.4] | 将推理（reasoning）和行动（action）交织：模型生成 thought → 执行 action（如搜索、计算）→ 观察结果 → 生成下一步 thought。在知识密集型 QA 和决策任务上显著提升。 | 将推理与外部工具/环境交互结合。启发了 Agent 框架（如 LangChain, AutoGPT）。 |
| **E.3.4** 反思与自纠 (Reflexion) | 2023 | `Reflexion: Language Agents with Verbal Reinforcement Learning` (Shinn et al.) | 模型执行任务后，对失败进行口头反思（verbal reflection），将反思存入记忆，下次尝试时参考。实现类似"从错误中学习"的能力。 | 引入了"长期记忆 + 自我批评"的 Agent 推理模式。在编程和决策任务上提升显著。 |

---

### E.4 推理时计算扩展 (Test-time Scaling)

**问题定义**: 在推理阶段投入更多计算资源（更多 token、更长的思考链），能否获得"免费的性能提升"？

| 节点 | 年份 | 代表论文 | 核心思想 |
|------|------|----------|----------|
| **E.4.1** OpenAI o1 | 2024 | `OpenAI o1 System Card` [PI-2.6.6] | 模型在回答前进行内部"思考"（隐式 CoT 生成），输出的思考过程被隐藏。推理时的计算量可动态扩展（longer thinking → better answers）。在 AIME 数学竞赛和科学推理上取得突破性提升。 |
| **E.4.2** DeepSeek-R1 | 2025 | `DeepSeek-R1: Incentivizing Reasoning via RL` [PI-2.6.5] | 纯 RL 训练（无 SFT 冷启动）产生推理模型。R1-Zero 版本在没有人工推理数据的情况下，自发学会了反思、验证、回溯等行为。开源、公开推理链（透明）。 |
| **E.4.3** 推理范式对比 | | | o1 将推理过程"黑箱化"（隐藏 CoT），DeepSeek-R1 将推理过程"透明化"（公开 CoT）。两者都证明推理时计算扩展是有效的 scaling 新维度。 |

---

### E.5 推理方法对比总结

| 方法 | 推理结构 | 是否需要训练 | 推理开销 | 代表场景 |
|------|----------|-------------|---------|----------|
| Zero-Shot CoT | 线性链 | 否（仅 prompt） | 1x | 数学题、常识推理 |
| Few-Shot CoT | 线性链 | 否 | 1x | 需要示例引导的复杂推理 |
| Self-Consistency | 多条线性链 + 投票 | 否 | N x (N条采样) | 提高推理鲁棒性 |
| ToT | 树状搜索 | 否 | 指数级 | 有明确评估函数的规划问题 |
| ReAct | 推理-行动交织 | 否 | 取决于工具调用次数 | 知识密集 QA、决策 |
| STaR | 线性链 | 是（微调） | 1x | 通过训练提升推理基准 |
| o1 / R1 | 内部长链思考 | 是（RL / 特殊训练） | 可变 | 数学竞赛、代码竞赛、科学推理 |

---

## 维度 F: 效率优化方法 (Efficiency Optimization)

### F.1 问题定义

**核心矛盾**: LLM 的模型规模和数据规模持续增长，但硬件资源（GPU 显存、带宽、算力）增长缓慢。如何用有限资源训练和部署越来越大的模型？

---

### F.2 参数高效微调 (Parameter-Efficient Fine-Tuning, PEFT)

| 节点 | 年份 | 代表论文 | 核心思想 | 优劣 |
|------|------|----------|----------|------|
| **F.2.1** LoRA | 2021 | `LoRA: Low-Rank Adaptation of Large Language Models` (Hu et al., Microsoft) [PI-2.7.4] | 基于一个"低秩假设"：模型适应下游任务时的权重更新矩阵 $\Delta W$ 具有低秩性质。将 $\Delta W$ 分解为两个小矩阵 $A$ 和 $B$ 的乘积（$A \in \mathbb{R}^{d \times r}, B \in \mathbb{R}^{r \times d}, r \ll d$）。仅训练 $A$ 和 $B$。 | **优势**: 降低可训练参数 10000x；不增加推理延迟（可与原权重合并）；可多任务切换（切换 LoRA 权重即可）。**劣势**: r 较小限制了拟合能力；需要针对不同任务调整 rank。 |
| **F.2.2** QLoRA | 2023 | `QLoRA: Efficient Finetuning of Quantized Language Models` (Dettmers et al., UW) [PI-2.7.5] | 将 LoRA 与 4-bit 量化结合。使用 4-bit NormalFloat 数据类型 + 双重量化 + 分页优化器。在单个 48GB GPU 上即可微调 65B 模型。 | **优势**: 极致降低微调门槛（消费级 GPU 微调大模型）。**劣势**: 训练速度比全精度慢（量化/反量化开销）。与 GPTQ/AWQ 配合可进一步降低推理成本。 |

---

### F.3 模型量化 (Quantization)

**问题定义**: 如何用更低精度（8-bit, 4-bit, 甚至 2-bit）存储和计算模型权重，尽量减少精度损失？

| 节点 | 年份 | 代表论文 | 核心思想 | 优劣 |
|------|------|----------|----------|------|
| **F.3.1** GPTQ | 2022 | `GPTQ: Accurate Post-Training Quantization` (Frantar et al., IST Austria / ETH) [PI-2.7.6] | 基于近似二阶信息（Hessian）的后训练量化方法。逐层量化权重，利用 Optimal Brain Quantization (OBQ) 算法补偿量化误差。GPT 模型可压缩至 3-4 bit，性能损失极小。ICLR 2023。 | **优势**: 无需重训练，校准数据量小（128 个样本），GPU 推理加速。**劣势**: 校准过程较慢（特别是大模型）；对激活值量化支持有限。 |
| **F.3.2** AWQ | 2023 | `AWQ: Activation-aware Weight Quantization` (Lin et al., MIT) [PI-2.7.7] | 基于一个发现：不是所有权重都同等重要——与较大激活值相乘的"显著权重"更关键。AWQ 通过逐通道缩放保护这些显著权重，再进行 INT3/INT4 量化。 | **优势**: 比 GPTQ 更快、更简单；硬件友好。**劣势**: 在极低比特（<3 bit）下仍有明显退化。 |
| **F.3.3** GGUF / GGML | 2023 | `llama.cpp` (Georgi Gerganov et al.) | 为 CPU 推理设计的量化格式。支持多种量化级别（Q4_0, Q4_K_M, Q5_K_M 等），在消费级设备（MacBook, 手机）上运行 LLM。 | **优势**: CPU 推理的极致优化；无需 GPU。**劣势**: 推理速度（tokens/s）远低于 GPU；不支持训练。 |
| **F.3.4** bitsandbytes | 2022 | `bitsandbytes` (Dettmers) | 8-bit 优化器和 4-bit 量化加载。可在现有深度学习框架中无缝使用。 | 训练/推理的过渡方案，降低显存占用。广泛用于 Hugging Face transformers 的量化加载。 |

**量化方法对比**:
| 方法 | 精度 | 是否需要校准 | 推理加速 | 主要用途 |
|------|------|------------|---------|----------|
| GPTQ | 2-8 bit | 是（128样本） | GPU | 模型部署 |
| AWQ | 3-4 bit | 是（少量） | GPU | 模型部署 |
| GGUF | 2-8 bit | 否 | CPU（Mac/Intel） | 本地/边缘部署 |
| bitsandbytes | 4/8 bit | 否 | GPU（有限加速） | 训练加载、低显存推理 |

---

### F.4 高效注意力机制

| 节点 | 年份 | 代表论文 / 模型 | 核心思想 | 影响 |
|------|------|----------------|----------|------|
| **F.4.1** FlashAttention v1/v2/v3 | 2022-2024 | FlashAttention (Dao et al., Stanford) [PI-2.7.8] | 通过 IO-aware 算法设计（tiling + recomputation），将标准注意力计算从 O(N²) 显存降至 O(N)，训练速度 2-4x。v2: 更好的并行策略；v3: 针对 H100 GPU 优化。 | 几乎成为所有 LLM 训练的必备组件。 |
| **F.4.2** Multi-Query Attention (MQA) | 2019 | `Fast Transformer Decoding` (Shazeer) | 所有注意力头共享同一组 Key/Value 矩阵（仅 Query 独立），大幅减少 KV cache 大小。 | PaLM 等使用 MQA。但可能略微损失精度。 |
| **F.4.3** Grouped-Query Attention (GQA) | 2023 | LLaMA 2 [PI-2.5.2] | MQA 和 MHA 的折中方案：将注意力头分组，组内共享 K/V。平衡了 KV cache 大小和注意力质量。 | LLaMA 2/3、Mistral、Qwen2、DeepSeek-V2 均采用 GQA。已成为事实标准。 |
| **F.4.4** Multi-head Latent Attention (MLA) | 2024 | DeepSeek-V2 [PI-2.5.10] | 将 K 和 V 矩阵压缩到低维潜在空间（latent space），在推理时从潜在空间恢复 K/V。KV cache 仅是潜在向量的缓存，远小于标准 GQA。 | DeepSeek 的核心创新之一。推理内存成本降至传统方法的 1/5-1/10。 |

---

### F.5 其他效率技术

| 技术 | 年份 | 核心思想 | 代表工作 | 效益 |
|------|------|----------|----------|------|
| **投机解码** (Speculative Decoding) | 2023 | 使用小模型（draft model）快速生成候选 token，大模型并行验证，加速自回归解码 2-3x | Leviathan et al. (2023), Medusa | 推理延迟降低；不影响输出质量 |
| **知识蒸馏** (Knowledge Distillation) | 2015 → LLM 时代 | 大模型（teacher）的知识通过软标签迁移到小模型（student） | DistilBERT (2019), Orca (2023) | 模型缩小 40%，保留 95%+ 性能 |
| **KV-cache 压缩** | 2023-2024 | 只保留重要 token 的 KV 条目（如通过注意力分数选择），或使用量化 KV cache | H2O, StreamingLLM, KIVI | 降低长序列推理的显存占用 |
| **滑动窗口注意力** (SWA) | 2023 | 每个 token 只关注前 W 个 token（而非完整上下文），推理内存线性增长 | Mistral 7B [PI-2.5.4] | 长序列推理内存可控 |

---

## 维度 G: 外部知识获取方法 (External Knowledge)

### G.1 问题定义

**核心问题**: LLM 的参数记忆（parametric knowledge）存在局限——知识有截止日期、事实可能错误、无法覆盖所有特定领域知识。如何让模型在推理时访问外部、新鲜的、可验证的知识？

---

### G.2 检索增强生成 (Retrieval-Augmented Generation, RAG)

| 节点 | 年份 | 代表论文 | 核心思想 | 演化关系 |
|------|------|----------|----------|----------|
| **G.2.1** 基础 RAG | 2020 | `Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks` (Lewis et al., Facebook AI) [PI-2.7.1] | 将预训练语言模型与外部知识检索结合。输入 query → 检索器（Dense Passage Retrieval, DPR）从知识库检索相关文档 → 生成器（BART/T5）基于检索到的文档生成回答。端到端可微。NeurIPS 2020。 | ⭐ RAG 范式的奠基性工作。将语言模型的"参数记忆"与"非参数检索记忆"融合。但检索器和生成器是单独训练的，非联合优化。 |
| **G.2.2** 现代 RAG 系统 | 2023-2024 | LangChain, LlamaIndex, DSPy | 模块化 RAG pipeline: 文档分块 (chunking) → 向量embedding → 向量数据库检索 → 重排序 (reranking) → top-k 上下文 + 用户 query → LLM 生成。支持多轮对话、多模态文档、混合检索（向量 + BM25）。 | 从学术概念变为工程最佳实践。但 RAG pipeline 的超参数（chunk size, top-k, embedding model）需大量手工调优。 |
| **G.2.3** Self-RAG | 2023 | `Self-RAG: Learning to Retrieve, Generate, and Critique` (Asai et al., UW) | 让 LLM 自主决定何时检索、如何评估检索结果质量。通过特殊的反思 token（`<RETRIEVE>`, `<RELEVANT>`, `<SUPPORTED>`）训练模型学会自我反思和适应性检索。 | 解决了"何时应该检索"的问题（不是所有问题都需要检索）。减少不必要的检索开支，提升事实性。 |
| **G.2.4** CRAG (Corrective RAG) | 2024 | `Corrective Retrieval Augmented Generation` (Yan et al.) | 对检索到的文档进行质量评估：如果文档不相关/质量低，自动触发知识精炼（如 web search）获取更好的文档。 | 增强了 RAG 对检索噪声的鲁棒性。 |
| **G.2.5** GraphRAG | 2024 | `GraphRAG: Unlocking LLM Discovery on Narrative Private Data` (Microsoft) | 从私有文本数据中自动构建知识图谱（实体 + 关系），用社区检测算法（Leiden）发现主题聚类，在回答问题前生成全局性的社区摘要。 | RAG 从"逐段检索"扩展到"全局语义理解"。适合需要在全局层面理解文本集（而非检索单段）的场景。计算开销大。 |

---

### G.3 工具使用 (Tool Use)

**问题定义**: LLM 不具备精确计算、代码执行、实时信息获取等能力。如何让 LLM 学会"何时以及如何使用外部工具"？

| 节点 | 年份 | 代表论文 | 核心思想 |
|------|------|----------|----------|
| **G.3.1** Toolformer | 2023 | `Toolformer: Language Models Can Teach Themselves to Use Tools` (Schick et al., Meta) | 通过自监督方式让 LLM 学会调用 API。模型在训练数据中插入 API 调用标记，用 API 返回结果替代原始提示。无需人工标注工具使用数据。 |
| **G.3.2** Gorilla | 2023 | `Gorilla: Large Language Model Connected with Massive APIs` (Patil et al., UC Berkeley) | 专门针对 API 调用场景微调的 LLM。能根据自然语言指令选择正确的 API，并生成正确的调用代码。应对 API 文档变化时的鲁棒性强。 |
| **G.3.3** PAL / ToRA | 2023 | `PAL: Program-Aided Language Models`, `ToRA: Tool-integrated Reasoning` | PAL: LLM 生成 Python 代码来解题，代码由解释器执行。ToRA: 将工具使用（代码执行）与推理链交织，在数学推理上提升显著。 |
| **G.3.4** Function Calling | 2023 | GPT-4, Claude, Gemini API | LLM 提供商在 API 层面支持"函数调用"：模型输出结构化的函数名 + 参数 JSON，由外部系统执行后返回结果。 | 已成为 LLM API 事实标准。使 LLM 无缝集成到软件系统中。 |

---

### G.4 长上下文扩展

**问题定义**: Transformer 推理复杂度 O(N²) 和位置编码的外推能力限制了上下文窗口。如何以合理成本扩展上下文长度？

| 技术 | 年份 | 核心思想 | 代表实现 |
|------|------|----------|----------|
| **位置插值 (Position Interpolation)** | 2023 | 将训练时的位置索引按比例缩放到更长范围，通过少量微调使模型适应扩展后的上下文 | `Extending Context Window of LLMs via Positional Interpolation` (Chen et al.) |
| **RoPE 扩展** | 2023 | 调整 RoPE 的旋转频率（base frequency），使模型能外推到更长位置 | NTK-aware scaling, YaRN (Peng et al., 2023) |
| **StreamingLLM** | 2023 | 发现注意力中的"注意力沉降"(attention sink) 现象——前几个 token 获得了不成比例的高注意力。保留初始 token + 滑动窗口可实现无限长度推理 | `Efficient Streaming Language Models with Attention Sinks` (Xiao et al.) |
| **Ring Attention** | 2023 | 在多个设备间分配长序列的注意力计算，通过环形通信实现 O(N²/P) 复杂度 | `Ring Attention with Blockwise Transformers` (Liu et al.) |

**上下文扩展进度表** (代表性模型):
| 年份 | 模型 | 上下文长度 |
|------|------|-----------|
| 2018 | GPT-1 | 512 |
| 2019 | GPT-2 | 1024 |
| 2020 | GPT-3 | 2048 |
| 2023 | GPT-4 (初版) | 8K |
| 2023 | Claude 2 | 100K |
| 2024 | GPT-4 Turbo | 128K |
| 2024 | Gemini 1.5 Pro | 1M (实验性) |
| 2024 | LLaMA 3.1, Qwen 2.5 | 128K |

---

## 附: 方法维度的交叉与协同

### 交叉矩阵：各维度方法如何协同工作

```
              A.架构   B.预训练  C.Scaling  D.对齐   E.推理   F.效率   G.知识
A.架构          —       强耦合    中度耦合   弱耦合   中度     强耦合   弱耦合
B.预训练      强耦合      —       强耦合    中度     弱       中度     弱耦合
C.Scaling     中度      强耦合      —       弱       弱       强耦合   弱
D.对齐        弱        中度      弱        —       强耦合   中度     弱
E.推理增强    中度      弱        弱        强耦合    —       弱       强耦合
F.效率优化    强耦合    中度      强耦合    中度     弱       —       弱耦合
G.外部知识    弱        弱        弱        弱       强耦合   弱       —
```

**典型协同案例**:
1. **DeepSeek-V3**: A(MoE + MLA) + B(AR LM + 多语言) + C(scaling to 671B) + F(超高效训练, $5.6M) → 性能超越 GPT-4o
2. **GPT-4**: A(Decoder-only) + B(AR LM) + C(极大 compute) + D(RLHF + 安全对齐) + E(CoT 训练) + G(工具使用) → 全面能力
3. **LLaMA 3 405B**: A(Decoder-only + GQA + RoPE) + B(15T tokens) + C(Chinchilla-optimal) + D(RLHF/DPO) + F(全量优化) + G(128K 长上下文) → 开源标杆

---

## 方法演化时间线 (2017–2026)

```
2017 ──  [Transformer] ────────────────────────────────────── A.1 架构起点
         [RLHF概念] ───────────────────────────────────────── D.2 对齐源头

2018 ──  [GPT-1 AR LM] [BERT MLM] ──────────────────────── B.1 + B.2 两大预训练范式确立

2019 ──  [GPT-2 Zero-Shot] [T5] [BART] [RoBERTa] [XLNet] ─ B.3/B.4; 范式繁荣
         [ALBERT 参数共享] ───────────────────────────────── A.2 编码器优化

2020 ──  [GPT-3 175B] [Scaling Laws] ──────────────────── C.1 Scaling 时代开启
         [RAG] ───────────────────────────────────────────── G.2 检索增强

2021 ──  [Switch Transformer MoE] [LoRA] ────────────────── A.4 + F.2 效率架构与微调
         [FLAN] ─────────────────────────────────────────── D.4 指令微调
         [RoPE] ──────────────────────────────────────────── A.6 位置编码革新

2022 ──  [InstructGPT/RLHF] [Constitutional AI] ────────── D.2/D.3 对齐工程化
         [Chinchilla] [PaLM] ────────────────────────────── C.1/C.2 修正 Scaling
         [CoT] [Self-Consistency] [ReAct] ──────────────── E.2/E.3 推理增强
         [GPTQ] [FlashAttention] ────────────────────────── F.3/F.4 效率基建

2023 ──  [GPT-4] [LLaMA] [Mistral] ──────────────────────── A.3 + D 开源+闭源架构
         [DPO] ──────────────────────────────────────────── D.3 对齐简化
         [ToT] [QLoRA] [AWQ] ────────────────────────────── E.3 + F 效率+推理
         [GQA (LLaMA 2)] [Self-RAG] ──────────────────────── A.6 + G.2

2024 ──  [LLaMA 3] [Mixtral] [Qwen2.5] [DeepSeek-V3] ──── A.3/A.4 开源爆发
         [o1 System Card] [Gemini] ──────────────────────── C.3 + E.4 推理时扩展
         [ORPO/KTO] [GraphRAG] ──────────────────────────── D.3 + G.2 细化
         [Phi-3 数据质量] [MLA] ──────────────────────────── B.5 + A.6

2025 ──  [DeepSeek-R1 RL推理] ──────────────────────────── E.4 纯RL推理
         [开源追赶闭源] 多模态深化 ──────────────────────── 全面融合

2026 ──  前沿: 推理时 Scaling, 超长上下文 Agent, 多模态基础模型 ...
```

---

## 方法论总体判断

### 已解决的问题
1. **预训练 + 微调范式**: BERT/GPT 确立的预训练范式已成熟，decoder-only + AR LM 成为主流
2. **Scaling 策略**: Chinchilla 最优计算定律给出了数据-模型配比的理论指导
3. **推理增强基础**: CoT / Self-Consistency / ReAct 等 prompt-level 推理方法已成熟
4. **模型量化**: GPTQ/AWQ/GGUF 使 4-bit 量化部署成为可行方案
5. **参数高效微调**: LoRA/QLoRA 大幅降低了微调门槛
6. **长上下文**: 从 2K 扩展到 128K+ 在工程上已解决

### 仍在演进的问题
1. **对齐的可扩展性与安全性**: RLHF/DPO 的对齐效果仍不够鲁棒，越狱攻击持续存在
2. **推理的可解释性**: o1/R1 的内部推理过程仍难完全信任
3. **幻觉抑制**: RAG 减少了幻觉但未根除，长文本生成中的事实一致性仍是挑战
4. **MoE 训练稳定性**: 负载均衡、专家坍缩仍是工程难题
5. **多模态深度融合**: 原生多模态架构（而非视觉编码器+LLM 拼接）仍在探索
6. **规模扩展的天花板**: 高质量文本数据正接近耗尽，合成数据的质量和多样性是瓶颈

### 未来方向预测
1. **推理时计算成为新的 scaling 维度**（pre-training → post-training → inference-time）
2. **Agent 框架的标准化**: LLM 从"语言接口"进化为"操作系统的自然语言 shell"
3. **超长上下文 + 结构化记忆**: 突破 1M token 到无限上下文的实用化
4. **数据质量 > 数据量**: 合成数据和课程学习将取代原始 web 数据
5. **开源生态与闭源模型的持续博弈**: DeepSeek 证明"开源可以匹敌闭源"的路径

---

## 来源说明

- **主要数据源**: `research/paper_inventory.md` 中的 65+ 篇论文，覆盖 2017-2026
- **标记规则**: `[PI-X.X.X]` 为 paper_inventory 编号
- **补充来源**: 本 agent 的领域知识（标注为补充，不编造来源）
- **未收入本清单但被提及的方法**: Mamba、Graph-of-Thought、Reflexion、ORPO/KTO/SimPO、Speculative Decoding 等 — 部分属于 query_plan 边界外，但作为对比纳入以完善分类体系
- **可靠性**: 所有标注 [PI-] 的方法均可追溯到 paper_inventory 中的具体论文；未标注的方法为领域常识或辅助对比信息
