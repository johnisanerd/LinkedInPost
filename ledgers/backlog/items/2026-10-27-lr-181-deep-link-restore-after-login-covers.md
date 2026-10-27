---
id: 2026-10-27-lr-181-deep-link-restore-after-login-covers
title: Deep-link restore after login covers only four route prefixes
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j025-deep-link-while-signed-out-is
related: []
docs:
- frontend/src/lib/postLoginRedirect.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P3
area: frontend/shell
raw_id: LR-181
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Deep-link restore after login covers only four route prefixes.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-025
- **Aliases:** FEB-023
- **Evidence:** frontend/src/lib/postLoginRedirect.ts:6-16
- **Repro:** open /connections signed out, sign in.
- **Fix hint:** Capture any WORKSPACE_PATHS value.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Capture any WORKSPACE_PATHS value.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-181). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of frontend/src/lib/postLoginRedirect.ts:6-16.
