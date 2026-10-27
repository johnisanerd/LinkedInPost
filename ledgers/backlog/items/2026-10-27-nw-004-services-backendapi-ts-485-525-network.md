---
id: 2026-10-27-nw-004-services-backendapi-ts-485-525-network
title: services/backendApi.ts:485-525 network-failure message tells end users to edit CORS_ALLOWED_ORIGINS, VITE_WORKER_URL and workers.dev firewall rules...
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related:
- 2026-10-27-lr-110-user-facing-network-errors-expose-operator
docs: []
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: new-finding
severity: P2
area: frontend/errors
raw_id: NW-004
source_file: docs/launch-readiness/findings/EXISTING-REVIEWS.md
---

## Problem

services/backendApi.ts:485-525 network-failure message tells end users to edit CORS_ALLOWED_ORIGINS, VITE_WORKER_URL and workers.dev firewall rules.

## Evidence and reproduction

- **Source:** launch-release/findings/raw/existing-reviews.md, row NEW-4
- **Alias:** NEW-4
- **Original tag:** new (not in a source; no severity given, defaulted to P2)
- **Current status:** open
- **Evidence:** none given
- **Covered by:** LR-110

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/EXISTING-REVIEWS.md (NW-004). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: still open in code (no code evidence given by reconciler); covered by LR-110.
