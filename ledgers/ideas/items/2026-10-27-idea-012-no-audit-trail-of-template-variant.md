---
id: 2026-10-27-idea-012-no-audit-trail-of-template-variant
title: No audit trail of template, variant and image per published post
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related: []
docs: []
status: captured
promoted_to: []
raw_id: IDEA-012
source_file: docs/launch-readiness/findings/LEGACY-TRACKERS.md
---

## Idea

No audit trail of template, variant and image per published post. Captured from the legacy tracker; not a commitment. - **Source:** launch-release/ledgers-legacy/ideas.md (Stage 8: keep an audit trail)
- **Detail:** ideas.md asks for an audit trail of which template, variant and image were used. A grep for audit trail / auditLog in worker/src found nothing.
- **Action:** Decide if the owner wants this at launch; if yes record post type and variant index at publish.

## Open questions

What would justify promoting this: a real user need, an owner decision, or a failing journey. read-only: grep for 'audit trail', 'auditLog', 'audit_log' in worker/src returned no files.

## Promotion

No promotion yet. If promoted, link the new backlog item here and set promoted_to.
