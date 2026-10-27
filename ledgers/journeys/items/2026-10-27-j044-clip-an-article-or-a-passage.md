---
id: 2026-10-27-j044-clip-an-article-or-a-passage
title: J-044 Clip an article or a passage
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Approved end user
trigger: Article visible in the feed.
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/index.ts
- worker/src/db/clips.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P1
core: 'yes'
external_service: none
legacy_id: J-044
---

## Purpose and scope

Clip an article or a passage. Priority P1, CORE yes. Imported from journey J-044 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: Article visible in the feed.

## Steps and information flow

1. Click the clip (scissors) button on an article, or select a passage and clip.
2. API: `ACTION createClip {"type":"article","articleTitle":"T","articleUrl":"https://example.com/a","source":"S","publishedAt":"2026-10-20","thumbnailUrl":"","passageText":""}`; also `type:"passage"`.
3. `ACTION listClips {}`; `ACTION updateClip {"id":"<id>","passageText":"edited"}`; `ACTION deleteClip {"id":"<id>"}`.

## Modules and code map

worker/src/index.ts (`createClip`...), worker/src/db/clips.ts, frontend/src/features/feed/components/DebateModeView.tsx

Code anchors that exist: worker/src/index.ts, worker/src/db/clips.ts

## Success and acceptance

Create returns the clip; invalid type -> `type must be "article" or "passage".`; missing title/url -> explicit errors; list shows only the caller's clips.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
