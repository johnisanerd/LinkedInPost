---
id: 2026-10-27-lr-129-the-wizard-deploy-step-timeout-cannot
title: The wizard deploy step timeout cannot fire on a silent hang, concurrent starts race, and the stream blocks forever
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j005-wizard-deploy-step-streaming-logs-timeout
related: []
docs:
- setup/wizard/steps/deploy.py
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P2
area: setup/wizard
raw_id: LR-129
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

The wizard deploy step timeout cannot fire on a silent hang, concurrent starts race, and the stream blocks forever.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-005
- **Aliases:** SET-025
- **Evidence:** setup/wizard/steps/deploy.py:20-91
- **Repro:** static.
- **Fix hint:** Use communicate(timeout) or a Timer, lock around start, per-run queue.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Use communicate(timeout) or a Timer, lock around start, per-run queue.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-129). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of setup/wizard/steps/deploy.py:20-91.
