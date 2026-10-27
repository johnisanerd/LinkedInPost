---
id: 2026-10-27-j135-frontend-built-with-the-wrong-google
title: J-135 Frontend built with the wrong Google client id
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: workflow
scope_type: section
scope: frontend
actor: Self-hosting operator
trigger: '`VITE_GOOGLE_CLIENT_ID` differs from the worker''s `GOOGLE_CLIENT_ID`; or the Pages origin missing from the OAuth client''s authorized JavaScript origins.'
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/index.ts
- SETUP.md
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P1
core: 'yes'
external_service: Google OAuth
legacy_id: J-135
---

## Purpose and scope

Frontend built with the wrong Google client id. Priority P1, CORE yes. Imported from journey J-135 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Self-hosting operator. Preconditions: `VITE_GOOGLE_CLIENT_ID` differs from the worker's `GOOGLE_CLIENT_ID`; or the Pages origin missing from the OAuth client's authorized JavaScript origins.

## Steps and information flow

1. Click the Google sign-in button.
2. Complete sign-in; observe the bootstrap error.

## Modules and code map

frontend/src/components/GoogleLoginButton.tsx, frontend/src/App.tsx, worker/src/index.ts (`verifySession`), SETUP.md

Code anchors that exist: worker/src/index.ts, SETUP.md

## Success and acceptance

Google popup shows `origin_mismatch`/`invalid_client` (origins) or bootstrap fails with `Unauthorized: Google token audience does not match this app.` shown in the red error box on the sign-in card; the operator doc (SETUP.md Step 2) lists the exact origins (`http://localhost:5173` only; `5174` used by `npm run dev` is not listed: CODE-READING FINDING).

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
