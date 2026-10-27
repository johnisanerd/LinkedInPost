---
id: 2026-10-27-j077-publish-to-instagram-image-required
title: J-077 Publish to Instagram (image required)
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: worker
actor: Approved end user
trigger: Instagram Business account connected (J-095); a selected image URL reachable by Meta.
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/index.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P1
core: 'yes'
external_service: Instagram
legacy_id: J-077
---

## Purpose and scope

Publish to Instagram (image required). Priority P1, CORE yes. Imported from journey J-077 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: Instagram Business account connected (J-095); a selected image URL reachable by Meta.

## Steps and information flow

1. Select channel Instagram, choose an image in the Media tab, click "Publish to Instagram".
2. `ACTION publishContent {"row":{...},"channel":"instagram","message":"caption","imageUrls":["https://..."]}`.
3. Repeat with no image.

## Modules and code map

worker/src/index.ts (`publishContent` instagram branch), worker/src/integrations/instagram

Code anchors that exist: worker/src/index.ts

## Success and acceptance

Step 2 returns `messageId` = Instagram post id and the post is live; step 3 -> `Instagram publishing requires a selected image.` Carousel: up to `MAX_IMAGES_PER_POST` images. Selected-but-private GCS URLs would make Meta reject the media; confirm bucket objects are public-readable (see J-143).

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
