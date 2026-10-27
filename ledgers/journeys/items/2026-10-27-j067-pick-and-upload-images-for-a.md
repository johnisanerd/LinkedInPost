---
id: 2026-10-27-j067-pick-and-upload-images-for-a
title: J-067 Pick and upload images for a post
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Approved end user
trigger: '`GOOGLE_CLOUD_STORAGE_BUCKET` and service account with `objectAdmin`; `SERPAPI_KEY` for search (if used).'
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/index.ts
- frontend/src/services/selectedImageUrls.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P1
core: 'yes'
external_service: other (Google Cloud Storage, SerpAPI)
legacy_id: J-067
---

## Purpose and scope

Pick and upload images for a post. Priority P1, CORE yes. Imported from journey J-067 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: `GOOGLE_CLOUD_STORAGE_BUCKET` and service account with `objectAdmin`; `SERPAPI_KEY` for search (if used).

## Steps and information flow

1. Editor -> Media tab (`ImageAssetManager`).
2. Search more: `ACTION fetchDraftImages {"topic":"...","searchQuery":"","count":8}`.
3. Promote a remote image: `ACTION promoteDraftImageUrl {...}`.
4. Upload a file: `ACTION uploadDraftImage {"topicId":"<id>","fileName":"a.png","contentType":"image/png","dataUrl":"data:image/png;base64,..."}`; try a non-image data URL and a very large file.
5. Download: `ACTION downloadDraftImage {...}`.

## Modules and code map

frontend/src/components/ImageAssetManager.tsx, worker/src/index.ts (`fetchDraftImages`, `uploadDraftImage`, `promoteDraftImageUrl`, `downloadDraftImage`), frontend/src/services/selectedImageUrls.ts

Code anchors that exist: worker/src/index.ts, frontend/src/services/selectedImageUrls.ts

## Success and acceptance

Search returns at most 8 URLs; upload returns `{imageUrl}` pointing into the bucket; non-image -> `Only image uploads are supported.`; missing `topicId` -> `topicId is required to upload an image.` No explicit size cap in `uploadDraftImage` (CODE-READING FINDING: only the Worker request limit applies; check behaviour and message for a 20 MB image). Selected URLs end up in `selected_image_urls_json`.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
