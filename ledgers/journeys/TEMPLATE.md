---
id: YYYY-MM-DD-short-slug
title: Actor achieves an observable outcome
status: planned
created: YYYY-MM-DD
updated: YYYY-MM-DD
journey_type: user
scope_type: section
scope: named-area
actor: Who starts or consumes this journey
trigger: What starts it
verification_owner: Who verifies the complete journey
source_revision: null
checked_at: null
modules: []
code_paths: []
related: []
docs: []
---

## Purpose and scope

Explain the user/workflow/information-flow outcome and exclusions. For feature
scope, use the existing feature record ID. Split independently verifiable variants.

## Actor, trigger and prerequisites

Actor, entry point, configuration/state, permissions, data, and external prerequisites.

## Steps and information flow

| Step | Entry/owner | Input → output/state | Handoff/failure behavior |
| --- | --- | --- | --- |
| 1 | Actual module/function | Concrete evidence | Next owner or recovery |

## Modules and code map

Explain each module's responsibility and participating folders/files. Maintain
modules/code_paths metadata. Source paths may name files or directories.

## Success and acceptance

Observable end-to-end outcomes, ownership and required acceptance checks. Separate
normal, failure, boundary and restart variants; passing a component is not enough.

## Failure, edge cases and recovery

What blocks/fails, what is retained, how retries/restarts behave, and who intervenes.

## Verification evidence

Pinned revision/date, commands/checks and results, doubles, exclusions and uncertainty.
Verified needs source_revision, checked_at with timezone, named verification owner,
nonempty evidence/code map, and no unresolved linked backlog work.

## Gaps and linked work

Link supporting evidence with related. Link tickets/features/reviews/research to
this journey using their journeys field; the board derives their current status.
Do not maintain a second manually updated ticket list/status here.

## Next actions

Required outcomes and dependencies. Search all linked work, respect active claims,
resolve required blockers, and rerun complete acceptance before declaring verified.
Do not auto-close unrelated work or treat closed tickets as test evidence.
