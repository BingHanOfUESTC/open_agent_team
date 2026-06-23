# LLM 强化学习后训练 - 论文清单

## 检索概况

| 项目 | 详情 |
|------|------|
| 检索日期 | 2026-06-23 |
| 检索源 | HuggingFace Papers API (arXiv 索引) |
| 总检索论文数 | 280 |
| 去重后数量 | 280 |
| 搜索批次 | 20 次 API 搜索，覆盖 11 个查询维度 |
| 覆盖子方向 | Q1(SFT), Q2(RM), Q3(PPO-RLHF), Q4(DPO), Q5(GRPO), Q6(AgentRL), Q7(Eval) |

> **注意**: arXiv API 在批量请求时返回 429/503 错误，故改用 HuggingFace Papers API 作为替代数据源。

### Q1: SFT 基础
> 监督微调在 LLM 后训练中的角色、数据构建策略、与 RL 的关系

**论文数**: 23 篇

| # | 论文标题 | 第一作者 | 年份 | arXiv ID | 核心贡献摘要 | 标签 |
|---|----------|----------|------|----------|-------------|------|
| 1 | Post-Training is About States, Not Tokens: A State Distribution View of SFT, RL, and On-Policy Distillation | Dong Nie | 2026 | [2605.22731](https://arxiv.org/abs/2605.22731) | Large language model post-training methods such as supervised fine-tuning (SFT), reinforcement learning (RL), and distillation are often analyzed thro | SFT |
| 2 | Why Does Reinforcement Learning Generalize? A Feature-Level Mechanistic Study of Post-Training in Large Language Models | Dan Shi | 2026 | [2604.25011](https://arxiv.org/abs/2604.25011) | Reinforcement learning (RL)-based post-training often improves the reasoning performance of large language models (LLMs) beyond the training domain, w | SFT |
| 3 | EditCaption: Human-Aligned Instruction Synthesis for Image Editing via Supervised Fine-Tuning and Direct Preference Opti | Xiangyuan Wang | 2026 | [2604.08213](https://arxiv.org/abs/2604.08213) | High-quality training triplets (source-target image pairs with precise editing instructions) are a critical bottleneck for scaling instruction-guided | SFT |
| 4 | TAU-R1: Visual Language Model for Traffic Anomaly Understanding | Yuqiang Lin | 2026 | [2603.19098](https://arxiv.org/abs/2603.19098) | Traffic Anomaly Understanding (TAU) is important for traffic safety in Intelligent Transportation Systems. Recent vision-language models (VLMs) have s | SFT |
| 5 | Supervised Fine-Tuning versus Reinforcement Learning: A Study of Post-Training Methods for Large Language Models | Haitao Jiang | 2026 | [2603.13985](https://arxiv.org/abs/2603.13985) | Pre-trained Large Language Model (LLM) exhibits broad capabilities, yet, for specific tasks or domains their attainment of higher accuracy and more re | SFT |
| 6 | AlignTune: Modular Toolkit for Post-Training Alignment of Large Language Models | R E Zera Marveen Lyngkhoi | 2026 | [2602.09621](https://arxiv.org/abs/2602.09621) | Post-training alignment is central to deploying large language models (LLMs), yet practical workflows remain split across backend-specific tools and a | SFT |
| 7 | ASTRA: Automated Synthesis of agentic Trajectories and Reinforcement Arenas | Xiaoyu Tian | 2026 | [2601.21558](https://arxiv.org/abs/2601.21558) | Large language models (LLMs) are increasingly used as tool-augmented agents for multi-step decision making, yet training robust tool-using agents rema | AgentRL |
| 8 | On the Non-decoupling of Supervised Fine-tuning and Reinforcement Learning in Post-training | Xueyan Niu | 2026 | [2601.07389](https://arxiv.org/abs/2601.07389) | Post-training of large language models routinely interleaves supervised fine-tuning (SFT) with reinforcement learning (RL). These two methods have dif | SFT |
| 9 | MindGPT-4ov: An Enhanced MLLM via a Multi-Stage Post-Training Paradigm | Wei Chen | 2025 | [2512.02895](https://arxiv.org/abs/2512.02895) | We present MindGPT-4ov, a multimodal large language model (MLLM) that introduces a general post-training paradigm spanning data production, model trai | SFT |
| 10 | PromptCoT 2.0: Scaling Prompt Synthesis for Large Language Model
  Reasoning | Xueliang Zhao | 2025 | [2509.19894](https://arxiv.org/abs/2509.19894) | Large language models (LLMs) are evolving from conversational systems into strong reasoners for tasks such as Olympiad mathematics and competitive pro | SFT |
| 11 | Towards a Unified View of Large Language Model Post-Training | Xingtai Lv | 2025 | [2509.04419](https://arxiv.org/abs/2509.04419) | Two major sources of training data exist for post-training modern language models: online (model-generated rollouts) data, and offline (human or other | SFT |
| 12 | Dream-Coder 7B: An Open Diffusion Language Model for Code | Zhihui Xie | 2025 | [2509.01142](https://arxiv.org/abs/2509.01142) | We present Dream-Coder 7B, an open-source discrete diffusion language model for code generation that exhibits emergent any-order generation capabiliti | SFT |
| 13 | EvoLM: In Search of Lost Language Model Training Dynamics | Zhenting Qi | 2025 | [2506.16029](https://arxiv.org/abs/2506.16029) | Modern language model (LM) training has been divided into multiple stages, making it difficult for downstream developers to evaluate the impact of des | SFT |
| 14 | Implicit Reward as the Bridge: A Unified View of SFT and DPO Connections | Bo Wang | 2025 | [2507.00018](https://arxiv.org/abs/2507.00018) | Post-training processes are essential phases in grounding pre-trained language models to real-world tasks, with learning from demonstrations or prefer | SFT |
| 15 | DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via
  Reinforcement Learning | DeepSeek-AI | 2025 | [2501.12948](https://arxiv.org/abs/2501.12948) | We introduce our first-generation reasoning models, DeepSeek-R1-Zero and DeepSeek-R1. DeepSeek-R1-Zero, a model trained via large-scale reinforcement | AgentRL |
| 16 | Preference Optimization for Reasoning with Pseudo Feedback | Fangkai Jiao | 2024 | [2411.16345](https://arxiv.org/abs/2411.16345) | Preference optimization techniques, such as Direct Preference Optimization (DPO), are frequently employed to enhance the reasoning capabilities of lar | PrefOpt, DPO_variants |
| 17 | PLaMo-100B: A Ground-Up Language Model Designed for Japanese Proficiency | Kenshin Abe | 2024 | [2410.07563](https://arxiv.org/abs/2410.07563) | We introduce PLaMo-100B, a large-scale language model designed for Japanese proficiency. The model was trained from scratch using 2 trillion tokens, w | SFT |
| 18 | Building Math Agents with Multi-Turn Iterative Preference Learning | Wei Xiong | 2024 | [2409.02392](https://arxiv.org/abs/2409.02392) | Recent studies have shown that large language models' (LLMs) mathematical problem-solving capabilities can be enhanced by integrating external tools, | DPO_variants |
| 19 | Arena Learning: Build Data Flywheel for LLMs Post-training via Simulated
  Chatbot Arena | Haipeng Luo | 2024 | [2407.10627](https://arxiv.org/abs/2407.10627) | Assessing the effectiveness of large language models (LLMs) presents substantial challenges. The method of conducting human-annotated battles in an on | SFT |
| 20 | Iterative Reasoning Preference Optimization | Richard Yuanzhe Pang | 2024 | [2404.19733](https://arxiv.org/abs/2404.19733) | Iterative preference optimization methods have recently been shown to perform well for general instruction tuning tasks, but typically make little imp | DPO_variants |
| 21 | ORPO: Monolithic Preference Optimization without Reference Model | Jiwoo Hong | 2024 | [2403.07691](https://arxiv.org/abs/2403.07691) | While recent preference alignment algorithms for language models have demonstrated promising results, supervised fine-tuning (SFT) remains imperative | DPO_variants |
| 22 | A Critical Evaluation of AI Feedback for Aligning Large Language Models | Archit Sharma | 2024 | [2402.12366](https://arxiv.org/abs/2402.12366) | Reinforcement learning with AI feedback (RLAIF) is a popular paradigm for improving the instruction-following abilities of powerful pre-trained langua | RLAIF |
| 23 | ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world
  APIs | Yujia Qin | 2023 | [2307.16789](https://arxiv.org/abs/2307.16789) | Despite the advancements of open-source large language models (LLMs) and their variants, e.g., LLaMA and Vicuna, they remain significantly limited in | AgentRL |

### Q2: Reward Modeling
> 奖励模型的设计、训练、泛化性、Reward Hacking 问题

**论文数**: 76 篇

| # | 论文标题 | 第一作者 | 年份 | arXiv ID | 核心贡献摘要 | 标签 |
|---|----------|----------|------|----------|-------------|------|
| 1 | The Flip Side of RLHF: On-Policy Feedback for Reward Model Self-Supervised Improvement | Xiaobo Wang | 2026 | [2605.30888](https://arxiv.org/abs/2605.30888) | Building strong reward models (RMs) for language model alignment is bottlenecked by the cost and difficulty of acquiring diverse and reliable preferen | RewardModel |
| 2 | Directional Alignment Mitigates Reward Hacking in Reinforcement Learning for Language Models | Wenlong Deng | 2026 | [2605.25189](https://arxiv.org/abs/2605.25189) | Reward hacking arises when a model improves a proxy reward by exploiting shortcuts rather than solving the intended task. We study this failure mode t | RewardModel |
| 3 | AutoRubric-T2I: Robust Rule-Based Reward Model for Text-to-Image Alignment | Kuei-Chun Kao | 2026 | [2605.17602](https://arxiv.org/abs/2605.17602) | Aligning Text-to-Image (T2I) generation models with human preferences increasingly relies on image reward models that score or rank generated images a | RewardModel |
| 4 | Hack-Verifiable Environments: Towards Evaluating Reward Hacking at Scale | Amit Roth | 2026 | [2605.20744](https://arxiv.org/abs/2605.20744) | Aligning autonomous agents with human intent remains a central challenge in modern AI. A key manifestation of this challenge is reward hacking, whereb | RewardModel |
| 5 | Unsupervised Process Reward Models | Artyom Gadetsky | 2026 | [2605.10158](https://arxiv.org/abs/2605.10158) | Process Reward Models (PRMs) are a powerful mechanism for steering large language model reasoning by providing fine-grained, step-level supervision. H | RewardModel |
| 6 | GRPO-VPS: Enhancing Group Relative Policy Optimization with Verifiable Process Supervision for Effective Reasoning | Jingyi Wang | 2026 | [2604.20659](https://arxiv.org/abs/2604.20659) | Reinforcement Learning with Verifiable Rewards (RLVR) has advanced the reasoning capabilities of Large Language Models (LLMs) by leveraging direct out | GRPO |
| 7 | Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges | Xiaohua Wang | 2026 | [2604.13602](https://arxiv.org/abs/2604.13602) | Reinforcement Learning from Human Feedback (RLHF) and related alignment paradigms have become central to steering large language models (LLMs) and mul | RewardModel |
| 8 | Stabilizing Rubric Integration Training via Decoupled Advantage Normalization | Zelin Tan | 2026 | [2603.26535](https://arxiv.org/abs/2603.26535) | We propose Process-Aware Policy Optimization (PAPO), a method that integrates process-level evaluation into Group Relative Policy Optimization (GRPO) | RewardModel |
| 9 | GOPO: Policy Optimization using Ranked Rewards | Kyuseong Choi | 2026 | [2602.03876](https://arxiv.org/abs/2602.03876) | Standard reinforcement learning from human feedback (RLHF) trains a reward model on pairwise preference data and then uses it for policy optimization. | DPO_variants |
| 10 | SCRIBE: Structured Mid-Level Supervision for Tool-Using Language Models | Yuxuan Jiang | 2026 | [2601.03555](https://arxiv.org/abs/2601.03555) | Training reliable tool-augmented agents remains a significant challenge, largely due to the difficulty of credit assignment in multi-step reasoning. W | AgentRL |
| 11 | Understanding Reward Hacking in Text-to-Image Reinforcement Learning | Yunqi Hong | 2026 | [2601.03468](https://arxiv.org/abs/2601.03468) | Reinforcement learning (RL) has become a standard approach for post-training large language models and, more recently, for improving image generation | RewardModel |
| 12 | SR-GRPO: Stable Rank as an Intrinsic Geometric Reward for Large Language Model Alignment | Yixuan Tang | 2025 | [2512.02807](https://arxiv.org/abs/2512.02807) | Aligning Large Language Models (LLMs) with human preferences typically relies on external supervision, which faces critical limitations: human annotat | RewardModel |
| 13 | Natural Emergent Misalignment from Reward Hacking in Production RL | Monte MacDiarmid | 2025 | [2511.18397](https://arxiv.org/abs/2511.18397) | We show that when large language models learn to reward hack on production RL environments, this can result in egregious emergent misalignment. We sta | RewardModel |
| 14 | GroundedPRM: Tree-Guided and Fidelity-Aware Process Reward Modeling for
  Step-Level Reasoning | Yao Zhang | 2025 | [2510.14942](https://arxiv.org/abs/2510.14942) | Process Reward Models (PRMs) aim to improve multi-step reasoning in Large Language Models (LLMs) by supervising intermediate steps and identifying err | RewardModel |
| 15 | Clean First, Align Later: Benchmarking Preference Data Cleaning for
  Reliable LLM Alignment | Min-Hsuan Yeh | 2025 | [2509.23564](https://arxiv.org/abs/2509.23564) | Human feedback plays a pivotal role in aligning large language models (LLMs) with human preferences. However, such feedback is often noisy or inconsis | Eval |
| 16 | Training Vision-Language Process Reward Models for Test-Time Scaling in
  Multimodal Reasoning: Key Insights and Lessons | Brandon Ong | 2025 | [2509.23250](https://arxiv.org/abs/2509.23250) | Process Reward Models (PRMs) provide step-level supervision that improves the reliability of reasoning in large language models. While PRMs have been | RewardModel |
| 17 | MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems | Yuki Ichihara | 2025 | [2509.22047](https://arxiv.org/abs/2509.22047) | Group Relative Policy Optimization (GRPO) has been shown to be an effective algorithm when an accurate reward model is available. However, such a high | GRPO |
| 18 | Adaptive Preference Optimization with Uncertainty-aware Utility Anchor | Xiaobo Wang | 2025 | [2509.10515](https://arxiv.org/abs/2509.10515) | Offline preference optimization methods are efficient for large language models (LLMs) alignment. Direct Preference optimization (DPO)-like learning, | DPO_variants |
| 19 | School of Reward Hacks: Hacking harmless tasks generalizes to misaligned behavior in LLMs | Mia Taylor | 2025 | [2508.17511](https://arxiv.org/abs/2508.17511) | Reward hacking--where agents exploit flaws in imperfect reward functions rather than performing tasks as intended--poses risks for AI alignment. Rewar | RewardModel |
| 20 | Cooper: Co-Optimizing Policy and Reward Models in Reinforcement Learning
  for Large Language Models | Haitao Hong | 2025 | [2508.05613](https://arxiv.org/abs/2508.05613) | Large language models (LLMs) have demonstrated remarkable performance in reasoning tasks, where reinforcement learning (RL) serves as a key algorithm | RewardModel |
| 21 | VRPRM: Process Reward Modeling via Visual Reasoning | Xinquan Chen | 2025 | [2508.03556](https://arxiv.org/abs/2508.03556) | Process Reward Model (PRM) is widely used in the post-training of Large Language Model (LLM) because it can perform fine-grained evaluation of the rea | RewardModel |
| 22 | Uncertainty-Based Methods for Automated Process Reward Data Construction
  and Output Aggregation in Mathematical Reason | Jiuzhou Han | 2025 | [2508.01773](https://arxiv.org/abs/2508.01773) | Large language models have demonstrated remarkable capabilities in complex mathematical reasoning tasks, but they inevitably generate errors throughou | RewardModel |
| 23 | The Bidirectional Process Reward Model | Lingyin Zhang | 2025 | [2508.01682](https://arxiv.org/abs/2508.01682) | Process Reward Models (PRMs) have emerged as a promising approach to enhance the reasoning quality of Large Language Models (LLMs) by assigning fine-g | RewardModel |
| 24 | Activation Reward Models for Few-Shot Model Alignment | Tianning Chai | 2025 | [2507.01368](https://arxiv.org/abs/2507.01368) | Aligning Large Language Models (LLMs) and Large Multimodal Models (LMMs) to human preferences is a central challenge in improving the quality of the m | RewardModel |
| 25 | Toward Evaluative Thinking: Meta Policy Optimization with Evolving
  Reward Models | Zae Myung Kim | 2025 | [2504.20157](https://arxiv.org/abs/2504.20157) | Reward-based alignment methods for large language models (LLMs) face two key limitations: vulnerability to reward hacking, where models exploit flaws | RewardModel |
| 26 | Pre-DPO: Improving Data Utilization in Direct Preference Optimization
  Using a Guiding Reference Model | Junshu Pan | 2025 | [2504.15843](https://arxiv.org/abs/2504.15843) | Direct Preference Optimization (DPO) simplifies reinforcement learning from human feedback (RLHF) for large language models (LLMs) by directly optimiz | DPO_variants |
| 27 | Energy-Based Reward Models for Robust Language Model Alignment | Anamika Lochab | 2025 | [2504.13134](https://arxiv.org/abs/2504.13134) | Reward models (RMs) are essential for aligning Large Language Models (LLMs) with human preferences. However, they often struggle with capturing comple | RewardModel |
| 28 | Learning from Reference Answers: Versatile Language Model Alignment
  without Binary Human Preference Data | Shuai Zhao | 2025 | [2504.09895](https://arxiv.org/abs/2504.09895) | Large language models~(LLMs) are expected to be helpful, harmless, and honest. In alignment scenarios such as safety, confidence, and general preferen | RewardModel |
| 29 | Adversarial Training of Reward Models | Alexander Bukharin | 2025 | [2504.06141](https://arxiv.org/abs/2504.06141) | Reward modeling has emerged as a promising approach for the scalable alignment of language models. However, contemporary reward models (RMs) often lac | RewardModel |
| 30 | Robust Reinforcement Learning from Human Feedback for Large Language Models Fine-Tuning | Kai Ye | 2025 | [2504.03784](https://arxiv.org/abs/2504.03784) | Reinforcement learning from human feedback (RLHF) has emerged as a key technique for aligning the output of large language models (LLMs) with human pr | RLHF |
| 31 | R-PRM: Reasoning-Driven Process Reward Modeling | Shuaijie She | 2025 | [2503.21295](https://arxiv.org/abs/2503.21295) | Large language models (LLMs) inevitably make mistakes when performing step-by-step mathematical reasoning. Process Reward Models (PRMs) have emerged a | RewardModel |
| 32 | Better Process Supervision with Bi-directional Rewarding Signals | Wenxiang Chen | 2025 | [2503.04618](https://arxiv.org/abs/2503.04618) | Process supervision, i.e., evaluating each step, is critical for complex large language model (LLM) reasoning and test-time searching with increased i | RewardModel |
| 33 | AlignDistil: Token-Level Language Model Alignment as Adaptive Policy
  Distillation | Songming Zhang | 2025 | [2503.02832](https://arxiv.org/abs/2503.02832) | In modern large language models (LLMs), LLM alignment is of crucial importance and is typically achieved through methods such as reinforcement learnin | RewardModel |
| 34 | Improving LLM General Preference Alignment via Optimistic Online Mirror
  Descent | Yuheng Zhang | 2025 | [2502.16852](https://arxiv.org/abs/2502.16852) | Reinforcement learning from human feedback (RLHF) has demonstrated remarkable effectiveness in aligning large language models (LLMs) with human prefer | RLHF |
| 35 | Preference Optimization via Contrastive Divergence: Your Reward Model is Secretly an NLL Estimator | Zhuotong Chen | 2025 | [2502.04567](https://arxiv.org/abs/2502.04567) | Existing studies on preference optimization (PO) have centered on constructing pairwise preference data following simple heuristics, such as maximizin | DPO_variants |
| 36 | Reusing Embeddings: Reproducible Reward Model Research in Large Language
  Model Alignment without GPUs | Hao Sun | 2025 | [2502.04357](https://arxiv.org/abs/2502.04357) | Large Language Models (LLMs) have made substantial strides in structured tasks through Reinforcement Learning (RL), demonstrating proficiency in mathe | RewardModel |
| 37 | Reward-aware Preference Optimization: A Unified Mathematical Framework
  for Model Alignment | Shengyang Sun | 2025 | [2502.00203](https://arxiv.org/abs/2502.00203) | The rapid development of large language model (LLM) alignment algorithms has resulted in a complex and fragmented landscape, with limited clarity on t | RewardModel |
| 38 | Beyond Reward Hacking: Causal Rewards for Large Language Model Alignment | Chaoqi Wang | 2025 | [2501.09620](https://arxiv.org/abs/2501.09620) | Recent advances in large language models (LLMs) have demonstrated significant progress in performing complex tasks. While Reinforcement Learning from | RewardModel |
| 39 | The Lessons of Developing Process Reward Models in Mathematical
  Reasoning | Zhenru Zhang | 2025 | [2501.07301](https://arxiv.org/abs/2501.07301) | Process Reward Models (PRMs) emerge as a promising approach for process supervision in mathematical reasoning of Large Language Models (LLMs), which a | RewardModel |
| 40 | AlphaPO -- Reward shape matters for LLM alignment | Aman Gupta | 2025 | [2501.03884](https://arxiv.org/abs/2501.03884) | Reinforcement Learning with Human Feedback (RLHF) and its variants have made huge strides toward the effective alignment of large language models (LLM | DPO_variants |
| 41 | PRMBench: A Fine-grained and Challenging Benchmark for Process-Level
  Reward Models | Mingyang Song | 2025 | [2501.03124](https://arxiv.org/abs/2501.03124) | Process-level Reward Models (PRMs) are crucial for complex reasoning and decision-making tasks, where each intermediate step plays an important role i | RewardModel |
| 42 | InfAlign: Inference-aware language model alignment | Ananth Balashankar | 2024 | [2412.19792](https://arxiv.org/abs/2412.19792) | Language model alignment has become a critical step in training modern generative language models. The goal of alignment is to finetune a reference mo | RewardModel |
| 43 | Sail into the Headwind: Alignment via Robust Rewards and Dynamic Labels against Reward Hacking | Paria Rashidinejad | 2024 | [2412.09544](https://arxiv.org/abs/2412.09544) | Aligning AI systems with human preferences typically suffers from the infamous reward hacking problem, where optimization of an imperfect reward model | RewardModel |
| 44 | Free Process Rewards without Process Labels | Lifan Yuan | 2024 | [2412.01981](https://arxiv.org/abs/2412.01981) | Different from its counterpart outcome reward models (ORMs), which evaluate the entire responses, a process reward model (PRM) scores a reasoning traj | RewardModel |
| 45 | Entropy Controllable Direct Preference Optimization | Motoki Omura | 2024 | [2411.07595](https://arxiv.org/abs/2411.07595) | In the post-training of large language models (LLMs), Reinforcement Learning from Human Feedback (RLHF) is an effective approach to achieve generation | DPO |
| 46 | CARMO: Dynamic Criteria Generation for Context-Aware Reward Modelling | Taneesh Gupta | 2024 | [2410.21545](https://arxiv.org/abs/2410.21545) | Reward modeling in large language models is susceptible to reward hacking, causing models to latch onto superficial features such as the tendency to g | RewardModel |
| 47 | On Designing Effective RL Reward at Training Time for LLM Reasoning | Jiaxuan Gao | 2024 | [2410.15115](https://arxiv.org/abs/2410.15115) | Reward models have been increasingly critical for improving the reasoning capability of LLMs. Existing research has shown that a well-trained reward m | RewardModel |
| 48 | Process Reward Model with Q-Value Rankings | Wendi Li | 2024 | [2410.11287](https://arxiv.org/abs/2410.11287) | Process Reward Modeling (PRM) is critical for complex reasoning and decision-making tasks where the accuracy of intermediate steps significantly influ | RewardModel |
| 49 | Align^2LLaVA: Cascaded Human and Large Language Model Preference
  Alignment for Multi-modal Instruction Curation | Hongzhe Huang | 2024 | [2409.18541](https://arxiv.org/abs/2409.18541) | Recent advances in Multi-modal Large Language Models (MLLMs), such as LLaVA-series models, are driven by massive machine-generated instruction-followi | RewardModel |
| 50 | Self-supervised Preference Optimization: Enhance Your Language Model
  with Preference Degree Awareness | Jian Li | 2024 | [2409.17791](https://arxiv.org/abs/2409.17791) | Recently, there has been significant interest in replacing the reward model in Reinforcement Learning with Human Feedback (RLHF) methods for Large Lan | PrefOpt |
| 51 | Sequence to Sequence Reward Modeling: Improving RLHF by Language
  Feedback | Jiayi Zhou | 2024 | [2409.00162](https://arxiv.org/abs/2409.00162) | Aligning the behavior of Large language models (LLMs) with human intentions and values remains a critical challenge. Reinforcement learning from human | RLHF |
| 52 | Learning Goal-Conditioned Representations for Language Reward Models | Vaskar Nath | 2024 | [2407.13887](https://arxiv.org/abs/2407.13887) | Techniques that learn improved representations via offline data or self-supervised objectives have shown impressive results in traditional reinforceme | RLHF |
| 53 | Spontaneous Reward Hacking in Iterative Self-Refinement | Jane Pan | 2024 | [2407.04549](https://arxiv.org/abs/2407.04549) | Language models are capable of iteratively improving their outputs based on natural language feedback, thus enabling in-context optimization of user p | RewardModel |
| 54 | Iterative Length-Regularized Direct Preference Optimization: A Case
  Study on Improving 7B Language Models to GPT-4 Lev | Jie Liu | 2024 | [2406.11817](https://arxiv.org/abs/2406.11817) | Direct Preference Optimization (DPO), a standard method for aligning language models with human preferences, is traditionally applied to offline prefe | DPO, DPO_variants |
| 55 | Step-level Value Preference Optimization for Mathematical Reasoning | Guoxin Chen | 2024 | [2406.10858](https://arxiv.org/abs/2406.10858) | Direct Preference Optimization (DPO) using an implicit reward model has proven to be an effective alternative to reinforcement learning from human fee | DPO_variants |
| 56 | Online DPO: Online Direct Preference Optimization with Fast-Slow Chasing | Biqing Qi | 2024 | [2406.05534](https://arxiv.org/abs/2406.05534) | Direct Preference Optimization (DPO) improves the alignment of large language models (LLMs) with human values by training directly on human preference | DPO |
| 57 | Scaling Laws for Reward Model Overoptimization in Direct Alignment
  Algorithms | Rafael Rafailov | 2024 | [2406.02900](https://arxiv.org/abs/2406.02900) | Reinforcement Learning from Human Feedback (RLHF) has been crucial to the recent success of Large Language Models (LLMs), however, it is often a compl | RewardModel |
| 58 | Improve Mathematical Reasoning in Language Models by Automated Process
  Supervision | Liangchen Luo | 2024 | [2406.06592](https://arxiv.org/abs/2406.06592) | Complex multi-step reasoning tasks, such as solving mathematical problems or generating code, remain a significant hurdle for even the most advanced l | RewardModel |
| 59 | Self-Exploring Language Models: Active Preference Elicitation for Online
  Alignment | Shenao Zhang | 2024 | [2405.19332](https://arxiv.org/abs/2405.19332) | Preference optimization, particularly through Reinforcement Learning from Human Feedback (RLHF), has achieved significant success in aligning Large La | PrefOpt |
| 60 | Aligning to Thousands of Preferences via System Message Generalization | Seongyun Lee | 2024 | [2405.17977](https://arxiv.org/abs/2405.17977) | Although humans inherently have diverse values, current large language model (LLM) alignment methods often assume that aligning LLMs with the general | Eval |
| 61 | RLHF Workflow: From Reward Modeling to Online RLHF | Hanze Dong | 2024 | [2405.07863](https://arxiv.org/abs/2405.07863) | We present the workflow of Online Iterative Reinforcement Learning from Human Feedback (RLHF) in this technical report, which is widely reported to ou | Eval |
| 62 | Value Augmented Sampling for Language Model Alignment and
  Personalization | Seungwook Han | 2024 | [2405.06639](https://arxiv.org/abs/2405.06639) | Aligning Large Language Models (LLMs) to cater to different human preferences, learning new skills, and unlearning harmful behavior is an important pr | RewardModel |
| 63 | Self-Play Preference Optimization for Language Model Alignment | Yue Wu | 2024 | [2405.00675](https://arxiv.org/abs/2405.00675) | Traditional reinforcement learning from human feedback (RLHF) approaches relying on parametric models like the Bradley-Terry model fall short in captu | PrefOpt |
| 64 | Asymptotics of Language Model Alignment | Joy Qiping Yang | 2024 | [2404.01730](https://arxiv.org/abs/2404.01730) | Let p denote a generative language model. Let r denote a reward model that returns a scalar that captures the degree at which a draw from p is preferr | RewardModel |
| 65 | Direct Preference Optimization of Video Large Multimodal Models from
  Language Model Reward | Ruohong Zhang | 2024 | [2404.01258](https://arxiv.org/abs/2404.01258) | Preference modeling techniques, such as direct preference optimization (DPO), has shown effective in enhancing the generalization abilities of large l | DPO |
| 66 | DMoERM: Recipes of Mixture-of-Experts for Effective Reward Modeling | Shanghaoran Quan | 2024 | [2403.01197](https://arxiv.org/abs/2403.01197) | The performance of the reward model (RM) is a critical factor in improving the effectiveness of the large language model (LLM) during alignment fine-t | RewardModel |
| 67 | Direct Preference Optimization with an Offset | Afra Amini | 2024 | [2402.10571](https://arxiv.org/abs/2402.10571) | Direct preference optimization (DPO) is a successful fine-tuning strategy for aligning large language models with human preferences without the need t | DPO, DPO_variants |
| 68 | MaxMin-RLHF: Towards Equitable Alignment of Large Language Models with
  Diverse Human Preferences | Souradip Chakraborty | 2024 | [2402.08925](https://arxiv.org/abs/2402.08925) | Reinforcement Learning from Human Feedback (RLHF) aligns language models to human preferences by employing a singular reward model derived from prefer | RLHF |
| 69 | Direct Language Model Alignment from Online AI Feedback | Shangmin Guo | 2024 | [2402.04792](https://arxiv.org/abs/2402.04792) | Direct alignment from preferences (DAP) methods, such as DPO, have recently emerged as efficient alternatives to reinforcement learning from human fee | RewardModel |
| 70 | Towards Efficient and Exact Optimization of Language Model Alignment | Haozhe Ji | 2024 | [2402.00856](https://arxiv.org/abs/2402.00856) | The alignment of language models with human preferences is vital for their application in real-world tasks. The problem is formulated as optimizing th | PrefOpt, RewardModel |
| 71 | West-of-N: Synthetic Preference Generation for Improved Reward Modeling | Alizée Pace | 2024 | [2401.12086](https://arxiv.org/abs/2401.12086) | The success of reinforcement learning from human feedback (RLHF) in language model alignment is strongly dependent on the quality of the underlying re | RLHF, RewardModel |
| 72 | Helping or Herding? Reward Model Ensembles Mitigate but do not Eliminate
  Reward Hacking | Jacob Eisenstein | 2023 | [2312.09244](https://arxiv.org/abs/2312.09244) | Reward models play a key role in aligning language model applications towards human preferences. However, this setup creates an incentive for the lang | RewardModel |
| 73 | On Diversified Preferences of Large Language Model Alignment | Dun Zeng | 2023 | [2312.07401](https://arxiv.org/abs/2312.07401) | Aligning large language models (LLMs) with human preferences has been recognized as the key to improving LLMs' interaction quality. However, in this p | RewardModel |
| 74 | Language Model Alignment with Elastic Reset | Michael Noukhovitch | 2023 | [2312.07551](https://arxiv.org/abs/2312.07551) | Finetuning language models with reinforcement learning (RL), e.g. from human feedback (HF), is a prominent method for alignment. But optimizing agains | RewardModel |
| 75 | Beyond One-Preference-Fits-All Alignment: Multi-Objective Direct
  Preference Optimization | Zhanhui Zhou | 2023 | [2310.03708](https://arxiv.org/abs/2310.03708) | A single language model (LM), despite aligning well with an average labeler through reinforcement learning from human feedback (RLHF), may not univers | RLHF, DPO_variants |
| 76 | Training a Helpful and Harmless Assistant with Reinforcement Learning
  from Human Feedback | Yuntao Bai | 2022 | [2204.05862](https://arxiv.org/abs/2204.05862) | We apply preference modeling and reinforcement learning from human feedback (RLHF) to finetune language models to act as helpful and harmless assistan | RLHF |

### Q3: PPO-based RLHF
> PPO 在 LLM 对齐中的算法改进、训练稳定性、scaling 特性

**论文数**: 42 篇

| # | 论文标题 | 第一作者 | 年份 | arXiv ID | 核心贡献摘要 | 标签 |
|---|----------|----------|------|----------|-------------|------|
| 1 | The Flip Side of RLHF: On-Policy Feedback for Reward Model Self-Supervised Improvement | Xiaobo Wang | 2026 | [2605.30888](https://arxiv.org/abs/2605.30888) | Building strong reward models (RMs) for language model alignment is bottlenecked by the cost and difficulty of acquiring diverse and reliable preferen | RewardModel |
| 2 | Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges | Xiaohua Wang | 2026 | [2604.13602](https://arxiv.org/abs/2604.13602) | Reinforcement Learning from Human Feedback (RLHF) and related alignment paradigms have become central to steering large language models (LLMs) and mul | RewardModel |
| 3 | GOPO: Policy Optimization using Ranked Rewards | Kyuseong Choi | 2026 | [2602.03876](https://arxiv.org/abs/2602.03876) | Standard reinforcement learning from human feedback (RLHF) trains a reward model on pairwise preference data and then uses it for policy optimization. | DPO_variants |
| 4 | Reflect: Transparent Principle-Guided Reasoning for Constitutional Alignment at Scale | Henry Bell | 2026 | [2601.18730](https://arxiv.org/abs/2601.18730) | The constitutional framework of alignment aims to align large language models (LLMs) with value-laden principles written in natural language (such as | RLAIF |
| 5 | Legal Alignment for Safe and Ethical AI | Noam Kolt | 2026 | [2601.04175](https://arxiv.org/abs/2601.04175) | Alignment of artificial intelligence (AI) encompasses the normative problem of specifying how AI systems should act and the technical problem of ensur | RLAIF |
| 6 | Co-Alignment: Rethinking Alignment as Bidirectional Human-AI Cognitive Adaptation | Yubo Li | 2025 | [2509.12179](https://arxiv.org/abs/2509.12179) | Current AI alignment through RLHF follows a single directional paradigm that AI conforms to human preferences while treating human cognition as fixed. | RLAIF |
| 7 | On the Inevitability of Left-Leaning Political Bias in Aligned Language
  Models | Thilo Hagendorff | 2025 | [2507.15328](https://arxiv.org/abs/2507.15328) | The guiding principle of AI alignment is to train large language models (LLMs) to be harmless, helpful, and honest (HHH). At the same time, there are | RLAIF |
| 8 | Robust Reinforcement Learning from Human Feedback for Large Language Models Fine-Tuning | Kai Ye | 2025 | [2504.03784](https://arxiv.org/abs/2504.03784) | Reinforcement learning from human feedback (RLHF) has emerged as a key technique for aligning the output of large language models (LLMs) with human pr | RLHF |
| 9 | Improving LLM General Preference Alignment via Optimistic Online Mirror
  Descent | Yuheng Zhang | 2025 | [2502.16852](https://arxiv.org/abs/2502.16852) | Reinforcement learning from human feedback (RLHF) has demonstrated remarkable effectiveness in aligning large language models (LLMs) with human prefer | RLHF |
| 10 | Reusing Embeddings: Reproducible Reward Model Research in Large Language
  Model Alignment without GPUs | Hao Sun | 2025 | [2502.04357](https://arxiv.org/abs/2502.04357) | Large Language Models (LLMs) have made substantial strides in structured tasks through Reinforcement Learning (RL), demonstrating proficiency in mathe | RewardModel |
| 11 | Beyond Reward Hacking: Causal Rewards for Large Language Model Alignment | Chaoqi Wang | 2025 | [2501.09620](https://arxiv.org/abs/2501.09620) | Recent advances in large language models (LLMs) have demonstrated significant progress in performing complex tasks. While Reinforcement Learning from | RewardModel |
| 12 | AlphaPO -- Reward shape matters for LLM alignment | Aman Gupta | 2025 | [2501.03884](https://arxiv.org/abs/2501.03884) | Reinforcement Learning with Human Feedback (RLHF) and its variants have made huge strides toward the effective alignment of large language models (LLM | DPO_variants |
| 13 | Align Anything: Training All-Modality Models to Follow Instructions with
  Language Feedback | Jiaming Ji | 2024 | [2412.15838](https://arxiv.org/abs/2412.15838) | Reinforcement learning from human feedback (RLHF) has proven effective in enhancing the instruction-following capabilities of large language models; h | RLHF |
| 14 | CARMO: Dynamic Criteria Generation for Context-Aware Reward Modelling | Taneesh Gupta | 2024 | [2410.21545](https://arxiv.org/abs/2410.21545) | Reward modeling in large language models is susceptible to reward hacking, causing models to latch onto superficial features such as the tendency to g | RewardModel |
| 15 | Regressing the Relative Future: Efficient Policy Optimization for
  Multi-turn RLHF | Zhaolin Gao | 2024 | [2410.04612](https://arxiv.org/abs/2410.04612) | Large Language Models (LLMs) have achieved remarkable success at tasks like summarization that involve a single turn of interaction. However, they can | RLHF |
| 16 | Language Models Learn to Mislead Humans via RLHF | Jiaxin Wen | 2024 | [2409.12822](https://arxiv.org/abs/2409.12822) | Language models (LMs) can produce errors that are hard to detect for humans, especially when the task is complex. RLHF, the most popular post-training | RLHF |
| 17 | Sequence to Sequence Reward Modeling: Improving RLHF by Language
  Feedback | Jiayi Zhou | 2024 | [2409.00162](https://arxiv.org/abs/2409.00162) | Aligning the behavior of Large language models (LLMs) with human intentions and values remains a critical challenge. Reinforcement learning from human | RLHF |
| 18 | Preference-Guided Reflective Sampling for Aligning Language Models | Hai Ye | 2024 | [2408.12163](https://arxiv.org/abs/2408.12163) | Large language models (LLMs) are aligned with human preferences by reinforcement learning from human feedback (RLHF). Effective data sampling is cruci | RLHF |
| 19 | Learning Goal-Conditioned Representations for Language Reward Models | Vaskar Nath | 2024 | [2407.13887](https://arxiv.org/abs/2407.13887) | Techniques that learn improved representations via offline data or self-supervised objectives have shown impressive results in traditional reinforceme | RLHF |
| 20 | WPO: Enhancing RLHF with Weighted Preference Optimization | Wenxuan Zhou | 2024 | [2406.11827](https://arxiv.org/abs/2406.11827) | Reinforcement learning from human feedback (RLHF) is a promising solution to align large language models (LLMs) more closely with human values. Off-po | Eval |
| 21 | Scaling Laws for Reward Model Overoptimization in Direct Alignment
  Algorithms | Rafael Rafailov | 2024 | [2406.02900](https://arxiv.org/abs/2406.02900) | Reinforcement Learning from Human Feedback (RLHF) has been crucial to the recent success of Large Language Models (LLMs), however, it is often a compl | RewardModel |
| 22 | Self-Exploring Language Models: Active Preference Elicitation for Online
  Alignment | Shenao Zhang | 2024 | [2405.19332](https://arxiv.org/abs/2405.19332) | Preference optimization, particularly through Reinforcement Learning from Human Feedback (RLHF), has achieved significant success in aligning Large La | PrefOpt |
| 23 | RLHF Workflow: From Reward Modeling to Online RLHF | Hanze Dong | 2024 | [2405.07863](https://arxiv.org/abs/2405.07863) | We present the workflow of Online Iterative Reinforcement Learning from Human Feedback (RLHF) in this technical report, which is widely reported to ou | Eval |
| 24 | Self-Play Preference Optimization for Language Model Alignment | Yue Wu | 2024 | [2405.00675](https://arxiv.org/abs/2405.00675) | Traditional reinforcement learning from human feedback (RLHF) approaches relying on parametric models like the Bradley-Terry model fall short in captu | PrefOpt |
| 25 | Extensive Self-Contrast Enables Feedback-Free Language Model Alignment | Xiao Liu | 2024 | [2404.00604](https://arxiv.org/abs/2404.00604) | Reinforcement learning from human feedback (RLHF) has been a central technique for recent large language model (LLM) alignment. However, its heavy dep | RLHF |
| 26 | MaxMin-RLHF: Towards Equitable Alignment of Large Language Models with
  Diverse Human Preferences | Souradip Chakraborty | 2024 | [2402.08925](https://arxiv.org/abs/2402.08925) | Reinforcement Learning from Human Feedback (RLHF) aligns language models to human preferences by employing a singular reward model derived from prefer | RLHF |
| 27 | West-of-N: Synthetic Preference Generation for Improved Reward Modeling | Alizée Pace | 2024 | [2401.12086](https://arxiv.org/abs/2401.12086) | The success of reinforcement learning from human feedback (RLHF) in language model alignment is strongly dependent on the quality of the underlying re | RLHF, RewardModel |
| 28 | Linear Alignment: A Closed-form Solution for Aligning Human Preferences
  without Tuning and Feedback | Songyang Gao | 2024 | [2401.11458](https://arxiv.org/abs/2401.11458) | The success of AI assistants based on Language Models (LLMs) hinges on Reinforcement Learning from Human Feedback (RLHF) to comprehend and align with | RLAIF, Eval |
| 29 | PokerGPT: An End-to-End Lightweight Solver for Multi-Player Texas
  Hold'em via Large Language Model | Chenghao Huang | 2024 | [2401.06781](https://arxiv.org/abs/2401.06781) | Poker, also known as Texas Hold'em, has always been a typical research target within imperfect information games (IIGs). IIGs have long served as a me | RLHF |
| 30 | Aligning Large Language Models with Human Preferences through
  Representation Engineering | Wenhao Liu | 2023 | [2312.15997](https://arxiv.org/abs/2312.15997) | Aligning large language models (LLMs) with human preferences is crucial for enhancing their utility in terms of helpfulness, truthfulness, safety, har | RLAIF |
| 31 | Iterative Preference Learning from Human Feedback: Bridging Theory and
  Practice for RLHF under KL-Constraint | Wei Xiong | 2023 | [2312.11456](https://arxiv.org/abs/2312.11456) | This paper studies the theoretical framework of the alignment process of generative models with Reinforcement Learning from Human Feedback (RLHF). We | DPO_variants |
| 32 | Data-Efficient Alignment of Large Language Models with Human Feedback
  Through Natural Language | Di Jin | 2023 | [2311.14543](https://arxiv.org/abs/2311.14543) | Learning from human feedback is a prominent technique to align the output of large language models (LLMs) with human expectations. Reinforcement learn | RLHF |
| 33 | On the Exploitability of Reinforcement Learning with Human Feedback for
  Large Language Models | Jiongxiao Wang | 2023 | [2311.09641](https://arxiv.org/abs/2311.09641) | Reinforcement Learning with Human Feedback (RLHF) is a methodology designed to align Large Language Models (LLMs) with human preferences, playing an i | RLHF |
| 34 | AI Alignment: A Comprehensive Survey | Jiaming Ji | 2023 | [2310.19852](https://arxiv.org/abs/2310.19852) | AI alignment aims to make AI systems behave in line with human intentions and values. As AI systems grow more capable, so do risks from misalignment. | RLAIF |
| 35 | BabyStories: Can Reinforcement Learning Teach Baby Language Models to
  Write Better Stories? | Xingmeng Zhao | 2023 | [2310.16681](https://arxiv.org/abs/2310.16681) | Language models have seen significant growth in the size of their corpus, leading to notable performance improvements. Yet, there has been limited pro | RLHF |
| 36 | AI Alignment and Social Choice: Fundamental Limitations and Policy
  Implications | Abhilash Mishra | 2023 | [2310.16048](https://arxiv.org/abs/2310.16048) | Aligning AI agents to human intentions and values is a key bottleneck in building safe and deployable AI applications. But whose values should AI agen | RLAIF |
| 37 | Beyond One-Preference-Fits-All Alignment: Multi-Objective Direct
  Preference Optimization | Zhanhui Zhou | 2023 | [2310.03708](https://arxiv.org/abs/2310.03708) | A single language model (LM), despite aligning well with an average labeler through reinforcement learning from human feedback (RLHF), may not univers | RLHF, DPO_variants |
| 38 | UltraFeedback: Boosting Language Models with High-quality Feedback | Ganqu Cui | 2023 | [2310.01377](https://arxiv.org/abs/2310.01377) | Reinforcement learning from human feedback (RLHF) has become a pivot technique in aligning large language models (LLMs) with human preferences. In RLH | RLHF |
| 39 | RLAIF: Scaling Reinforcement Learning from Human Feedback with AI
  Feedback | Harrison Lee | 2023 | [2309.00267](https://arxiv.org/abs/2309.00267) | Reinforcement learning from human feedback (RLHF) is effective at aligning large language models (LLMs) to human preferences, but gathering high quali | RLAIF |
| 40 | Aligning Language Models with Offline Reinforcement Learning from Human
  Feedback | Jian Hu | 2023 | [2308.12050](https://arxiv.org/abs/2308.12050) | Learning from human preferences is crucial for language models (LMs) to effectively cater to human needs and societal values. Previous research has ma | RLHF |
| 41 | Fine-Grained Human Feedback Gives Better Rewards for Language Model
  Training | Zeqiu Wu | 2023 | [2306.01693](https://arxiv.org/abs/2306.01693) | Language models (LMs) often exhibit undesirable text generation behaviors, including generating false, toxic, or irrelevant outputs. Reinforcement lea | RLHF |
| 42 | Training a Helpful and Harmless Assistant with Reinforcement Learning
  from Human Feedback | Yuntao Bai | 2022 | [2204.05862](https://arxiv.org/abs/2204.05862) | We apply preference modeling and reinforcement learning from human feedback (RLHF) to finetune language models to act as helpful and harmless assistan | RLHF |

### Q4: DPO 及变体
> 直接偏好优化的方法族：DPO、KTO、ORPO、SimPO、CPO、IPO 等

**论文数**: 80 篇

| # | 论文标题 | 第一作者 | 年份 | arXiv ID | 核心贡献摘要 | 标签 |
|---|----------|----------|------|----------|-------------|------|
| 1 | BiasGRPO: Stabilizing Bias Mitigation in High-Variance Reward Landscapes via Group-Relative Policy Optimization | Saket Reddy | 2026 | [2606.04807](https://arxiv.org/abs/2606.04807) | Mitigating social bias in Large Language Models (LLMs) presents a distinct alignment challenge: unlike verifiable tasks, bias lacks a single ground tr | GRPO |
| 2 | AutoRubric-T2I: Robust Rule-Based Reward Model for Text-to-Image Alignment | Kuei-Chun Kao | 2026 | [2605.17602](https://arxiv.org/abs/2605.17602) | Aligning Text-to-Image (T2I) generation models with human preferences increasingly relies on image reward models that score or rank generated images a | RewardModel |
| 3 | Conditional Equivalence of DPO and RLHF: Implicit Assumption, Failure Modes, and Provable Alignment | Zhiqin Yang | 2026 | [2605.20834](https://arxiv.org/abs/2605.20834) | Direct Preference Optimization (DPO) has emerged as a popular alternative to Reinforcement Learning from Human Feedback (RLHF), offering theoretical e | DPO_variants |
| 4 | Mechanistic Analysis of Alignment Algorithms in Language Models | Aarush Sinha | 2026 | [2606.09850](https://arxiv.org/abs/2606.09850) | Post-training alignment algorithms are predominantly evaluated as black boxes, obscuring how they reshape language models' internal computations. We p | PrefOpt, DPO_variants |
| 5 | EditCaption: Human-Aligned Instruction Synthesis for Image Editing via Supervised Fine-Tuning and Direct Preference Opti | Xiangyuan Wang | 2026 | [2604.08213](https://arxiv.org/abs/2604.08213) | High-quality training triplets (source-target image pairs with precise editing instructions) are a critical bottleneck for scaling instruction-guided | SFT |
| 6 | Unifying Group-Relative and Self-Distillation Policy Optimization via Sample Routing | Gengsheng Li | 2026 | [2604.02288](https://arxiv.org/abs/2604.02288) | Reinforcement learning with verifiable rewards (RLVR) has become a standard paradigm for post-training large language models. While Group Relative Pol | GRPO |
| 7 | Aligning Multimodal Sequential Recommendations via Robust Direct Preference Optimization with Sparse MoE | Hejin Huang | 2026 | [2603.29259](https://arxiv.org/abs/2603.29259) | Preference-based alignment objectives have been widely adopted, from RLHF-style pairwise learning in large language models to emerging applications in | DPO_variants |
| 8 | Uni-DPO: A Unified Paradigm for Dynamic Preference Optimization of LLMs | Shangpin Peng | 2026 | [2506.10054](https://arxiv.org/abs/2506.10054) | Direct Preference Optimization (DPO) has emerged as a cornerstone of reinforcement learning from human feedback (RLHF) due to its simplicity and effic | DPO_variants |
| 9 | GOPO: Policy Optimization using Ranked Rewards | Kyuseong Choi | 2026 | [2602.03876](https://arxiv.org/abs/2602.03876) | Standard reinforcement learning from human feedback (RLHF) trains a reward model on pairwise preference data and then uses it for policy optimization. | DPO_variants |
| 10 | Latent Adversarial Regularization for Offline Preference Optimization | Enyi Jiang | 2026 | [2601.22083](https://arxiv.org/abs/2601.22083) | Learning from human feedback typically relies on preference optimization that constrains policy updates through token-level regularization. However, p | PrefOpt |
| 11 | CAPO: Confidence Aware Preference Optimization Learning for Multilingual Preferences | Rhitabrat Pokharel | 2025 | [2511.07691](https://arxiv.org/abs/2511.07691) | Preference optimization is a critical post-training technique used to align large language models (LLMs) with human preferences, typically by fine-tun | DPO_variants |
| 12 | Aligning Diffusion Language Models via Unpaired Preference Optimization | Vaibhav Jindal | 2025 | [2510.23658](https://arxiv.org/abs/2510.23658) | Diffusion language models (dLLMs) are an emerging alternative to autoregressive (AR) generators, but aligning them to human preferences is challenging | DPO_variants |
| 13 | ORPO-Distill: Mixed-Policy Preference Optimization for Cross-Architecture LLM Distillation | Aasheesh Singh | 2025 | [2509.25100](https://arxiv.org/abs/2509.25100) | We introduce ORPO-Distill, a general-purpose method for cross-architecture LLM distillation that formulates the problem as a preference optimization t | DPO_variants |
| 14 | PromptCoT 2.0: Scaling Prompt Synthesis for Large Language Model
  Reasoning | Xueliang Zhao | 2025 | [2509.19894](https://arxiv.org/abs/2509.19894) | Large language models (LLMs) are evolving from conversational systems into strong reasoners for tasks such as Olympiad mathematics and competitive pro | SFT |
| 15 | Adaptive Preference Optimization with Uncertainty-aware Utility Anchor | Xiaobo Wang | 2025 | [2509.10515](https://arxiv.org/abs/2509.10515) | Offline preference optimization methods are efficient for large language models (LLMs) alignment. Direct Preference optimization (DPO)-like learning, | DPO_variants |
| 16 | Sem-DPO: Mitigating Semantic Inconsistency in Preference Optimization
  for Prompt Engineering | Anas Mohamed | 2025 | [2507.20133](https://arxiv.org/abs/2507.20133) | Generative AI can now synthesize strikingly realistic images from text, yet output quality remains highly sensitive to how prompts are phrased. Direct | PrefOpt |
| 17 | MaPPO: Maximum a Posteriori Preference Optimization with Prior Knowledge | Guangchen Lan | 2025 | [2507.21183](https://arxiv.org/abs/2507.21183) | As the era of large language models (LLMs) on behalf of users unfolds, Preference Optimization (PO) methods have become a central approach to aligning | DPO_variants |
| 18 | Implicit Reward as the Bridge: A Unified View of SFT and DPO Connections | Bo Wang | 2025 | [2507.00018](https://arxiv.org/abs/2507.00018) | Post-training processes are essential phases in grounding pre-trained language models to real-world tasks, with learning from demonstrations or prefer | SFT |
| 19 | Smoothed Preference Optimization via ReNoise Inversion for Aligning
  Diffusion Models with Varied Human Preferences | Yunhong Lu | 2025 | [2506.02698](https://arxiv.org/abs/2506.02698) | Direct Preference Optimization (DPO) aligns text-to-image (T2I) generation models with human preferences using pairwise preference data. Although subs | DPO_variants |
| 20 | LLaDA 1.5: Variance-Reduced Preference Optimization for Large Language
  Diffusion Models | Fengqi Zhu | 2025 | [2505.19223](https://arxiv.org/abs/2505.19223) | While Masked Diffusion Models (MDMs), such as LLaDA, present a promising paradigm for language modeling, there has been relatively little effort in al | PrefOpt |
| 21 | InfiFPO: Implicit Model Fusion via Preference Optimization in Large
  Language Models | Yanggan Gu | 2025 | [2505.13878](https://arxiv.org/abs/2505.13878) | Model fusion combines multiple Large Language Models (LLMs) with different strengths into a more powerful, integrated model through lightweight traini | PrefOpt |
| 22 | SGDPO: Self-Guided Direct Preference Optimization for Language Model
  Alignment | Wenqiao Zhu | 2025 | [2505.12435](https://arxiv.org/abs/2505.12435) | Direct Preference Optimization (DPO) is broadly utilized for aligning Large Language Models (LLMs) with human values because of its flexibility. Despi | PrefOpt |
| 23 | Pre-DPO: Improving Data Utilization in Direct Preference Optimization
  Using a Guiding Reference Model | Junshu Pan | 2025 | [2504.15843](https://arxiv.org/abs/2504.15843) | Direct Preference Optimization (DPO) simplifies reinforcement learning from human feedback (RLHF) for large language models (LLMs) by directly optimiz | DPO_variants |
| 24 | Enhancing LLM Reasoning with Iterative DPO: A Comprehensive Empirical
  Investigation | Songjun Tu | 2025 | [2503.12854](https://arxiv.org/abs/2503.12854) | Recent advancements in post-training methodologies for large language models (LLMs) have highlighted reinforcement learning (RL) as a critical compone | DPO_variants |
| 25 | AlignDistil: Token-Level Language Model Alignment as Adaptive Policy
  Distillation | Songming Zhang | 2025 | [2503.02832](https://arxiv.org/abs/2503.02832) | In modern large language models (LLMs), LLM alignment is of crucial importance and is typically achieved through methods such as reinforcement learnin | RewardModel |
| 26 | Active Learning for Direct Preference Optimization | Branislav Kveton | 2025 | [2503.01076](https://arxiv.org/abs/2503.01076) | Direct preference optimization (DPO) is a form of reinforcement learning from human feedback (RLHF) where the policy is learned directly from preferen | DPO_variants |
| 27 | AMPO: Active Multi-Preference Optimization | Taneesh Gupta | 2025 | [2502.18293](https://arxiv.org/abs/2502.18293) | Multi-preference optimization enriches language-model alignment beyond pairwise preferences by contrasting entire sets of helpful and undesired respon | PrefOpt |
| 28 | Less is More: Improving LLM Alignment via Preference Data Selection | Xun Deng | 2025 | [2502.14560](https://arxiv.org/abs/2502.14560) | Direct Preference Optimization (DPO) has emerged as a promising approach for aligning large language models with human preferences. While prior work m | DPO_variants |
| 29 | Safe at the Margins: A General Approach to Safety Alignment in
  Low-Resource English Languages -- A Singlish Case Study | Isaac Lim | 2025 | [2502.12485](https://arxiv.org/abs/2502.12485) | To ensure safe usage, Large Language Models (LLMs) typically undergo alignment with human-defined values. However, this alignment often relies on prim | DPO_variants |
| 30 | Uncovering the Impact of Chain-of-Thought Reasoning for Direct
  Preference Optimization: Lessons from Text-to-SQL | Hanbing Liu | 2025 | [2502.11656](https://arxiv.org/abs/2502.11656) | Direct Preference Optimization (DPO) has proven effective in complex reasoning tasks like math word problems and code generation. However, when applie | DPO |
| 31 | DPO-Shift: Shifting the Distribution of Direct Preference Optimization | Xiliang Yang | 2025 | [2502.07599](https://arxiv.org/abs/2502.07599) | Direct Preference Optimization (DPO) and its variants have become increasingly popular for aligning language models with human preferences. These meth | DPO |
| 32 | Preference Optimization via Contrastive Divergence: Your Reward Model is Secretly an NLL Estimator | Zhuotong Chen | 2025 | [2502.04567](https://arxiv.org/abs/2502.04567) | Existing studies on preference optimization (PO) have centered on constructing pairwise preference data following simple heuristics, such as maximizin | DPO_variants |
| 33 | SimulPL: Aligning Human Preferences in Simultaneous Machine Translation | Donglei Yu | 2025 | [2502.00634](https://arxiv.org/abs/2502.00634) | Simultaneous Machine Translation (SiMT) generates translations while receiving streaming source inputs. This requires the SiMT model to learn a read/w | DPO_variants |
| 34 | Reward-aware Preference Optimization: A Unified Mathematical Framework
  for Model Alignment | Shengyang Sun | 2025 | [2502.00203](https://arxiv.org/abs/2502.00203) | The rapid development of large language model (LLM) alignment algorithms has resulted in a complex and fragmented landscape, with limited clarity on t | RewardModel |
| 35 | AlphaPO -- Reward shape matters for LLM alignment | Aman Gupta | 2025 | [2501.03884](https://arxiv.org/abs/2501.03884) | Reinforcement Learning with Human Feedback (RLHF) and its variants have made huge strides toward the effective alignment of large language models (LLM | DPO_variants |
| 36 | DPO Kernels: A Semantically-Aware, Kernel-Enhanced, and Divergence-Rich
  Paradigm for Direct Preference Optimization | Amitava Das | 2025 | [2501.03271](https://arxiv.org/abs/2501.03271) | The rapid rise of large language models (LLMs) has unlocked many applications but also underscores the challenge of aligning them with diverse values | DPO |
| 37 | SDPO: Segment-Level Direct Preference Optimization for Social Agents | Aobo Kong | 2025 | [2501.01821](https://arxiv.org/abs/2501.01821) | Social agents powered by large language models (LLMs) can simulate human social behaviors but fall short in handling complex goal-oriented social dial | DPO |
| 38 | Preference Optimization for Reasoning with Pseudo Feedback | Fangkai Jiao | 2024 | [2411.16345](https://arxiv.org/abs/2411.16345) | Preference optimization techniques, such as Direct Preference Optimization (DPO), are frequently employed to enhance the reasoning capabilities of lar | PrefOpt, DPO_variants |
| 39 | Direct Preference Optimization Using Sparse Feature-Level Constraints | Qingyu Yin | 2024 | [2411.07618](https://arxiv.org/abs/2411.07618) | The alignment of large language models (LLMs) with human preferences remains a key challenge. While post-training techniques like Reinforcement Learni | DPO |
| 40 | Entropy Controllable Direct Preference Optimization | Motoki Omura | 2024 | [2411.07595](https://arxiv.org/abs/2411.07595) | In the post-training of large language models (LLMs), Reinforcement Learning from Human Feedback (RLHF) is an effective approach to achieve generation | DPO |
| 41 | Varco Arena: A Tournament Approach to Reference-Free Benchmarking Large
  Language Models | Seonil Son | 2024 | [2411.01281](https://arxiv.org/abs/2411.01281) | The rapid advancement of Large Language Models (LLMs) necessitates robust evaluation methodologies. Current benchmarking approaches often rely on comp | Eval |
| 42 | A Comprehensive Survey of Direct Preference Optimization: Datasets,
  Theories, Variants, and Applications | Wenyi Xiao | 2024 | [2410.15595](https://arxiv.org/abs/2410.15595) | With the rapid advancement of large language models (LLMs), aligning policy models with human preferences has become increasingly critical. Direct Pre | DPO |
| 43 | Unintentional Unalignment: Likelihood Displacement in Direct Preference
  Optimization | Noam Razin | 2024 | [2410.08847](https://arxiv.org/abs/2410.08847) | Direct Preference Optimization (DPO) and its variants are increasingly used for aligning language models with human preferences. Although these method | DPO |
| 44 | PLaMo-100B: A Ground-Up Language Model Designed for Japanese Proficiency | Kenshin Abe | 2024 | [2410.07563](https://arxiv.org/abs/2410.07563) | We introduce PLaMo-100B, a large-scale language model designed for Japanese proficiency. The model was trained from scratch using 2 trillion tokens, w | SFT |
| 45 | Accelerated Preference Optimization for Large Language Model Alignment | Jiafan He | 2024 | [2410.06293](https://arxiv.org/abs/2410.06293) | Reinforcement Learning from Human Feedback (RLHF) has emerged as a pivotal tool for aligning large language models (LLMs) with human preferences. Dire | PrefOpt, DPO_variants |
| 46 | Self-supervised Preference Optimization: Enhance Your Language Model
  with Preference Degree Awareness | Jian Li | 2024 | [2409.17791](https://arxiv.org/abs/2409.17791) | Recently, there has been significant interest in replacing the reward model in Reinforcement Learning with Human Feedback (RLHF) methods for Large Lan | PrefOpt |
| 47 | Modulated Intervention Preference Optimization (MIPO): Keep the Easy,
  Refine the Difficult | Cheolhun Jang | 2024 | [2409.17545](https://arxiv.org/abs/2409.17545) | Preference optimization methods typically begin training with a well-trained SFT model as a reference model. In RLHF and DPO, a regularization term is | Eval |
| 48 | Building Math Agents with Multi-Turn Iterative Preference Learning | Wei Xiong | 2024 | [2409.02392](https://arxiv.org/abs/2409.02392) | Recent studies have shown that large language models' (LLMs) mathematical problem-solving capabilities can be enhanced by integrating external tools, | DPO_variants |
| 49 | Bridging and Modeling Correlations in Pairwise Data for Direct
  Preference Optimization | Yuxin Jiang | 2024 | [2408.07471](https://arxiv.org/abs/2408.07471) | Direct preference optimization (DPO), a widely adopted offline preference optimization algorithm, aims to align large language models (LLMs) with huma | DPO |
| 50 | Understanding Reference Policies in Direct Preference Optimization | Yixin Liu | 2024 | [2407.13709](https://arxiv.org/abs/2407.13709) | Direct Preference Optimization (DPO) has become a widely used training method for the instruction fine-tuning of large language models (LLMs). In this | DPO |
| 51 | β-DPO: Direct Preference Optimization with Dynamic β | Junkang Wu | 2024 | [2407.08639](https://arxiv.org/abs/2407.08639) | Direct Preference Optimization (DPO) has emerged as a compelling approach for training Large Language Models (LLMs) to adhere to human preferences. Ho | DPO |
| 52 | EmPO: Emotion Grounding for Empathetic Response Generation through
  Preference Optimization | Ondrej Sotolar | 2024 | [2406.19071](https://arxiv.org/abs/2406.19071) | Empathetic response generation is a desirable aspect of conversational agents, crucial for facilitating engaging and emotionally intelligent multi-tur | PrefOpt |
| 53 | Not All Preference Pairs Are Created Equal: A Recipe for
  Annotation-Efficient Iterative Preference Learning | Sen Yang | 2024 | [2406.17312](https://arxiv.org/abs/2406.17312) | Iterative preference learning, though yielding superior performances, requires online annotated preference labels. In this work, we study strategies t | DPO_variants |
| 54 | Direct Multi-Turn Preference Optimization for Language Agents | Wentao Shi | 2024 | [2406.14868](https://arxiv.org/abs/2406.14868) | Adapting Large Language Models (LLMs) for agent tasks is critical in developing language agents. Direct Preference Optimization (DPO) is a promising t | DPO, PrefOpt |
| 55 | Iterative Length-Regularized Direct Preference Optimization: A Case
  Study on Improving 7B Language Models to GPT-4 Lev | Jie Liu | 2024 | [2406.11817](https://arxiv.org/abs/2406.11817) | Direct Preference Optimization (DPO), a standard method for aligning language models with human preferences, is traditionally applied to offline prefe | DPO, DPO_variants |
| 56 | Eliminating Biased Length Reliance of Direct Preference Optimization via
  Down-Sampled KL Divergence | Junru Lu | 2024 | [2406.10957](https://arxiv.org/abs/2406.10957) | Direct Preference Optimization (DPO) has emerged as a prominent algorithm for the direct and robust alignment of Large Language Models (LLMs) with hum | DPO |
| 57 | Step-level Value Preference Optimization for Mathematical Reasoning | Guoxin Chen | 2024 | [2406.10858](https://arxiv.org/abs/2406.10858) | Direct Preference Optimization (DPO) using an implicit reward model has proven to be an effective alternative to reinforcement learning from human fee | DPO_variants |
| 58 | Direct Preference Optimization for Suppressing Hallucinated Prior Exams
  in Radiology Report Generation | Oishi Banerjee | 2024 | [2406.06496](https://arxiv.org/abs/2406.06496) | Recent advances in generative vision-language models (VLMs) have exciting potential implications for AI in radiology, yet VLMs are also known to produ | DPO |
| 59 | Online DPO: Online Direct Preference Optimization with Fast-Slow Chasing | Biqing Qi | 2024 | [2406.05534](https://arxiv.org/abs/2406.05534) | Direct Preference Optimization (DPO) improves the alignment of large language models (LLMs) with human values by training directly on human preference | DPO |
| 60 | Self-Exploring Language Models: Active Preference Elicitation for Online
  Alignment | Shenao Zhang | 2024 | [2405.19332](https://arxiv.org/abs/2405.19332) | Preference optimization, particularly through Reinforcement Learning from Human Feedback (RLHF), has achieved significant success in aligning Large La | PrefOpt |
| 61 | Multi-Reference Preference Optimization for Large Language Models | Hung Le | 2024 | [2405.16388](https://arxiv.org/abs/2405.16388) | How can Large Language Models (LLMs) be aligned with human intentions and values? A typical solution is to gather human preference on model outputs an | PrefOpt |
| 62 | SimPO: Simple Preference Optimization with a Reference-Free Reward | Yu Meng | 2024 | [2405.14734](https://arxiv.org/abs/2405.14734) | Direct Preference Optimization (DPO) is a widely used offline preference optimization algorithm that reparameterizes reward functions in reinforcement | DPO_variants |
| 63 | Annotation-Efficient Preference Optimization for Language Model
  Alignment | Yuu Jinnai | 2024 | [2405.13541](https://arxiv.org/abs/2405.13541) | Preference optimization is a standard approach to fine-tuning large language models to align with human preferences. The quality, diversity, and quant | PrefOpt |
| 64 | Self-Play Preference Optimization for Language Model Alignment | Yue Wu | 2024 | [2405.00675](https://arxiv.org/abs/2405.00675) | Traditional reinforcement learning from human feedback (RLHF) approaches relying on parametric models like the Bradley-Terry model fall short in captu | PrefOpt |
| 65 | Iterative Reasoning Preference Optimization | Richard Yuanzhe Pang | 2024 | [2404.19733](https://arxiv.org/abs/2404.19733) | Iterative preference optimization methods have recently been shown to perform well for general instruction tuning tasks, but typically make little imp | DPO_variants |
| 66 | Binary Classifier Optimization for Large Language Model Alignment | Seungjae Jung | 2024 | [2404.04656](https://arxiv.org/abs/2404.04656) | Aligning Large Language Models (LLMs) to human preferences through preference optimization has been crucial but labor-intensive, necessitating for eac | PrefOpt |
| 67 | Direct Preference Optimization of Video Large Multimodal Models from
  Language Model Reward | Ruohong Zhang | 2024 | [2404.01258](https://arxiv.org/abs/2404.01258) | Preference modeling techniques, such as direct preference optimization (DPO), has shown effective in enhancing the generalization abilities of large l | DPO |
| 68 | Configurable Safety Tuning of Language Models with Synthetic Preference
  Data | Victor Gallego | 2024 | [2404.00495](https://arxiv.org/abs/2404.00495) | State-of-the-art language model fine-tuning techniques, such as Direct Preference Optimization (DPO), restrict user control by hard-coding predefined | PrefOpt |
| 69 | ORPO: Monolithic Preference Optimization without Reference Model | Jiwoo Hong | 2024 | [2403.07691](https://arxiv.org/abs/2403.07691) | While recent preference alignment algorithms for language models have demonstrated promising results, supervised fine-tuning (SFT) remains imperative | DPO_variants |
| 70 | Curry-DPO: Enhancing Alignment using Curriculum Learning & Ranked
  Preferences | Pulkit Pattnaik | 2024 | [2403.07230](https://arxiv.org/abs/2403.07230) | Direct Preference Optimization (DPO) is an effective technique that leverages pairwise preference data (usually one chosen and rejected response pair | DPO_variants |
| 71 | Learning to Use Tools via Cooperative and Interactive Agents | Zhengliang Shi | 2024 | [2403.03031](https://arxiv.org/abs/2403.03031) | Tool learning empowers large language models (LLMs) as agents to use external tools to extend their capability. Existing methods employ one single LLM | AgentRL |
| 72 | Direct Preference Optimization with an Offset | Afra Amini | 2024 | [2402.10571](https://arxiv.org/abs/2402.10571) | Direct preference optimization (DPO) is a successful fine-tuning strategy for aligning large language models with human preferences without the need t | DPO, DPO_variants |
| 73 | Direct Language Model Alignment from Online AI Feedback | Shangmin Guo | 2024 | [2402.04792](https://arxiv.org/abs/2402.04792) | Direct alignment from preferences (DAP) methods, such as DPO, have recently emerged as efficient alternatives to reinforcement learning from human fee | RewardModel |
| 74 | KTO: Model Alignment as Prospect Theoretic Optimization | Kawin Ethayarajh | 2024 | [2402.01306](https://arxiv.org/abs/2402.01306) | Kahneman & Tversky's prospect theory tells us that humans perceive random variables in a biased but well-defined manner; for example, humans are famou | DPO_variants |
| 75 | Towards Efficient and Exact Optimization of Language Model Alignment | Haozhe Ji | 2024 | [2402.00856](https://arxiv.org/abs/2402.00856) | The alignment of language models with human preferences is vital for their application in real-world tasks. The problem is formulated as optimizing th | PrefOpt, RewardModel |
| 76 | Iterative Preference Learning from Human Feedback: Bridging Theory and
  Practice for RLHF under KL-Constraint | Wei Xiong | 2023 | [2312.11456](https://arxiv.org/abs/2312.11456) | This paper studies the theoretical framework of the alignment process of generative models with Reinforcement Learning from Human Feedback (RLHF). We | DPO_variants |
| 77 | Beyond One-Preference-Fits-All Alignment: Multi-Objective Direct
  Preference Optimization | Zhanhui Zhou | 2023 | [2310.03708](https://arxiv.org/abs/2310.03708) | A single language model (LM), despite aligning well with an average labeler through reinforcement learning from human feedback (RLHF), may not univers | RLHF, DPO_variants |
| 78 | Beyond Reverse KL: Generalizing Direct Preference Optimization with
  Diverse Divergence Constraints | Chaoqi Wang | 2023 | [2309.16240](https://arxiv.org/abs/2309.16240) | The increasing capabilities of large language models (LLMs) raise opportunities for artificial general intelligence but concurrently amplify safety co | DPO |
| 79 | Aligning Large Language Models with Human: A Survey | Yufei Wang | 2023 | [2307.12966](https://arxiv.org/abs/2307.12966) | Large Language Models (LLMs) trained on extensive textual corpora have emerged as leading solutions for a broad array of Natural Language Processing ( | Eval |
| 80 | Direct Preference Optimization: Your Language Model is Secretly a Reward
  Model | Rafael Rafailov | 2023 | [2305.18290](https://arxiv.org/abs/2305.18290) | While large-scale unsupervised language models (LMs) learn broad world knowledge and some reasoning skills, achieving precise control of their behavio | DPO, PrefOpt |

### Q5: GRPO 及 Group-wise 方法
> 基于组相对策略优化的方法，包括与 PPO 的对比

**论文数**: 31 篇

| # | 论文标题 | 第一作者 | 年份 | arXiv ID | 核心贡献摘要 | 标签 |
|---|----------|----------|------|----------|-------------|------|
| 1 | BiasGRPO: Stabilizing Bias Mitigation in High-Variance Reward Landscapes via Group-Relative Policy Optimization | Saket Reddy | 2026 | [2606.04807](https://arxiv.org/abs/2606.04807) | Mitigating social bias in Large Language Models (LLMs) presents a distinct alignment challenge: unlike verifiable tasks, bias lacks a single ground tr | GRPO |
| 2 | Mechanistic Analysis of Alignment Algorithms in Language Models | Aarush Sinha | 2026 | [2606.09850](https://arxiv.org/abs/2606.09850) | Post-training alignment algorithms are predominantly evaluated as black boxes, obscuring how they reshape language models' internal computations. We p | PrefOpt, DPO_variants |
| 3 | Latent-GRPO: Group Relative Policy Optimization for Latent Reasoning | Jingcheng Deng | 2026 | [2604.27998](https://arxiv.org/abs/2604.27998) | Latent reasoning offers a more efficient alternative to explicit reasoning by compressing intermediate reasoning into continuous representations and s | GRPO |
| 4 | GRPO-VPS: Enhancing Group Relative Policy Optimization with Verifiable Process Supervision for Effective Reasoning | Jingyi Wang | 2026 | [2604.20659](https://arxiv.org/abs/2604.20659) | Reinforcement Learning with Verifiable Rewards (RLVR) has advanced the reasoning capabilities of Large Language Models (LLMs) by leveraging direct out | GRPO |
| 5 | Unifying Group-Relative and Self-Distillation Policy Optimization via Sample Routing | Gengsheng Li | 2026 | [2604.02288](https://arxiv.org/abs/2604.02288) | Reinforcement learning with verifiable rewards (RLVR) has become a standard paradigm for post-training large language models. While Group Relative Pol | GRPO |
| 6 | Stabilizing Rubric Integration Training via Decoupled Advantage Normalization | Zelin Tan | 2026 | [2603.26535](https://arxiv.org/abs/2603.26535) | We propose Process-Aware Policy Optimization (PAPO), a method that integrates process-level evaluation into Group Relative Policy Optimization (GRPO) | RewardModel |
| 7 | Towards Unified Multimodal Interleaved Generation via Group Relative Policy Optimization | Ming Nie | 2026 | [2603.09538](https://arxiv.org/abs/2603.09538) | Unified vision-language models have made significant progress in multimodal understanding and generation, yet they largely fall short in producing mul | GRPO |
| 8 | Demystifying Group Relative Policy Optimization: Its Policy Gradient is a U-Statistic | Hongyi Zhou | 2026 | [2603.01162](https://arxiv.org/abs/2603.01162) | Group relative policy optimization (GRPO), a core methodological component of DeepSeekMath and DeepSeek-R1, has emerged as a cornerstone for scaling r | GRPO |
| 9 | EBPO: Empirical Bayes Shrinkage for Stabilizing Group-Relative Policy Optimization | Kevin Han | 2026 | [2602.05165](https://arxiv.org/abs/2602.05165) | Reinforcement Learning with Verifiable Rewards (RLVR) has proven effective for enhancing the reasoning capabilities of Large Language Models (LLMs). H | GRPO |
| 10 | Information-Consistent Language Model Recommendations through Group Relative Policy Optimization | Sonal Prabhune | 2025 | [2512.12858](https://arxiv.org/abs/2512.12858) | Large Language Models (LLMs) are increasingly deployed in business-critical domains such as finance, education, healthcare, and customer support, wher | GRPO |
| 11 | DaGRPO: Rectifying Gradient Conflict in Reasoning via Distinctiveness-Aware Group Relative Policy Optimization | Xuan Xie | 2025 | [2512.06337](https://arxiv.org/abs/2512.06337) | The evolution of Large Language Models (LLMs) has catalyzed a paradigm shift from superficial instruction following to rigorous long-horizon reasoning | GRPO |
| 12 | SR-GRPO: Stable Rank as an Intrinsic Geometric Reward for Large Language Model Alignment | Yixuan Tang | 2025 | [2512.02807](https://arxiv.org/abs/2512.02807) | Aligning Large Language Models (LLMs) with human preferences typically relies on external supervision, which faces critical limitations: human annotat | RewardModel |
| 13 | Real-Time Long Horizon Air Quality Forecasting via Group-Relative Policy Optimization | Inha Kang | 2025 | [2511.22169](https://arxiv.org/abs/2511.22169) | Accurate long horizon forecasting of particulate matter (PM) concentration fields is essential for operational public health decisions. However, achie | GRPO |
| 14 | Sharpness-Guided Group Relative Policy Optimization via Probability Shaping | Tue Le | 2025 | [2511.00066](https://arxiv.org/abs/2511.00066) | Reinforcement learning with verifiable rewards (RLVR) has become a practical route to improve large language model reasoning, and Group Relative Polic | GRPO |
| 15 | Training-Free Group Relative Policy Optimization | Yuzheng Cai | 2025 | [2510.08191](https://arxiv.org/abs/2510.08191) | Recent advances in Large Language Model (LLM) agents have demonstrated their promising general capabilities. However, their performance in specialized | GRPO |
| 16 | Group-Relative REINFORCE Is Secretly an Off-Policy Algorithm:
  Demystifying Some Myths About GRPO and Its Friends | Chaorui Yao | 2025 | [2509.24203](https://arxiv.org/abs/2509.24203) | Off-policy reinforcement learning (RL) for large language models (LLMs) is attracting growing interest, driven by practical constraints in real-world | GRPO |
| 17 | GRPO-MA: Multi-Answer Generation in GRPO for Stable and Efficient
  Chain-of-Thought Training | Hongcheng Wang | 2025 | [2509.24494](https://arxiv.org/abs/2509.24494) | Recent progress, such as DeepSeek-R1, has shown that the GRPO algorithm, a Reinforcement Learning (RL) approach, can effectively train Chain-of-Though | AgentRL |
| 18 | MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems | Yuki Ichihara | 2025 | [2509.22047](https://arxiv.org/abs/2509.22047) | Group Relative Policy Optimization (GRPO) has been shown to be an effective algorithm when an accurate reward model is available. However, such a high | GRPO |
| 19 | ArGen: Auto-Regulation of Generative AI via GRPO and Policy-as-Code | Kapil Madan | 2025 | [2509.07006](https://arxiv.org/abs/2509.07006) | This paper introduces ArGen (Auto-Regulation of Generative AI systems), a framework for aligning Large Language Models (LLMs) with complex sets of con | RLAIF |
| 20 | Group Relative Policy Optimization for Speech Recognition | Prashanth Gurunath Shivakumar | 2025 | [2509.01939](https://arxiv.org/abs/2509.01939) | Speech Recognition has seen a dramatic shift towards adopting Large Language Models (LLMs). This shift is partly driven by good scalability properties | GRPO |
| 21 | Can Group Relative Policy Optimization Improve Thai Legal Reasoning and
  Question Answering? | Pawitsapak Akarajaradwong | 2025 | [2507.09638](https://arxiv.org/abs/2507.09638) | The Retrieval-Augmented Generation (RAG) systems' performance on Thai legal question answering is still limited, especially for questions requiring ex | GRPO |
| 22 | Fine-Tuning Next-Scale Visual Autoregressive Models with Group Relative
  Policy Optimization | Matteo Gallici | 2025 | [2505.23331](https://arxiv.org/abs/2505.23331) | Fine-tuning pre-trained generative models with Reinforcement Learning (RL) has emerged as an effective approach for aligning outputs more closely with | GRPO |
| 23 | DINO-R1: Incentivizing Reasoning Capability in Vision Foundation Models | Chenbin Pan | 2025 | [2505.24025](https://arxiv.org/abs/2505.24025) | The recent explosive interest in the reasoning capabilities of large language models, such as DeepSeek-R1, has demonstrated remarkable success through | AgentRL |
| 24 | Revisiting Group Relative Policy Optimization: Insights into On-Policy and Off-Policy Training | Youssef Mroueh | 2025 | [2505.22257](https://arxiv.org/abs/2505.22257) | We revisit Group Relative Policy Optimization (GRPO) in both on-policy and off-policy optimization regimes. Our motivation comes from recent work on o | GRPO |
| 25 | Stable Reinforcement Learning for Efficient Reasoning | Muzhi Dai | 2025 | [2505.18086](https://arxiv.org/abs/2505.18086) | The success of Deepseek-R1 has drawn the LLM community's attention to reinforcement learning (RL) methods like GRPO. However, such rule-based 0/1 outc | AgentRL |
| 26 | Visionary-R1: Mitigating Shortcuts in Visual Reasoning with
  Reinforcement Learning | Jiaer Xia | 2025 | [2505.14677](https://arxiv.org/abs/2505.14677) | Learning general-purpose reasoning capabilities has long been a challenging problem in AI. Recent research in large language models (LLMs), such as De | AgentRL |
| 27 | DisCO: Reinforcing Large Reasoning Models with Discriminative
  Constrained Optimization | Gang Li | 2025 | [2505.12366](https://arxiv.org/abs/2505.12366) | The recent success and openness of DeepSeek-R1 have brought widespread attention to Group Relative Policy Optimization (GRPO) as a reinforcement learn | AgentRL |
| 28 | S-GRPO: Early Exit via Reinforcement Learning in Reasoning Models | Muzhi Dai | 2025 | [2505.07686](https://arxiv.org/abs/2505.07686) | As Test-Time Scaling emerges as an active research focus in the large language model community, advanced post-training methods increasingly emphasize | AgentRL |
| 29 | SARI: Structured Audio Reasoning via Curriculum-Guided Reinforcement
  Learning | Cheng Wen | 2025 | [2504.15900](https://arxiv.org/abs/2504.15900) | Recent work shows that reinforcement learning(RL) can markedly sharpen the reasoning ability of large language models (LLMs) by prompting them to "thi | AgentRL |
| 30 | CPPO: Accelerating the Training of Group Relative Policy
  Optimization-Based Reasoning Models | Zhihang Lin | 2025 | [2503.22342](https://arxiv.org/abs/2503.22342) | This paper introduces Completion Pruning Policy Optimization (CPPO) to accelerate the training of reasoning models based on Group Relative Policy Opti | GRPO |
| 31 | VoiceGRPO: Modern MoE Transformers with Group Relative Policy
  Optimization GRPO for AI Voice Health Care Applications  | Enkhtogtokh Togootogtokh | 2025 | [2503.03797](https://arxiv.org/abs/2503.03797) | This research introduces a novel AI techniques as Mixture-of-Experts Transformers with Group Relative Policy Optimization (GRPO) for voice health care | GRPO |

### Q6: Agentic RL
> 用于 Agent 能力训练的 RL 方法：tool use、multi-step reasoning

**论文数**: 64 篇

| # | 论文标题 | 第一作者 | 年份 | arXiv ID | 核心贡献摘要 | 标签 |
|---|----------|----------|------|----------|-------------|------|
| 1 | On Effectiveness and Efficiency of Agentic Tool-calling and RL Training | Tong Liu | 2026 | [2606.00135](https://arxiv.org/abs/2606.00135) | Tool-calling is a central component of modern large language model (LLM) agents, equipping them with skills beyond their parametric knowledge. This pa | AgentRL |
| 2 | Hack-Verifiable Environments: Towards Evaluating Reward Hacking at Scale | Amit Roth | 2026 | [2605.20744](https://arxiv.org/abs/2605.20744) | Aligning autonomous agents with human intent remains a central challenge in modern AI. A key manifestation of this challenge is reward hacking, whereb | RewardModel |
| 3 | Exploration and Exploitation Errors Are Measurable for Language Model Agents | Jaden Park | 2026 | [2604.13151](https://arxiv.org/abs/2604.13151) | Language Model (LM) agents are increasingly used in complex open-ended decision-making tasks, from AI coding to physical AI. A core requirement in the | AgentRL |
| 4 | SLEA-RL: Step-Level Experience Augmented Reinforcement Learning for Multi-Turn Agentic Training | Prince Zizhuang Wang | 2026 | [2603.18079](https://arxiv.org/abs/2603.18079) | Large Language Model (LLM) agents have shown strong results on multi-turn tool-use tasks, yet they operate in isolation during training, failing to le | AgentRL |
| 5 | Tool-R0: Self-Evolving LLM Agents for Tool-Learning from Zero Data | Emre Can Acikgoz | 2026 | [2602.21320](https://arxiv.org/abs/2602.21320) | Large language models (LLMs) are becoming the foundation for autonomous agents that can use tools to solve complex tasks. Reinforcement learning (RL) | AgentRL |
| 6 | Gecko: A Simulation Environment with Stateful Feedback for Refining Agent Tool Calls | Zeyu Zhang | 2026 | [2602.19218](https://arxiv.org/abs/2602.19218) | The ability to use tools is fundamental for large language model (LLM) agents. Given a task, existing systems use LLMs to plan and generate tool calls | AgentRL |
| 7 | Evolving Interpretable Constitutions for Multi-Agent Coordination | Ujwal Kumar | 2026 | [2602.00755](https://arxiv.org/abs/2602.00755) | Constitutional AI has focused on single-model alignment using fixed principles. However, multi-agent systems create novel alignment challenges through | RLAIF |
| 8 | ASTRA: Automated Synthesis of agentic Trajectories and Reinforcement Arenas | Xiaoyu Tian | 2026 | [2601.21558](https://arxiv.org/abs/2601.21558) | Large language models (LLMs) are increasingly used as tool-augmented agents for multi-step decision making, yet training robust tool-using agents rema | AgentRL |
| 9 | From Passive Metric to Active Signal: The Evolving Role of Uncertainty Quantification in Large Language Models | Jiaxin Zhang | 2026 | [2601.15690](https://arxiv.org/abs/2601.15690) | While Large Language Models (LLMs) show remarkable capabilities, their unreliability remains a critical barrier to deployment in high-stakes domains. | AgentRL |
| 10 | Institutional AI: Governing LLM Collusion in Multi-Agent Cournot Markets via Public Governance Graphs | Marcantonio Bracale Syrnikov | 2026 | [2601.11369](https://arxiv.org/abs/2601.11369) | Multi-agent LLM ensembles can converge on coordinated, socially harmful equilibria. This paper advances an experimental framework for evaluating Insti | RLAIF |
| 11 | The Confidence Dichotomy: Analyzing and Mitigating Miscalibration in Tool-Use Agents | Weihao Xuan | 2026 | [2601.07264](https://arxiv.org/abs/2601.07264) | Autonomous agents based on large language models (LLMs) are rapidly evolving to handle multi-turn tasks, but ensuring their trustworthiness remains a | AgentRL |
| 12 | SCRIBE: Structured Mid-Level Supervision for Tool-Using Language Models | Yuxuan Jiang | 2026 | [2601.03555](https://arxiv.org/abs/2601.03555) | Training reliable tool-augmented agents remains a significant challenge, largely due to the difficulty of credit assignment in multi-step reasoning. W | AgentRL |
| 13 | Agent-R1: Training Powerful LLM Agents with End-to-End Reinforcement Learning | Mingyue Cheng | 2025 | [2511.14460](https://arxiv.org/abs/2511.14460) | Large Language Models (LLMs) are increasingly being explored for building Agents capable of active environmental interaction (e.g., via tool use) to s | AgentRL |
| 14 | TheMCPCompany: Creating General-purpose Agents with Task-specific Tools | Reza Esfandiarpoor | 2025 | [2510.19286](https://arxiv.org/abs/2510.19286) | Since the introduction of the Model Context Protocol (MCP), the number of available tools for Large Language Models (LLMs) has increased significantly | AgentRL |
| 15 | Information Gain-based Policy Optimization: A Simple and Effective
  Approach for Multi-Turn LLM Agents | Guoqing Wang | 2025 | [2510.14967](https://arxiv.org/abs/2510.14967) | Large language model (LLM)-based agents are increasingly trained with reinforcement learning (RL) to enhance their ability to interact with external e | AgentRL |
| 16 | Training-Free Group Relative Policy Optimization | Yuzheng Cai | 2025 | [2510.08191](https://arxiv.org/abs/2510.08191) | Recent advances in Large Language Model (LLM) agents have demonstrated their promising general capabilities. However, their performance in specialized | GRPO |
| 17 | Scaling LLM Multi-turn RL with End-to-end Summarization-based Context
  Management | Miao Lu | 2025 | [2510.06727](https://arxiv.org/abs/2510.06727) | We study reinforcement learning (RL) fine-tuning of large language model (LLM) agents for long-horizon multi-turn tool use, where context length quick | AgentRL |
| 18 | Multi-Agent Tool-Integrated Policy Optimization | Zhanfeng Mo | 2025 | [2510.04678](https://arxiv.org/abs/2510.04678) | Large language models (LLMs) increasingly rely on multi-turn tool-integrated planning for knowledge-intensive and complex reasoning tasks. Existing im | AgentRL |
| 19 | GRPO-MA: Multi-Answer Generation in GRPO for Stable and Efficient
  Chain-of-Thought Training | Hongcheng Wang | 2025 | [2509.24494](https://arxiv.org/abs/2509.24494) | Recent progress, such as DeepSeek-R1, has shown that the GRPO algorithm, a Reinforcement Learning (RL) approach, can effectively train Chain-of-Though | AgentRL |
| 20 | Process-Supervised Reinforcement Learning for Interactive Multimodal Tool-Use Agents | Weiting Tan | 2025 | [2509.14480](https://arxiv.org/abs/2509.14480) | Effective interactive tool use requires agents to master Tool Integrated Reasoning (TIR): a complex process involving multi-turn planning and long-con | AgentRL |
| 21 | Tool-R1: Sample-Efficient Reinforcement Learning for Agentic Tool Use | Yabo Zhang | 2025 | [2509.12867](https://arxiv.org/abs/2509.12867) | Large language models (LLMs) have demonstrated strong capabilities in language understanding and reasoning, yet they remain limited when tackling real | AgentRL |
| 22 | SFR-DeepResearch: Towards Effective Reinforcement Learning for
  Autonomously Reasoning Single Agents | Xuan-Phi Nguyen | 2025 | [2509.06283](https://arxiv.org/abs/2509.06283) | Equipping large language models (LLMs) with complex, interleaved reasoning and tool-use capabilities has become a key focus in agentic AI research, es | AgentRL |
| 23 | Democracy-in-Silico: Institutional Design as Alignment in AI-Governed
  Polities | Trisanth Srinivasan | 2025 | [2508.19562](https://arxiv.org/abs/2508.19562) | This paper introduces Democracy-in-Silico, an agent-based simulation where societies of advanced AI agents, imbued with complex psychological personas | RLAIF |
| 24 | School of Reward Hacks: Hacking harmless tasks generalizes to misaligned behavior in LLMs | Mia Taylor | 2025 | [2508.17511](https://arxiv.org/abs/2508.17511) | Reward hacking--where agents exploit flaws in imperfect reward functions rather than performing tasks as intended--poses risks for AI alignment. Rewar | RewardModel |
| 25 | Feedback-Driven Tool-Use Improvements in Large Language Models via
  Automated Build Environments | Junjie Ye | 2025 | [2508.08791](https://arxiv.org/abs/2508.08791) | Effective tool use is essential for large language models (LLMs) to interact meaningfully with their environment. However, progress is limited by the | AgentRL |
| 26 | AgentFly: Extensible and Scalable Reinforcement Learning for LM Agents | Renxi Wang | 2025 | [2507.14897](https://arxiv.org/abs/2507.14897) | Language model (LM) agents have gained significant attention for their ability to autonomously complete tasks through interactions with environments, | AgentRL |
| 27 | Investigating Non-Transitivity in LLM-as-a-Judge | Yi Xu | 2025 | [2502.14074](https://arxiv.org/abs/2502.14074) | Automatic evaluation methods based on large language models (LLMs) are emerging as the standard tool for assessing the instruction-following abilities | Eval |
| 28 | DINO-R1: Incentivizing Reasoning Capability in Vision Foundation Models | Chenbin Pan | 2025 | [2505.24025](https://arxiv.org/abs/2505.24025) | The recent explosive interest in the reasoning capabilities of large language models, such as DeepSeek-R1, has demonstrated remarkable success through | AgentRL |
| 29 | Stable Reinforcement Learning for Efficient Reasoning | Muzhi Dai | 2025 | [2505.18086](https://arxiv.org/abs/2505.18086) | The success of Deepseek-R1 has drawn the LLM community's attention to reinforcement learning (RL) methods like GRPO. However, such rule-based 0/1 outc | AgentRL |
| 30 | Gaming Tool Preferences in Agentic LLMs | Kazem Faghih | 2025 | [2505.18135](https://arxiv.org/abs/2505.18135) | Large language models (LLMs) can now access a wide range of external tools, thanks to the Model Context Protocol (MCP). This greatly expands their abi | AgentRL |
| 31 | Visionary-R1: Mitigating Shortcuts in Visual Reasoning with
  Reinforcement Learning | Jiaer Xia | 2025 | [2505.14677](https://arxiv.org/abs/2505.14677) | Learning general-purpose reasoning capabilities has long been a challenging problem in AI. Recent research in large language models (LLMs), such as De | AgentRL |
| 32 | DisCO: Reinforcing Large Reasoning Models with Discriminative
  Constrained Optimization | Gang Li | 2025 | [2505.12366](https://arxiv.org/abs/2505.12366) | The recent success and openness of DeepSeek-R1 have brought widespread attention to Group Relative Policy Optimization (GRPO) as a reinforcement learn | AgentRL |
| 33 | VeriReason: Reinforcement Learning with Testbench Feedback for
  Reasoning-Enhanced Verilog Generation | Yiting Wang | 2025 | [2505.11849](https://arxiv.org/abs/2505.11849) | Automating Register Transfer Level (RTL) code generation using Large Language Models (LLMs) offers substantial promise for streamlining digital circui | AgentRL |
| 34 | S-GRPO: Early Exit via Reinforcement Learning in Reasoning Models | Muzhi Dai | 2025 | [2505.07686](https://arxiv.org/abs/2505.07686) | As Test-Time Scaling emerges as an active research focus in the large language model community, advanced post-training methods increasingly emphasize | AgentRL |
| 35 | Reinforcement Learning for Reasoning in Large Language Models with One
  Training Example | Yiping Wang | 2025 | [2504.20571](https://arxiv.org/abs/2504.20571) | We show that reinforcement learning with verifiable reward using one training example (1-shot RLVR) is effective in incentivizing the math reasoning c | AgentRL |
| 36 | SARI: Structured Audio Reasoning via Curriculum-Guided Reinforcement
  Learning | Cheng Wen | 2025 | [2504.15900](https://arxiv.org/abs/2504.15900) | Recent work shows that reinforcement learning(RL) can markedly sharpen the reasoning ability of large language models (LLMs) by prompting them to "thi | AgentRL |
| 37 | SRPO: A Cross-Domain Implementation of Large-Scale Reinforcement
  Learning on LLM | Xiaojiang Zhang | 2025 | [2504.14286](https://arxiv.org/abs/2504.14286) | Recent advances of reasoning models, exemplified by OpenAI's o1 and DeepSeek's R1, highlight the significant potential of Reinforcement Learning (RL) | AgentRL |
| 38 | Understanding R1-Zero-Like Training: A Critical Perspective | Zichen Liu | 2025 | [2503.20783](https://arxiv.org/abs/2503.20783) | DeepSeek-R1-Zero has shown that reinforcement learning (RL) at scale can directly enhance the reasoning capabilities of LLMs without supervised fine-t | AgentRL |
| 39 | Med-R1: Reinforcement Learning for Generalizable Medical Reasoning in
  Vision-Language Models | Yuxiang Lai | 2025 | [2503.13939](https://arxiv.org/abs/2503.13939) | Vision-language models (VLMs) have advanced reasoning in natural scenes, but their role in medical imaging remains underexplored. Medical reasoning ta | AgentRL |
| 40 | Vision-R1: Incentivizing Reasoning Capability in Multimodal Large
  Language Models | Wenxuan Huang | 2025 | [2503.06749](https://arxiv.org/abs/2503.06749) | DeepSeek-R1-Zero has successfully demonstrated the emergence of reasoning capabilities in LLMs purely through Reinforcement Learning (RL). Inspired by | AgentRL |
| 41 | Think Inside the JSON: Reinforcement Strategy for Strict LLM Schema
  Adherence | Bhavik Agarwal | 2025 | [2502.14905](https://arxiv.org/abs/2502.14905) | In this paper, we address the challenge of enforcing strict schema adherence in large language model (LLM) generation by leveraging LLM reasoning capa | AgentRL |
| 42 | SMART: Self-Aware Agent for Tool Overuse Mitigation | Cheng Qian | 2025 | [2502.11435](https://arxiv.org/abs/2502.11435) | Current Large Language Model (LLM) agents demonstrate strong reasoning and tool use capabilities, but often lack self-awareness, failing to balance th | AgentRL |
| 43 | DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via
  Reinforcement Learning | DeepSeek-AI | 2025 | [2501.12948](https://arxiv.org/abs/2501.12948) | We introduce our first-generation reasoning models, DeepSeek-R1-Zero and DeepSeek-R1. DeepSeek-R1-Zero, a model trained via large-scale reinforcement | AgentRL |
| 44 | SDPO: Segment-Level Direct Preference Optimization for Social Agents | Aobo Kong | 2025 | [2501.01821](https://arxiv.org/abs/2501.01821) | Social agents powered by large language models (LLMs) can simulate human social behaviors but fall short in handling complex goal-oriented social dial | DPO |
| 45 | Multi-modal Agent Tuning: Building a VLM-Driven Agent for Efficient Tool
  Usage | Zhi Gao | 2024 | [2412.15606](https://arxiv.org/abs/2412.15606) | The advancement of large language models (LLMs) prompts the development of multi-modal agents, which are used as a controller to call external tools, | AgentRL |
| 46 | ScribeAgent: Towards Specialized Web Agents Using Production-Scale
  Workflow Data | Junhong Shen | 2024 | [2411.15004](https://arxiv.org/abs/2411.15004) | Large Language Model (LLM) agents are rapidly improving to handle increasingly complex web-based tasks. Most of these agents rely on general-purpose, | AgentRL |
| 47 | Synthesizing Post-Training Data for LLMs through Multi-Agent Simulation | Shuo Tang | 2024 | [2410.14251](https://arxiv.org/abs/2410.14251) | Post-training is essential for enabling large language models (LLMs) to follow human instructions. However, its effectiveness depends on high-quality | Eval |
| 48 | Building Math Agents with Multi-Turn Iterative Preference Learning | Wei Xiong | 2024 | [2409.02392](https://arxiv.org/abs/2409.02392) | Recent studies have shown that large language models' (LLMs) mathematical problem-solving capabilities can be enhanced by integrating external tools, | DPO_variants |
| 49 | EmPO: Emotion Grounding for Empathetic Response Generation through
  Preference Optimization | Ondrej Sotolar | 2024 | [2406.19071](https://arxiv.org/abs/2406.19071) | Empathetic response generation is a desirable aspect of conversational agents, crucial for facilitating engaging and emotionally intelligent multi-tur | PrefOpt |
| 50 | Direct Multi-Turn Preference Optimization for Language Agents | Wentao Shi | 2024 | [2406.14868](https://arxiv.org/abs/2406.14868) | Adapting Large Language Models (LLMs) for agent tasks is critical in developing language agents. Direct Preference Optimization (DPO) is a promising t | DPO, PrefOpt |
| 51 | Auto Arena of LLMs: Automating LLM Evaluations with Agent Peer-battles
  and Committee Discussions | Ruochen Zhao | 2024 | [2405.20267](https://arxiv.org/abs/2405.20267) | As LLMs evolve on a daily basis, there is an urgent need for a trustworthy evaluation method that can provide robust evaluation results in a timely fa | Eval |
| 52 | Learning to Use Tools via Cooperative and Interactive Agents | Zhengliang Shi | 2024 | [2403.03031](https://arxiv.org/abs/2403.03031) | Tool learning empowers large language models (LLMs) as agents to use external tools to extend their capability. Existing methods employ one single LLM | AgentRL |
| 53 | ToolTalk: Evaluating Tool-Usage in a Conversational Setting | Nicholas Farn | 2023 | [2311.10775](https://arxiv.org/abs/2311.10775) | Large language models (LLMs) have displayed massive improvements in reason- ing and decision-making skills and can hold natural conversations with use | AgentRL |
| 54 | AI Alignment and Social Choice: Fundamental Limitations and Policy
  Implications | Abhilash Mishra | 2023 | [2310.16048](https://arxiv.org/abs/2310.16048) | Aligning AI agents to human intentions and values is a key bottleneck in building safe and deployable AI applications. But whose values should AI agen | RLAIF |
| 55 | MetaTool Benchmark for Large Language Models: Deciding Whether to Use
  Tools and Which to Use | Yue Huang | 2023 | [2310.03128](https://arxiv.org/abs/2310.03128) | Large language models (LLMs) have garnered significant attention due to their impressive natural language processing (NLP) capabilities. Recently, man | AgentRL |
| 56 | RLAdapter: Bridging Large Language Models to Reinforcement Learning in
  Open Worlds | Wanpeng Zhang | 2023 | [2309.17176](https://arxiv.org/abs/2309.17176) | While reinforcement learning (RL) shows remarkable success in decision-making problems, it often requires a lot of interactions with the environment, | AgentRL |
| 57 | Identifying the Risks of LM Agents with an LM-Emulated Sandbox | Yangjun Ruan | 2023 | [2309.15817](https://arxiv.org/abs/2309.15817) | Recent advances in Language Model (LM) agents and tool use, exemplified by applications like ChatGPT Plugins, enable a rich set of capabilities but al | AgentRL |
| 58 | ModelScope-Agent: Building Your Customizable Agent System with
  Open-source Large Language Models | Chenliang Li | 2023 | [2309.00986](https://arxiv.org/abs/2309.00986) | Large language models (LLMs) have recently demonstrated remarkable capabilities to comprehend human intentions, engage in reasoning, and design planni | AgentRL |
| 59 | ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world
  APIs | Yujia Qin | 2023 | [2307.16789](https://arxiv.org/abs/2307.16789) | Despite the advancements of open-source large language models (LLMs) and their variants, e.g., LLaMA and Vicuna, they remain significantly limited in | AgentRL |
| 60 | Towards A Unified Agent with Foundation Models | Norman Di Palo | 2023 | [2307.09668](https://arxiv.org/abs/2307.09668) | Language Models and Vision Language Models have recently demonstrated unprecedented capabilities in terms of understanding human intentions, reasoning | AgentRL |
| 61 | Large Language Models as Tool Makers | Tianle Cai | 2023 | [2305.17126](https://arxiv.org/abs/2305.17126) | Recent research shows the potential of enhancing the problem-solving ability of large language models (LLMs) through the use of external tools. Howeve | AgentRL |
| 62 | ToolCoder: Teach Code Generation Models to use API search tools | Kechi Zhang | 2023 | [2305.04032](https://arxiv.org/abs/2305.04032) | Automatically generating source code from natural language descriptions has been a growing field of research in recent years. However, current large-s | AgentRL |
| 63 | ChatGPT-steered Editing Instructor for Customization of Abstractive
  Summarization | Wen Xiao | 2023 | [2305.02483](https://arxiv.org/abs/2305.02483) | Tailoring outputs of large language models, such as ChatGPT, to specific user needs remains a challenge despite their impressive generation quality. I | AgentRL |
| 64 | API-Bank: A Comprehensive Benchmark for Tool-Augmented LLMs | Minghao Li | 2023 | [2304.08244](https://arxiv.org/abs/2304.08244) | Recent research has demonstrated that Large Language Models (LLMs) can enhance their capabilities by utilizing external tools. However, three pivotal | AgentRL |

### Q7: 评估与 Benchmark
> 对齐评估框架、benchmark、human evaluation 方法论

**论文数**: 57 篇

| # | 论文标题 | 第一作者 | 年份 | arXiv ID | 核心贡献摘要 | 标签 |
|---|----------|----------|------|----------|-------------|------|
| 1 | The Flip Side of RLHF: On-Policy Feedback for Reward Model Self-Supervised Improvement | Xiaobo Wang | 2026 | [2605.30888](https://arxiv.org/abs/2605.30888) | Building strong reward models (RMs) for language model alignment is bottlenecked by the cost and difficulty of acquiring diverse and reliable preferen | RewardModel |
| 2 | Who judges the judges? Governance from metrics: a runtime framework for continuous LLM compliance monitoring | Jehanne Dussert | 2026 | [2605.24737](https://arxiv.org/abs/2605.24737) | Current approaches to AI compliance treat conformity as a binary, audit-time verdict rather than a continuous, measurable property of production syste | RLAIF |
| 3 | TAU-R1: Visual Language Model for Traffic Anomaly Understanding | Yuqiang Lin | 2026 | [2603.19098](https://arxiv.org/abs/2603.19098) | Traffic Anomaly Understanding (TAU) is important for traffic safety in Intelligent Transportation Systems. Recent vision-language models (VLMs) have s | SFT |
| 4 | References Improve LLM Alignment in Non-Verifiable Domains | Kejian Shi | 2026 | [2602.16802](https://arxiv.org/abs/2602.16802) | While Reinforcement Learning with Verifiable Rewards (RLVR) has shown strong effectiveness in reasoning tasks, it cannot be directly applied to non-ve | Eval |
| 5 | SCRIBE: Structured Mid-Level Supervision for Tool-Using Language Models | Yuxuan Jiang | 2026 | [2601.03555](https://arxiv.org/abs/2601.03555) | Training reliable tool-augmented agents remains a significant challenge, largely due to the difficulty of credit assignment in multi-step reasoning. W | AgentRL |
| 6 | MindGPT-4ov: An Enhanced MLLM via a Multi-Stage Post-Training Paradigm | Wei Chen | 2025 | [2512.02895](https://arxiv.org/abs/2512.02895) | We present MindGPT-4ov, a multimodal large language model (MLLM) that introduces a general post-training paradigm spanning data production, model trai | SFT |
| 7 | Uncovering the Computational Ingredients of Human-Like Representations
  in LLMs | Zach Studdiford | 2025 | [2510.01030](https://arxiv.org/abs/2510.01030) | The ability to translate diverse patterns of inputs into structured patterns of behavior has been thought to rest on both humans' and machines' abilit | Eval |
| 8 | Clean First, Align Later: Benchmarking Preference Data Cleaning for
  Reliable LLM Alignment | Min-Hsuan Yeh | 2025 | [2509.23564](https://arxiv.org/abs/2509.23564) | Human feedback plays a pivotal role in aligning large language models (LLMs) with human preferences. However, such feedback is often noisy or inconsis | Eval |
| 9 | Icon^{2}: Aligning Large Language Models Using Self-Synthetic
  Preference Data via Inherent Regulation | Qiyuan Chen | 2025 | [2509.05605](https://arxiv.org/abs/2509.05605) | Large Language Models (LLMs) require high quality preference datasets to align with human preferences. However, conventional methods for constructing | Eval |
| 10 | Alignment and Safety in Large Language Models: Safety Mechanisms,
  Training Paradigms, and Emerging Challenges | Haoran Lu | 2025 | [2507.19672](https://arxiv.org/abs/2507.19672) | Due to the remarkable capabilities and growing impact of large language models (LLMs), they have been deeply integrated into many aspects of society. | Eval |
| 11 | Investigating Non-Transitivity in LLM-as-a-Judge | Yi Xu | 2025 | [2502.14074](https://arxiv.org/abs/2502.14074) | Automatic evaluation methods based on large language models (LLMs) are emerging as the standard tool for assessing the instruction-following abilities | Eval |
| 12 | The Leaderboard Illusion | Shivalika Singh | 2025 | [2504.20879](https://arxiv.org/abs/2504.20879) | Measuring progress is fundamental to the advancement of any scientific field. As benchmarks play an increasingly central role, they also grow more sus | Eval |
| 13 | Aligning Multimodal LLM with Human Preference: A Survey | Tao Yu | 2025 | [2503.14504](https://arxiv.org/abs/2503.14504) | Large language models (LLMs) can handle a wide variety of general tasks with simple prompts, without the need for task-specific training. Multimodal L | Eval |
| 14 | SciFi-Benchmark: Leveraging Science Fiction To Improve Robot Behavior | Pierre Sermanet | 2025 | [2503.10706](https://arxiv.org/abs/2503.10706) | Given the recent rate of progress in artificial intelligence (AI) and robotics, a tantalizing question is emerging: would robots controlled by emergin | RLAIF |
| 15 | DiffPO: Diffusion-styled Preference Optimization for Efficient
  Inference-Time Alignment of Large Language Models | Ruizhe Chen | 2025 | [2503.04240](https://arxiv.org/abs/2503.04240) | Inference-time alignment provides an efficient alternative for aligning LLMs with humans. However, these approaches still face challenges, such as lim | Eval |
| 16 | OmniAlign-V: Towards Enhanced Alignment of MLLMs with Human Preference | Xiangyu Zhao | 2025 | [2502.18411](https://arxiv.org/abs/2502.18411) | Recent advancements in open-source multi-modal large language models (MLLMs) have primarily focused on enhancing foundational capabilities, leaving a | Eval |
| 17 | SimPER: A Minimalist Approach to Preference Alignment without Hyperparameters | Teng Xiao | 2025 | [2502.00883](https://arxiv.org/abs/2502.00883) | Existing preference optimization objectives for language model alignment require additional hyperparameters that must be extensively tuned to achieve | Eval |
| 18 | Principled Data Selection for Alignment: The Hidden Risks of Difficult
  Examples | Chengqian Gao | 2025 | [2502.09650](https://arxiv.org/abs/2502.09650) | The alignment of large language models (LLMs) often assumes that using more clean data yields better outcomes, overlooking the match between model cap | Eval |
| 19 | PRMBench: A Fine-grained and Challenging Benchmark for Process-Level
  Reward Models | Mingyang Song | 2025 | [2501.03124](https://arxiv.org/abs/2501.03124) | Process-level Reward Models (PRMs) are crucial for complex reasoning and decision-making tasks, where each intermediate step plays an important role i | RewardModel |
| 20 | InfAlign: Inference-aware language model alignment | Ananth Balashankar | 2024 | [2412.19792](https://arxiv.org/abs/2412.19792) | Language model alignment has become a critical step in training modern generative language models. The goal of alignment is to finetune a reference mo | RewardModel |
| 21 | ALMA: Alignment with Minimal Annotation | Michihiro Yasunaga | 2024 | [2412.04305](https://arxiv.org/abs/2412.04305) | Recent approaches to large language model (LLM) alignment typically require millions of human annotations or rely on external aligned models for synth | Eval |
| 22 | Weighted-Reward Preference Optimization for Implicit Model Fusion | Ziyi Yang | 2024 | [2412.03187](https://arxiv.org/abs/2412.03187) | While fusing heterogeneous open-source LLMs with varying architectures and sizes can potentially integrate the strengths of different models, existing | Eval |
| 23 | Varco Arena: A Tournament Approach to Reference-Free Benchmarking Large
  Language Models | Seonil Son | 2024 | [2411.01281](https://arxiv.org/abs/2411.01281) | The rapid advancement of Large Language Models (LLMs) necessitates robust evaluation methodologies. Current benchmarking approaches often rely on comp | Eval |
| 24 | LLM-Inference-Bench: Inference Benchmarking of Large Language Models on
  AI Accelerators | Krishna Teja Chitty-Venkata | 2024 | [2411.00136](https://arxiv.org/abs/2411.00136) | Large Language Models (LLMs) have propelled groundbreaking advancements across several domains and are commonly used for text generation applications. | Eval |
| 25 | CAMEL-Bench: A Comprehensive Arabic LMM Benchmark | Sara Ghaboura | 2024 | [2410.18976](https://arxiv.org/abs/2410.18976) | Recent years have witnessed a significant interest in developing large multimodal models (LMMs) capable of performing various visual reasoning and und | Eval |
| 26 | Synthesizing Post-Training Data for LLMs through Multi-Agent Simulation | Shuo Tang | 2024 | [2410.14251](https://arxiv.org/abs/2410.14251) | Post-training is essential for enabling large language models (LLMs) to follow human instructions. However, its effectiveness depends on high-quality | Eval |
| 27 | JudgeBench: A Benchmark for Evaluating LLM-based Judges | Sijun Tan | 2024 | [2410.12784](https://arxiv.org/abs/2410.12784) | LLM-based judges have emerged as a scalable alternative to human evaluation and are increasingly used to assess, compare, and improve models. However, | Eval |
| 28 | Cheating Automatic LLM Benchmarks: Null Models Achieve High Win Rates | Xiaosen Zheng | 2024 | [2410.07137](https://arxiv.org/abs/2410.07137) | Automatic LLM benchmarks, such as AlpacaEval 2.0, Arena-Hard-Auto, and MT-Bench, have become popular for evaluating language models due to their cost- | Eval |
| 29 | Uncovering Factor Level Preferences to Improve Human-Model Alignment | Juhyun Oh | 2024 | [2410.06965](https://arxiv.org/abs/2410.06965) | Despite advancements in Large Language Model (LLM) alignment, understanding the reasons behind LLM preferences remains crucial for bridging the gap be | Eval |
| 30 | Modulated Intervention Preference Optimization (MIPO): Keep the Easy,
  Refine the Difficult | Cheolhun Jang | 2024 | [2409.17545](https://arxiv.org/abs/2409.17545) | Preference optimization methods typically begin training with a well-trained SFT model as a reference model. In RLHF and DPO, a regularization term is | Eval |
| 31 | Style over Substance: Failure Modes of LLM Judges in Alignment
  Benchmarking | Benjamin Feuer | 2024 | [2409.15268](https://arxiv.org/abs/2409.15268) | The release of ChatGPT in November 2022 sparked an explosion of interest in post-training and an avalanche of new preference optimization (PO) methods | Eval |
| 32 | Towards a Unified View of Preference Learning for Large Language Models:
  A Survey | Bofei Gao | 2024 | [2409.02795](https://arxiv.org/abs/2409.02795) | Large Language Models (LLMs) exhibit remarkably powerful capabilities. One of the crucial factors to achieve success is aligning the LLM's output with | Eval |
| 33 | I-SHEEP: Self-Alignment of LLM from Scratch through an Iterative
  Self-Enhancement Paradigm | Yiming Liang | 2024 | [2408.08072](https://arxiv.org/abs/2408.08072) | Large Language Models (LLMs) have achieved significant advancements, however, the common learning paradigm treats LLMs as passive information reposito | Eval |
| 34 | Arena Learning: Build Data Flywheel for LLMs Post-training via Simulated
  Chatbot Arena | Haipeng Luo | 2024 | [2407.10627](https://arxiv.org/abs/2407.10627) | Assessing the effectiveness of large language models (LLMs) presents substantial challenges. The method of conducting human-annotated battles in an on | SFT |
| 35 | Reward Steering with Evolutionary Heuristics for Decoding-time Alignment | Chia-Yu Hung | 2024 | [2406.15193](https://arxiv.org/abs/2406.15193) | The widespread applicability and increasing omnipresence of LLMs have instigated a need to align LLM responses to user and stakeholder preferences. Ma | Eval |
| 36 | WPO: Enhancing RLHF with Weighted Preference Optimization | Wenxuan Zhou | 2024 | [2406.11827](https://arxiv.org/abs/2406.11827) | Reinforcement learning from human feedback (RLHF) is a promising solution to align large language models (LLMs) more closely with human values. Off-po | Eval |
| 37 | From Crowdsourced Data to High-Quality Benchmarks: Arena-Hard and
  BenchBuilder Pipeline | Tianle Li | 2024 | [2406.11939](https://arxiv.org/abs/2406.11939) | The rapid evolution of language models has necessitated the development of more challenging benchmarks. Current static benchmarks often struggle to co | Eval |
| 38 | Magpie: Alignment Data Synthesis from Scratch by Prompting Aligned LLMs
  with Nothing | Zhangchen Xu | 2024 | [2406.08464](https://arxiv.org/abs/2406.08464) | High-quality instruction data is critical for aligning large language models (LLMs). Although some models, such as Llama-3-Instruct, have open weights | Eval |
| 39 | MixEval: Deriving Wisdom of the Crowd from LLM Benchmark Mixtures | Jinjie Ni | 2024 | [2406.06565](https://arxiv.org/abs/2406.06565) | Evaluating large language models (LLMs) is challenging. Traditional ground-truth-based benchmarks fail to capture the comprehensiveness and nuance of | Eval |
| 40 | Inverse Constitutional AI: Compressing Preferences into Principles | Arduin Findeis | 2024 | [2406.06560](https://arxiv.org/abs/2406.06560) | Feedback data plays an important role in fine-tuning and evaluating state-of-the-art AI models. Often pairwise text preferences are used: given two te | RLAIF |
| 41 | Auto Arena of LLMs: Automating LLM Evaluations with Agent Peer-battles
  and Committee Discussions | Ruochen Zhao | 2024 | [2405.20267](https://arxiv.org/abs/2405.20267) | As LLMs evolve on a daily basis, there is an urgent need for a trustworthy evaluation method that can provide robust evaluation results in a timely fa | Eval |
| 42 | Aligning to Thousands of Preferences via System Message Generalization | Seongyun Lee | 2024 | [2405.17977](https://arxiv.org/abs/2405.17977) | Although humans inherently have diverse values, current large language model (LLM) alignment methods often assume that aligning LLMs with the general | Eval |
| 43 | RLHF Workflow: From Reward Modeling to Online RLHF | Hanze Dong | 2024 | [2405.07863](https://arxiv.org/abs/2405.07863) | We present the workflow of Online Iterative Reinforcement Learning from Human Feedback (RLHF) in this technical report, which is widely reported to ou | Eval |
| 44 | Length-Controlled AlpacaEval: A Simple Way to Debias Automatic
  Evaluators | Yann Dubois | 2024 | [2404.04475](https://arxiv.org/abs/2404.04475) | LLM-based auto-annotators have become a key component of the LLM development process due to their cost-effectiveness and scalability compared to human | Eval |
| 45 | Extensive Self-Contrast Enables Feedback-Free Language Model Alignment | Xiao Liu | 2024 | [2404.00604](https://arxiv.org/abs/2404.00604) | Reinforcement learning from human feedback (RLHF) has been a central technique for recent large language model (LLM) alignment. However, its heavy dep | RLHF |
| 46 | Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference | Wei-Lin Chiang | 2024 | [2403.04132](https://arxiv.org/abs/2403.04132) | Large Language Models (LLMs) have unlocked new capabilities and applications; however, evaluating the alignment with human preferences still poses sig | Eval |
| 47 | tinyBenchmarks: evaluating LLMs with fewer examples | Felipe Maia Polo | 2024 | [2402.14992](https://arxiv.org/abs/2402.14992) | The versatility of large language models (LLMs) led to the creation of diverse benchmarks that thoroughly test a variety of language models' abilities | Eval |
| 48 | Dissecting Human and LLM Preferences | Junlong Li | 2024 | [2402.11296](https://arxiv.org/abs/2402.11296) | As a relative quality comparison of model responses, human and Large Language Model (LLM) preferences serve as common alignment goals in model fine-tu | Eval |
| 49 | Linear Alignment: A Closed-form Solution for Aligning Human Preferences
  without Tuning and Feedback | Songyang Gao | 2024 | [2401.11458](https://arxiv.org/abs/2401.11458) | The success of AI assistants based on Language Models (LLMs) hinges on Reinforcement Learning from Human Feedback (RLHF) to comprehend and align with | RLAIF, Eval |
| 50 | Reasons to Reject? Aligning Language Models with Judgments | Weiwen Xu | 2023 | [2312.14591](https://arxiv.org/abs/2312.14591) | As humans, we consistently engage in interactions with our peers and receive feedback in the form of natural language. This language feedback allows u | Eval |
| 51 | AlignBench: Benchmarking Chinese Alignment of Large Language Models | Xiao Liu | 2023 | [2311.18743](https://arxiv.org/abs/2311.18743) | Alignment has become a critical step for instruction-tuned Large Language Models (LLMs) to become helpful assistants. However, effective evaluation of | Eval |
| 52 | MetaTool Benchmark for Large Language Models: Deciding Whether to Use
  Tools and Which to Use | Yue Huang | 2023 | [2310.03128](https://arxiv.org/abs/2310.03128) | Large language models (LLMs) have garnered significant attention due to their impressive natural language processing (NLP) capabilities. Recently, man | AgentRL |
| 53 | Benchmarking Cognitive Biases in Large Language Models as Evaluators | Ryan Koo | 2023 | [2309.17012](https://arxiv.org/abs/2309.17012) | Large Language Models (LLMs) have recently been shown to be effective as automatic evaluators with simple prompting and in-context learning. In this w | Eval |
| 54 | Large Language Model as a User Simulator | Chuyi Kong | 2023 | [2308.11534](https://arxiv.org/abs/2308.11534) | The unparalleled performance of closed-sourced ChatGPT has sparked efforts towards its democratization, with notable strides made by leveraging real u | Eval |
| 55 | Aligning Large Language Models with Human: A Survey | Yufei Wang | 2023 | [2307.12966](https://arxiv.org/abs/2307.12966) | Large Language Models (LLMs) trained on extensive textual corpora have emerged as leading solutions for a broad array of Natural Language Processing ( | Eval |
| 56 | Judging LLM-as-a-judge with MT-Bench and Chatbot Arena | Lianmin Zheng | 2023 | [2306.05685](https://arxiv.org/abs/2306.05685) | Evaluating large language model (LLM) based chat assistants is challenging due to their broad capabilities and the inadequacy of existing benchmarks i | Eval |
| 57 | API-Bank: A Comprehensive Benchmark for Tool-Augmented LLMs | Minghao Li | 2023 | [2304.08244](https://arxiv.org/abs/2304.08244) | Recent research has demonstrated that Large Language Models (LLMs) can enhance their capabilities by utilizing external tools. However, three pivotal | AgentRL |

---

## 里程碑论文确认

| 论文 | arXiv ID | 检索状态 | 年份 | 第一作者 | 备注 |
|------|----------|----------|------|----------|------|
| Proximal Policy Optimization Algorithms | [1707.06347](https://arxiv.org/abs/1707.06347) | ✅ 已通过 HuggingFace API 确认 | 2017 | John Schulman | PPO 原始论文，方法基础 |
| Training language models to follow instructions with human feedback | [2203.02155](https://arxiv.org/abs/2203.02155) | ✅ 已通过 HuggingFace API 确认 | 2022 | Long Ouyang | InstructGPT / RLHF 范式确立 |
| Direct Preference Optimization: Your Language Model is Secretly a Reward Model | [2305.18290](https://arxiv.org/abs/2305.18290) | ✅ 在 DPO 搜索结果中确认 | 2023 | Rafael Rafailov | DPO 转折点，偏好优化里程碑 |
| Llama 2: Open Foundation and Fine-Tuned Chat Models | [2307.09288](https://arxiv.org/abs/2307.09288) | ✅ 已通过 HuggingFace API 确认 | 2023 | Hugo Touvron | 工业级 RLHF 实践，开源社区基石 |
| Constitutional AI: Harmlessness from AI Feedback | [2212.08073](https://arxiv.org/abs/2212.08073) | ✅ 在 RLAIF 搜索结果中确认 | 2022 | Yuntao Bai | RLAIF 方法，Constitutional AI 范式 |

## 其他关键论文 (已确认在库)

| arXiv ID | 论文标题 | 子方向 | 年份 | 重要性说明 |
|----------|----------|--------|------|-----------|
| [2306.05685](https://arxiv.org/abs/2306.05685) | Judging LLM-as-a-judge with MT-Bench and Chatbot Arena | Q7 | 2023 | MT-Bench 和 Chatbot Arena 原始论文 |
| [2405.14734](https://arxiv.org/abs/2405.14734) | SimPO: Simple Preference Optimization with a Reference-Free Reward | Q4 | 2024 | DPO 主要变体，无参考模型 |
| [2403.07691](https://arxiv.org/abs/2403.07691) | ORPO: Monolithic Preference Optimization without Reference Model | Q4 | 2024 | DPO 变体，合并 SFT+偏好优化 |
| [2402.01306](https://arxiv.org/abs/2402.01306) | KTO: Model Alignment as Prospect Theoretic Optimization | Q4 | 2024 | DPO 变体，基于前景理论 |
| [2310.01377](https://arxiv.org/abs/2310.01377) | UltraFeedback: Boosting Language Models with High-quality Feedback | Q2 | 2023 | 高质量偏好数据集构建 |
| [2404.04475](https://arxiv.org/abs/2404.04475) | Length-Controlled AlpacaEval | Q7 | 2024 | AlpacaEval 长度偏差修正 |
| [2311.18743](https://arxiv.org/abs/2311.18743) | AlignBench: Benchmarking Chinese Alignment of LLMs | Q7 | 2023 | 中文对齐评估基准 |
| [2309.00267](https://arxiv.org/abs/2309.00267) | RLAIF: Scaling RLHF with AI Feedback | Q2 | 2023 | RLAIF 核心方法 |
| [2402.08925](https://arxiv.org/abs/2402.08925) | MaxMin-RLHF: Towards Equitable Alignment of LLMs | Q3 | 2024 | 公平性导向 RLHF |
| [2308.12050](https://arxiv.org/abs/2308.12050) | Aligning Language Models with Offline RLHF | Q3 | 2023 | 离线 RLHF 方法 |
| [2404.00604](https://arxiv.org/abs/2404.00604) | Extensive Self-Contrast Enables Feedback-Free LM Alignment | Q3 | 2024 | 无反馈自对比对齐 |
| [2406.05534](https://arxiv.org/abs/2406.05534) | Online DPO: Online Direct Preference Optimization with Fast-Slow Chasing | Q4 | 2024 | 在线 DPO |
| [2405.00675](https://arxiv.org/abs/2405.00675) | Self-Play Preference Optimization for Language Model Alignment | Q4 | 2024 | 自博弈偏好优化 |
| [2410.15595](https://arxiv.org/abs/2410.15595) | A Comprehensive Survey of Direct Preference Optimization | Q4 | 2024 | DPO 综述 |
| [2509.22047](https://arxiv.org/abs/2509.22047) | MO-GRPO: Mitigating Reward Hacking of GRPO | Q5 | 2025 | GRPO 奖励破解缓解 |
| [2406.14868](https://arxiv.org/abs/2406.14868) | Direct Multi-Turn Preference Optimization for Language Agents | Q4/Q6 | 2024 | 多轮 Agent 偏好优化 |
| [2406.10957](https://arxiv.org/abs/2406.10957) | Eliminating Biased Length Reliance of DPO | Q4 | 2024 | DPO 长度偏差解决方案 |
| [2412.01981](https://arxiv.org/abs/2412.01981) | Free Process Rewards without Process Labels | Q2 | 2024 | 无监督过程奖励模型 |
| [2405.07863](https://arxiv.org/abs/2405.07863) | RLHF Workflow: From Reward Modeling to Online RLHF | Q3/Q7 | 2024 | RLHF 全流程实践 |
| [2601.07389](https://arxiv.org/abs/2601.07389) | On the Non-decoupling of SFT and RL in Post-Training | Q1 | 2026 | SFT 与 RL 关系分析 |

---

## 子方向统计

| 子方向 | 论文数 |
|--------|--------|
| Q1: SFT 基础 | 23 |
| Q2: Reward Modeling | 76 |
| Q3: PPO-based RLHF | 42 |
| Q4: DPO 及变体 | 80 |
| Q5: GRPO 及 Group-wise 方法 | 31 |
| Q6: Agentic RL | 64 |
| Q7: 评估与 Benchmark | 57 |
| 未分类 | 3 |
| **合计去重** | **280** |

> 注: 一篇论文可能被分类到多个子方向。统计基于多标签分类。

## 未分类论文

以下论文在自动分类中未匹配到明确的子方向，需要人工审核：

- [2507.11502](https://arxiv.org/abs/2507.11502) - HKGAI-V1: Towards Regional Sovereign Large Language Model for Hong Kong
- [2406.20060](https://arxiv.org/abs/2406.20060) - Applying RLAIF for Code Generation with API-usage in Lightweight LLMs
- [2212.08073](https://arxiv.org/abs/2212.08073) - Constitutional AI: Harmlessness from AI Feedback

---

## 检索局限与后续工作

1. **数据源限制**: 主要依赖 HuggingFace Papers API（arXiv 索引），可能遗漏未在 HF 注册的论文
2. **搜索覆盖**: 每次搜索仅返回 15-20 篇，且 HF 搜索为语义搜索，可能遗漏关键词不匹配但相关的工作
3. **经典论文**: 2020 年前的经典论文在语义搜索中排名可能较低
4. **中文论文**: 中文社区工作（如 DeepSeek 技术报告）可能未被充分覆盖
5. **arXiv 不可用**: 因 API 429/503 错误，未能完成原计划的 arXiv 直接检索
6. **待补充**: 需要用 Semantic Scholar API 进行引用追踪，发现被引但未被搜索命中的论文

**建议后续由 lineage_mapping_agent 和 method_taxonomy_agent 进行深度分析和补充。**

---

*生成时间: 2026-06-23 | 生成 Agent: paper_discovery_agent | 数据源: HuggingFace Papers API*