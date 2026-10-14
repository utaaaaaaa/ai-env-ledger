#!/bin/bash
# xhs_search.sh — search Xiaohongshu notes via OpenCLI browser session.
# Works around the broken `opencli xiaohongshu search` filter-panel adapter
# by driving the browser session directly and reading the result list.
#
# Usage: bash xhs_search.sh "关键词" [数量]

set -euo pipefail

NODE_BIN="/c/Users/15937/.workbuddy/binaries/node/versions/22.22.2-6"
export PATH="$NODE_BIN:$PATH"

KEYWORD="${1:-}"
LIMIT="${2:-10}"

if [ -z "$KEYWORD" ]; then
  echo "usage: bash xhs_search.sh <keyword> [limit]" >&2
  exit 1
fi

# percent-encode the keyword for the URL
ENCODED=$("$NODE_BIN/node.exe" -e "console.log(encodeURIComponent(process.argv[1]))" "$KEYWORD")
URL="https://www.xiaohongshu.com/search_result?keyword=${ENCODED}"

opencli browser xhs open "$URL" >/dev/null
sleep 3

opencli browser xhs find \
  --css "section.note-item a.title, .note-item a.title" \
  --limit "$LIMIT" --text-max 60 \
| "$NODE_BIN/node.exe" -e '
const fs = require("fs");
let raw = "";
process.stdin.on("data", d => raw += d);
process.stdin.on("end", () => {
  let j;
  try { j = JSON.parse(raw); } catch { console.log(raw.slice(0, 800)); process.exit(0); }
  const items = j.entries || [];
  if (!items.length) { console.log("no results"); process.exit(0); }
  items.forEach((it, n) => {
    const a = it.attrs || {};
    const href = (a.href || "").split("?")[0];
    console.log(`${n + 1}. ${it.text}\n   https://www.xiaohongshu.com${href}`);
  });
});'