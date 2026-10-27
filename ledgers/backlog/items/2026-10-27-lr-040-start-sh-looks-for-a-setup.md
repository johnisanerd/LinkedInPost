---
id: 2026-10-27-lr-040-start-sh-looks-for-a-setup
title: start.sh looks for a setup/setup.py that does not exist, silently skips provisioning in production mode, and never starts the worker.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j001-web-setup-wizard-end-to-end
- 2026-10-27-j011-local-development-loop
- 2026-10-27-j014-start-sh-unified-launcher
related: []
docs:
- start.sh
- AGENTS.md
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P1
area: setup/cli
raw_id: LR-040
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

start.sh looks for a setup/setup.py that does not exist, silently skips provisioning in production mode, and never starts the worker.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-001, J-011, J-014
- **Aliases:** ARCH-005
- **Evidence:** start.sh:176-178,204
- **Repro:** (static check) Open start.sh:176-178,204 and confirm the behaviour described in the summary; then exercise the matching journey (J-001, J-011, J-014) to observe it.
- **Fix hint:** Point to $PROJECT_ROOT/setup.py, fail loudly if missing, and start the worker or correct AGENTS.md.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Point to $PROJECT_ROOT/setup.py, fail loudly if missing, and start the worker or correct AGENTS.md.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-040). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of start.sh:176-178,204.
