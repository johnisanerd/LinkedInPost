---
id: 2026-10-27-j051-trending-panels-youtube-linkedin-instagram-use
title: J-051 Trending panels (YouTube, LinkedIn, Instagram) use deployment-wide credentials
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Approved end user
trigger: '`YOUTUBE_API_KEY` / `LINKEDIN_ACCESS_TOKEN` / `INSTAGRAM_ACCESS_TOKEN` + `INSTAGRAM_USER_ID` as worker secrets (or not).'
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/index.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P2
core: 'no'
external_service: YouTube, LinkedIn, Instagram
legacy_id: J-051
---

## Purpose and scope

Trending panels (YouTube, LinkedIn, Instagram) use deployment-wide credentials. Priority P2, CORE no. Imported from journey J-051 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: `YOUTUBE_API_KEY` / `LINKEDIN_ACCESS_TOKEN` / `INSTAGRAM_ACCESS_TOKEN` + `INSTAGRAM_USER_ID` as worker secrets (or not).

## Steps and information flow

1. `/feed` trending section, or `ACTION trendingYouTube {"query":"ai"}`, `ACTION trendingLinkedIn {"orgId":"123"}`, `ACTION trendingInstagram {"query":"ai"}`, `ACTION trendingSearch {"topic":"ai","region":"US","genre":"general","windowDays":3}`.
2. Run with no secrets configured.

## Modules and code map

worker/src/index.ts (`trendingYouTube`, `trendingLinkedIn`, `trendingInstagram`, `trendingSearch`), frontend/src/features/trending/

Code anchors that exist: worker/src/index.ts

## Success and acceptance

With no key, YouTube returns `{items:[]}`, LinkedIn `{elements:[]}`, Instagram `{data:[]}` (silent empty, not an error). With keys, results show. These use env-level tokens, not the per-user D1 tokens, so every tenant reads with the operator's quota/identity. USE-CASES.md says "fallback to mock data": no mock fallback exists in the worker (the frontend may; check `frontend/src/features/trending/api`).

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
