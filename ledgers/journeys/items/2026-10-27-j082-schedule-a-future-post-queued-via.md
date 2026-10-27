---
id: 2026-10-27-j082-schedule-a-future-post-queued-via
title: J-082 Schedule a future post (queued via Durable Object)
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Approved end user
trigger: LinkedIn connected; DO binding `SCHEDULED_LINKEDIN_PUBLISH` present (J-133).
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/index.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P0
core: 'yes'
external_service: LinkedIn, Cloudflare
legacy_id: J-082
---

## Purpose and scope

Schedule a future post (queued via Durable Object). Priority P0, CORE yes. Imported from journey J-082 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: LinkedIn connected; DO binding `SCHEDULED_LINKEDIN_PUBLISH` present (J-133).

## Steps and information flow

1. In the editor, set a schedule time (control `aria-label="Schedule post time"`) 10 minutes ahead; click publish.
2. Wire: `ACTION updateRowStatus {... "postTime":"2026-10-28 09:30" ...}` then `ACTION publishContent {"row":{... "postTime":"2026-10-28 09:30"},"channel":"linkedin","message":"..."}`.
3. Observe the `ScheduledPublishBanner`; `/topics` shows the row as scheduled.
4. Wait for the time.

## Modules and code map

worker/src/index.ts (`publishContent`, `armScheduledPublish`), worker/src/scheduled-publish/*, frontend/src/features/scheduled-publish/, frontend/src/features/content-schedule-calendar/

Code anchors that exist: worker/src/index.ts

## Success and acceptance

Step 2 returns `deliveryMode:"queued"`, `scheduledTime:"2026-10-28 09:30"`; alert "Scheduled ... queued for LinkedIn at ...". Posted at the time (see J-083 for what actually runs). The `postTime` format must be `YYYY-MM-DD HH:mm` or `parseScheduledTimeToTimestamp` returns null and the post publishes immediately.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
