---
id: 2026-10-27-j003-fresh-cloudflare-account-against-the-committed
title: J-003 Fresh Cloudflare account against the committed wrangler ids
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: workflow
scope_type: section
scope: worker
actor: Self-hosting operator
trigger: Operator whose Cloudflare account is NOT the repo owner's; untouched clone.
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- setup/cloudflare.py
- setup/worker_config.py
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P1
core: 'yes'
external_service: Cloudflare
legacy_id: J-003
---

## Purpose and scope

Fresh Cloudflare account against the committed wrangler ids. Priority P1, CORE yes. Imported from journey J-003 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Self-hosting operator. Preconditions: Operator whose Cloudflare account is NOT the repo owner's; untouched clone.

## Steps and information flow

1. Open `worker/wrangler.jsonc`: it contains a concrete `database_id` (not a placeholder), concrete KV `id`/`preview_id`, the owner's `GOOGLE_CLIENT_ID`, `ALLOWED_EMAILS`, `ADMIN_EMAILS`, `GOOGLE_CLOUD_STORAGE_BUCKET`, `GENERATION_WORKER_URL`.
2. Run `python setup.py --cloudflare`.
3. `provision_d1_database()` treats any id that is not empty / `REPLACE_WITH_*` / `00000000-0000-0000-0000-000000000001` as already provisioned and skips `wrangler d1 create`; it then runs `_apply_d1_migrations(remote=True)` against that id.
- CODE-READING FINDING: a non-owner operator hits the owner's D1 id (auth error from Cloudflare) or, worse, if the same account, reuses the owner's database. Same for KV ids. The wizard has no "reset ids" step.

## Modules and code map

worker/wrangler.jsonc, setup/cloudflare.py (`provision_d1_database`, `_d1_id_is_placeholder`, `_patch_d1_database_id`), setup/worker_config.py

Code anchors that exist: setup/cloudflare.py, setup/worker_config.py

## Success and acceptance

After setup, `worker/wrangler.jsonc` `d1_databases[0].database_id` equals an id returned by `npx wrangler d1 list` for the operator's account, and `ADMIN_EMAILS` / `ALLOWED_EMAILS` contain the operator's email, not the owner's.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
