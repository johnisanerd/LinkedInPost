---
id: YYYY-MM-DD-short-slug
title: State of the application or named area
status: draft
created: YYYY-MM-DD
updated: YYYY-MM-DD
scope_type: overall
scope: application
reviewer: null
reviewed_at: null
source_revision: null
previous_review: null
journeys: []
related: []
docs: []
---

## Scope and revision

Use overall/application, section/<stable-area-name>, or feature/<feature-record-id>.
Name the exact reviewed commit, inspected areas, and explicit exclusions. A scoped
review must not imply a whole-application audit.

## Executive summary

What works, the most important conflict/risk, and the recommended direction.

## Current state and capabilities

Separate implemented and verified, partial, missing, and unknown behavior. For an
overall review, use subsections for major areas and link their latest scoped reviews.

## Changes since previous review

Link the prior review of this same scope and explain what changed. For the first
review, say there is no previous review; do not invent a historical baseline.

## Conflicts and architectural issues

Prioritize concrete design/code/document conflicts, boundary bypasses, coupling,
resource/performance problems, and integration risks. State impact and evidence;
link actionable issues to the backlog. Say when no issue was established.

## Direction and priorities

Recommend the next few outcomes and why they matter. Distinguish recommendations
from accepted decisions; link decision records rather than silently changing design.

## Follow-up work

Link existing/new backlog, feature, research, and decision IDs using related too.
The backlog owns claims and task status; this review does not duplicate that board.

## Evidence and limitations

Sources and revisions, commands/check results, uncertainty and what was not tested.
Complete means the review is finished, not that the application is production-ready.
