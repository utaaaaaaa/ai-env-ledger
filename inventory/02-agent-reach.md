# 🌐 Agent Reach 渠道状态

- **版本**：v1.5.0
- **安装日期**：2026-10-14
- **来源**：`Panniantong/Agent-Reach`（96.9k star，MIT）
- **可执行**：`C:\Users\15937\.workbuddy\binaries\python\envs\default\Scripts\agent-reach.exe`
- **配置目录**：`~/.agent-reach/`（`config.yaml` 存各平台 Cookie）

> ⚠️ `agent-reach doctor` 的计数**偏保守**：它看不到浏览器登录态、不读环境变量、不启动远端服务。
> 官方读数 5/16，**实测可用 12 个**（含 Exa，见下表，2026-10-15 更新）。

---

## 渠道总表（16 个）

| # | 渠道 | 实测状态 | 前置条件 |
|---|---|---|---|
| 1 | 🌐 网页阅读（Jina Reader） | ✅ | 无 |
| 2 | 📺 YouTube 字幕 | ✅ | yt-dlp + `--js-runtimes node` |
| 3 | 📡 RSS/Atom | ✅ | 无 |
| 4 | 📺 B站（完整版） | ✅ | Chrome 登录（账号 Warren-E） |
| 5 | 📕 小红书 | ✅ | Chrome 登录；search 用自建脚本 |
| 6 | 📈 雪球 | ✅ | Cookie（有效期短） |
| 7 | 💬 V2EX | ✅ | 带代理调用 |
| 8 | 🐦 Twitter/X | ✅ | Cookie + 代理（用 `twitter_env.sh`） |
| 9 | 👽 Reddit | ✅ | Chrome 登录 + 梯子 |
| 10 | 📘 Facebook | ✅ | Chrome 登录 |
| 11 | 🐙 GitHub | ✅ | hosts.yml 双写（见下） |
| 12 | 🔍 Exa 语义搜索 | ✅ | **实测可用**（官方免费 MCP 端点，无需 API Key，2026-10-15 验证返回真实结果） |
| 13 | 📷 Instagram | ❌ | 需梯子 + 手机号注册（价值最低，可跳过） |
| 14 | 💼 LinkedIn | ❌ | 需登录 |
| 15 | 🎯 Boss直聘 | ❌ | 需专用 Chrome 登录 zhipin |
| 16 | 🎙️ 小宇宙播客 | ❌ | 需 Groq API Key + ffmpeg |

---

## 凭据存放位置（⚠️ 不含明文）

| 平台 | 凭据位置 | 备注 |
|---|---|---|
| Twitter | `~/.config/bird/credentials.env`（`AUTH_TOKEN` / `CT0`） | 由 `twitter_env.sh` 读取 |
| 雪球 | `~/.agent-reach/config.yaml` → `xueqiu_cookie` | `xq_a_token` + `u` 缺一不可 |
| GitHub | `~/.config/gh/hosts.yml` **和** `%APPDATA%\GitHub CLI\hosts.yml` | **两个位置都要写**，gh 与 Agent Reach 读的不同 |
| 小红书 / Reddit / Facebook / B站 | Chrome 浏览器会话（OpenCLI 扩展） | 不落盘，依赖浏览器登录态 |
| B站/其他走代理的 | `~/.agent-reach/config.yaml` → `bilibili_proxy` | 代理专用键 |
| Exa（MCP 搜索） | `~/.mcporter/mcporter.json` → `baseUrl`（`https://mcp.exa.ai/mcp`） | **不需要 API Key**（官方免费端点）；命令在受管 node workspace，需手动加 PATH |
| 代理 | `~/.agent-reach/config.yaml` → `proxy` | `http://127.0.0.1:7890` |

> **⚠️ 重要结论（2026-10-15 核实）**：**官网 README 明确「完全免费，所有 API 免费」——没有任何渠道要求付费 API Key**（README L96 / L111 / L232）。
> 已跑通渠道全靠 **Cookie（Twitter/雪球）+ PAT（GitHub）+ 浏览器登录态（小红书/Reddit/FB/B站）+ 免费 MCP 端点（Exa）**。
> 全仓库**无 `requires_api_key` 类字段** → 手机端弹窗「标注需要 API Key」来自技能市场元数据，与官方口径不符。
> 唯一沾 key 的是 Groq Whisper（小宇宙/无字幕视频转录，**有免费额度**，可选功能）。
> 手机端等其他设备无法使用本套凭据：文件在本机，且浏览器登录态不可迁移。

---

## 常用命令

```bash
# 体检
agent-reach doctor

# Twitter 搜索（自动加载 Cookie + 代理）
bash scripts/twitter_env.sh twitter search "关键词" -n 5

# 小红书搜索（绕过上游 search bug）
bash scripts/xhs_search.sh "露营装备" 10

# 雪球行情
python -c "from agent_reach.channels.xueqiu import XueqiuChannel; print(XueqiuChannel().get_stock_quote('SH600519'))"

# OpenCLI 扩展状态
opencli doctor
```
