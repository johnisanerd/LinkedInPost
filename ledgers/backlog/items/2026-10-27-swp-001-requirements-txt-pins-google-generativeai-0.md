---
id: 2026-10-27-swp-001-requirements-txt-pins-google-generativeai-0
title: requirements.txt pins google-generativeai==0.8.2, a deprecated package that nothing in the repo imports.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j001-web-setup-wizard-end-to-end
- 2026-10-27-j011-local-development-loop
related: []
docs:
- setup.md
- requirements.txt
- setup.py
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: investigation
severity: P3
area: setup/deps
raw_id: SWP-001
source_file: docs/launch-readiness/findings/SWEEP.md
---

## Problem

requirements.txt pins google-generativeai==0.8.2, a deprecated package that nothing in the repo imports. An unused pinned package can make pip fail or downgrade protobuf against google-api-python-client>=2.157, breaking the first-run install for no benefit.

## Evidence and reproduction

- **Source:** docs/launch-readiness/findings/raw/setup.md SET-033 (the "hypothesis on protobuf conflicts" clause, setup.md:333)
- **Journeys:** J-001, J-011
- **Confidence:** confirmed-by-reading
- **Evidence:** requirements.txt:6; grep for generativeai over automations/, scripts/, setup/, setup.py, frontend/server finds only requirements.txt
- **Why it matters:** An unused pinned package can make pip fail or downgrade protobuf against google-api-python-client>=2.157, breaking the first-run install for no benefit.
- **Repro or check:** `grep -rn generativeai --include=*.py .` (expect no hit outside node_modules), then in a clean venv `pip install -r requirements.txt && pip check`.
- **Fix hint:** Delete the google-generativeai line; if pip check passes without it nothing else is needed.

## Acceptance criteria

- The question in the title is answered in Attempts with file:line evidence and a clear yes/no.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Delete the google-generativeai line; if pip check passes without it nothing else is needed.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/SWEEP.md (SWP-001). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: requirements.txt:6; grep generativeai over automations scripts setup setup.py frontend/server.
