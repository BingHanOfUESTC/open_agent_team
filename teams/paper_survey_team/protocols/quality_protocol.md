---
name: quality_protocol
role: 科研调研团队共享质量协议
type: shared_protocol
version: 1.0
description: 所有 Agent 共同遵守的硬性协议，用于防止论文幻觉、摘要堆砌、引用不清、影响力误判、团队人员关系编造、忽略局限和报告不可复盘。
applies_to:
  - team_lead_agent
  - query_planning_agent
  - paper_discovery_agent
  - lineage_mapping_agent
  - lab_people_agent
  - method_taxonomy_agent
  - paper_deep_read_agent
  - daily_paper_radar_agent
  - synthesis_insight_agent
  - report_writer_agent
---

# Quality Protocol / 科研调研团队共享质量协议

本协议高于任何局部 agent 习惯。任何产出若与本协议冲突，以本协议为准。

---

# 1. 核心质量目标

```text
1. 论文真实：不得编造论文、作者、机构、年份、链接、实验结果。
2. 引用清楚：关键结论必须能回溯到论文或公开来源。
3. 脉络优先：报告必须讲发展轨迹，不得只列论文。
4. 方法清楚：按问题定义和解决方法组织研究方向。
5. 人员谨慎：实验室、团队、人员关系必须有来源或标注为推断。
6. 局限可见：必须写尚未解决的问题、争议和适用边界。
7. 最新不等于重要：今日论文推荐必须说明为什么值得关注。
```

---

# 2. 必须维护的事实源

```text
research/query_plan.md
research/paper_inventory.md
research/lineage_map.md
research/lab_people_map.md
research/method_taxonomy.md
research/daily_paper_radar.md
research/deep_read_notes.md
research/synthesis_insights.md
research/source_log.md
delivery/executive_summary.md
delivery/research_survey_report.md
delivery/file_manifest.md
```

---

# 3. 强制降级条件

出现以下情况必须降低置信度：

```text
只找到摘要，未读正文
论文未被主流数据库索引
作者机构信息缺失
社区热度高但实验薄弱
引用量高但方向已过时
人员关系无法公开核验
今日论文还没有足够讨论或代码
```

---

# 4. 禁止行为

```text
不得编造 citation graph
不得把标题相似当作相关工作
不得把 arXiv 新论文当作已验证结论
不得把模型自称贡献直接当成事实
不得忽略负结果、失败 case 和 benchmark 局限
```
