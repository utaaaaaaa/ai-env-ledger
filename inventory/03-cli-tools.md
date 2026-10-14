# 🛠 命令行工具清单

> 所有工具均装入**受管目录**，不污染系统环境。

## Python 侧

| 工具 | 版本 | 绝对路径 | 用途 |
|---|---|---|---|
| `agent-reach` | 1.5.0 | `C:\Users\15937\.workbuddy\binaries\python\envs\default\Scripts\agent-reach.exe` | 互联网渠道管理 |
| `yt-dlp` | 2026.08.19 | 同目录 `yt-dlp.exe` | YouTube 字幕 |
| `twitter` | 0.8.6 | 同目录 `twitter.exe` | Twitter 搜索（⚠️ 入口名是 `twitter` 不是 `twitter-cli`；PyPI 版 0.8.5 已过时） |

**运行时必须加入 PATH**：
```bash
export PATH="/c/Users/15937/.workbuddy/binaries/python/envs/default/Scripts:$PATH"
```

---

## Node 侧

| 工具 | 版本 | 绝对路径 | 用途 |
|---|---|---|---|
| `opencli` | 1.8.8 | `C:\Users\15937\.workbuddy\binaries\node\versions\22.22.2-6\opencli` | 浏览器会话驱动 |
| `mcporter` | 0.9.0 | `...\node\workspace\node_modules\.bin\mcporter.cmd` | MCP 客户端 / Exa 搜索 |
| `npm` | 10.9.7 | `...\node\versions\22.22.2-6\npm.cmd` | 包管理（源用 npmmirror） |

**运行时必须加入 PATH**：
```bash
export PATH="/c/Users/15937/.workbuddy/binaries/node/versions/22.22.2-6:/c/Users/15937/.workbuddy/binaries/node/workspace/node_modules/.bin:$PATH"
```

---

## 系统级

| 工具 | 用途 | 备注 |
|---|---|---|
| `gh` | GitHub CLI | 已配置认证（双 hosts.yml） |
| `git` | 版本控制 | 走代理见 `04-network.md` |
| `curl` | 网络请求 | 沙箱下 `github.com` 与 `raw.githubusercontent.com` 直连被拦，需走代理 |

---

## OpenCLI 扩展

- **Chrome 扩展版本**：v1.0.24
- **Daemon 端口**：19825（使用时自动启动）
- **安装地址**：`https://chromewebstore.google.com/detail/opencli/ildkmabpimmkaediidaifkhjpohdnifk`
- 解锁渠道：Reddit / Facebook / Instagram / 小红书 / B站字幕
