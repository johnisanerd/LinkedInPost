---
id: 2026-10-27-cons-130-admin-replace-prompt-budget-edit
title: 'Admin: replace prompt() budget edit'
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related:
- 2026-10-27-lr-100-admin-panel-actions-have-no-error
docs: []
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: ux-gap
severity: P1
area: frontend/admin
raw_id: CONS-130
source_file: docs/launch-readiness/findings/EXISTING-REVIEWS.md
---

## Problem

Admin: replace prompt() budget edit.

## Evidence and reproduction

- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C12-1
- **Alias:** C12-1
- **Original tag:** HIGH (mapped to P1)
- **Current status:** open
- **Evidence:** features/saas/AdminPanel.tsx:79 (native prompt; silently returns on invalid input)
- **Covered by:** LR-100

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/EXISTING-REVIEWS.md (CONS-130). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: still open in code (native prompt; silently returns on invalid input); covered by LR-100.
