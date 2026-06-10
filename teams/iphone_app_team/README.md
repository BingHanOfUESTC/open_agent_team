# iPhone App Team / iPhone App 设计研发交付团队

`iphone_app_team` 是一套面向 iPhone App 的 multi-agent team。  
目标很明确：

> Boss 给出 `目标平台 + App 类型 + 粗需求 + 规模`，团队负责把它细化成完整的 iPhone App 设计与研发工程方案，最终交付给 Boss 接手编译、测试、发布。

这套团队不是运营团队，也不是上架代运营团队。  
它的重点是：

```text
把 App 需求设计出来
把信息架构和交互方案拆清楚
把 iOS 工程结构和模块边界定义清楚
把 handoff 做到 Boss 可直接接手编译
不带已知 compile blocker 交付
遇到不确定实现时优先查 Apple 官方文档
接口锁定后默认并发推进实现
```

---

# 1. 默认定位

```text
目标：完整 iPhone App 设计与研发工程方案
适用：内容型 / 工具型 / 社区型 / 电商型 / SaaS 配套 / AI 应用型 iPhone App
默认阶段：从 Boss 输入推导到可执行 design + development 交付
Boss 职责：最后自行编译、测试、发布
团队职责：完成需求细化、产品方案、设计方案、iOS 研发拆分、技术方案、集成验收与交接文档
```

默认研发节奏：

```text
先串行完成：产品定位 -> 功能架构 -> 信息架构 -> 设计系统 -> 技术方案
再锁定：模块边界、接口契约、状态结构、依赖方式
锁定后并发推进：iOS 实现、后端接入、埋点与观测方案
最后集中做：联调、自检、build readiness 验收
```

---

# 2. 最终组织架构

```text
Boss
│
└── @team_lead_agent
    ├── @product_strategy_agent
    ├── @feature_architect_agent
    ├── @information_architecture_agent
    ├── @design_system_agent
    ├── @technical_director_agent
    ├── @ios_engineer_agent
    ├── @backend_integration_agent
    ├── @analytics_engineer_agent
    └── @integration_qa_agent
```

补充说明：

```text
backend_integration_agent：纯本地工具类 App 可弱化或跳过
analytics_engineer_agent：若只求最小可用成品，可降级为基础调试埋点
integration_qa_agent：负责联调、自检、build readiness，不负责上架代办
```

---

# 3. 每个 Agent 的职责

```text
agents/team_lead_agent.md                 总控。接收 Boss 粗需求，统筹全案，推进到可交付 handoff。
agents/product_strategy_agent.md         定义 App 定位、目标用户、范围、复杂度、MVP 边界。
agents/feature_architect_agent.md        设计核心功能、用户流程、状态变化、业务规则。
agents/information_architecture_agent.md 设计导航结构、页面树、信息层级、内容组织与关键流程。
agents/design_system_agent.md            设计视觉方向、设计系统、组件规范、iPhone 交互体验。
agents/technical_director_agent.md       锁定 iOS 技术方案、语言、工程模板、依赖方式、模块边界。
agents/ios_engineer_agent.md             定义 iOS 工程结构、页面实现分层、状态管理、启动与依赖注入。
agents/backend_integration_agent.md      定义 API、鉴权、数据同步、推送、文件/媒体、服务端接入方案。
agents/analytics_engineer_agent.md       定义调试埋点、行为日志、错误追踪、校验口径和问题定位能力。
agents/integration_qa_agent.md           负责集成验收、handoff 缺口检查、build readiness 检查。
protocols/quality_protocol.md               团队共享质量协议。
protocols/delivery_protocol.md              最终交付协议。
```

研发相关 agent 的附加要求：

```text
遇到不确定的 iOS API、Swift / SwiftUI / UIKit 行为、权限、生命周期、并发模型、系统组件接入方式时，必须优先查阅 Apple 官方文档
不得用模糊记忆替代官方定义
不得用未经确认的第三方二手说法覆盖 Apple 官方约束
```

---

# 4. 平台优先原则

`目标平台` 是第一层必填项，必须先于交互细节和技术细节锁定。

默认目标平台就是：

```text
iPhone (iOS)
```

如果 Boss 明确要求：

```text
iPhone only
iPhone + iPad
```

团队在研发前必须进一步锁定：

```text
Swift / SwiftUI / UIKit / 混合方案
包管理方式：SPM / CocoaPods（如必须）
项目模板
最低 iOS 版本
关键 SDK / 库版本
构建入口
```

平台未锁定时，不得进入代码研发阶段。

接口和架构未锁定时，也不得并发开展具体实现。

---

# 5. Boss Input 标准模板

Boss 不需要先把 App 全部想清楚。  
你只需要给出粗输入，团队会继续细化。

最小可用模板：

```markdown
# Boss Input

## 目标平台
必填。
默认写：iPhone (iOS)

## App 类型
必填。
一句话即可。

## 核心需求
可选。
用 2-6 句话描述你想要的功能、体验或目标。

## 规模
可选。
示例：MVP / 可交付研发工程 / 第一版完整交付

## 偏好
可选。

## 禁区
可选。
```

推荐模板：

```markdown
# Boss Input

## 目标平台
iPhone (iOS)

## App 类型
一款帮助用户记录日常习惯并通过可视化反馈提升持续性的 App。

## 核心需求
我希望它至少包含习惯创建、每日打卡、统计回顾和提醒能力。
我不想自己先定义完整的信息架构和页面细节，希望团队帮我细化完成。

## 目标用户
希望主要面向 20-40 岁、愿意长期自我管理的 iPhone 用户。

## 规模
先做完整可交付研发工程的 MVP。

## 数据/联网要求
可先本地优先，必要时支持账户同步。

## 偏好
界面简洁、反馈清晰、交互不要太重。

## 禁区
不要复杂社交，不要过度游戏化，不要必须依赖复杂后台。
```

---

# 6. Boss 不需要先想清楚的内容

默认情况下，你不需要先提供：

```text
完整 PRD
完整页面结构
完整交互稿
完整设计系统
完整 iOS 架构
完整接口定义
完整埋点设计
完整 QA 清单
```

这些内容由团队细化完成。

---

# 7. 团队会自动帮你细化的内容

当你给出平台、App 类型和粗需求后，团队默认继续完成：

```text
产品定位与范围
目标用户与复杂度判断
核心功能拆分
信息架构与页面树
关键用户流程
视觉方向与设计系统
iOS 技术方案
平台对应的语言、工程模板、依赖方式
iOS 工程架构
接口与服务端接入方案
调试埋点方案
集成验收与 handoff 清单
```

当以下内容锁定后，团队应默认并发推进研发：

```text
模块边界
页面状态模型
API 契约
依赖方式
关键数据结构
```

---

# 8. 交付标准

团队交付给 Boss 的结果，默认要满足：

```text
目标平台已锁定
语言、依赖、工程模板已锁定
核心功能、页面结构和用户流程可被清晰描述
iOS、后端接入、埋点 owner 清晰
模块依赖和接口边界清晰
build readiness checklist 已完成
无已知 compile blocker
无未声明依赖
无缺失关键资源清单
无未说明的环境前提
关键不确定点已被 Apple 官方文档确认
```

如果达不到这些标准，就不能声称“Boss 可直接接手编译”。

---

# 9. 当前保留文件

当前目录只保留 multi-agent team 本身的 `.md` 文件：

```text
README.md
agents/team_lead_agent.md
agents/product_strategy_agent.md
agents/feature_architect_agent.md
agents/information_architecture_agent.md
agents/design_system_agent.md
agents/technical_director_agent.md
agents/ios_engineer_agent.md
agents/backend_integration_agent.md
agents/analytics_engineer_agent.md
agents/integration_qa_agent.md
protocols/quality_protocol.md
protocols/delivery_protocol.md
```
