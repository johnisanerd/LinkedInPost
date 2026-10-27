---
id: 2026-10-27-lr-113-image-search-and-provider-calls-do
title: Image search and provider calls do not check response status or shape and have no timeout, so one hung provider blocks the generate response.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j067-pick-and-upload-images-for-a
- 2026-10-27-j068-ai-image-generation-text-and-reference
related: []
docs:
- generation-worker/src/modules/image-search/index.ts
- generation-worker/src/modules/image-generation/providers/pixazo.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P2
area: generation-worker
raw_id: LR-113
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Image search and provider calls do not check response status or shape and have no timeout, so one hung provider blocks the generate response.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-067, J-068
- **Aliases:** GWP-017
- **Evidence:** generation-worker/src/modules/image-search/index.ts:38-40; generation-worker/src/modules/image-generation/providers/pixazo.ts:28-32
- **Repro:** static.
- **Fix hint:** Shared fetchJson with timeout and expectOk, validate imageUrl.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Shared fetchJson with timeout and expectOk, validate imageUrl.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-113). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of generation-worker/src/modules/image-search/index.ts:38-40.
