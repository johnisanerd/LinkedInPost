---
id: 2026-10-27-j084-cancel-a-scheduled-post
title: J-084 Cancel a scheduled post
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Approved end user
trigger: A queued post (J-082).
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/scheduled-publish/handleCancelDispatch.ts
- worker/src/scheduled-publish/ScheduledPublishAlarm.ts
- frontend/src/features/scheduled-publish/usePendingScheduledPublish.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P1
core: 'yes'
external_service: Cloudflare
legacy_id: J-084
---

## Purpose and scope

Cancel a scheduled post. Priority P1, CORE yes. Imported from journey J-084 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: A queued post (J-082).

## Steps and information flow

1. Click "Cancel schedule" in the banner / delivery panel.
2. Wire: `ACTION cancelScheduledPublish {"topicId":"<id>","scheduledTime":"2026-10-28 09:30","channel":"linkedin"}`.
3. Repeat with a wrong `scheduledTime`, and with a `topicId` of another tenant's post.

## Modules and code map

worker/src/scheduled-publish/handleCancelDispatch.ts, worker/src/scheduled-publish/ScheduledPublishAlarm.ts, frontend/src/features/scheduled-publish/ScheduledPublishBanner.tsx, frontend/src/features/scheduled-publish/usePendingScheduledPublish.ts

Code anchors that exist: worker/src/scheduled-publish/handleCancelDispatch.ts, worker/src/scheduled-publish/ScheduledPublishAlarm.ts, frontend/src/features/scheduled-publish/usePendingScheduledPublish.ts

## Success and acceptance

`{success:true,cancelled:true}`; DO storage and alarm removed; the post does not fire. Wrong time -> `Scheduled time does not match the armed task. Refresh and try again.` (409 inside the DO, surfaced as an Error). CODE-READING FINDING: the dispatcher does not check that the caller owns `topicId` (DO name is `topicId::channel`, no user component); any signed-in user who knows both values can cancel. Note `channel` omitted defaults to `linkedin`, so cancelling a non-LinkedIn schedule without `channel` silently reports `cancelled:false`.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
