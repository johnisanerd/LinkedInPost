---
id: 2026-10-27-lr-082-retrying-publish-after-a-failure-creates
title: Retrying publish after a failure creates another draft copy of an already published post
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j088-double-click-on-publish
- 2026-10-27-j089-post-is-live-but-marking-it
- 2026-10-27-j091-republish-an-already-published-post
related: []
docs:
- frontend/src/components/dashboard/hooks/useDashboardQueue.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P2
area: frontend/editor
raw_id: LR-082
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Retrying publish after a failure creates another draft copy of an already published post.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-088, J-089, J-091
- **Aliases:** FEA-012
- **Evidence:** frontend/src/components/dashboard/hooks/useDashboardQueue.ts:602-750
- **Repro:** Open a Published post, edit, click Publish while the LinkedIn token is revoked; click again: two draft copies in the queue.
- **Fix hint:** Remember the created copy topicId and reuse it on retry, or delete the copy on failure.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Remember the created copy topicId and reuse it on retry, or delete the copy on failure.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-082). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of frontend/src/components/dashboard/hooks/useDashboardQueue.ts:602-750.
