---
id: 2026-10-27-lr-052-loadstoredconfig-omits-imagegen-enrichmentskills-and-youtube
title: loadStoredConfig omits imageGen, enrichmentSkills and YouTube fields, so saved settings are ignored then wiped and YouTube never shows connected.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j068-ai-image-generation-text-and-reference
- 2026-10-27-j081-youtube-as-a-publish-target
- 2026-10-27-j097-connect-youtube
- 2026-10-27-j113-enrichment-page-and-node-catalog-admin
- 2026-10-27-j120-admin-settings-default-channel-allowed-models
related: []
docs:
- worker/src/index.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P1
area: worker/config
raw_id: LR-052
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

loadStoredConfig omits imageGen, enrichmentSkills and YouTube fields, so saved settings are ignored then wiped and YouTube never shows connected.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-068, J-081, J-097, J-113, J-120
- **Aliases:** WKA-008
- **Evidence:** worker/src/index.ts:3138-3177 vs 4659-4715; worker/src/index.ts:3213-3214
- **Repro:** static. Executor: save an image provider in Settings, reload; connect YouTube, reload `bootstrap` and inspect `config.hasYouTubeAccessToken`.
- **Fix hint:** Add the missing fields to loadStoredConfig and saveConfig and move the imageGen block ahead of the early return in toPublicConfig.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Add the missing fields to loadStoredConfig and saveConfig and move the imageGen block ahead of the early return in toPublicConfig.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-052). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of worker/src/index.ts:3138-3177 vs 4659-4715.
