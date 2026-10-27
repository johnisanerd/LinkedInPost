---
id: 2026-10-27-j085-schedule-in-the-past
title: J-085 Schedule in the past
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Approved end user
trigger: Editor open.
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- frontend/src/features/content-schedule-calendar/scheduleValidation.ts
- worker/src/index.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P1
core: 'yes'
external_service: LinkedIn
legacy_id: J-085
---

## Purpose and scope

Schedule in the past. Priority P1, CORE yes. Imported from journey J-085 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: Editor open.

## Steps and information flow

1. In the calendar or editor schedule control pick a time earlier than now (the UI helper `isLocalScheduleInPast` should block it).
2. API bypass: `ACTION publishContent {"row":{... "postTime":"2020-01-01 00:00"},"channel":"linkedin","message":"x"}`.

## Modules and code map

frontend/src/features/content-schedule-calendar/scheduleValidation.ts, worker/src/index.ts (`publishContent`)

Code anchors that exist: frontend/src/features/content-schedule-calendar/scheduleValidation.ts, worker/src/index.ts

## Success and acceptance

UI blocks or warns on a past slot. API: because the arm branch requires `scheduledAt > Date.now() + 60000`, a past or near-now `postTime` is NOT queued: the call publishes immediately and returns `deliveryMode:"sent"`. The user who typed a past time must be told this will publish now before they confirm.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
