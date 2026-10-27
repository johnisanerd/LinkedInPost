---
id: 2026-10-27-j110-draft-approve-and-send-a-newsletter
title: J-110 Draft, approve and send a newsletter issue manually
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: worker
actor: Approved end user
trigger: A newsletter with recipients.
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/newsletter/handlers.ts
- worker/src/newsletter/draftCreator.ts
- worker/src/newsletter/emailRenderer.ts
- worker/src/newsletter/scheduler.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P2
core: 'no'
external_service: Gmail, Telegram
legacy_id: J-110
---

## Purpose and scope

Draft, approve and send a newsletter issue manually. Priority P2, CORE no. Imported from journey J-110 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: A newsletter with recipients.

## Steps and information flow

1. `ACTION newsletter.createDraftByNewsletter {"newsletterId":"<id>"}` (or `newsletter.createDraftNow {}`).
2. `ACTION newsletter.issue.update {"issueId":"<id>","subject":"...","rendered_content":"<html>"}`.
3. `ACTION newsletter.approveIssue {"issueId":"<id>"}`, then `ACTION newsletter.sendApproved {"issueId":"<id>"}`.
4. Try send before approve; try `newsletter.regenerateIssue` on a sent issue.

## Modules and code map

worker/src/newsletter/handlers.ts, worker/src/newsletter/draftCreator.ts, worker/src/newsletter/emailRenderer.ts, worker/src/newsletter/scheduler.ts

Code anchors that exist: worker/src/newsletter/handlers.ts, worker/src/newsletter/draftCreator.ts, worker/src/newsletter/emailRenderer.ts, worker/src/newsletter/scheduler.ts

## Success and acceptance

Send before approve -> `Cannot send issue with status 'draft' — must be approved first`; regenerate sent -> `Cannot regenerate an issue that has already been sent.`; recipients receive the mail; `markIssueSent` flips status.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
