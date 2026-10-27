---
id: 2026-10-27-uc-020-trending-fallback-to-mock-data
title: 'Trending: "fallback to mock data"'
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related:
- 2026-10-27-lr-094-trending-falls-back-to-hard-coded
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
raw_id: UC-020
source_file: docs/launch-readiness/findings/EXISTING-REVIEWS.md
---

## Problem

Trending: "fallback to mock data".

## Evidence and reproduction

- **Source:** launch-release/findings/raw/existing-reviews.md section 2, row U-J11
- **Alias:** U-J11
- **Original tag:** ✅ (no severity given, defaulted to P2)
- **Current status:** partial
- **Evidence:** features/trending/hooks/useTrending.ts:280-292 mock-loading timer when !useRealApis (mock fallback is real code - confirm it cannot reach prod users)
- **Covered by:** LR-094

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/EXISTING-REVIEWS.md (UC-020). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: partial; still open in code (mock fallback is real code - confirm it cannot reach prod users); covered by LR-094.
