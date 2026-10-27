---
id: 2026-10-27-lr-049-cors-allows-only-get-post-and
title: CORS allows only GET, POST and OPTIONS, so the automations DELETE and PUT calls fail preflight from the Pages origin
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j114-automation-rules-admin
- 2026-10-27-j118-youtube-comment-polling-schedule
- 2026-10-27-j131-cors-frontend-origin-not-allowed-or
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
severity: P1
area: worker/api
raw_id: LR-049
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

CORS allows only GET, POST and OPTIONS, so the automations DELETE and PUT calls fail preflight from the Pages origin.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-114, J-118, J-131
- **Aliases:** WKA-018
- **Evidence:** worker/src/index.ts:6313-6318
- **Repro:** static. Executor: delete an automation rule in the browser and watch the network tab for a failed preflight.
- **Fix hint:** Add PUT and DELETE (and PATCH) to Access-Control-Allow-Methods.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Add PUT and DELETE (and PATCH) to Access-Control-Allow-Methods.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-049). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of worker/src/index.ts:6313-6318.
