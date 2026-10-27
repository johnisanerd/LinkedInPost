---
id: 2026-10-27-lr-042-setup-py-imports-dotenv-at-the
title: setup.py imports dotenv at the top before the dependency installer runs, so a clean interpreter fails and --web never installs anything.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j001-web-setup-wizard-end-to-end
- 2026-10-27-j002-headless-full-bootstrap-with-python-setup
- 2026-10-27-j007-re-running-setup-py-is-idempotent
related: []
docs:
- setup.py
- setup/python_requirements.py
- requirements.txt
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P1
area: setup/cli
raw_id: LR-042
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

setup.py imports dotenv at the top before the dependency installer runs, so a clean interpreter fails and --web never installs anything.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-001, J-002, J-007
- **Aliases:** SET-009
- **Evidence:** setup.py:55; setup/python_requirements.py:11-16
- **Repro:** static / fresh venv: `python setup.py --web` without `pip install -r requirements.txt`.
- **Fix hint:** Wrap the dotenv import in try/except, run the ensure-deps step first, probe all of requirements.txt.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Wrap the dotenv import in try/except, run the ensure-deps step first, probe all of requirements.txt.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-042). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of setup.py:55.
