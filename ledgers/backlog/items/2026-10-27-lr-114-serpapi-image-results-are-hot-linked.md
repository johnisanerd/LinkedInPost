---
id: 2026-10-27-lr-114-serpapi-image-results-are-hot-linked
title: SerpAPI image results are hot-linked from arbitrary hosts with no https or content validation
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j067-pick-and-upload-images-for-a
- 2026-10-27-j076-publish-now-to-linkedin
related: []
docs:
- generation-worker/src/modules/image-search/index.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P2
area: generation-worker
raw_id: LR-114
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

SerpAPI image results are hot-linked from arbitrary hosts with no https or content validation.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-067, J-076
- **Aliases:** GWP-018
- **Evidence:** generation-worker/src/modules/image-search/index.ts:51-60
- **Repro:** static.
- **Fix hint:** Require https, prefer thumbnail when original fails, validate at promote time.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Require https, prefer thumbnail when original fails, validate at promote time.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-114). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of generation-worker/src/modules/image-search/index.ts:51-60.
