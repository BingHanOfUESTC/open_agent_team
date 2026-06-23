# Source Log / 检索来源日志

> **生成时间**: 2026-06-23
> **生成 Agent**: paper_discovery_agent

## 检索来源记录

| # | 来源 | 查询/Search Term | 限制 | 结果数 | 状态 | 备注 |
|---|------|-----------------|------|--------|------|------|
| 1 | HuggingFace Papers API | reinforcement learning human feedback language model | 20 | 20 | ✅ 成功 | RLHF 核心检索 |
| 2 | HuggingFace Papers API | direct preference optimization | 20 | 20 | ✅ 成功 | DPO 方法检索 |
| 3 | HuggingFace Papers API | preference optimization language model | 20 | 20 | ✅ 成功 | 偏好优化广泛检索 |
| 4 | HuggingFace Papers API | proximal policy optimization language model RLHF | 20 | 20 | ✅ 成功 | PPO+LLM 检索 |
| 5 | HuggingFace Papers API | reward model language model alignment | 20 | 20 | ✅ 成功 | Reward Model 检索 |
| 6 | HuggingFace Papers API | group relative policy optimization GRPO | 20 | 20 | ✅ 成功 | GRPO 方法检索 |
| 7 | HuggingFace Papers API | reinforcement learning agent tool use language model | 20 | 20 | ✅ 成功 | Agent RL 检索 |
| 8 | HuggingFace Papers API | instruction tuning supervised fine-tuning language model | 20 | 20 | ✅ 成功 | SFT 检索 |
| 9 | HuggingFace Papers API | KTO ORPO SimPO preference optimization | 20 | 20 | ✅ 成功 | DPO 变体检索 |
| 10 | HuggingFace Papers API | RLAIF constitutional AI alignment | 20 | 20 | ✅ 成功 | RLAIF 检索 |
| 11 | HuggingFace Papers API | LLM evaluation benchmark alignment AlpacaEval MT-Bench | 20 | 20 | ✅ 成功 | 评估检索 |
| 12 | HuggingFace Papers API | supervised fine-tuning language model post-training | 15 | 15 | ✅ 成功 | SFT 补充检索 |
| 13 | HuggingFace Papers API | self-instruct instruction tuning data generation | 15 | 0 | ❌ 失败 | SSL 错误 |
| 14 | HuggingFace Papers API | AlpacaEval MT-Bench Chatbot Arena LLM evaluation | 15 | 15 | ✅ 成功 | 评估补充 |
| 15 | HuggingFace Papers API | LLM alignment evaluation benchmark human preference | 15 | 15 | ✅ 成功 | 评估补充 |
| 16 | HuggingFace Papers API | reward over-optimization reward hacking language model | 15 | 15 | ✅ 成功 | RM 补充 |
| 17 | HuggingFace Papers API | iterative DPO online preference learning | 15 | 15 | ✅ 成功 | DPO 变体补充 |
| 18 | HuggingFace Papers API | DeepSeek-R1 reasoning reinforcement learning GRPO | 15 | 15 | ✅ 成功 | AgentRL 补充 |
| 19 | HuggingFace Papers API | WebGPT toolformer language model agent tool use | 15 | 15 | ✅ 成功 | AgentRL 补充 |
| 20 | HuggingFace Papers API | process reward model outcome reward model PRM ORM | 15 | 15 | ✅ 成功 | RM 补充 |
| 21 | arXiv API (curl) | reinforcement learning from human feedback cat:cs.CL | 30 | 0 | ❌ 429 | 速率限制 |
| 22 | arXiv API (curl) | preference optimization cat:cs.CL | 30 | 0 | ❌ 429 | 速率限制 |
| 23 | arXiv API (curl) | direct preference optimization cat:cs.CL | 30 | 0 | ❌ 429 | 速率限制 |
| 24 | arXiv API (curl) | proximal policy optimization language model cat:cs.CL | 20 | 0 | ❌ Timeout | 超时 |
| 25 | arXiv API (curl) | reward model language model cat:cs.CL | 20 | 0 | ❌ SSL Error | SSL 错误 |
| 26 | arXiv API (curl) | group relative policy optimization cat:cs.CL | 20 | 0 | ❌ 502 | 服务不可用 |
| 27 | arXiv API (curl) | reinforcement learning agent language model cat:cs.CL | 20 | 0 | ❌ 429 | 速率限制 |
| 28 | arXiv API (curl) | instruction tuning language model cat:cs.CL | 20 | 0 | ❌ Timeout | 超时 |
| 29 | Semantic Scholar API | reinforcement learning human feedback | 10 | 0 | ❌ 429 | 速率限制 |

## 里程碑论文验证

| arXiv ID | 论文 | 验证方式 | 结果 |
|----------|------|----------|------|
| 1707.06347 | PPO (Schulman et al., 2017) | HuggingFace API `/api/papers/1707.06347` | ✅ 已确认 |
| 2203.02155 | InstructGPT (Ouyang et al., 2022) | HuggingFace API `/api/papers/2203.02155` | ✅ 已确认 |
| 2305.18290 | DPO (Rafailov et al., 2023) | 在 "direct preference optimization" 搜索结果中 | ✅ 已确认 |
| 2307.09288 | Llama 2 (Touvron et al., 2023) | HuggingFace API `/api/papers/2307.09288` | ✅ 已确认 |
| 2212.08073 | Constitutional AI (Bai et al., 2022) | 在 "RLAIF constitutional AI" 搜索结果中 | ✅ 已确认 |

## 搜索方法论

- **主数据源**: HuggingFace Papers API (`https://huggingface.co/api/papers/search`)
- **单个论文验证**: HuggingFace Papers API (`https://huggingface.co/api/papers/{id}`)
- **搜索策略**: 先进行 11 个宽覆盖搜索（每批 20 篇），再进行 9 个专项补充搜索（每批 15 篇）
- **去重**: 基于 arXiv ID 去重
- **分类**: 基于搜索标签 + 标题/摘要关键词多标签分类

## 已知局限

1. 未完成 arXiv 原生 API 检索（因 429/503 错误）
2. 未完成 Semantic Scholar 引用追踪（因 429 错误）
3. 搜索 API 每次仅返回 15-20 篇，可能遗漏部分相关论文
4. HuggingFace 索引可能未涵盖所有 arXiv 论文
5. 关键词覆盖可能不够全面，部分子方向（如 Q1 SFT）论文数偏少

## 建议后续步骤

1. ✅ paper_inventory.md 已生成 → 进入 lineage_mapping 阶段
2. 需要 Semantic Scholar 引用追踪以发现被引论文
3. 建议人工补充 DeepSeek-R1 技术报告、Qwen 技术报告等中文社区工作
4. 建议对 Q1(SFT) 方向进行额外专项检索
