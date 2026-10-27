---
id: 2026-10-27-j074-post-templates-crud
title: J-074 Post templates CRUD
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Tenant admin
trigger: Sheet connected.
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/index.ts
- worker/src/persistence/drafts.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P2
core: 'yes'
external_service: Google Sheets
legacy_id: J-074
---

## Purpose and scope

Post templates CRUD. Priority P2, CORE yes. Imported from journey J-074 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Tenant admin. Preconditions: Sheet connected.

## Steps and information flow

1. `/rules` -> "Post templates" -> Create / "Save changes".
2. API: `ACTION createPostTemplate {"name":"Case study","rules":"..."}`, `ACTION listPostTemplates {}`, `ACTION updatePostTemplate {"templateId":"<id>","name":"...","rules":"..."}`, `ACTION deletePostTemplate {"templateId":"<id>"}`.
3. Disable the sheet and call `listPostTemplates`.

## Modules and code map

worker/src/index.ts, worker/src/persistence/drafts.ts (`SheetsGateway`), frontend/src/pages/GlobalRulesPage.tsx

Code anchors that exist: worker/src/index.ts, worker/src/persistence/drafts.ts

## Success and acceptance

Templates round-trip in the sheet's template tab. With Sheets unreachable, `listPostTemplates` returns `[]` and logs the error (UI cannot tell "none" from "failed"). Without a sheet, `listPostTemplates` returns `[]`, while create/update/delete throw the missing-spreadsheet error.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
