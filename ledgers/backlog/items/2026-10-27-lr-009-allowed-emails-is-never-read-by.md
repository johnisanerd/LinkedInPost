---
id: 2026-10-27-lr-009-allowed-emails-is-never-read-by
title: ALLOWED_EMAILS is never read by the worker and new users default to status active, so any verified Google account gets in
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j015-approved-user-signs-in-self-hosted
- 2026-10-27-j017-non-approved-google-account-signs-in
- 2026-10-27-j140-tenant-a-cannot-read-or-modify
related: []
docs:
- worker/src/index.ts
- worker/src/db/users.ts
- worker/migrations/0019_user_status_budget.sql
- SETUP.md
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P0
area: worker/auth
raw_id: LR-009
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

ALLOWED_EMAILS is never read by the worker and new users default to status active, so any verified Google account gets in.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-015, J-017, J-140
- **Aliases:** ARCH-002
- **Evidence:** worker/src/index.ts:136 (type only); worker/src/db/users.ts:21-30 with worker/migrations/0019_user_status_budget.sql:2
- **Repro:** (static check) Open worker/src/index.ts:136 (type only) and confirm the behaviour described in the summary; then exercise the matching journey (J-015, J-017, J-140) to observe it.
- **Fix hint:** Read ALLOWED_EMAILS in verifySession and reject before upsertUser, or insert new users as pending in selfHosted mode; fix the SETUP.md verification line.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Read ALLOWED_EMAILS in verifySession and reject before upsertUser, or insert new users as pending in selfHosted mode; fix the SETUP.md verification line.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-009). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of worker/src/index.ts:136 (type only).
