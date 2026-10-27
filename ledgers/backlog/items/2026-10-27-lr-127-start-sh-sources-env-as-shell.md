---
id: 2026-10-27-lr-127-start-sh-sources-env-as-shell
title: start.sh sources .env as shell code (mangles JSON values, executes content) and has no cleanup trap on Ctrl+C
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j001-web-setup-wizard-end-to-end
- 2026-10-27-j011-local-development-loop
- 2026-10-27-j014-start-sh-unified-launcher
related: []
docs:
- start.sh
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P2
area: setup/cli
raw_id: LR-127
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

start.sh sources .env as shell code (mangles JSON values, executes content) and has no cleanup trap on Ctrl+C.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-001, J-011, J-014
- **Aliases:** SET-029
- **Evidence:** start.sh:80-85,221-240,255-273
- **Repro:** static.
- **Fix hint:** Parse .env with python-dotenv or grep, add a trap to kill background processes.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Parse .env with python-dotenv or grep, add a trap to kill background processes.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-127). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of start.sh:80-85,221-240,255-273.
