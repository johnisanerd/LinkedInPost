---
id: 2026-10-27-j112-newsletter-actions-are-not-tenant-scoped
title: J-112 Newsletter actions are not tenant-scoped
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: worker
actor: Non-approved / unauthorised user
trigger: Tenant A has a newsletter/issue with ids; tenant B signed in.
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/index.ts
- worker/src/newsletter/handlers.ts
- worker/src/newsletter/persistence.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P0
core: 'yes'
external_service: Gmail
legacy_id: J-112
---

## Purpose and scope

Newsletter actions are not tenant-scoped. Priority P0, CORE yes. Imported from journey J-112 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Non-approved / unauthorised user. Preconditions: Tenant A has a newsletter/issue with ids; tenant B signed in.

## Steps and information flow

1. As B: `ACTION newsletter.approveIssue {"issueId":"<A's issue>"}`.
2. As B: `ACTION newsletter.sendApproved {"issueId":"<A's issue>"}`, `ACTION newsletter.issue.update {"issueId":"<A's issue>","subject":"x"}`, `ACTION newsletter.delete {"newsletterId":"<A's newsletter>"}`, `ACTION newsletter.listIssuesByNewsletter {"newsletterId":"<A's newsletter>"}`, `ACTION newsletter.regenerateIssue {...}`.

## Modules and code map

worker/src/index.ts (`newsletter.*` cases), worker/src/newsletter/handlers.ts, worker/src/newsletter/persistence.ts

Code anchors that exist: worker/src/index.ts, worker/src/newsletter/handlers.ts, worker/src/newsletter/persistence.ts

## Success and acceptance

Desired: all refused (not found / forbidden). CODE-READING FINDING: these handlers take only `issueId`/`newsletterId` and run `WHERE id = ?` with no `spreadsheet_id` or user check (`handleApproveNewsletterIssue(db, issueId)`, `handleSendApprovedNewsletterIssue`, `handleDeleteNewsletter(db, newsletterId)`). Ids are UUID-like so exploitation needs the id, but ids appear in URLs/UI/exports. Cross-tenant read/modify/send.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
