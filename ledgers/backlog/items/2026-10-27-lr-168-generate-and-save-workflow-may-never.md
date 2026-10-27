---
id: 2026-10-27-lr-168-generate-and-save-workflow-may-never
title: Generate-and-save workflow may never save because the card is returned from inside a setState updater
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j061-custom-workflows-post-types
related: []
docs:
- frontend/src/features/review/context/useReviewFlowActions.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: investigation
severity: P3
area: frontend/editor
raw_id: LR-168
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Generate-and-save workflow may never save because the card is returned from inside a setState updater. Suspected, not confirmed (see Confidence in the evidence).

## Evidence and reproduction

- **Confidence:** hypothesis
- **Journeys:** J-061
- **Aliases:** FEA-029
- **Evidence:** frontend/src/features/review/context/useReviewFlowActions.ts:344-357
- **Repro:** Styles tab > pick a card > "Generate and save"; check whether a custom workflow appears.
- **Fix hint:** Build the card object before calling setGeneratedCards and return it.

## Acceptance criteria

- The question in the title is answered in Attempts with file:line evidence and a clear yes/no.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Build the card object before calling setGeneratedCards and return it.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-168). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: hypothesis from static reading of frontend/src/features/review/context/useReviewFlowActions.ts:344-357; confirm by running the Repro and observing the described behaviour.
