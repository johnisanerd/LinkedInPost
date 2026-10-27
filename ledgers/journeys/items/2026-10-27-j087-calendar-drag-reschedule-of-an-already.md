---
id: 2026-10-27-j087-calendar-drag-reschedule-of-an-already
title: J-087 Calendar drag-reschedule of an already queued post
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Approved end user
trigger: A queued scheduled post (J-082).
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/index.ts
- worker/src/scheduled-publish/ScheduledPublishAlarm.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P1
core: 'yes'
external_service: Cloudflare
legacy_id: J-087
---

## Purpose and scope

Calendar drag-reschedule of an already queued post. Priority P1, CORE yes. Imported from journey J-087 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: A queued scheduled post (J-082).

## Steps and information flow

1. Open the schedule calendar; drag the event to a later slot (`handleCalendarRescheduleCommit`).
2. Wire: `ACTION updatePostSchedule {"row":{...},"postTime":"2026-10-29 10:00"}`.
3. Wait past the OLD time and past the NEW time.

## Modules and code map

frontend/src/components/dashboard/index.tsx (`handleCalendarRescheduleCommit`, `handleUpdatePostSchedule`), worker/src/index.ts (`updatePostSchedule`, `publishContent`), worker/src/scheduled-publish/ScheduledPublishAlarm.ts

Code anchors that exist: worker/src/index.ts, worker/src/scheduled-publish/ScheduledPublishAlarm.ts

## Success and acceptance

Desired: post fires at the new time only. CODE-READING FINDING: `updatePostSchedule` only updates the row's `postTime`; nothing re-arms a Durable Object (`armScheduledPublish` is called only from `publishContent`). At the old time the DO runs `executeScheduledPublish`, sees `row.postTime != task.scheduledTime` and silently returns; no DO exists for the new time, so the post never fires. Errors in the drag handler are swallowed (`catch {}`), so the UI shows the new slot as fine.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
