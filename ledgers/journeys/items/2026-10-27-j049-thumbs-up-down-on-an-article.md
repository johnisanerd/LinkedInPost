---
id: 2026-10-27-j049-thumbs-up-down-on-an-article
title: J-049 Thumbs up/down on an article
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Approved end user
trigger: Feed article.
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/index.ts
- worker/migrations/0021_article_feedback.sql
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P3
core: 'no'
external_service: none
legacy_id: J-049
---

## Purpose and scope

Thumbs up/down on an article. Priority P3, CORE no. Imported from journey J-049 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: Feed article.

## Steps and information flow

1. `ACTION setArticleFeedback {"articleUrl":"https://example.com/a","vote":"up"}`; `{"vote":null}` removes; `{"vote":"x"}` errors.
2. `ACTION getArticleFeedback {}`.

## Modules and code map

worker/src/index.ts, worker/migrations/0021_article_feedback.sql, frontend/src/features/feed/

Code anchors that exist: worker/src/index.ts, worker/migrations/0021_article_feedback.sql

## Success and acceptance

`{vote:"up"}` / `{vote:null}`; `vote must be "up" or "down".`; map returned is per user.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
