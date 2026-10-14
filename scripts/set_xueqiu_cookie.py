"""
set_xueqiu_cookie.py — write Xueqiu cookies into Agent Reach config.

Accepts EITHER:
  1) Cookie-Editor "Header String" export:  u=xxx; xq_a_token=yyy; ...
  2) Cookie-Editor "JSON" export:           [{"domain":".xueqiu.com","name":"u","value":"..."}, ...]

Usage:
  python set_xueqiu_cookie.py --file cookies.txt          # raw string in file
  python set_xueqiu_cookie.py --file cookies.json         # JSON export in file
  cat cookies.txt | python set_xueqiu_cookie.py --stdin
  python set_xueqiu_cookie.py --file c.txt --dry-run      # preview only
"""
import argparse
import json
import os
import sys

CONFIG = os.path.expanduser("~/.agent-reach/config.yaml")
NEEDED = ("xq_a_token", "u", "device_id", "s", "xq_r_token", "xq_is_fresh")


def load_text(path, use_stdin):
    if use_stdin:
        return sys.stdin.read()
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def to_cookie_string(raw):
    raw = raw.strip()
    if not raw:
        raise SystemExit("empty input")
    # JSON export -> filter xueqiu domains -> rebuild header string
    if raw[0] in "[{":
        items = json.loads(raw)
        pairs = {}
        for it in items:
            dom = str(it.get("domain", ""))
            if "xueqiu" not in dom:
                continue
            name, val = it.get("name"), it.get("value")
            if name and val is not None:
                pairs[name] = val
        if not pairs:
            raise SystemExit("no xueqiu.com cookies found in JSON export")
        return "; ".join(f"{k}={v}" for k, v in pairs.items()), pairs
    # already a header string
    pairs = {}
    for part in raw.split(";"):
        if "=" in part:
            k, v = part.split("=", 1)
            pairs[k.strip()] = v.strip()
    return "; ".join(f"{k}={v}" for k, v in pairs.items()), pairs


def yaml_quote(value):
    # single-quoted YAML scalar; escape embedded single quotes by doubling
    return "'" + value.replace("'", "''") + "'"


def write_config(cookie_str, dry_run=False):
    lines = []
    if os.path.exists(CONFIG):
        with open(CONFIG, "r", encoding="utf-8") as f:
            lines = f.read().splitlines()
    kept = [ln for ln in lines if not ln.strip().startswith("xueqiu_cookie:")]
    kept.append(f"xueqiu_cookie: {yaml_quote(cookie_str)}")
    new_text = "\n".join(kept) + "\n"
    if dry_run:
        print("[dry-run] would write to", CONFIG)
        print("[dry-run] keys:", ", ".join(sorted(cookie_str.split("; ")[0].split("=")[0:1])))
        return
    os.makedirs(os.path.dirname(CONFIG), exist_ok=True)
    with open(CONFIG, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("wrote xueqiu_cookie ->", CONFIG)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file")
    ap.add_argument("--stdin", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    if not args.file and not args.stdin:
        ap.error("need --file or --stdin")

    raw = load_text(args.file, args.stdin)
    cookie_str, pairs = to_cookie_string(raw)

    missing = [k for k in ("xq_a_token", "u") if k not in pairs]
    print("parsed cookies:", ", ".join(sorted(pairs.keys())))
    if missing:
        print("WARNING missing critical keys:", ", ".join(missing),
              "-> quote API may return 400")

    write_config(cookie_str, args.dry_run)


if __name__ == "__main__":
    main()