---
id: 2026-10-27-j095-connect-instagram
title: J-095 Connect Instagram
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: worker
actor: Approved end user
trigger: '`INSTAGRAM_APP_ID`, `INSTAGRAM_APP_SECRET`; redirect `/auth/instagram/callback` registered; account is Business/Creator.'
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/index.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P1
core: 'yes'
external_service: Instagram
legacy_id: J-095
---

## Purpose and scope

Connect Instagram. Priority P1, CORE yes. Imported from journey J-095 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: `INSTAGRAM_APP_ID`, `INSTAGRAM_APP_SECRET`; redirect `/auth/instagram/callback` registered; account is Business/Creator.

## Steps and information flow

1. `/connections` -> Instagram -> Connect (`ACTION startInstagramAuth {}`).
2. Authorize in popup; callback `GET /auth/instagram/callback`.

## Modules and code map

worker/src/index.ts (`startInstagramAuth`, `handleInstagramCallback`), worker/src/integrations/instagram

Code anchors that exist: worker/src/index.ts

## Success and acceptance

`social_integrations` row for `instagram` with username; `bootstrap.config.hasInstagramAccessToken` true; missing app id -> `Instagram OAuth is not configured in the Worker environment. Add INSTAGRAM_APP_ID and INSTAGRAM_APP_SECRET first.`

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
