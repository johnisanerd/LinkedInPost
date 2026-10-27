---
id: 2026-10-27-lr-038-the-enriched-creator-swallows-every-group
title: The enriched creator swallows every group error (including 401/403/429), has no retry or concurrency limit, and hides the real cause.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j053-generate-a-draft-from-the-queue
- 2026-10-27-j122-llm-provider-failure-and-fallback
related: []
docs:
- generation-worker/src/modules/_shared/creator.ts
- generation-worker/src/modules/_shared/orchestrator.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P1
area: generation-worker
raw_id: LR-038
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

The enriched creator swallows every group error (including 401/403/429), has no retry or concurrency limit, and hides the real cause.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-053, J-122
- **Aliases:** GWP-008
- **Evidence:** generation-worker/src/modules/_shared/creator.ts:187-212; generation-worker/src/modules/_shared/orchestrator.ts:160-189
- **Repro:** static; use a low-quota Gemini key and observe fewer than 4 variants or a generic error.
- **Fix hint:** Wrap group calls in withRetry for 429/5xx, cap concurrency, collect errors into trace.creatorErrors and include the first in the thrown message.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Wrap group calls in withRetry for 429/5xx, cap concurrency, collect errors into trace.creatorErrors and include the first in the thrown message.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-038). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of generation-worker/src/modules/_shared/creator.ts:187-212.
