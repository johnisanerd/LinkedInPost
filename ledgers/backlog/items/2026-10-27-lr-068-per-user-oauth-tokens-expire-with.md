---
id: 2026-10-27-lr-068-per-user-oauth-tokens-expire-with
title: Per-user OAuth tokens expire with no refresh path, needs_reauth is never set, and the Gmail 401 refresh uses and overwrites the shared token.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j078-send-via-gmail
- 2026-10-27-j090-publish-fails-because-the-channel-token
- 2026-10-27-j096-connect-gmail
- 2026-10-27-j097-connect-youtube
- 2026-10-27-j105-stored-token-can-no-longer-be
related: []
docs:
- worker/src/index.ts
- worker/src/db/socialIntegrations.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P1
area: worker/publish
raw_id: LR-068
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Per-user OAuth tokens expire with no refresh path, needs_reauth is never set, and the Gmail 401 refresh uses and overwrites the shared token.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-078, J-090, J-096, J-097, J-105
- **Aliases:** WKA-015, WKB-007
- **Evidence:** worker/src/index.ts:5117-5133,4004-4031; worker/src/db/socialIntegrations.ts:125
- **Repro:** static. Executor: connect Gmail as user B, wait over one hour, send.
- **Fix hint:** Refresh from the user refresh_token_enc, persist to social_integrations only, and call markSocialIntegrationNeedsReauth on terminal 401.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Refresh from the user refresh_token_enc, persist to social_integrations only, and call markSocialIntegrationNeedsReauth on terminal 401.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-068). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of worker/src/index.ts:5117-5133,4004-4031.
