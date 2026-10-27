---
id: 2026-10-27-inv-012-does-the-worker-reject-over-length
title: Does the worker reject over-length posts before changing status? (FEA-025)
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related:
- 2026-10-27-lr-159-there-is-no-per-channel-length
docs:
- worker/src/index.ts
- frontend/src/features/review/context/useReviewFlowActions.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: investigation
severity: P2
area: worker/publish
raw_id: INV-012
source_file: docs/launch-readiness/findings/INVESTIGATE.md
---

## Problem

Does the worker reject over-length posts before changing status? (FEA-025). Long posts could leave a row Approved but unpublished with a provider error.

## Evidence and reproduction

- **Question:** The frontend has only an empty-text check. Does the worker validate channel length limits, or does the provider error appear after the row is set to Approved?
- **Why it matters:** Long posts could leave a row Approved but unpublished with a provider error.
- **How to settle it:** Read publishContent in worker/src/index.ts and frontend/src/features/review/context/useReviewFlowActions.ts:624-721. To settle: paste more than 3000 characters and click Publish to LinkedIn on a test account; note the row status afterwards.
- **Related items:** LR-159
- **Owner:**

## Acceptance criteria

- The question in the title is answered in Attempts with file:line evidence and a clear yes/no.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/INVESTIGATE.md (INV-012). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: grep found no length limits in review or editor code per the raw review; the worker side was not checked. Covered by LR-159..
