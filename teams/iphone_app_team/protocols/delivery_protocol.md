---
name: delivery_protocol
role: iPhone App 设计研发最终交付协议
type: shared_protocol
version: 1.0
description: 规定 iPhone App multi-agent team 的最终交付结构、必备文件、验收标准与总包整理方式，保证产物是完整可执行的设计研发方案，而不是零散灵感。
applies_to:
  - team_lead_agent
  - integration_qa_agent
---

# Delivery Protocol / iPhone App 设计研发最终交付协议

---

# 1. 最终交付目标

默认最终交付不是一句 pitch，也不是只有一个 PRD。

默认必须包含：

```text
00_boss_brief.md
01_producer_project_plan.md
02_product_strategy.md
03_feature_architecture.md
04_information_architecture.md
05_design_system_direction.md
06_technical_plan.md
07_ios_architecture_plan.md
08_backend_integration_plan.md
09_analytics_instrumentation_plan.md
10_integration_qa_report.md
delivery/executive_summary.md
delivery/full_app_package.md
delivery/file_manifest.md
```

以及以下事实源：

```text
design/feature_registry.md
design/screen_map.md
design/component_inventory.md
tech/module_dependency_matrix.md
tech/platform_build_spec.md
dev/ios_architecture.md
dev/api_contract_matrix.md
dev/analytics_event_spec.md
qa/integration_checklist.md
qa/build_readiness_checklist.md
qa/risk_register.md
```

---

# 2. full_app_package.md 要求

`delivery/full_app_package.md` 必须是完整总包，不得只是索引。

它至少要整合：

```text
产品定义
目标用户
项目范围与复杂度
核心功能
信息架构与页面树
设计系统方向
iOS 技术方案
平台与构建规格
研发实现与联调方案
风险与验收结论
```

其中“研发实现与联调方案”必须明确：

```text
哪些工作先串行完成
哪些模块在接口锁定后并发实现
并发实现依赖的契约文件是什么
Apple 官方文档决定了哪些关键实现约束
```

---

# 3. 验收标准

一套方案只有在满足以下条件时才可判定为“可交付”：

```text
目标平台已锁定
语言、依赖、工程模板已锁定
核心功能、页面结构和用户流程可被清晰描述
iOS、后端接入、埋点 owner 清晰
模块依赖和接口边界清晰
build readiness checklist 已完成
无已知 compile blocker
Boss 可依据交付件接手编译与测试
研发中的关键不确定点已被 Apple 官方文档确认
```

---

# 4. 禁止行为

不得以以下内容冒充正式交付：

```text
只有 App 点子，没有功能与流程设计
只有页面想法，没有信息架构和状态定义
只有技术名词，没有模块边界与联调方案
没有平台构建规格和依赖清单
带着已知编译阻塞交付
只有“后续补充”
```
