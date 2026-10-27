---
id: 2026-10-27-lr-135-every-request-re-verifies-the-google
title: Every request re-verifies the Google token over the network with 3-5 sequential reads, and a swallowed upsert failure is reported as Access denied.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j015-approved-user-signs-in-self-hosted
- 2026-10-27-j021-google-id-token-expires-mid-session
- 2026-10-27-j040-topic-list-merges-sheets-and-d1
- 2026-10-27-j145-operator-health-check-of-both-workers
related: []
docs:
- worker/src/index.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P2
area: worker/auth
raw_id: LR-135
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Every request re-verifies the Google token over the network with 3-5 sequential reads, and a swallowed upsert failure is reported as Access denied.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-015, J-021, J-040, J-145
- **Aliases:** WKA-020
- **Evidence:** worker/src/index.ts:3031-3085,3068
- **Repro:** static. Executor: time `bootstrap` and watch the subrequest log; run 20 parallel actions.
- **Fix hint:** Verify the JWT locally against cached Google JWKS, cache verified sessions briefly, surface DB errors as 5xx.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Verify the JWT locally against cached Google JWKS, cache verified sessions briefly, surface DB errors as 5xx.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-135). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of worker/src/index.ts:3031-3085,3068.
