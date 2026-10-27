---
id: 2026-10-27-j086-timezone-semantics-of-a-scheduled-time
title: J-086 Timezone semantics of a scheduled time
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Approved end user
trigger: Browser timezone different from UTC (e.g. IST, UTC+5:30).
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/scheduled-publish/time.ts
- frontend/src/features/content-schedule-calendar/calendarTemporal.ts
- frontend/src/features/content-schedule-calendar/scheduleValidation.ts
- worker/src/index.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P1
core: 'yes'
external_service: LinkedIn, Cloudflare
legacy_id: J-086
---

## Purpose and scope

Timezone semantics of a scheduled time. Priority P1, CORE yes. Imported from journey J-086 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: Browser timezone different from UTC (e.g. IST, UTC+5:30).

## Steps and information flow

1. Schedule a post for local 09:30 (UI sends `postTime: "2026-10-28 09:30"`, local wall time, no zone).
2. Read the worker logic: `parseScheduledTimeToTimestamp` uses `Date.UTC(y, m-1, d, h, min)`.
3. Compare the actual fire time to 09:30 local.

## Modules and code map

worker/src/scheduled-publish/time.ts, frontend/src/features/content-schedule-calendar/calendarTemporal.ts, frontend/src/features/content-schedule-calendar/scheduleValidation.ts, worker/src/index.ts

Code anchors that exist: worker/src/scheduled-publish/time.ts, frontend/src/features/content-schedule-calendar/calendarTemporal.ts, frontend/src/features/content-schedule-calendar/scheduleValidation.ts, worker/src/index.ts

## Success and acceptance

Desired: fires at 09:30 local. CODE-READING FINDING: the string is interpreted as UTC, so a UTC+5:30 user's 09:30 post fires at 15:00 local; a UTC-8 user's fires 8 h early (and a "future" local time may be already "in the past" in UTC, see J-085). The same applies to the DO check `row.postTime === task.scheduledTime`. No timezone is stored with the row.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
