---
id: 2026-10-27-lr-079-several-env-names-read-by-the
title: Several env names read by the code (YOUTUBE_CLIENT_ID, OAUTH_REDIRECT_BASE_URL, WORKER_SHARED_SECRET and others) are missing from .env.example.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j001-web-setup-wizard-end-to-end
- 2026-10-27-j002-headless-full-bootstrap-with-python-setup
related: []
docs:
- worker/src/index.ts
- worker/src/automations/routes.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P2
area: docs/env
raw_id: LR-079
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Several env names read by the code (YOUTUBE_CLIENT_ID, OAUTH_REDIRECT_BASE_URL, WORKER_SHARED_SECRET and others) are missing from .env.example.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-001, J-002
- **Aliases:** ARCH-014
- **Evidence:** worker/src/index.ts:3276,3457,3108; worker/src/automations/routes.ts:24
- **Repro:** (static check) Open worker/src/index.ts:3276,3457,3108 and confirm the behaviour described in the summary; then exercise the matching journey (J-001, J-002) to observe it.
- **Fix hint:** Add the missing keys with comments and unify GOOGLE_CREDENTIALS_JSON versus GOOGLE_SERVICE_ACCOUNT_JSON.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Add the missing keys with comments and unify GOOGLE_CREDENTIALS_JSON versus GOOGLE_SERVICE_ACCOUNT_JSON.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-079). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of worker/src/index.ts:3276,3457,3108.
