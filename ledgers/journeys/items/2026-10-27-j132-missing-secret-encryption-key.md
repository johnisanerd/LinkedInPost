---
id: 2026-10-27-j132-missing-secret-encryption-key
title: J-132 Missing `SECRET_ENCRYPTION_KEY`
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: workflow
scope_type: section
scope: worker
actor: Self-hosting operator
trigger: Worker without `SECRET_ENCRYPTION_KEY`.
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
priority: P1
core: 'yes'
external_service: LinkedIn
legacy_id: J-132
---

## Purpose and scope

Missing `SECRET_ENCRYPTION_KEY`. Priority P1, CORE yes. Imported from journey J-132 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Self-hosting operator. Preconditions: Worker without `SECRET_ENCRYPTION_KEY`.

## Steps and information flow

1. Complete the LinkedIn authorization in the popup (J-094).

## Modules and code map

worker/src/index.ts (`requireSecretEncryptionKey`, `handleLinkedInCallback`, `persistLinkedInConnection`), setup/worker_config.py

Code anchors that exist: worker/src/index.ts, setup/worker_config.py

## Success and acceptance

Popup shows `Missing SECRET_ENCRYPTION_KEY in the Worker environment.` CODE-READING FINDING: in `handleLinkedInCallback`, `persistLinkedInConnection` (KV) runs before `requireSecretEncryptionKey`; the per-user D1 upsert is wrapped in `.catch(() => undefined)` only for the DB call, so the error ends the flow after the shared token was already saved: the popup says failed while the shared slot changed. `startLinkedInAuth` does not pre-check the key, so the user finds out only at the end.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
