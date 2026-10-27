---
id: 2026-10-27-inv-017-do-two-rows-with-the-same
title: Do two rows with the same topic text share one editor state? (FEA-014)
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related:
- 2026-10-27-lr-083-the-review-workspace-is-not-keyed
docs:
- frontend/src/features/review/context/useReviewFlowState.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: investigation
severity: P2
area: frontend/editor
raw_id: INV-017
source_file: docs/launch-readiness/findings/INVESTIGATE.md
---

## Problem

Do two rows with the same topic text share one editor state? (FEA-014). Edits could be saved onto the wrong post.

## Evidence and reproduction

- **Question:** initKey is built from row.topic, so a published post and its draft copy get the same key. Does Save Draft then write into the previous row?
- **Why it matters:** Edits could be saved onto the wrong post.
- **How to settle it:** Read frontend/src/features/review/context/useReviewFlowState.ts:376-397. To settle: open published post P, then its copy via browser history, edit, Save Draft, and check which row changed.
- **Related items:** LR-083
- **Owner:**

## Acceptance criteria

- The question in the title is answered in Attempts with file:line evidence and a clear yes/no.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/INVESTIGATE.md (INV-017). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: raw item is marked hypothesis; merged into LR-083, which says confirmed-by-reading. Not run. Covered by LR-083..
