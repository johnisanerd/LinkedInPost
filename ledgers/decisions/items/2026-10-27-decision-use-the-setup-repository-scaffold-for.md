---
id: 2026-10-27-decision-use-the-setup-repository-scaffold-for
title: Use the setup repository scaffold for this project's ledgers
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related: []
docs: []
status: accepted
authority: 'Owner instruction in chat on 2026-10-27: the ledger structure is set in the setup repository; copy it here and move the other ledgers in.'
supersedes: []
superseded_by: []
---

## Decision

The project's development records use the ledgers/ scaffold from the setup repository (~/setup, origin P1927/setup), installed with tools/install.py. Record formats, statuses, and checks follow ledgers/PROTOCOL.md.

## Rationale and alternatives

Chosen by the owner. The alternative was a template or workflow that the owner did not name.

## Consequences

The earlier launch-release folder layout was replaced. Its evidence files moved to docs/launch-readiness/.
