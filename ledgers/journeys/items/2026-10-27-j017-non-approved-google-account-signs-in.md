---
id: 2026-10-27-j017-non-approved-google-account-signs-in
title: J-017 Non-approved Google account signs in
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: worker
actor: Non-approved / unauthorised user
trigger: A Google account whose email is in neither `ALLOWED_EMAILS` nor `ADMIN_EMAILS`, never seen before.
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/index.ts
- worker/src/db/users.ts
- worker/src/auth.ts
- worker/migrations/0019_user_status_budget.sql
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P0
core: 'yes'
external_service: Google OAuth
legacy_id: J-017
---

## Purpose and scope

Non-approved Google account signs in. Priority P0, CORE yes. Imported from journey J-017 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Non-approved / unauthorised user. Preconditions: A Google account whose email is in neither `ALLOWED_EMAILS` nor `ADMIN_EMAILS`, never seen before.

## Steps and information flow

1. Sign in with that account.
2. Observe the UI: expected "Access request pending" ("Your access request is pending review...").
3. Directly: `ACTION bootstrap {}` with that account's `T`.
4. Then `ACTION addTopic {"topic":"x"}`.
- CODE-READING FINDING: `verifySession` calls `upsertUser` first (inserts a row), then `checkUserAccess` reads `users.status`. Migration 0019 defines `status TEXT NOT NULL DEFAULT 'active'`, so every new Google account becomes `active` on first sign-in. `ALLOWED_EMAILS` exists only as an `Env` field (grep shows no other use in worker/src). Expected block does not happen.

## Modules and code map

worker/src/index.ts (`verifySession`, `resolveAdminEmailAllowlist`, `Env.ALLOWED_EMAILS`), worker/src/db/users.ts (`upsertUser`, `getUserStatus`), worker/src/auth.ts (`checkUserAccess`), worker/migrations/0019_user_status_budget.sql

Code anchors that exist: worker/src/index.ts, worker/src/db/users.ts, worker/src/auth.ts, worker/migrations/0019_user_status_budget.sql

## Success and acceptance

Desired: Step 3 returns `{"ok":false,"error":"Access not granted. Request access at the homepage."}` and no `users` row with `status='active'` is created. (Currently expected to FAIL: bootstrap returns a session.)

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
