---
id: 2026-10-27-j118-youtube-comment-polling-schedule
title: J-118 YouTube comment polling schedule
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Tenant admin
trigger: YouTube connected; GitHub Actions secrets `YOUTUBE_API_KEY`, `YOUTUBE_OAUTH_TOKEN`, `VITE_WORKER_URL`, `WORKER_SCHEDULER_SECRET`.
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/automations/routes.ts
- automations/youtube_poller.py
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P2
core: 'no'
external_service: YouTube
legacy_id: J-118
---

## Purpose and scope

YouTube comment polling schedule. Priority P2, CORE no. Imported from journey J-118 in docs/launch-readiness/journeys/JOURNEYS.md. The journey designer marked part of this journey NOT IMPLEMENTED per code reading.

## Actor, trigger and prerequisites

Persona: Tenant admin. Preconditions: YouTube connected; GitHub Actions secrets `YOUTUBE_API_KEY`, `YOUTUBE_OAUTH_TOKEN`, `VITE_WORKER_URL`, `WORKER_SCHEDULER_SECRET`.

## Steps and information flow

1. `/automations` -> YouTube scheduler, enter `0 */6 * * *`, Save (`PUT /automations/youtube/schedule`; errors are swallowed: "silently ignored").
2. Run the workflow manually (`workflow_dispatch` with `channel_id`) -> `automations/youtube_poller.py` posts to `POST /automations/internal/youtube/poll` with header `X-Scheduler-Secret`.

## Modules and code map

frontend/src/features/automations/YouTubeScheduler.tsx, worker/src/automations/routes.ts, .github/workflows/youtube-comment-poll.yml, automations/youtube_poller.py

Code anchors that exist: worker/src/automations/routes.ts, automations/youtube_poller.py

## Success and acceptance

`GET /automations/youtube/schedule` returns the saved cron; manual dispatch records `lastPolledAt`. (NOT IMPLEMENTED per code reading: `.github/workflows/youtube-comment-poll.yml` has its `schedule:` block commented out, so the saved cron never triggers anything; the UI text "Use a GitHub Actions cron expression" is not wired to the workflow.)

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record. Not implemented per the journey designer: see the NOT IMPLEMENTED text in the steps.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
