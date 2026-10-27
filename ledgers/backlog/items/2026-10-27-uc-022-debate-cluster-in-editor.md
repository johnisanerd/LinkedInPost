---
id: 2026-10-27-uc-022-debate-cluster-in-editor
title: Debate/cluster "in editor"
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related:
- 2026-10-27-lr-163-use-cases-md-and-related-docs
docs: []
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: wiring-gap
severity: P2
area: frontend/use-cases
raw_id: UC-022
source_file: docs/launch-readiness/findings/EXISTING-REVIEWS.md
---

## Problem

Debate/cluster "in editor".

## Evidence and reproduction

- **Source:** docs/launch-readiness/findings/raw/existing-reviews.md section 2, row U-J12b
- **Alias:** U-J12b
- **Original tag:** ✅ (no severity given, defaulted to P2)
- **Current status:** partial
- **Evidence:** consumers are feed/DraftContextView.tsx:111,143,159, ArticleDetailView.tsx:189 (lives in Feed, not editor sidebar)
- **Covered by:** LR-163

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/EXISTING-REVIEWS.md (UC-022). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: partial; still open in code (lives in Feed, not editor sidebar); covered by LR-163.
