---
id: 2026-10-27-tst-016-no-automated-test-asserts-send-via
title: 'No automated test asserts: Send via WhatsApp'
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j079-send-via-whatsapp
related: []
docs:
- frontend/tests/e2e/add-topic.spec.ts
- frontend/tests/e2e/connections.spec.ts
- frontend/tests/e2e/journeys/07-connections-setup.spec.ts
- frontend/tests/e2e/journeys/18-channel-previews.spec.ts
- frontend/tests/e2e/journeys/06-publish-channels.spec.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: test-gap
severity: P1
area: Scheduling and publishing
raw_id: TST-016
source_file: docs/launch-readiness/findings/TEST-COVERAGE.md
---

## Problem

No automated test asserts: Send via WhatsApp.

## Evidence and reproduction

- **Journeys:** J-079
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'WhatsApp|wamid'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned 24 file(s): frontend/tests/e2e/add-topic.spec.ts, frontend/tests/e2e/connections.spec.ts, frontend/tests/e2e/journeys/07-connections-setup.spec.ts, frontend/tests/e2e/journeys/18-channel-previews.spec.ts, frontend/tests/e2e/journeys/06-publish-channels.spec.ts. None of these asserts the pass check (they match the term in an unrelated assertion or a mock).
- **Repro:** `messageId` = wamid; invalid number -> normalizer error; the code sends non-template messages ("Send non-template WhatsApp messages through Meta Cloud API"), which Meta rejects outside the customer service window: the error text from Meta must reach the user.
- **Fix hint:** add a test that asserts: a WhatsApp send returns a wamid, and invalid numbers or Meta errors reach the user. Test file suggestion: worker/src/channels/whatsapp.test.ts

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

add a test that asserts: a WhatsApp send returns a wamid, and invalid numbers or Meta errors reach the user. Test file suggestion: worker/src/channels/whatsapp.test.ts

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/TEST-COVERAGE.md (TST-016). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: grepped test globs and read test titles for the journey's route/action/message text; no test run.
