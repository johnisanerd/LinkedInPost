---
id: 2026-10-27-lr-061-gemini-token-usage-is-read-from
title: Gemini token usage is read from the wrong field, so Gemini calls log 0 tokens and the usage budget never moves.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j058-streaming-generation-bypasses-the-monthly-token
- 2026-10-27-j124-usage-meter-and-usage-page
- 2026-10-27-j125-monthly-token-budget-exhausted
- 2026-10-27-j126-self-hosted-deployment-still-enforces-the
related: []
docs:
- worker/src/llm/providers/gemini.ts
- worker/src/generation/types.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: investigation
severity: P1
area: worker/llm
raw_id: LR-061
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Gemini token usage is read from the wrong field, so Gemini calls log 0 tokens and the usage budget never moves. Suspected, not confirmed (see Confidence in the evidence).

## Evidence and reproduction

- **Confidence:** hypothesis
- **Journeys:** J-058, J-124..J-126
- **Aliases:** WKB-013
- **Evidence:** worker/src/llm/providers/gemini.ts:115,177; worker/src/generation/types.ts:139-142
- **Repro:** static. Executor: run one generation, then `SELECT prompt_tokens, completion_tokens FROM llm_usage_log ORDER BY created_at DESC LIMIT 1`.
- **Fix hint:** Read payload.usageMetadata first, fall back to the candidate path, fix the type; confirm with one live call.

## Acceptance criteria

- The question in the title is answered in Attempts with file:line evidence and a clear yes/no.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Read payload.usageMetadata first, fall back to the candidate path, fix the type; confirm with one live call.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-061). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: hypothesis from static reading of worker/src/llm/providers/gemini.ts:115,177; confirm by running the Repro and observing the described behaviour.
