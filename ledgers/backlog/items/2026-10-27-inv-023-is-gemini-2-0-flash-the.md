---
id: 2026-10-27-inv-023-is-gemini-2-0-flash-the
title: Is gemini-2.0-flash, the model the wizard uses to validate the Gemini key, still served for new keys?
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j001-web-setup-wizard-end-to-end
- 2026-10-27-j004-generation-worker-deploy-requires-an-llm
related:
- 2026-10-27-lr-130-the-wizard-api-key-step-requires
- 2026-10-27-lr-193-the-static-gemini-model-list-and
docs:
- setup.md
- setup/wizard/steps/apikeys.py
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: investigation
severity: P3
area: setup/wizard
raw_id: INV-023
source_file: docs/launch-readiness/findings/SWEEP.md
---

## Problem

Is gemini-2.0-flash, the model the wizard uses to validate the Gemini key, still served for new keys?. Any non-200 blocks the whole wizard (LR-130); a retired model name would block every new user with a valid key. Suspected, not confirmed (see Confidence in the evidence).

## Evidence and reproduction

- **Source:** launch-release/findings/raw/setup.md SET-026 (setup.md:263, "Model name validity is a hypothesis")
- **Journeys:** J-001, J-004
- **Confidence:** hypothesis
- **Evidence:** setup/wizard/steps/apikeys.py:51
- **Why it matters:** Any non-200 blocks the whole wizard (LR-130); a retired model name would block every new user with a valid key.
- **Repro or check:** `curl -s -o /dev/null -w '%{http_code}' -H 'x-goog-api-key: $KEY' -H 'content-type: application/json' -d '{"contents":[{"parts":[{"text":"hi"}]}]}' https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent` with a fresh key; also run ListModels and look for the id. Related: LR-193.
- **Fix hint:** decide: switch validation to the ListModels call (no model name), or update the id to a current model.

## Acceptance criteria

- The question in the title is answered in Attempts with file:line evidence and a clear yes/no.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

decide: switch validation to the ListModels call (no model name), or update the id to a current model.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/SWEEP.md (INV-023). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: setup/wizard/steps/apikeys.py:51.
