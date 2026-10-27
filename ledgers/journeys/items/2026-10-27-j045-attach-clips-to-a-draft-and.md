---
id: 2026-10-27-j045-attach-clips-to-a-draft-and
title: J-045 Attach clips to a draft and cluster them
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: worker
actor: Approved end user
trigger: At least two clips and a topic.
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
priority: P2
core: 'yes'
external_service: LLM provider
legacy_id: J-045
---

## Purpose and scope

Attach clips to a draft and cluster them. Priority P2, CORE yes. Imported from journey J-045 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: At least two clips and a topic.

## Steps and information flow

1. `ACTION assignClipToPost {"clipId":"<c>","postId":"<topicId>"}`; `ACTION unassignClipFromPost {...}`.
2. `ACTION clusterDraftClips {"draftText":"...","clips":[{"title":"A","snippet":"..."},{"title":"B","snippet":"..."}]}`.

## Modules and code map

worker/src/index.ts, worker/src/db/clips.ts

Code anchors that exist: worker/src/index.ts, worker/src/db/clips.ts

## Success and acceptance

Assign returns the link; cluster returns `{themes:[{name,indices}],support:[...],challenge:[...]}`; empty clips returns empty arrays without an LLM call. `postId` ownership is not checked against the topic table in the dispatcher (CODE-READING FINDING: verify `assignClipToPost` in db/clips.ts).

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
