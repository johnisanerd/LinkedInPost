"""Journey contracts, reverse work links, and grouped journey board rendering."""
from __future__ import annotations

from datetime import datetime

STATUSES = frozenset({'planned', 'partial', 'verified', 'failing', 'blocked', 'retired'})
SECTIONS = ('Purpose and scope', 'Actor, trigger and prerequisites', 'Steps and information flow',
            'Modules and code map', 'Success and acceptance', 'Failure, edge cases and recovery',
            'Verification evidence', 'Gaps and linked work', 'Next actions')


def work_links(records: list[dict]) -> dict[str, list[dict]]:
    """Build reverse links once: records' journeys fields are the link authority."""
    links: dict[str, list[dict]] = {}
    for record in records:
        values = record['meta'].get('journeys', [])
        if isinstance(values, list):
            for value in dict.fromkeys(v for v in values if isinstance(v, str)):
                links.setdefault(value, []).append(record)
    return links


def check_record_links(record: dict, by_id: dict) -> list[str]:
    values = record['meta'].get('journeys', [])
    if not isinstance(values, list):
        return ['journeys must be a list of journey record IDs']
    errors = []
    for value in values:
        target = by_id.get(str(value))
        if not isinstance(value, str) or not target or target['kind'] != 'journeys':
            errors.append(f'journeys contains an unknown or non-journey ID: {value}')
    for value in record['meta'].get('related', []) if isinstance(record['meta'].get('related', []), list) else []:
        target = by_id.get(str(value))
        if target and target['kind'] == 'journeys' and value not in values:
            errors.append('journey work references must use journeys, not only related')
    if record['kind'] == 'journeys' and values:
        errors.append('journey relationships use related; journeys links belong to work/evidence records')
    return errors


def unresolved_tickets(linked: list[dict]) -> list[dict]:
    return [r for r in linked if r['kind'] == 'backlog' and r['meta']['status'] != 'closed']


def check_journey(record: dict, by_id: dict, root, resolve_path, links: dict) -> list[str]:
    meta, errors = record['meta'], []
    if meta.get('journey_type') not in ('user', 'workflow', 'information-flow'):
        errors.append('journey_type must be user, workflow, or information-flow')
    if meta.get('scope_type') not in ('overall', 'section', 'feature'):
        errors.append('journey scope_type must be overall, section, or feature')
    for field in ('scope', 'actor', 'trigger', 'verification_owner'):
        if not isinstance(meta.get(field), str) or not meta[field].strip():
            errors.append(f'journey requires {field}')
    if meta.get('scope_type') == 'overall' and meta.get('scope') != 'application':
        errors.append('overall journey scope must be application')
    if meta.get('scope_type') == 'feature':
        feature = by_id.get(str(meta.get('scope')))
        if not feature or feature['kind'] != 'features':
            errors.append('feature journey scope must name a feature record ID')
    for field in ('modules', 'code_paths'):
        values = meta.get(field)
        if not isinstance(values, list) or any(not isinstance(v, str) or not v.strip() for v in values):
            errors.append(f'{field} must be a list of nonempty strings')
    for path in meta.get('code_paths', []) if isinstance(meta.get('code_paths'), list) else []:
        try:
            if isinstance(path, str) and not resolve_path(root, path).exists():
                errors.append(f'journey code path does not exist: {path}')
        except ValueError as exc:
            errors.append(str(exc))
    if meta.get('checked_at'):
        try:
            if datetime.fromisoformat(str(meta['checked_at'])).tzinfo is None:
                raise ValueError('timezone missing')
        except (ValueError, TypeError):
            errors.append('checked_at requires an ISO timestamp with timezone')
    for value in meta.get('related', []) if isinstance(meta.get('related', []), list) else []:
        work = by_id.get(str(value))
        if work and work['kind'] == 'backlog' and meta['id'] not in work['meta'].get('journeys', []):
            errors.append('backlog references require the ticket journeys link')
    if meta.get('status') == 'verified':
        errors.extend(check_verified(record, links))
    return errors


def check_verified(record: dict, links: dict) -> list[str]:
    meta, errors = record['meta'], []
    for field in ('source_revision', 'checked_at'):
        if not meta.get(field):
            errors.append(f'verified journey requires {field}')
    for field in ('modules', 'code_paths'):
        if not meta.get(field):
            errors.append(f'verified journey requires nonempty {field}')
    for section in SECTIONS:
        marker = f'## {section}\n'
        text = record['body'].split(marker, 1)[-1].split('\n## ', 1)[0].strip() if marker in record['body'] else ''
        if not text:
            errors.append(f'verified journey requires nonempty {section}')
    pending = unresolved_tickets(links.get(meta['id'], []))
    if pending:
        errors.append('verified journey has unresolved linked backlog: ' + ', '.join(r['meta']['id'] for r in pending))
    return errors


def record_link(record: dict, cell, *, own: bool = False) -> str:
    meta = record['meta']
    title = cell(meta['title']).replace('[', '\\[').replace(']', '\\]')
    prefix = '' if own else f"../{record['kind']}/"
    return f"[{title}]({prefix}{record['folder']}/{record['path'].name})"


def render_board(records: list[dict], cell) -> str:
    journeys = sorted((r for r in records if r['kind'] == 'journeys'), key=lambda r: r['meta']['id'])
    links = work_links(records)
    lines = ['# Journeys ledger', '', '<!-- Generated by tools/ledgers/manage.py index; edit records, not rows. -->', '',
             'See [protocol](../PROTOCOL.md), [template](TEMPLATE.md), and [all ledgers](../README.md).', '',
             'Work links come from each record\'s journeys field. Status is a claim at the named checked revision;',
             'closed tickets alone do not prove the complete journey works.', '']
    for scope_type in ('overall', 'section', 'feature'):
        lines += [f'## {scope_type.title()} journeys', '']
        active = [r for r in journeys if r['folder'] == 'items' and r['meta']['scope_type'] == scope_type]
        scopes = sorted({r['meta']['scope'] for r in active})
        if not scopes:
            lines += [f'No {scope_type} journeys recorded yet.', '']
        for scope in scopes:
            lines += [f'### {cell(scope)}', '']
            lines += journey_table([r for r in active if r['meta']['scope'] == scope], links, cell)
    lines += ['## Linked work and evidence', '']
    for journey in journeys:
        lines += [f"### {cell(journey['meta']['id'])}", '',
                  '| Linked record | Kind | Status |', '| --- | --- | --- |']
        for work in links.get(journey['meta']['id'], []):
            lines.append('| ' + ' | '.join([record_link(work, cell), cell(work['kind']), cell(work['meta']['status'])]) + ' |')
        lines.append('')
    lines += ['## Archived journeys', '']
    lines += journey_table([r for r in journeys if r['folder'] == 'archive'], links, cell)
    return '\n'.join(lines)


def journey_table(journeys: list[dict], links: dict, cell) -> list[str]:
    lines = ['| Journey | Type | State | Open tickets | Checked at | Source revision |',
             '| --- | --- | --- | --- | --- | --- |']
    for journey in journeys:
        meta = journey['meta']
        count = len(unresolved_tickets(links.get(meta['id'], [])))
        lines.append('| ' + ' | '.join([record_link(journey, cell, own=True), cell(meta['journey_type']),
                     cell(meta['status']), str(count), cell(meta.get('checked_at')), cell(meta.get('source_revision'))]) + ' |')
    return [*lines, '']
