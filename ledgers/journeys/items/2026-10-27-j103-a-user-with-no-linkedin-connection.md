---
id: 2026-10-27-j103-a-user-with-no-linkedin-connection
title: J-103 A user with no LinkedIn connection publishes through someone else's token
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: worker
actor: Non-approved / unauthorised user
trigger: SaaS; user A connected LinkedIn earlier; user B signed up, never connected anything, has a sheet (J-031 resolved).
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/index.ts
- worker/src/db/socialIntegrations.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P0
core: 'yes'
external_service: LinkedIn
legacy_id: J-103
---

## Purpose and scope

A user with no LinkedIn connection publishes through someone else's token. Priority P0, CORE yes. Imported from journey J-103 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Non-approved / unauthorised user. Preconditions: SaaS; user A connected LinkedIn earlier; user B signed up, never connected anything, has a sheet (J-031 resolved).

## Steps and information flow

1. As B: `ACTION publishContent {"row":{...},"channel":"linkedin","message":"hello"}`.
2. Inspect which account posted.
- CODE-READING FINDING: each OAuth callback calls `persistLinkedInConnection(env, accessToken, personUrn)` which writes the KV `shared-config` (single global slot, last writer wins) in addition to the per-user D1 row. `publishContent` tries `getSocialIntegration(userId,'linkedin')` first and falls back to `config.linkedin*` from KV when B has none, so B posts as A (or whoever connected last). Same pattern for Instagram, Gmail, WhatsApp, Telegram and the trending actions (env tokens).

## Modules and code map

worker/src/index.ts (`publishContent`, `persistLinkedInConnection`, `handleLinkedInCallback`, `loadStoredConfig`), worker/src/db/socialIntegrations.ts

Code anchors that exist: worker/src/index.ts, worker/src/db/socialIntegrations.ts

## Success and acceptance

Desired: B gets `LinkedIn publishing is not configured...`/"connect your account" and nothing is posted. Expected to FAIL today in multi-tenant deployments (single-owner self-hosted is fine and relies on this fallback).

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
