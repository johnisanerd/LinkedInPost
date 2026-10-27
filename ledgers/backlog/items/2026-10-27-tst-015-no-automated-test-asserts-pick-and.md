---
id: 2026-10-27-tst-015-no-automated-test-asserts-pick-and
title: 'No automated test asserts: Pick and upload images for a post'
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j067-pick-and-upload-images-for-a
related: []
docs:
- tests-e2e/e2e/journeys/47-wiring-loop28.spec.ts
- tests-e2e/e2e/journeys/60-wiring-loop35.spec.ts
- tests-e2e/e2e/journeys/39-wiring-loop25.spec.ts
- tests-e2e/e2e/journeys/48-wiring-loop29.spec.ts
- frontend/tests/e2e/journeys/04-review-edit.spec.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: test-gap
severity: P1
area: Review, edit, variants and images
raw_id: TST-015
source_file: docs/launch-readiness/findings/TEST-COVERAGE.md
---

## Problem

No automated test asserts: Pick and upload images for a post.

## Evidence and reproduction

- **Journeys:** J-067
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'uploadDraftImage|Only image uploads|fetchDraftImages'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned 4 file(s): tests-e2e/e2e/journeys/47-wiring-loop28.spec.ts, tests-e2e/e2e/journeys/60-wiring-loop35.spec.ts, tests-e2e/e2e/journeys/39-wiring-loop25.spec.ts, tests-e2e/e2e/journeys/48-wiring-loop29.spec.ts. None of these asserts the pass check (they match the term in an unrelated assertion or a mock).
- **Repro:** Search returns at most 8 URLs; upload returns `{imageUrl}` pointing into the bucket; non-image -> `Only image uploads are supported.`; missing `topicId` -> `topicId is required to upload an image.` No explicit size cap in `uploadDraftImage` (CODE-READING FINDING: only the Worker request limit applies; check behaviour and message for a 20 MB image). Selected URLs end up in `selected_image_urls_json`.
- **Fix hint:** add a test that asserts: image search returns at most 8 URLs and non-image or missing-topicId uploads give the documented errors. Test file suggestion: frontend/tests/e2e/journeys/04-review-edit.spec.ts

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

add a test that asserts: image search returns at most 8 URLs and non-image or missing-topicId uploads give the documented errors. Test file suggestion: frontend/tests/e2e/journeys/04-review-edit.spec.ts

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/TEST-COVERAGE.md (TST-015). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: grepped test globs and read test titles for the journey's route/action/message text; no test run.
