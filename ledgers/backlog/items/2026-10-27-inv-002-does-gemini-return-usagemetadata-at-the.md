---
id: 2026-10-27-inv-002-does-gemini-return-usagemetadata-at-the
title: Does Gemini return usageMetadata at the top level of the response? (WKB-013)
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related:
- 2026-10-27-lr-061-gemini-token-usage-is-read-from
docs: []
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: investigation
severity: P1
area: worker/llm
raw_id: INV-002
source_file: docs/launch-readiness/findings/INVESTIGATE.md
---

## Problem

Does Gemini return usageMetadata at the top level of the response? (WKB-013). If true, llm_usage_log token sums stay 0 and checkTokenBudget never trips: the per-user budget does nothing for Gemini calls.

## Evidence and reproduction

- **Question:** gemini.ts reads payload.candidates?.[0]?.usageMetadata. Is usageMetadata actually a top-level field of the generateContent response, so the code logs 0 tokens?
- **Why it matters:** If true, llm_usage_log token sums stay 0 and checkTokenBudget never trips: the per-user budget does nothing for Gemini calls.
- **How to settle it:** Make one live Gemini generateContent call with a test key and log Object.keys(payload); or read the current Gemini API reference for GenerateContentResponse.usageMetadata. Then run one generation and `SELECT prompt_tokens, completion_tokens FROM llm_usage_log ORDER BY created_at DESC LIMIT 1` on the local D1.
- **Related items:** LR-061, WKB-013
- **Owner:**

## Acceptance criteria

- The question in the title is answered in Attempts with file:line evidence and a clear yes/no.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/INVESTIGATE.md (INV-002). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: code reads candidates[0].usageMetadata at worker/src/llm/providers/gemini.ts:115 and 177 and declares it under candidates in worker/src/generation/types.ts:139. The Gemini API shape was not checked here (no network). Covered by LR-061..
