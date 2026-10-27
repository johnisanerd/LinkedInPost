---
id: 2026-10-27-lr-133-the-google-audience-check-runs-only
title: The Google audience check runs only if GOOGLE_CLIENT_ID is set, and CORS falls back to * when CORS_ALLOWED_ORIGINS is empty.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j028-worker-without-google-client-id-accepts
- 2026-10-27-j131-cors-frontend-origin-not-allowed-or
- 2026-10-27-j135-frontend-built-with-the-wrong-google
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
raw_id: LR-133
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

The Google audience check runs only if GOOGLE_CLIENT_ID is set, and CORS falls back to * when CORS_ALLOWED_ORIGINS is empty.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-028, J-131, J-135
- **Aliases:** ARCH-011
- **Evidence:** worker/src/index.ts:6304-6308 and the audience check near 3061
- **Repro:** (static check) Open worker/src/index.ts:6304-6308 and the audience check near 3061 and confirm the behaviour described in the summary; then exercise the matching journey (J-028, J-131, J-135) to observe it.
- **Fix hint:** Reject when GOOGLE_CLIENT_ID is unset and default CORS to deny.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Reject when GOOGLE_CLIENT_ID is unset and default CORS to deny.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-133). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of worker/src/index.ts:6304-6308 and the audience check near 3061.
