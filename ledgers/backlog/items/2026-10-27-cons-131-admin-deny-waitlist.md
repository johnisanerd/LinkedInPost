---
id: 2026-10-27-cons-131-admin-deny-waitlist
title: 'Admin: Deny waitlist'
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
raw_id: CONS-131
source_file: docs/launch-readiness/findings/EXISTING-REVIEWS.md
---

## Problem

Admin: Deny waitlist.

## Evidence and reproduction

- **Source:** docs/launch-readiness/findings/raw/existing-reviews.md section 1, row C12-2
- **Alias:** C12-2
- **Original tag:** HIGH (mapped to P1)
- **Current status:** open
- **Evidence:** AdminPanel.tsx:172-... only Approve (:69); no deny endpoint in worker/service
- **Covered by:** LR-100

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/EXISTING-REVIEWS.md (CONS-131). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: still open in code (AdminPanel.tsx:172-... only Approve (:69); no deny endpoint in worker/service); covered by LR-100.
