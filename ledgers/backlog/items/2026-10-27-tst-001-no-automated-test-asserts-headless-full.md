---
id: 2026-10-27-tst-001-no-automated-test-asserts-headless-full
title: 'No automated test asserts: Headless full bootstrap with `python setup.py --all`'
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j002-headless-full-bootstrap-with-python-setup
related: []
docs:
- setup.py
- setup/tests/test_cli.py
- tests/test_mutation_tester.py
- tests/setup/test_cli.py
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: test-gap
severity: P1
area: First-run, setup and install
raw_id: TST-001
source_file: docs/launch-readiness/findings/TEST-COVERAGE.md
---

## Problem

No automated test asserts: Headless full bootstrap with `python setup.py --all`.

## Evidence and reproduction

- **Journeys:** J-002
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'setup.py --all|exit code|GENERATION_WORKER_URL'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned 2 file(s): setup/tests/test_cli.py, tests/test_mutation_tester.py. None of these asserts the pass check (they match the term in an unrelated assertion or a mock).
- **Repro:** Exit code 0; `GET {WORKER_URL}/` returns `{"ok":true,"data":{"status":"ok","backend":"cloudflare-worker"}}`; the main worker `GENERATION_WORKER_URL` var points at the generation worker URL.
- **Fix hint:** add a test that asserts: run the --all pipeline with subprocess and network mocked and assert exit code 0 and the GENERATION_WORKER_URL var written. Test file suggestion: tests/setup/test_cli.py

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

add a test that asserts: run the --all pipeline with subprocess and network mocked and assert exit code 0 and the GENERATION_WORKER_URL var written. Test file suggestion: tests/setup/test_cli.py

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/TEST-COVERAGE.md (TST-001). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: grepped test globs and read test titles for the journey's route/action/message text; no test run.
