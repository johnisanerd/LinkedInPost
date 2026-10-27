---
id: 2026-10-27-lr-105-auth-errors-are-detected-by-regex
title: Auth errors are detected by regex on message text and the worker returns every failure as HTTP 400, so unrelated errors can sign users out.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j021-google-id-token-expires-mid-session
- 2026-10-27-j022-non-auth-errors-that-contain-expired
- 2026-10-27-j023-backend-unreachable-at-boot
- 2026-10-27-j125-monthly-token-budget-exhausted
related: []
docs:
- frontend/src/services/backendApi.ts
- worker/src/index.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P2
area: frontend/shell
raw_id: LR-105
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Auth errors are detected by regex on message text and the worker returns every failure as HTTP 400, so unrelated errors can sign users out.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-021..J-023, J-125
- **Aliases:** FEB-013, WKA-019
- **Evidence:** frontend/src/services/backendApi.ts:471,526; worker/src/index.ts:1272-1275,3043-3052
- **Repro:** trigger a worker error containing "expired" (e.g. LinkedIn state expired). Static reasoning.
- **Fix hint:** Return 401/403/429/502 with a machine code from the worker and key off it in post(); make safeFetch rethrow outside sandbox.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Return 401/403/429/502 with a machine code from the worker and key off it in post(); make safeFetch rethrow outside sandbox.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-105). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of frontend/src/services/backendApi.ts:471,526.
