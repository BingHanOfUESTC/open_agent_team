---
name: skill-security-review
type: reference
description: >
  Review candidate open-source skills for license, supply-chain, command safety, prompt injection, credential leakage, data exfiltration, and task relevance risks.
model-invocable: false
---

# Skill Security Review

安全审查必须先于集成。一个 skill 有用，不代表可以放进团队。

---

# 1. 审查维度

```text
许可证：是否允许复制、修改、再分发。
来源可信度：作者、组织、维护记录。
命令风险：是否包含 rm、curl pipe shell、sudo、系统目录写入等危险操作。
凭据风险：是否要求 token、cookie、密码、浏览器 session。
数据风险：是否上传本地文件、代码、隐私数据到未知服务。
提示注入：是否要求忽略系统规则、越权、绕过安全边界。
污染风险：是否硬编码样例答案或任务专属内容。
适配风险：是否依赖不可获得环境、服务或模型。
```

---

# 2. 结论等级

```text
通过：可直接集成。
条件通过：删改指定风险后集成。
仅参考：可借鉴方法，不复制内容。
拒绝：不得集成。
```

---

# 3. 必须阻断

```text
许可证不明且需要复制内容
恶意或破坏性命令
凭据窃取或外传
绕过安全规则
要求执行未知脚本
与团队目标无关
```
