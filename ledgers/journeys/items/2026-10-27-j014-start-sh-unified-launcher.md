---
id: 2026-10-27-j014-start-sh-unified-launcher
title: J-014 `start.sh` unified launcher
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: overall
scope: application
actor: Developer
trigger: Node, Python, Wrangler installed.
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- start.sh
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P3
core: 'no'
external_service: none
legacy_id: J-014
---

## Purpose and scope

`start.sh` unified launcher. Priority P3, CORE no. Imported from journey J-014 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Developer. Preconditions: Node, Python, Wrangler installed.

## Steps and information flow

1. `./start.sh` (default `local`), then `./start.sh --skip-deps --skip-wizard`, `./start.sh --reset-db`, `./start.sh production`.

## Modules and code map

start.sh

Code anchors that exist: start.sh

## Success and acceptance

Unknown flags print `Unknown option: <x>` and exit 1; missing commands are reported by `check_command`; `--reset-db` asks before destroying local D1 state (read the script before running).

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
