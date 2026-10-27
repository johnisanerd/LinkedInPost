---
id: 2026-10-27-wrap-007-import-scripts-preserved-in-repo
title: Import scripts were only in scratch; now preserved in docs/launch-readiness/importers with checksums
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related: []
docs: []
status: closed
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: process
raw_id: WRAP-007
source_file: wrap-up (this session)
resolution: fixed
---

## Problem

The three scripts that generated the ledger records lived in the session scratch folder, so they would be lost when the session ends.

## Evidence and reproduction

`ls docs/launch-readiness/importers` and `cat docs/launch-readiness/importers/SHA256SUMS`.

## Acceptance criteria

- The scripts are in the repository with checksums.

## Plan

Preserve as evidence only; they are not run again (see WRAP-002).

## Attempts

- 2026-10-27 — Copied gen_ledgers.py, gen_video_backlog.py, wrap_ledger.py into docs/launch-readiness/importers with SHA256SUMS. Copied the current on-disk state; gen_ledgers.py had changed on disk during the session and its diff was not reviewed.

## Verification

Checksums written with shasum -a 256 on the copies in the commit.

