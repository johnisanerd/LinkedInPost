---
id: 2026-10-27-lr-050-the-generation-worker-accepts-requests-when
title: The generation worker accepts requests when WORKER_SHARED_SECRET is empty (CORS *, non-constant-time compare), so it can be called without auth.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j053-generate-a-draft-from-the-queue
- 2026-10-27-j055-generation-worker-down-mis-secreted-or
- 2026-10-27-j060-generation-worker-is-open-when-worker
- 2026-10-27-j145-operator-health-check-of-both-workers
related: []
docs:
- generation-worker/src/index.ts
- worker/src/generation/generationWorkerClient.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P1
area: worker/auth
raw_id: LR-050
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

The generation worker accepts requests when WORKER_SHARED_SECRET is empty (CORS *, non-constant-time compare), so it can be called without auth.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-053, J-055, J-060, J-145
- **Aliases:** ARCH-003, GWP-003
- **Evidence:** generation-worker/src/index.ts:41-44,18-24; worker/src/generation/generationWorkerClient.ts:89
- **Repro:** static; deploy without WORKER_SHARED_SECRET and POST /v1/generate with no header.
- **Fix hint:** Fail closed (503) when the secret is empty outside an explicit dev flag, constant-time compare, drop the bare-secret form and CORS *.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Fail closed (503) when the secret is empty outside an explicit dev flag, constant-time compare, drop the bare-secret form and CORS *.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-050). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of generation-worker/src/index.ts:41-44,18-24.
