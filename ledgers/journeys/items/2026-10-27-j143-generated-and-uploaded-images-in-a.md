---
id: 2026-10-27-j143-generated-and-uploaded-images-in-a
title: J-143 Generated and uploaded images in a shared bucket
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: worker
actor: Non-approved / unauthorised user
trigger: '`GOOGLE_CLOUD_STORAGE_BUCKET` shared by all tenants.'
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
core: 'yes'
external_service: other (Google Cloud Storage)
legacy_id: J-143
---

## Purpose and scope

Generated and uploaded images in a shared bucket. Priority P2, CORE yes. Imported from journey J-143 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Non-approved / unauthorised user. Preconditions: `GOOGLE_CLOUD_STORAGE_BUCKET` shared by all tenants.

## Steps and information flow

1. Upload an image (J-067); copy its URL.
2. Open the URL in a private window without signing in.
3. As another tenant call `ACTION promoteDraftImageUrl {...}` / `ACTION downloadDraftImage {...}` with that URL; `ACTION deleteRow` on a topic whose `topicId` collides in prefix.

## Modules and code map

worker/src/index.ts (`uploadBytesToGcs`, `gcsObjectPrefixFromTopicId`, `downloadDraftImage`, `deleteGcsObjectsForTopicRow`, `safeFetch`), worker/src/media

Code anchors that exist: worker/src/index.ts

## Success and acceptance

Document the intended model: URLs must be public-readable for Instagram/LinkedIn to fetch them (so anyone with the URL can view), object names must be unguessable (`gcsObjectPrefixFromTopicId`), and `deleteGcsObjectsForTopicRow` must not delete objects outside the caller's own prefix. `downloadDraftImage` fetches an arbitrary URL on behalf of the user: confirm it blocks private/internal addresses (SSRF) — `safeFetch` is used for token verification; check `downloadDraftImage`.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
