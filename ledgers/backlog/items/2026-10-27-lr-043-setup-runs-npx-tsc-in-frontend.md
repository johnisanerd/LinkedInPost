---
id: 2026-10-27-lr-043-setup-runs-npx-tsc-in-frontend
title: setup runs npx tsc in frontend/ without installing dependencies, so setup aborts on a clean clone, and the check does not run on every path.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j001-web-setup-wizard-end-to-end
- 2026-10-27-j002-headless-full-bootstrap-with-python-setup
- 2026-10-27-j009-tsc-noemit-gate-inside-setup-py
related: []
docs:
- setup/cloudflare.py
- setup.py
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P1
area: setup/cli
raw_id: LR-043
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

setup runs npx tsc in frontend/ without installing dependencies, so setup aborts on a clean clone, and the check does not run on every path.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-001, J-002, J-009
- **Aliases:** SET-010, ARCH-015
- **Evidence:** setup/cloudflare.py:575-586; setup.py:98-104
- **Repro:** static. Fresh clone, `python setup.py --cloudflare`.
- **Fix hint:** npm ci in frontend/ first (or skip when absent), and fix the docs or run the check on all paths including generation-worker.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

npm ci in frontend/ first (or skip when absent), and fix the docs or run the check on all paths including generation-worker.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-043). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of setup/cloudflare.py:575-586.
