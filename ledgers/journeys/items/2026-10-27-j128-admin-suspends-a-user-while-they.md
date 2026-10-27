---
id: 2026-10-27-j128-admin-suspends-a-user-while-they
title: J-128 Admin suspends a user while they are signed in
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Tenant admin
trigger: User U with a live session; admin on `/admin`.
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/index.ts
- worker/src/auth.ts
- worker/src/scheduled-publish/ScheduledPublishAlarm.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P1
core: 'yes'
external_service: none
legacy_id: J-128
---

## Purpose and scope

Admin suspends a user while they are signed in. Priority P1, CORE yes. Imported from journey J-128 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Tenant admin. Preconditions: User U with a live session; admin on `/admin`.

## Steps and information flow

1. Admin clicks "Suspend" for U.
2. U triggers any action (e.g. `ACTION getRows {}`) and any streaming call (`POST /api/generate/stream`).
3. U's scheduled posts (J-082) fire.

## Modules and code map

worker/src/index.ts, worker/src/auth.ts, worker/src/scheduled-publish/ScheduledPublishAlarm.ts, frontend/src/App.tsx

Code anchors that exist: worker/src/index.ts, worker/src/auth.ts, worker/src/scheduled-publish/ScheduledPublishAlarm.ts

## Success and acceptance

Steps 2: `Access denied: your account has been suspended. Contact support.` (action path) and HTTP 401 `Unauthorized` (stream path: `verifySession` throws, reported as 401). U's UI shows a generic notice (the sign-out/"suspended" screen only appears at bootstrap, since the mid-session message does not match `AUTH_ERROR_PATTERN`). Step 3: the DO alarm does not call `verifySession`, so a suspended user's already-queued posts still publish (CODE-READING FINDING).

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
