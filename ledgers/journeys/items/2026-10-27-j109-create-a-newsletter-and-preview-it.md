---
id: 2026-10-27-j109-create-a-newsletter-and-preview-it
title: J-109 Create a newsletter and preview it
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Approved end user
trigger: Sheet connected (the `newsletter.*` config actions use `storedConfig.spreadsheetId`).
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/newsletter/handlers.ts
- worker/migrations/0016_newsletter.sql
- worker/migrations/0018_newsletters_multi.sql
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P2
core: 'no'
external_service: Gmail
legacy_id: J-109
---

## Purpose and scope

Create a newsletter and preview it. Priority P2, CORE no. Imported from journey J-109 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: Sheet connected (the `newsletter.*` config actions use `storedConfig.spreadsheetId`).

## Steps and information flow

1. `/campaign` -> Newsletter tab -> `NewsletterWizard`.
2. Wire: `ACTION newsletter.create {"name":"Weekly","config":{...},"autoApprove":false}`; `ACTION newsletter.list {}`; `ACTION newsletter.preview {}`; `ACTION newsletter.getConfig {}`; `ACTION newsletter.saveConfig {...}`.

## Modules and code map

frontend/src/features/campaign/components/newsletter/, worker/src/newsletter/handlers.ts, worker/migrations/0016_newsletter.sql, worker/migrations/0018_newsletters_multi.sql

Code anchors that exist: worker/src/newsletter/handlers.ts, worker/migrations/0016_newsletter.sql, worker/migrations/0018_newsletters_multi.sql

## Success and acceptance

Newsletter listed; preview returns rendered HTML/subject. Missing sheet -> `No spreadsheet configured.`

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
