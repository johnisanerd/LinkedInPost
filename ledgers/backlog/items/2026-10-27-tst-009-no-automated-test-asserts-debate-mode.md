---
id: 2026-10-27-tst-009-no-automated-test-asserts-debate-mode
title: 'No automated test asserts: "Debate mode" returns an invented opposing article'
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j047-debate-mode-returns-an-invented-opposing
related: []
docs:
- tests-e2e/e2e/journeys/65-wiring-loop40.spec.ts
- tests-e2e/e2e/journeys/51-wiring-loop30.spec.ts
- tests-e2e/e2e/journeys/62-wiring-loop36.spec.ts
- tests-e2e/e2e/journeys/57-wiring-loop33.spec.ts
- tests-e2e/e2e/journeys/65-wiring-loop43.spec.ts
- frontend/tests/e2e/journeys/12-feed-feature.spec.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: test-gap
severity: P1
area: Feed and clipping
raw_id: TST-009
source_file: docs/launch-readiness/findings/TEST-COVERAGE.md
---

## Problem

No automated test asserts: "Debate mode" returns an invented opposing article.

## Evidence and reproduction

- **Journeys:** J-047
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'findDebateArticle|Debate'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned 15 file(s): tests-e2e/e2e/journeys/65-wiring-loop40.spec.ts, tests-e2e/e2e/journeys/51-wiring-loop30.spec.ts, tests-e2e/e2e/journeys/62-wiring-loop36.spec.ts, tests-e2e/e2e/journeys/57-wiring-loop33.spec.ts, tests-e2e/e2e/journeys/65-wiring-loop43.spec.ts. None of these asserts the pass check (they match the term in an unrelated assertion or a mock).
- **Repro:** CODE-READING FINDING: the prompt says "Generate a realistic opposing article ... Plausible publication name (e.g. Harvard Business Review)". The result is fabricated (title, source, summary) and the UI offers "Clip". Pass requires that the UI visibly labels it AI-generated / not a real article and that clipping does not save a fake URL as a source. A user quoting it on LinkedIn would publish a false citation.
- **Fix hint:** add a test that asserts: the debate-mode article is labelled AI-generated and cannot be clipped as a real article. Test file suggestion: frontend/tests/e2e/journeys/12-feed-feature.spec.ts

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

add a test that asserts: the debate-mode article is labelled AI-generated and cannot be clipped as a real article. Test file suggestion: frontend/tests/e2e/journeys/12-feed-feature.spec.ts

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/TEST-COVERAGE.md (TST-009). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: grepped test globs and read test titles for the journey's route/action/message text; no test run.
