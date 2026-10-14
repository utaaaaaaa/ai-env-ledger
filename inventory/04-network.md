# 🌍 网络与代理配置

## mihomo 代理核心

| 项 | 值 |
|---|---|
| 监听端口 | `127.0.0.1:7890`（HTTP + SOCKS 混合） |
| 核心程序 | `C:\Users\15937\WorkBuddy\2026-10-02-01-51-17\mihomo_core\mihomo-windows-amd64-compatible.exe` |
| 配置文件 | `C:\Users\15937\.config\clash\profiles\1791642004247.yml`（零界订阅） |
| 数据目录 | `C:\Users\15937\.config\clash`（含 Country.mmdb） |
| RESTful API | `127.0.0.1:9090` |

**启动命令**：
```bash
"C:/Users/15937/WorkBuddy/2026-10-02-01-51-17/mihomo_core/mihomo-windows-amd64-compatible.exe" \
  -f "C:/Users/15937/.config/clash/profiles/1791642004247.yml" \
  -d "C:/Users/15937/.config/clash"
```
约 12 秒后 7890 可用。

**开机自启**：`C:\Users\15937\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\mihomo_proxy_autostart.vbs`（隐藏窗口运行，删除该文件即取消）

**探活判据**：`curl http://127.0.0.1:7890` 返回 HTTP 400 即代表在监听。

---

## 沙箱网络可达性（实测 2026-10-13）

| 域名 | 直连 | 说明 |
|---|---|---|
| `api.github.com` | ✅ 200 | 无需代理 |
| `codeload.github.com` | ✅ 301 | 下载 zip |
| `objects.githubusercontent.com` | ✅ | |
| `github.com` | ❌ 000 | **需代理** |
| `raw.githubusercontent.com` | ❌ 000 | **需代理**（走代理后正常） |
| `www.v2ex.com` | ❌ 000 | **需代理**（走代理 200） |

---

## ⚠️ 三个已知坑

1. **沙箱自带 `HTTP_PROXY=127.0.0.1:7468`**：会劫持代理导致调用静默失败。自建脚本已强制覆盖为 `7890`，可用 `TWITTER_PROXY` 覆盖。
2. **代理管不到 Chrome**：代理只作用于命令行进程，Chrome 访问被墙站点需用户自己的梯子。
3. **Clash 桌面端冲突**：CFW 与 mihomo 都占 7890，切换时先杀掉 mihomo 进程。

---

## git 走代理

```bash
git -c http.proxy=http://127.0.0.1:7890 clone https://github.com/xxx/yyy.git
# 或
export http_proxy=http://127.0.0.1:7890 https_proxy=http://127.0.0.1:7890
```

## pip / npm 源

- npm：`--registry=https://registry.npmmirror.com`
- pip：PyPI 直连可用（`pypi.org` 200）
