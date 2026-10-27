---
id: 2026-10-27-j076-publish-now-to-linkedin
title: J-076 Publish now to LinkedIn
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Approved end user
trigger: LinkedIn connected for this user (J-094); text approved; sheet connected.
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- frontend/src/components/dashboard/hooks/useDashboardQueue.ts
- worker/src/index.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P0
core: 'yes'
external_service: LinkedIn
legacy_id: J-076
---

## Purpose and scope

Publish now to LinkedIn. Priority P0, CORE yes. Imported from journey J-076 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: LinkedIn connected for this user (J-094); text approved; sheet connected.

## Steps and information flow

1. Editor footer: click "Publish to LinkedIn" (label from `CHANNEL_OPTIONS`).
2. Wire: `ACTION updateRowStatus {"row":{...},"status":"Approved","selectedText":"<text>","selectedImageId":"","postTime":"","emailTo":"","emailCc":"","emailBcc":"","emailSubject":"","selectedImageUrlsJson":""}` then `ACTION publishContent {"row":{...},"channel":"linkedin","message":"<text>","imageUrl":"","imageUrls":[]}`.
3. Open the LinkedIn profile feed.

## Modules and code map

frontend/src/components/dashboard/hooks/useDashboardQueue.ts (`publishFromReviewEditor`, `publishRowToSelectedChannel`), worker/src/index.ts (`publishContent`, `markPublishedForChannel`), worker/src/integrations/linkedin

Code anchors that exist: frontend/src/components/dashboard/hooks/useDashboardQueue.ts, worker/src/index.ts

## Success and acceptance

`publishContent` returns `{success:true,channel:"linkedin",messageId:"<urn>",deliveryMode:"sent",mediaMode:"text"|"image"}`; the post exists on LinkedIn with the exact approved text; D1 row `status='Published'`, `post_time` set; a line is appended to the posted-log Google Doc; the UI alert says `Published "<topic>" to LinkedIn as a text post.` Empty text -> `Approved content text is empty. Approve or edit the draft before sending it.`

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
