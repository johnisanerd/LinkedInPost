---
id: 2026-10-27-j097-connect-youtube
title: J-097 Connect YouTube
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: worker
actor: Approved end user
trigger: Google OAuth client with YouTube scopes enabled; `/auth/youtube/callback` registered.
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/index.ts
- worker/src/automations/platforms/youtube.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P2
core: 'no'
external_service: YouTube
legacy_id: J-097
---

## Purpose and scope

Connect YouTube. Priority P2, CORE no. Imported from journey J-097 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: Google OAuth client with YouTube scopes enabled; `/auth/youtube/callback` registered.

## Steps and information flow

1. `/connections` -> YouTube -> Connect (`ACTION startYouTubeAuth {}`).
2. Authorize; callback `GET /auth/youtube/callback`.

## Modules and code map

worker/src/index.ts (`startYouTubeAuth`, `handleYouTubeCallback`), worker/src/automations/platforms/youtube.ts

Code anchors that exist: worker/src/index.ts, worker/src/automations/platforms/youtube.ts

## Success and acceptance

Row `youtube` with channel title (`persistYouTubeConnection`, `upsertSocialIntegration`); `youtubeAuthAvailable` true in `bootstrap.config`; this only enables comment automation (J-118), not publishing (J-081).

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
