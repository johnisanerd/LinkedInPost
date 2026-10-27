---
id: 2026-10-27-j106-bulk-import-by-pasting-campaign-json
title: J-106 Bulk import by pasting campaign JSON
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Approved end user
trigger: '`FEATURE_CAMPAIGN` true; sheet connected.'
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/persistence/drafts.ts
- worker/src/index.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P2
core: 'no'
external_service: Google Sheets
legacy_id: J-106
---

## Purpose and scope

Bulk import by pasting campaign JSON. Priority P2, CORE no. Imported from journey J-106 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: `FEATURE_CAMPAIGN` true; sheet connected.

## Steps and information flow

1. `/campaign` -> choose "Paste JSON" -> paste `{"version":1,"posts":[{"topicId":"t1","topic":"...","date":"2026-11-01","variants":["a","b"],"postTime":"2026-11-01 09:00"}]}`.
2. Review in the list/calendar, click import.
3. Wire: `ACTION bulkImportCampaign {"posts":[{...}]}`.

## Modules and code map

frontend/src/features/campaign/CampaignPage.tsx, frontend/src/features/campaign/validate/, worker/src/persistence/drafts.ts (`coerceBulkCampaignPostsFromPayload`), worker/src/index.ts (`bulkImportCampaign`)

Code anchors that exist: worker/src/persistence/drafts.ts, worker/src/index.ts

## Success and acceptance

Returns `{success:true,imported:N}`; rows appear in `/topics` as Draft; invalid JSON is caught by `parseCampaignPaste` in the UI with a field-level message; with `campaign: false` the route redirects to `/topics` and the action throws `Campaign import is disabled for this deployment.`

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
