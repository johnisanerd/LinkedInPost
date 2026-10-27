---
id: 2026-10-27-inv-016-are-the-static-gemini-model-ids
title: Are the static Gemini model ids retired? (WKB-045)
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related:
- 2026-10-27-lr-193-the-static-gemini-model-list-and
docs:
- worker/src/llm/providers/gemini.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: investigation
severity: P3
area: worker/llm
raw_id: INV-016
source_file: docs/launch-readiness/findings/INVESTIGATE.md
---

## Problem

Are the static Gemini model ids retired? (WKB-045). Users would see 404 errors when live model discovery fails.

## Evidence and reproduction

- **Question:** The fallback catalog and GOOGLE_MODEL_DEFAULT use gemini-2.0-flash, 1.5-flash and 1.5-pro. Are they still served?
- **Why it matters:** Users would see 404 errors when live model discovery fails.
- **How to settle it:** Compare worker/src/llm/providers/gemini.ts:4-9 and worker/src/llm/google-model-policy.ts:1 against the current Gemini models list endpoint with a test key.
- **Related items:** LR-193
- **Owner:**

## Acceptance criteria

- The question in the title is answered in Attempts with file:line evidence and a clear yes/no.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/INVESTIGATE.md (INV-016). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: depends on current Google model availability, not checkable offline. Covered by LR-193..
