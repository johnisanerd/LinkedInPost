---
id: 2026-10-27-lr-017-the-frontend-dev-port-5175-is
title: The frontend dev port 5175 is missing from worker CORS and Google origins, and Playwright waits on 5174, so local sign-in and E2E break.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j011-local-development-loop
- 2026-10-27-j013-documented-developer-test-commands-exist
- 2026-10-27-j131-cors-frontend-origin-not-allowed-or
related: []
docs:
- frontend/vite.config.ts
- start.sh
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P1
area: deploy/config
raw_id: LR-017
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

The frontend dev port 5175 is missing from worker CORS and Google origins, and Playwright waits on 5174, so local sign-in and E2E break.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-011, J-013, J-131
- **Aliases:** ARCH-006
- **Evidence:** frontend/vite.config.ts:78; worker/wrangler.jsonc:57,91
- **Repro:** (static check) Open frontend/vite.config.ts:78 and confirm the behaviour described in the summary; then exercise the matching journey (J-011, J-013, J-131) to observe it.
- **Fix hint:** Pick one port and set it in vite.config.ts, playwright.config.ts, CORS vars, start.sh and the docs.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Pick one port and set it in vite.config.ts, playwright.config.ts, CORS vars, start.sh and the docs.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-017). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of frontend/vite.config.ts:78.
