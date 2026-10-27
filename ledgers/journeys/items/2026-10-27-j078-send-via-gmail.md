---
id: 2026-10-27-j078-send-via-gmail
title: J-078 Send via Gmail
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Approved end user
trigger: Gmail connected (J-096); To address.
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/index.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P1
core: 'yes'
external_service: Gmail
legacy_id: J-078
---

## Purpose and scope

Send via Gmail. Priority P1, CORE yes. Imported from journey J-078 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: Gmail connected (J-096); To address.

## Steps and information flow

1. Editor -> Email tab: fill To, Cc, Bcc, Subject; the form saves via `ACTION saveEmailFields {"row":{...},"emailTo":"a@b.co","emailCc":"","emailBcc":"","emailSubject":"Hi"}`.
2. Click "Send via Gmail": `ACTION publishContent {"row":{...},"channel":"gmail","message":"..."}`.
3. Repeat with an empty To.

## Modules and code map

frontend/src/features/review-editor/components, worker/src/index.ts (gmail branch), worker/src/integrations/gmail

Code anchors that exist: worker/src/index.ts

## Success and acceptance

Mail arrives with subject/body; row `Published`; empty To -> UI notice "Gmail needs at least one To address..."; refresh-token revoked -> actionable error and `needs_reauth` visible in `/connections`.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
