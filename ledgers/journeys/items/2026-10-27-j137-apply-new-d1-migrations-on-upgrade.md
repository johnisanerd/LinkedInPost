---
id: 2026-10-27-j137-apply-new-d1-migrations-on-upgrade
title: J-137 Apply new D1 migrations on upgrade
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: workflow
scope_type: section
scope: worker
actor: Self-hosting operator
trigger: A deployment on an older migration level; new code deployed.
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- setup/cloudflare.py
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P1
core: 'yes'
external_service: Cloudflare
legacy_id: J-137
---

## Purpose and scope

Apply new D1 migrations on upgrade. Priority P1, CORE yes. Imported from journey J-137 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Self-hosting operator. Preconditions: A deployment on an older migration level; new code deployed.

## Steps and information flow

1. `cd worker && npx wrangler d1 migrations apply linkedin-pipeline-db --remote` (or `python setup.py --cloudflare`, which applies local then remote).
2. For the generation worker: `python setup.py --cloudflare` also calls `_apply_generation_worker_d1_migrations`.
3. Deploy workers; sign in.

## Modules and code map

worker/migrations/*.sql, setup/cloudflare.py (`_apply_d1_migrations`, `_apply_generation_worker_d1_migrations`), .github/workflows/deploy-workers.yml

Code anchors that exist: setup/cloudflare.py

## Success and acceptance

Lists 0001..0021 as applied; existing users keep working and become `status='active'` with `monthly_token_budget=500000` (defaults from 0019); `pipeline_state` rows preserved by the rebuild in 0010 (verify row counts before/after on a copy). Deploying code BEFORE migrating gives runtime `no such column/table` errors (J-133): the deploy workflow/docs must order migrate-then-deploy. The 0019 file header comment says 0018 (cosmetic).

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
