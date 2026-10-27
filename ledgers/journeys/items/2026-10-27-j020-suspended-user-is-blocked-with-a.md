---
id: 2026-10-27-j020-suspended-user-is-blocked-with-a
title: J-020 Suspended user is blocked with a clear screen
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Non-approved / unauthorised user
trigger: A `users` row with `status='suspended'` (admin clicked "Suspend").
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/auth.ts
- worker/src/index.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P1
core: 'yes'
external_service: Google OAuth
legacy_id: J-020
---

## Purpose and scope

Suspended user is blocked with a clear screen. Priority P1, CORE yes. Imported from journey J-020 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Non-approved / unauthorised user. Preconditions: A `users` row with `status='suspended'` (admin clicked "Suspend").

## Steps and information flow

1. Sign in as that user.
2. Click "Sign out" on the screen.

## Modules and code map

frontend/src/App.tsx (`accessPending`), worker/src/auth.ts, worker/src/index.ts (`verifySession`)

Code anchors that exist: worker/src/auth.ts, worker/src/index.ts

## Success and acceptance

`bootstrap` returns `Access denied: your account has been suspended. Contact support.`; UI shows "Access request pending" with the text "Your account has been suspended. Contact support for help."; "Sign out" clears `localStorage["google_id_token"]`.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
