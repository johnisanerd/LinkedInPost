---
id: 2026-10-27-lr-163-use-cases-md-and-related-docs
title: USE-CASES.md and related docs make stale or false claims about the editor layout, button labels, CSV append and debate features.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j076-publish-now-to-linkedin
- 2026-10-27-j106-bulk-import-by-pasting-campaign-json
related: []
docs:
- USE-CASES.md
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P3
area: docs
raw_id: LR-163
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

USE-CASES.md and related docs make stale or false claims about the editor layout, button labels, CSV append and debate features.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-076, J-106
- **Aliases:** U-J1.6, U-J1.7, U-J1.9, U-J6, U-J8, U-J12b, U-E2E, F-2
- **Evidence:** USE-CASES.md; frontend/src/features/review-editor/screens/EditorScreen.tsx:227-250
- **Repro:** (static check) Open USE-CASES.md and confirm the behaviour described in the summary; then exercise the matching journey (J-076, J-106) to observe it.
- **Fix hint:** Correct the docs to match the shipped behaviour.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Correct the docs to match the shipped behaviour.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-163). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of USE-CASES.md.
