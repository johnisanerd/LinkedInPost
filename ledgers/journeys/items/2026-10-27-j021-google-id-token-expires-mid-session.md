---
id: 2026-10-27-j021-google-id-token-expires-mid-session
title: J-021 Google ID token expires mid-session (401-equivalent)
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Approved end user
trigger: Signed in for more than the token lifetime (Google ID tokens last about one hour); the app only stores the ID token in `localStorage`, there is no refresh code in App.tsx.
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- frontend/src/services/backendApi.ts
- frontend/src/components/dashboard/hooks/useDashboardQueue.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P1
core: 'yes'
external_service: Google OAuth
legacy_id: J-021
---

## Purpose and scope

Google ID token expires mid-session (401-equivalent). Priority P1, CORE yes. Imported from journey J-021 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: Signed in for more than the token lifetime (Google ID tokens last about one hour); the app only stores the ID token in `localStorage`, there is no refresh code in App.tsx.

## Steps and information flow

1. Open the editor on a topic, type changes, do not save.
2. After expiry trigger any action (e.g. click a Quick Change or "Publish to LinkedIn").

## Modules and code map

frontend/src/App.tsx (`handleAuthExpired`), frontend/src/services/backendApi.ts (`AUTH_ERROR_PATTERN`, `post`), frontend/src/components/dashboard/hooks/useDashboardQueue.ts (`handleFailure`), frontend/src/features/editor/DraftEditor.tsx

Code anchors that exist: frontend/src/services/backendApi.ts, frontend/src/components/dashboard/hooks/useDashboardQueue.ts

## Success and acceptance

Worker returns HTTP 400 `{"ok":false,"error":"Unauthorized: invalid or expired Google token."}` (not 401). `handleFailure` matches `AUTH_ERROR_PATTERN` and calls `onAuthExpired`, which signs the user out with "Your Google session expired. Sign in again to continue." Desired: unsaved editor text is preserved or the user is warned (CODE-READING FINDING: editor history is component state only; it is lost on sign-out).

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
