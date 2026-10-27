---
id: 2026-10-27-cons-044-addtopic-save-toast-saved-ns-ago
title: AddTopic save toast / "Saved Ns ago"
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related:
- 2026-10-27-lr-183-there-is-no-transient-toast-system
docs: []
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: ux-gap
severity: P1
area: frontend/queue
raw_id: CONS-044
source_file: docs/launch-readiness/findings/EXISTING-REVIEWS.md
---

## Problem

AddTopic save toast / "Saved Ns ago".

## Evidence and reproduction

- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C04-5
- **Alias:** C04-5
- **Original tag:** HIGH (mapped to P1)
- **Current status:** open
- **Evidence:** features/add-topic/AddTopicPage.tsx:296 onSaved only; no toast system exists in app
- **Covered by:** LR-183

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/EXISTING-REVIEWS.md (CONS-044). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: still open in code (features/add-topic/AddTopicPage.tsx:296 onSaved only; no toast system exists in app); covered by LR-183.
