---
id: 2026-10-27-j127-empty-admin-emails-makes-the-repo
title: J-127 Empty `ADMIN_EMAILS` makes the repo owner an admin
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: workflow
scope_type: section
scope: worker
actor: Self-hosting operator
trigger: Worker deployed with `ADMIN_EMAILS` unset or empty.
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/index.ts
- setup/worker_config.py
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P0
core: 'yes'
external_service: none
legacy_id: J-127
---

## Purpose and scope

Empty `ADMIN_EMAILS` makes the repo owner an admin. Priority P0, CORE yes. Imported from journey J-127 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Self-hosting operator. Preconditions: Worker deployed with `ADMIN_EMAILS` unset or empty.

## Steps and information flow

1. Sign in as `99pratyush@gmail.com` (or inspect `resolveAdminEmailAllowlist`).
2. Sign in as the operator.

## Modules and code map

worker/src/index.ts (`DEFAULT_ADMIN_EMAIL`, `resolveAdminEmailAllowlist`), worker/wrangler.jsonc, setup/worker_config.py

Code anchors that exist: worker/src/index.ts, setup/worker_config.py

## Success and acceptance

Desired: with no `ADMIN_EMAILS`, nobody is admin (or deploy refuses). CODE-READING FINDING: `resolveAdminEmailAllowlist` falls back to `DEFAULT_ADMIN_EMAIL = '99pratyush@gmail.com'`, so on any customer's deployment missing the variable, the project author gets admin (shared config, tokens, all users) and the real operator is not admin. The committed `worker/wrangler.jsonc` also lists the owner's and another person's emails in `ALLOWED_EMAILS`/`ADMIN_EMAILS`.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
