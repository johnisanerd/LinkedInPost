---
id: 2026-10-27-lr-078-a-literal-dev-google-auth-bypass
title: A literal DEV_GOOGLE_AUTH_BYPASS_SECRET is committed in worker/wrangler.jsonc env.local and in the tracked frontend/.env.development.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j012-dev-auth-bypass-for-local-work
- 2026-10-27-j136-dev-auth-bypass-secret-present-in
related:
- 2026-10-27-lr-134-default-admin-email-is-hard-coded
docs:
- frontend/.env.development
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P2
area: deploy/config
raw_id: LR-078
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

A literal DEV_GOOGLE_AUTH_BYPASS_SECRET is committed in worker/wrangler.jsonc env.local and in the tracked frontend/.env.development.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-012, J-136
- **Aliases:** ARCH-012 (committed secret)
- **Evidence:** worker/wrangler.jsonc:100; frontend/.env.development
- **Repro:** (static check) Open worker/wrangler.jsonc:100 and confirm the behaviour described in the summary; then exercise the matching journey (J-012, J-136) to observe it.
- **Fix hint:** Move the local secret to untracked .dev.vars and untrack .env.development values.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Move the local secret to untracked .dev.vars and untrack .env.development values.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-078). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of worker/wrangler.jsonc:100.
