---
id: 2026-10-27-inv-022-is-the-veo-generatevideo-url-a
title: Is the Veo :generateVideo URL a real Gemini endpoint, or does every Veo video request fail?
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j068-ai-image-generation-text-and-reference
related: []
docs:
- worker/src/image-gen/providers/veo.ts
- generation-worker/src/image-gen/providers/veo.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: investigation
severity: P3
area: worker/image-gen
raw_id: INV-022
source_file: docs/launch-readiness/findings/SWEEP.md
---

## Problem

Is the Veo :generateVideo URL a real Gemini endpoint, or does every Veo video request fail?. If the path is invalid, video generation always returns 404 after the user selects it, in two copies of the provider. Suspected, not confirmed (see Confidence in the evidence).

## Evidence and reproduction

- **Source:** launch-release/findings/raw/worker-b.md WKB-027 (worker-b.md:270, "Veo uses a :generateVideo path that is not a documented Gemini endpoint (hypothesis, low impact)")
- **Journeys:** J-068
- **Confidence:** hypothesis
- **Evidence:** worker/src/image-gen/providers/veo.ts:11 and generation-worker/src/image-gen/providers/veo.ts:11
- **Why it matters:** If the path is invalid, video generation always returns 404 after the user selects it, in two copies of the provider.
- **Repro or check:** Compare the path with the current Gemini API Veo docs (the documented call is a long-running predict on the model), or run one request with a real key and read the HTTP status; also grep the UI for a path that offers video (`grep -rn veo frontend/src worker/src`).
- **Fix hint:** decide: fix the path in both copies, or remove Veo from the model catalog if video is out of scope for launch.

## Acceptance criteria

- The question in the title is answered in Attempts with file:line evidence and a clear yes/no.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

decide: fix the path in both copies, or remove Veo from the model catalog if video is out of scope for launch.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/SWEEP.md (INV-022). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: worker/src/image-gen/providers/veo.ts:11.
