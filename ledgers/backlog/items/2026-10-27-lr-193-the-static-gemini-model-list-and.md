---
id: 2026-10-27-lr-193-the-static-gemini-model-list-and
title: The static Gemini model list and defaults are likely stale
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j121-pick-provider-and-model-per-purpose
- 2026-10-27-j122-llm-provider-failure-and-fallback
related: []
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
raw_id: LR-193
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

The static Gemini model list and defaults are likely stale. Suspected, not confirmed (see Confidence in the evidence).

## Evidence and reproduction

- **Confidence:** hypothesis
- **Journeys:** J-121, J-122
- **Aliases:** WKB-045
- **Evidence:** worker/src/llm/providers/gemini.ts:4-9; worker/src/llm/google-model-policy.ts:1
- **Repro:** static; check the live list vs the static list.
- **Fix hint:** Update defaults to a current model and surface discovery failure.

## Acceptance criteria

- The question in the title is answered in Attempts with file:line evidence and a clear yes/no.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Update defaults to a current model and surface discovery failure.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-193). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: hypothesis from static reading of worker/src/llm/providers/gemini.ts:4-9; confirm by running the Repro and observing the described behaviour.
