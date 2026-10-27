---
id: 2026-10-27-j007-re-running-setup-py-is-idempotent
title: J-007 Re-running setup.py is idempotent; `--skip-google` path
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: workflow
scope_type: section
scope: setup
actor: Self-hosting operator
trigger: A completed first run.
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- setup.py
- setup/google_resources.py
- setup/python_requirements.py
- setup/cloudflare.py
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P2
core: 'yes'
external_service: Google Sheets, Cloudflare
legacy_id: J-007
---

## Purpose and scope

Re-running setup.py is idempotent; `--skip-google` path. Priority P2, CORE yes. Imported from journey J-007 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Self-hosting operator. Preconditions: A completed first run.

## Steps and information flow

1. `python setup.py --cloudflare --skip-google`.
2. `python setup.py --cloudflare` (without `--skip-google`; the default path calls `_create_google_resources` and `ensure_google_setup_python_deps()`).
3. Compare sheet / folder / doc created.

## Modules and code map

setup.py, setup/google_resources.py, setup/python_requirements.py, setup/cloudflare.py

Code anchors that exist: setup.py, setup/google_resources.py, setup/python_requirements.py, setup/cloudflare.py

## Success and acceptance

Step 1 prints "Google resource creation: skipped by flag" and leaves existing resources; step 2 reuses the existing LINKEDIN folder, content calendar sheet and posted doc (does not create duplicates); KV namespaces reused, D1 not recreated.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
