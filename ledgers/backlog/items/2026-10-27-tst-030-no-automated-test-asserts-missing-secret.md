---
id: 2026-10-27-tst-030-no-automated-test-asserts-missing-secret
title: 'No automated test asserts: Missing `SECRET_ENCRYPTION_KEY`'
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j132-missing-secret-encryption-key
related: []
docs:
- setup/wizard/tests/test_apikeys.py
- tests/setup/test_setup_wiring.py
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: test-gap
severity: P1
area: Failure and recovery
raw_id: TST-030
source_file: docs/launch-readiness/findings/TEST-COVERAGE.md
---

## Problem

No automated test asserts: Missing `SECRET_ENCRYPTION_KEY`.

## Evidence and reproduction

- **Journeys:** J-132
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'SECRET_ENCRYPTION_KEY'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned 2 file(s): setup/wizard/tests/test_apikeys.py, tests/setup/test_setup_wiring.py. None of these asserts the pass check (they match the term in an unrelated assertion or a mock).
- **Repro:** Popup shows `Missing SECRET_ENCRYPTION_KEY in the Worker environment.` CODE-READING FINDING: in `handleLinkedInCallback`, `persistLinkedInConnection` (KV) runs before `requireSecretEncryptionKey`; the per-user D1 upsert is wrapped in `.catch(() => undefined)` only for the DB call, so the error ends the flow after the shared token was already saved: the popup says failed while the shared slot changed. `startLinkedI...
- **Fix hint:** add a test that asserts: LinkedIn callback without SECRET_ENCRYPTION_KEY fails before persisting any token. Test file suggestion: worker/src/oauth.test.ts

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

add a test that asserts: LinkedIn callback without SECRET_ENCRYPTION_KEY fails before persisting any token. Test file suggestion: worker/src/oauth.test.ts

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/TEST-COVERAGE.md (TST-030). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: grepped test globs and read test titles for the journey's route/action/message text; no test run.
