# Development ledgers

The canonical entry point for repository development knowledge and work.
Read [the protocol](PROTOCOL.md) before filing or working an item.

| Ledger | Records | Index |
| --- | --- | --- |
| Backlog | Actionable bugs, gaps, investigations, refactors, documentation work | [Backlog](backlog/README.md) |
| Features | Intended capabilities, user journeys, acceptance checks, delivery evidence | [Features](features/README.md) |
| Decisions | Settled choices, authority, rationale, supersession | [Decisions](decisions/README.md) |
| Ideas | Uncommitted possibilities, parked directions, promotion links | [Ideas](ideas/README.md) |
| Research | Questions, sources, methods, findings, uncertainty, recommendations | [Research](research/README.md) |
| Journeys | User/workflow/information-flow contracts, code maps, acceptance and linked work | [Journeys](journeys/README.md) |
| Reviews | Dated application/section/feature state, architectural conflicts, and direction | [Reviews](reviews/README.md) |
| Documents | Authority and ownership of design/reference documents | [Documents](documents/README.md) |

Each ledger has a `TEMPLATE.md`, `items/`, `archive/`, and generated README.
Item files are authoritative; indexes are projections. Do not edit index rows.

```bash
python3 tools/ledgers/manage.py index  # regenerate indexes
python3 tools/ledgers/manage.py check  # metadata, relationships, paths, indexes
python3 -m unittest discover -s tools/ledgers -p 'test_*.py'
```

These are development records for this repository. Product runtime ticket state,
signals, and target-project I/O ledgers keep their existing owners and lifecycle.
Link their task IDs/evidence where useful; this folder is not another runtime
scheduler and does not automatically control agents or update documents.

## Starting a project

All eight ledgers start empty. Copy the matching template when there is an actual
idea, research question, feature, decision, gap, or document to register. Do not
invent decisions or mark capabilities implemented merely to fill the structure.
Register each authoritative design document in the document ledger and link its
related work and evidence. See [BOOTSTRAP.md](../BOOTSTRAP.md).
