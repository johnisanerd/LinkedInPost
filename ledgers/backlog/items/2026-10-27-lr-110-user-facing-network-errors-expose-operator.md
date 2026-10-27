---
id: 2026-10-27-lr-110-user-facing-network-errors-expose-operator
title: User-facing network errors expose operator text (CORS_ALLOWED_ORIGINS, VITE_WORKER_URL, workers.dev firewall advice)
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j023-backend-unreachable-at-boot
- 2026-10-27-j024-frontend-built-without-vite-worker-url
related: []
docs:
- frontend/src/services/backendApi.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P2
area: frontend/shell
raw_id: LR-110
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

User-facing network errors expose operator text (CORS_ALLOWED_ORIGINS, VITE_WORKER_URL, workers.dev firewall advice).

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-023, J-024
- **Aliases:** C13-1, NEW-4
- **Evidence:** frontend/src/services/backendApi.ts:485-525
- **Repro:** (static check) Open frontend/src/services/backendApi.ts:485-525 and confirm the behaviour described in the summary; then exercise the matching journey (J-023, J-024) to observe it.
- **Fix hint:** Show a plain-language message to users and log the operator hint to the console only.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Show a plain-language message to users and log the operator hint to the console only.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-110). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of frontend/src/services/backendApi.ts:485-525.
