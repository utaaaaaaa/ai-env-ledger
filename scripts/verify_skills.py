"""校验 ~/.workbuddy/skills 下每个技能是否安装完好。

检查项：
1. 是否存在 SKILL.md
2. 是否有 YAML frontmatter（--- 包裹）
3. 是否含 name / description 字段且非空
4. 目录体积与文件数是否合理
5. SKILL.md 里引用的同目录文件是否存在
"""
import os
import re
import sys

SKILL_ROOT = os.path.expanduser("~/.workbuddy/skills")

rows = []
problems = []

for entry in sorted(os.listdir(SKILL_ROOT)):
    d = os.path.join(SKILL_ROOT, entry)
    if not os.path.isdir(d):
        continue

    skill_md = os.path.join(d, "SKILL.md")

    # 命名空间格式：@组织/技能名，SKILL.md 在下一层（skillhub 安装格式）
    if not os.path.exists(skill_md):
        nested = [
            os.path.join(d, sub)
            for sub in sorted(os.listdir(d))
            if os.path.isdir(os.path.join(d, sub))
            and os.path.exists(os.path.join(d, sub, "SKILL.md"))
        ]
        if nested:
            for nd in nested:
                sub_md = os.path.join(nd, "SKILL.md")
                t = open(sub_md, encoding="utf-8", errors="ignore").read()
                m = re.match(r"^---\s*\n(.*?)\n---\s*\n", t, re.S)
                nm = re.search(r"^name:\s*(.+)$", m.group(1), re.M) if m else None
                dm = re.search(r"^(?:description|desc):\s*(.+)$", m.group(1), re.M | re.S) if m else None
                desc = " ".join(x.strip() for x in dm.group(1).splitlines()).strip() if dm else ""
                nf = sum(len(f) for _, _, f in os.walk(nd))
                sz = sum(
                    os.path.getsize(os.path.join(r, f))
                    for r, _, fs in os.walk(nd)
                    for f in fs
                ) / 1024
                status = "OK" if (m and nm and desc) else "元数据不全"
                if status != "OK":
                    problems.append((entry + "/" + os.path.basename(nd), status, []))
                rows.append((
                    f"{entry}/{os.path.basename(nd)}（命名空间）",
                    status,
                    len(nm.group(1).strip()) if nm else 0,
                    len(desc),
                    nf,
                    sz,
                ))
            continue

    has_md = os.path.exists(skill_md)
    name = desc = ""
    fm_ok = False
    size = 0
    nfiles = 0
    missing_refs = []

    for root, _, files in os.walk(d):
        for f in files:
            p = os.path.join(root, f)
            nfiles += 1
            try:
                size += os.path.getsize(p)
            except OSError:
                pass

    if has_md:
        text = open(skill_md, encoding="utf-8", errors="ignore").read()
        m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
        if m:
            fm_ok = True
            fm = m.group(1)
            nm = re.search(r"^name:\s*(.+)$", fm, re.M)
            dm = re.search(r"^(?:description|desc):\s*(.+)$", fm, re.M | re.S)
            name = nm.group(1).strip() if nm else ""
            if dm:
                desc = " ".join(x.strip() for x in dm.group(1).splitlines()).strip()
        # 检查正文里引用的相对路径文件是否存在（形如 references/xxx.md 或 xxx.py）
        # 排除 URL 内的路径片段（如 https://x.com/assets/a.json）
        for ref in set(re.findall(r"`?((?:references|scripts|assets)/[\w./-]+)`?", text)):
            positions = [m.start() for m in re.finditer(re.escape(ref), text)]
            in_url = False
            for idx in positions:
                ctx = text[max(0, idx - 60):idx + len(ref) + 10]
                if "://" in ctx:
                    in_url = True
                    break
            if in_url:
                continue  # 外部 URL，不是本地引用
            if not os.path.exists(os.path.join(d, ref)):
                missing_refs.append(ref)

    status = "OK"
    if not has_md:
        status = "缺 SKILL.md"
    elif not fm_ok:
        status = "缺 frontmatter"
    elif not name or not desc:
        status = "元数据不全"
    elif missing_refs:
        status = f"引用缺失x{len(missing_refs)}"

    if status != "OK":
        problems.append((entry, status, missing_refs[:3]))

    rows.append((entry, status, len(name), len(desc), nfiles, size / 1024))

W = 34
print(f"{'技能目录':<{W}} {'状态':<14} {'name':<6}{'desc':<7}{'文件':<6}{'体积KB':>9}")
print("-" * 84)
for entry, status, nl, dl, nf, kb in rows:
    print(f"{entry:<{W}} {status:<14} {nl:<6}{dl:<7}{nf:<6}{kb:>9.0f}")

print("-" * 84)
ok = sum(1 for r in rows if r[1] == "OK")
print(f"合计 {len(rows)} 个技能目录：{ok} 个完好，{len(rows)-ok} 个有问题")

if problems:
    print("\n问题明细：")
    for entry, status, refs in problems:
        print(f"  - {entry}: {status}" + (f"  缺失 {refs}" if refs else ""))