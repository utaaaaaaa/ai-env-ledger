#!/bin/bash
# ensure_proxy.sh — ensure mihomo proxy (127.0.0.1:7890) is alive; start it if dead.
# Usage: bash ensure_proxy.sh   (exit 0 = proxy ready)
# Probing: connection refused -> dead ; any HTTP response (incl. 400) -> alive.

PORT=7890
MIHOMO="C:/Users/15937/WorkBuddy/2026-10-02-01-51-17/mihomo_core/mihomo-windows-amd64-compatible.exe"
PROFILE="C:/Users/15937/.config/clash/profiles/1791642004247.yml"
DATADIR="C:/Users/15937/.config/clash"

probe() {
  curl -s -m 4 -o /dev/null "http://127.0.0.1:$PORT" 2>/dev/null
}

if probe; then
  echo "PROXY: ALIVE (port $PORT responding)"
  exit 0
fi

echo "PROXY: DEAD, starting mihomo core..."
"$MIHOMO" -f "$PROFILE" -d "$DATADIR" >/dev/null 2>&1 &

for i in $(seq 1 15); do
  sleep 1
  if probe; then
    echo "PROXY: READY after ${i}s"
    exit 0
  fi
done

echo "PROXY: FAILED to start within 15s"
exit 1
