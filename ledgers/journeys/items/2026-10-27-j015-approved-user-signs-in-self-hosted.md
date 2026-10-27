---
id: 2026-10-27-j015-approved-user-signs-in-self-hosted
title: J-015 Approved user signs in (self-hosted)
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Approved end user
trigger: '`features.yaml` `deploymentMode: selfHosted`; worker has `GOOGLE_CLIENT_ID`, `ADMIN_EMAILS`; user''s Google account.'
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/index.ts
- worker/src/db/users.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P0
core: 'yes'
external_service: Google OAuth
legacy_id: J-015
---

## Purpose and scope

Approved user signs in (self-hosted). Priority P0, CORE yes. Imported from journey J-015 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: `features.yaml` `deploymentMode: selfHosted`; worker has `GOOGLE_CLIENT_ID`, `ADMIN_EMAILS`; user's Google account.

## Steps and information flow

1. Open `{FRONTEND}/` (non-saas has no `/` route; the catch-all shows "Sign in", "Use an approved Google account to open the workspace.").
2. Click the Google sign-in button (`GoogleLoginButton`).
3. Frontend stores the id token in `localStorage["google_id_token"]` and calls `ACTION bootstrap {}`.

## Modules and code map

frontend/src/App.tsx, frontend/src/components/GoogleLoginButton.tsx, worker/src/index.ts (`verifySession`, `bootstrap`), worker/src/db/users.ts

Code anchors that exist: worker/src/index.ts, worker/src/db/users.ts

## Success and acceptance

`bootstrap` returns `{email,isAdmin,config,onboardingCompleted,integrations}`; app navigates to `/topics`; a `users` row exists for the email (D1 `users`).

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
