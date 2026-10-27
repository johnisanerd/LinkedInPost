---
id: 2026-10-27-j009-tsc-noemit-gate-inside-setup-py
title: J-009 `tsc --noEmit` gate inside setup.py
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: workflow
scope_type: section
scope: setup
actor: Self-hosting operator
trigger: Any Worker flag passed (`--install-worker-deps`, `--cloudflare`, `--deploy-worker`, `--sync-github-secrets`, `--all`).
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- setup/cloudflare.py
- setup.py
- AGENTS.md
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P2
core: 'yes'
external_service: none
legacy_id: J-009
---

## Purpose and scope

`tsc --noEmit` gate inside setup.py. Priority P2, CORE yes. Imported from journey J-009 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Self-hosting operator. Preconditions: Any Worker flag passed (`--install-worker-deps`, `--cloudflare`, `--deploy-worker`, `--sync-github-secrets`, `--all`).

## Steps and information flow

1. Run `python setup.py --install-worker-deps` on a tree with a TS type error in `frontend/` or `worker/`.

## Modules and code map

setup/cloudflare.py (`run_typescript_dry_run`), setup.py, AGENTS.md

Code anchors that exist: setup/cloudflare.py, setup.py, AGENTS.md

## Success and acceptance

`run_typescript_dry_run()` raises `RuntimeError("<label> type check failed ...")`, aborting setup (an unrelated type error in frontend blocks a worker-only deploy). On a clean tree both print "no type errors".

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
