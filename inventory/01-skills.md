# 🧩 技能包清单

安装位置：`C:\Users\15937\.workbuddy\skills\`（用户级，所有会话生效）

---

## Anthropic 官方技能（15 个）

- **来源**：`anthropics/skills`（180.9k star）
- **安装日期**：2026-10-14
- **许可证**：Apache-2.0
- **审计**：通过（0 恶意特征）

| 技能 | 用途 | 状态 |
|---|---|---|
| `anthropic-mcp-builder` | 开发高质量 MCP 服务器（Python FastMCP / TS SDK） | ✅ |
| `anthropic-webapp-testing` | Web 应用自动化测试（Playwright） | ✅ |
| `anthropic-claude-api` | Claude API 工程实践、提示词缓存 | ✅ |
| `anthropic-frontend-design` | 前端视觉设计与动效 | ✅ |
| `anthropic-algorithmic-art` | 算法生成艺术（p5.js / 流场） | ✅ |
| `anthropic-canvas-design` | 海报、画布类视觉设计 | ✅ |
| `anthropic-theme-factory` | 10 套预设主题快速套用 | ✅ |
| `anthropic-brand-guidelines` | Anthropic 品牌规范 | ✅ |
| `anthropic-internal-comms` | 内部沟通文书 | ✅ |
| `anthropic-doc-coauthoring` | 文档协同写作流程 | ✅ |
| `anthropic-academy-guide` | 教学/课程材料 | ✅ |
| `anthropic-skill-creator` | 教助手造新技能（能力自扩展） | ✅ |
| `anthropic-slack-gif-creator` | Slack 动图制作 | ✅ |
| `anthropic-web-artifacts-builder` | 单文件网页产物 | ✅ |
| `anthropic-discernment-nudge` | 判断力提示 | ✅ |

### ⏸ 未安装（4 个，许可证受限）

| 技能 | 原因 |
|---|---|
| `docx` | © 2025 Anthropic, PBC，受 Anthropic 服务条款约束（source-available，非开源） |
| `pdf` | 同上 |
| `pptx` | 同上 |
| `xlsx` | 同上 |

---

## Agent Reach 技能（1 个）

| 技能 | 位置 | 用途 | 状态 |
|---|---|---|---|
| `agent-reach` | `C:\Users\15937\.agents\skills\agent-reach` | 互联网渠道调用指南 | ✅ |

---

## 本仓库自建 / 其他（3 个）

| 技能 | 用途 | 状态 |
|---|---|---|
| `find-skill-skillhub__skillhub` | 从 SkillHub 搜索安装技能 | ✅ |
| `flight-price-api-fallback` | 机票价格降级数据源（Kiwi API） | ✅ |
| `@indiv-yaoyao/gh-cli-readonly-agent` | gh CLI 只读操作规范 | ✅ |

---

## 社区技能（skills.sh 2026 榜单 · 4 个）

- **来源**：SkillHub 社区源，装在 `~/.workbuddy/skills/@<命名空间>/`
- **安装日期**：2026-10-16
- **触发**：用户发来榜单截图，点名安装第 2 / 9 / 10 名

| 榜单排名 | 技能（命名空间/名称） | 用途 | 状态 |
|---|---|---|---|
| 🥈 2 | `@user_9ea429aa/grill-me` | 方案追问入口（自身仅 18 行） | ✅ 需配合下一条 |
| — | `@user_692c63a9/plan-grilling` | **grill-me 的实现依赖**：逐问深挖方案决策树 | ✅ 补装 |
| 9 | `@user_0b46df4a/mp-handoff` | 把对话压缩成交接文档给下一个 agent（Matt Pocock 原版镜像，MIT） | ✅ |
| 10 | `@clawhub_ivangdavila/triage` | 任务优先级 P0–P3 自动学习与分流 | ✅ |

> **依赖坑（重要）**：`grill-me` 本体只有一句「Load and execute the `plan-grilling` skill」——**少了 plan-grilling 就是空壳**，已一并补装，依赖链闭合。
> **安全审计**：4 个技能均为纯 Markdown 指令，无脚本、无外发请求、无凭据读取；`mp-handoff` 反而明确要求对 API key / 密码脱敏。
> **版本选择**：市场上同名技能有多个作者版本（grill-me 有 11 个），本次按榜单截图的中文描述精确匹配——如 handoff 选「对话交接」语义的 mp-handoff，而非 Obsidian 库版本。
