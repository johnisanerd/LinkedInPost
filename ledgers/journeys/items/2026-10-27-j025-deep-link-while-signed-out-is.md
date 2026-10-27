---
id: 2026-10-27-j025-deep-link-while-signed-out-is
title: J-025 Deep link while signed out is restored after login
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Approved end user
trigger: Signed out.
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- frontend/src/features/topic-navigation/utils/workspaceRoutes.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P3
core: 'no'
external_service: Google OAuth
legacy_id: J-025
---

## Purpose and scope

Deep link while signed out is restored after login. Priority P3, CORE no. Imported from journey J-025 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: Signed out.

## Steps and information flow

1. Open `{FRONTEND}/topics/new` directly.
2. Sign in.

## Modules and code map

frontend/src/App.tsx (`LoginRedirect`, `PostLoginDeepLinkRestore`), frontend/src/features/topic-navigation/utils/workspaceRoutes.ts

Code anchors that exist: frontend/src/features/topic-navigation/utils/workspaceRoutes.ts

## Success and acceptance

`sessionStorage` key (POST_LOGIN_REDIRECT_KEY) holds `/topics/new` before login; after login the app lands on `/topics/new`, then the key is removed. In private mode where storage throws, the app still lands on `/topics`.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
