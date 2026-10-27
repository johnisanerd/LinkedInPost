#!/usr/bin/env python3
"""Rebuild the Items table of LEDGER.md from findings/*.md headings (`### ID Pn area - title`, ID = 1-4 letters, dash, digits), preserving Status/Verified
columns already recorded in LEDGER.md. Run from anywhere: python3 launch-release/build_ledger.py"""
import re, pathlib
root = pathlib.Path(__file__).parent
led = root / "LEDGER.md"
old = {}  # status.json is the source of truth for Status/Verified
import json
if (root/"status.json").exists():
    for k,v in json.load(open(root/"status.json")).items():
        old[k]=(v[0],v[1])
rows = []
for f in sorted((root / "findings").glob("*.md")):
    for m in re.finditer(r"^#{2,4}\s+([A-Z]{1,4}-\d+)\s*[·:-]?\s*(P[0-3])\s*[·:-]?\s*(.+?)\s+[·–:-]\s+(.+)$", f.read_text(), re.M):
        i, sev, area, title = m.groups()
        st, ver = old.get(i, ("open", ""))
        rows.append((sev, i, area, title.strip()[:150].replace("|", "/"), st, ver, f.name))
rows.sort(key=lambda r: (r[0], r[1]))
cnt = {}
for r in rows:
    cnt[(r[0], r[4])] = cnt.get((r[0], r[4]), 0) + 1
summ = "\n".join(f"- {s}: " + ", ".join(f"{st} {n}" for (s2, st), n in sorted(cnt.items()) if s2 == s) for s in ("P0", "P1", "P2", "P3") if any(k[0] == s for k in cnt))
head = led.read_text().split("## Summary")[0] if led.exists() else "# Release delivery ledger\n\n"
tail = ""
if led.exists():
    t = led.read_text()
    k = t.find("## Frozen / post-launch")
    tail = t[k:] if k >= 0 else ""
body = ["## Summary", summ, "", "## Items", "| ID | Sev | Area | Title | Status | Verified | Source |", "|---|---|---|---|---|---|---|"]
body += [f"| {i} | {sev} | {a} | {t} | {st} | {ver} | {src} |" for sev, i, a, t, st, ver, src in rows]
led.write_text(head + "\n".join(body) + "\n\n" + (tail or "## Frozen / post-launch (explicitly not in this release)\n\n## Verification log\n"))
print(len(rows), "items")
