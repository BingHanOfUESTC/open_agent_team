---
name: quality_protocol
role: iPhone App 设计研发共享质量协议
type: shared_protocol
version: 1.0
description: 所有 Agent 共同遵守的硬性协议，用于防止 iPhone App 项目中的方向漂移、信息架构混乱、技术实现断层、联调失败以及交付不完整。
applies_to:
  - team_lead_agent
  - product_strategy_agent
  - feature_architect_agent
  - information_architecture_agent
  - design_system_agent
  - technical_director_agent
  - ios_engineer_agent
  - backend_integration_agent
  - analytics_engineer_agent
  - integration_qa_agent
---

# Quality Protocol / iPhone App 设计研发共享质量协议

本协议高于局部 agent 习惯。任何产出若与本协议冲突，以本协议为准。

---

# 1. 核心目标

本协议解决以下高风险问题：

```text
1. 方向漂移：目标用户、App 定位、项目范围前后不一致。
2. 功能膨胀：MVP 失控，核心价值还没验证就堆大量外围功能。
3. 信息架构混乱：页面树、导航结构、状态定义互相冲突。
4. 设计不可实现：视觉与交互规范含糊，无法稳定落地为 iOS 界面。
5. 技术脱节：性能、包管理、模块依赖、调试与联调方式不在前期设计中。
6. iOS 体验失真：忽略 iPhone 交互习惯、权限约束、离线与弱网现实。
7. 研发断层：产品和设计存在，但 iOS、后端接入、埋点没有对应实现边界。
8. 联调失败：模块之间接口、状态、配置结构不一致。
9. 平台错配：目标平台、语言、依赖管理、项目模板选择错误。
10. 交付不完整：只有概念，没有可执行规格、可联调结构与 handoff 口径。
11. 编译失效：存在已知构建阻塞、缺失依赖、缺失资源、未声明环境要求。
12. 文档失真：研发实现建立在未核实的记忆或二手说法上，而不是 Apple 官方定义。
13. 并发失序：在接口、状态和依赖未锁定前盲目并发，导致返工和联调冲突。
```

---

# 2. 全案唯一事实源

完整项目必须维护以下事实源：

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

任何关键功能、页面、模块边界与联调流程进入正式方案前，必须先写入对应事实源。

凡是涉及以下内容的不确定问题：

```text
Swift 语言行为
SwiftUI 生命周期与状态管理
UIKit 控件和导航行为
系统权限
通知
后台任务
文件系统
网络与鉴权系统能力
本地化、可访问性、系统组件接入
```

研发相关 agent 必须优先查阅 Apple 官方文档。

其中 `tech/platform_build_spec.md` 必须在研发前锁定：

```text
目标平台
UI 技术方案
语言
包管理方式
工程模板
最低 iOS 版本
关键 SDK / 库版本
构建命令或构建入口
```

---

# 3. MVP 纪律

必须遵守：

```text
1. 核心价值验证优先于功能扩张。
2. MVP 只保留验证核心使用场景和完整闭环的最低必要功能。
3. 任何高依赖后台、多角色协同、复杂富媒体或复杂权限链路，默认不进入 MVP，除非有充分理由。
4. 如果某功能不能清楚说明“验证哪一个价值或实现目标”，应删减或降级。
5. 如果某功能没有明确的实现归属 agent，也不得进入正式方案。
```

---

# 4. Screen Map 纪律

必须生成并维护：

```text
design/screen_map.md
```

至少覆盖：

```text
导航结构
页面树
关键页面状态
列表与详情关系
主要创建/编辑/提交路径
```

硬规则：

```text
不要让导航层级过深
关键功能路径必须可追踪
异常、空状态、权限状态必须提前定义
```

---

# 5. 技术与集成纪律

必须生成并维护：

```text
tech/module_dependency_matrix.md
tech/platform_build_spec.md
```

至少覆盖：

```text
目标平台
最低 iOS 版本
语言与工程模板
包管理方式
模块 owner
接口依赖
配置来源
调试方式
集成顺序
```

硬规则：

```text
技术方案必须与 iPhone 平台一致
必须明确 SwiftUI / UIKit / 混合方案的边界
关键模块必须定义接口和失败降级方式
性能风险必须在方案期可见，不能留到联调前爆炸
接口、状态模型、依赖方式锁定前，不得并发推进具体实现
```

---

# 6. 研发执行纪律

必须生成并维护：

```text
dev/ios_architecture.md
dev/api_contract_matrix.md
dev/analytics_event_spec.md
qa/integration_checklist.md
qa/build_readiness_checklist.md
```

硬规则：

```text
iOS、后端接入、埋点必须有明确 owner
每个关键功能都要说明运行位置、依赖服务、配置来源与失败降级方案
分析事件必须有命名、触发时机、参数和校验规则
联调验收必须有 checklist
交付前必须做 build readiness 自检，不能带着已知 compile blocker 交付
接口锁定后，应默认并发推进可独立实现的研发任务
```

---

# 7. QA 风险分级

所有问题至少分为：

```text
P0：会导致核心流程无法跑通、工程无法联调、工程无法编译、Boss 无法接手
P1：会显著破坏体验、实现效率、稳定性或 handoff 质量
P2：可保留观察的问题或优化项
```
