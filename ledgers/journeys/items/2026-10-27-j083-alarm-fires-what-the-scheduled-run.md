---
id: 2026-10-27-j083-alarm-fires-what-the-scheduled-run
title: 'J-083 Alarm fires: what the scheduled run actually executes'
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: worker
actor: Background / agent actor
trigger: A post queued per J-082 by a tenant (non-admin) whose sheet is in D1 `users.spreadsheet_id`, with its own LinkedIn token in D1 `social_integrations`.
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/scheduled-publish/ScheduledPublishAlarm.ts
- worker/src/scheduled-publish/durablePublishScheduler.ts
- worker/src/scheduled-publish/types.ts
- worker/src/index.ts
- worker/src/services.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P0
core: 'yes'
external_service: LinkedIn, Cloudflare, Google Sheets
legacy_id: J-083
---

## Purpose and scope

Alarm fires: what the scheduled run actually executes. Priority P0, CORE yes. Imported from journey J-083 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Background / agent actor. Preconditions: A post queued per J-082 by a tenant (non-admin) whose sheet is in D1 `users.spreadsheet_id`, with its own LinkedIn token in D1 `social_integrations`.

## Steps and information flow

1. Let the Durable Object alarm fire (`ScheduledPublishAlarm.alarm()` -> `executeScheduledPublish(env, task)`).
2. Read worker logs (`observability` enabled) and the row status.
- CODE-READING FINDING A: `armScheduledPublish` is called with `userId`, but `handleArm` persists only `{topicId,topic,date,scheduledTime,intent,channel,recipientId}`; `userId` is dropped, so `task.userId` is undefined at fire time.
- CODE-READING FINDING B: `executeScheduledPublish` calls `loadStoredConfig(env)` and `buildServices(env)` with no user, so `config.spreadsheetId` is the KV `shared-config` sheet (not the tenant's) and `pipeline` has `userId=''`; `getRowByTopicId` finds no row and the function returns silently (`if (!row) return;`).
- CODE-READING FINDING C: every guard in `executeScheduledPublish` (`status != approved`, `postTime mismatch`, empty text) returns without logging or marking the row, so failures are invisible.

## Modules and code map

worker/src/scheduled-publish/ScheduledPublishAlarm.ts, worker/src/scheduled-publish/durablePublishScheduler.ts, worker/src/scheduled-publish/types.ts, worker/src/index.ts (`executeScheduledPublish`, `loadStoredConfig`, `buildServices`), worker/src/services.ts

Code anchors that exist: worker/src/scheduled-publish/ScheduledPublishAlarm.ts, worker/src/scheduled-publish/durablePublishScheduler.ts, worker/src/scheduled-publish/types.ts, worker/src/index.ts, worker/src/services.ts

## Success and acceptance

At the scheduled time the post appears on the right account, D1 row `status='Published'`. Currently expected to FAIL for multi-tenant (non-admin or non-KV-sheet) users; for the single-owner self-hosted deployment (admin sheet == KV sheet, global LinkedIn token) it likely works. A row that stays `Approved` after the time with no log line is the symptom.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
