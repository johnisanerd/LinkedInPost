---
id: 2026-10-27-cons-087-merge-approve-publish-semantics
title: Merge Approve+Publish semantics
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related:
- 2026-10-27-lr-026-the-editor-footer-publish-posts-immediately
docs: []
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: ux-gap
severity: P1
area: frontend/publish
raw_id: CONS-087
source_file: docs/launch-readiness/findings/EXISTING-REVIEWS.md
---

## Problem

Merge Approve+Publish semantics.

## Evidence and reproduction

- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C07-6
- **Alias:** C07-6
- **Original tag:** HIGH (mapped to P1)
- **Current status:** open
- **Evidence:** EditorScreen.tsx:357,382 handleApprove still in footer
- **Covered by:** LR-026

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/EXISTING-REVIEWS.md (CONS-087). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: still open in code (EditorScreen.tsx:357,382 handleApprove still in footer); covered by LR-026.
