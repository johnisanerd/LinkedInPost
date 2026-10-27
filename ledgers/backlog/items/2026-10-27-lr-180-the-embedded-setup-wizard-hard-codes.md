---
id: 2026-10-27-lr-180-the-embedded-setup-wizard-hard-codes
title: The embedded setup wizard hard-codes http://localhost:3456 and is reachable in production at /setup
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j010-in-app-setup-page-in-a
related: []
docs:
- frontend/src/features/setup-wizard/setupService.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P3
area: frontend/setup
raw_id: LR-180
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

The embedded setup wizard hard-codes http://localhost:3456 and is reachable in production at /setup.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-010
- **Aliases:** FEB-028
- **Evidence:** frontend/src/features/setup-wizard/setupService.ts:68-132; frontend/src/features/setup-wizard/steps/FinalStep.tsx:144
- **Repro:** admin clicks Setup on a deployed site.
- **Fix hint:** Hide Setup unless dev/local and align the port.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Hide Setup unless dev/local and align the port.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-180). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of frontend/src/features/setup-wizard/setupService.ts:68-132.
