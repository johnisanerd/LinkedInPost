---
id: 2026-10-27-j041-open-the-feed-cache-first-auto
title: J-041 Open the feed (cache-first, auto-fetch when stale)
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Approved end user
trigger: Interest group with topics (J-043) or topics selected.
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/index.ts
- worker/src/db/feedArticles.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P2
core: 'yes'
external_service: 'other (news providers: RSS / NewsAPI / SerpAPI)'
legacy_id: J-041
---

## Purpose and scope

Open the feed (cache-first, auto-fetch when stale). Priority P2, CORE yes. Imported from journey J-041 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: Interest group with topics (J-043) or topics selected.

## Steps and information flow

1. Open `/feed`.
2. API: `ACTION getFeedArticles {"topics":["AI agents"]}`.

## Modules and code map

frontend/src/features/feed/FeedPage.tsx, worker/src/index.ts (`getFeedArticles`), worker/src/db/feedArticles.ts, packages/researcher

Code anchors that exist: worker/src/index.ts, worker/src/db/feedArticles.ts

## Success and acceptance

Returns `{articles,fetchedAt,stale}`. Fresh (<24 h) cache returned immediately; stale/empty triggers `trendingSearch` for the first topic only and saves a snapshot. Errors in the auto-fetch are swallowed (empty list, no message): confirm the UI explains an empty feed.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
