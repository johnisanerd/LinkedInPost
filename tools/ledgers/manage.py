#!/usr/bin/env python3
"""Generate development ledger indexes and validate their structural contract.

Requires PyYAML from requirements-ledgers.txt. No runtime ticket or Git mutations.
"""
from __future__ import annotations

import argparse
import importlib.util
import re
from datetime import date, datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
# Load the sibling by path so CLI execution and imported tools use one owner,
# without depending on an installed package named tools.
_JOURNEY_SPEC = importlib.util.spec_from_file_location('_ledger_journeys', Path(__file__).with_name('journeys.py'))
_JOURNEYS = importlib.util.module_from_spec(_JOURNEY_SPEC)
_JOURNEY_SPEC.loader.exec_module(_JOURNEYS)
STATES = {
    'backlog': {'open', 'in-progress', 'blocked', 'closed'},
    'features': {'proposed', 'planned', 'in-progress', 'implemented', 'verified', 'retired'},
    'decisions': {'accepted', 'superseded'},
    'ideas': {'captured', 'exploring', 'parked', 'promoted', 'rejected'},
    'research': {'planned', 'in-progress', 'complete', 'superseded'},
    'documents': {'current', 'review-needed', 'superseded', 'historical'},
    'reviews': {'draft', 'complete', 'superseded'},
    'journeys': _JOURNEYS.STATUSES,
}
SECTIONS = {
    'journeys': _JOURNEYS.SECTIONS,
    'backlog': ('Problem', 'Evidence and reproduction', 'Acceptance criteria', 'Plan', 'Attempts', 'Verification'),
    'features': ('Capability and journeys', 'Acceptance criteria', 'Delivery evidence'),
    'decisions': ('Decision', 'Rationale and alternatives', 'Consequences'),
    'ideas': ('Idea', 'Open questions', 'Promotion'),
    'research': ('Question', 'Sources and method', 'Findings', 'Limits', 'Recommendations and follow-up'),
    'documents': ('Authority and purpose', 'Maintenance', 'Known gaps'),
    'reviews': ('Scope and revision', 'Executive summary', 'Current state and capabilities', 'Changes since previous review', 'Conflicts and architectural issues', 'Direction and priorities', 'Follow-up work', 'Evidence and limitations'),
}


def read_records(root: Path) -> list[dict]:
    records = []
    for kind in STATES:
        for folder in ('items', 'archive'):
            for path in sorted((root / 'ledgers' / kind / folder).glob('*.md')):
                if path.name == 'README.md':
                    continue
                raw = path.read_text(encoding='utf-8')
                if not raw.startswith('---\n') or '\n---\n' not in raw[4:]:
                    raise ValueError(f'{path}: missing YAML front matter')
                front, body = raw[4:].split('\n---\n', 1)
                meta = yaml.safe_load(front)
                if not isinstance(meta, dict):
                    raise ValueError(f'{path}: metadata must be a mapping')
                records.append(dict(kind=kind, folder=folder, path=path, meta=meta, body=body))
    return records


def local_path(root: Path, value: str) -> Path:
    path = (root / value).resolve()
    if Path(value).is_absolute() or not path.is_relative_to(root.resolve()):
        raise ValueError(f'path must stay repository-relative: {value}')
    return path


def check_claim(meta: dict, body: str) -> list[str]:
    errors = []
    if meta['status'] not in {'in-progress', 'blocked'}:
        return errors
    for key in ('owner', 'branch', 'worktree', 'claimed_at'):
        if not isinstance(meta.get(key), str) or not meta[key].strip():
            errors.append(f'active claim requires {key}')
    if meta.get('branch') in {'HEAD', 'main', 'master'}:
        errors.append('claim must name a dedicated branch')
    if meta.get('claimed_at'):
        try:
            stamp = datetime.fromisoformat(str(meta['claimed_at']))
            if stamp.tzinfo is None:
                errors.append('claimed_at requires a timezone offset')
        except ValueError:
            errors.append('claimed_at requires an ISO timestamp')
    if meta['status'] == 'blocked' and not meta.get('blocked_reason'):
        errors.append('blocked item requires blocked_reason')
    if not re.search(r'(?m)^- \d{4}-\d{2}-\d{2}', body):
        errors.append('claim requires a dated Attempts entry')
    return errors


def check_metadata(record: dict) -> list[str]:
    meta, kind, body = record['meta'], record['kind'], record['body']
    errors = []
    for key in ('id', 'title', 'status', 'created', 'updated'):
        if not meta.get(key):
            errors.append(f'missing {key}')
    rid = str(meta.get('id', ''))
    if not re.fullmatch(r'\d{4}-\d{2}-\d{2}-[a-z0-9]+(?:-[a-z0-9]+)*', rid):
        errors.append('invalid date-slug id')
    if record['path'].stem != rid:
        errors.append('filename must match id')
    if meta.get('status') not in STATES[kind]:
        errors.append(f'invalid {kind} status')
    for key in ('created', 'updated'):
        try:
            date.fromisoformat(str(meta.get(key, '')))
        except ValueError:
            errors.append(f'{key} must be an ISO date')
    for section in SECTIONS[kind]:
        if not re.search(r'^## ' + re.escape(section) + r'\s*$', body, re.M):
            errors.append(f'missing section: {section}')
    if kind == 'backlog' and meta.get('status') in STATES[kind]:
        errors.extend(check_claim(meta, body))
        if (record['folder'] == 'archive') != (meta['status'] == 'closed'):
            errors.append('closed backlog belongs in archive; other states belong in items')
        if meta['status'] == 'closed' and not meta.get('resolution'):
            errors.append('closed backlog requires resolution')
        if meta['status'] == 'closed' and not section_text(body, 'Verification'):
            errors.append('closed backlog requires nonempty Verification')
    if kind == 'reviews':
        errors.extend(check_review(meta, body))
    if kind == 'research' and meta.get('status') == 'complete' and not meta.get('source_revision'):
        errors.append('complete research requires source_revision')
    if kind == 'decisions' and not meta.get('authority'):
        errors.append('decision requires authority')
    if kind == 'ideas' and meta.get('status') == 'promoted' and not meta.get('promoted_to'):
        errors.append('promoted idea requires promoted_to')
    return errors


def section_text(body: str, name: str) -> str:
    heading = f'## {name}\n'
    return body.split(heading, 1)[-1].split('\n## ', 1)[0].strip() if heading in body else ''


def check_references(record: dict, ids: set[str], root: Path) -> list[str]:
    meta, errors = record['meta'], []
    for key in ('related', 'supersedes', 'superseded_by', 'promoted_to'):
        values = meta.get(key, [])
        if not isinstance(values, list):
            errors.append(f'{key} must be a list')
        elif any(not isinstance(v, str) or v not in ids for v in values):
            errors.append(f'{key} contains unknown record IDs')
    paths = meta.get('docs')
    if not isinstance(paths, list):
        errors.append('docs must be a list of repository-relative paths')
        paths = []
    if record['kind'] == 'documents':
        if not meta.get('scope') or not meta.get('owner') or not meta.get('role'):
            errors.append('document requires scope, owner, and role')
        paths = [*paths, meta.get('path')]
    for value in paths:
        try:
            if not isinstance(value, str) or not local_path(root, value).is_file():
                errors.append(f'missing document: {value}')
        except ValueError as exc:
            errors.append(str(exc))
    return errors


def review_time(value: object) -> datetime:
    stamp = datetime.fromisoformat(str(value))
    if stamp.tzinfo is None:
        raise ValueError('reviewed_at requires a timezone offset')
    return stamp


def check_review(meta: dict, body: str) -> list[str]:
    errors = []
    if meta.get('scope_type') not in ('overall', 'section', 'feature'):
        errors.append('review scope_type must be overall, section, or feature')
    if not isinstance(meta.get('scope'), str) or not meta['scope'].strip():
        errors.append('review requires a nonempty scope')
    if meta.get('scope_type') == 'overall' and meta.get('scope') != 'application':
        errors.append('overall review scope must be application')
    if meta.get('reviewed_at'):
        try:
            review_time(meta['reviewed_at'])
        except (ValueError, TypeError):
            errors.append('reviewed_at requires an ISO timestamp with timezone')
    if meta.get('status') in ('complete', 'superseded'):
        for key in ('reviewer', 'source_revision', 'reviewed_at'):
            if not isinstance(meta.get(key), (str, datetime)) or not str(meta[key]).strip():
                errors.append(f'completed review requires {key}')
        for section in SECTIONS['reviews']:
            if not section_text(body, section):
                errors.append(f'completed review requires nonempty {section}')
    return errors


def check_review_links(record: dict, by_id: dict) -> list[str]:
    meta, errors = record['meta'], []
    if meta.get('scope_type') == 'feature':
        feature = by_id.get(str(meta.get('scope')))
        if not feature or feature['kind'] != 'features':
            errors.append('feature review scope must name an existing feature record ID')
    previous = meta.get('previous_review')
    if previous is None:
        return errors
    prior = by_id.get(str(previous))
    if not prior or prior['kind'] != 'reviews' or previous == meta.get('id'):
        return [*errors, 'previous_review must name another review record']
    old = prior['meta']
    if (old.get('scope_type'), old.get('scope')) != (meta.get('scope_type'), meta.get('scope')):
        errors.append('previous_review must have the same scope_type and scope')
    if old.get('status') not in ('complete', 'superseded'):
        errors.append('previous_review must refer to a completed or superseded review')
    try:
        if meta.get('reviewed_at') and review_time(old.get('reviewed_at')) >= review_time(meta['reviewed_at']):
            errors.append('previous_review must be older than this review')
    except (ValueError, TypeError):
        pass  # Timestamp errors are reported by check_review for each record.
    return errors


def render_reviews(records: list[dict]) -> str:
    reviews = [r for r in records if r['kind'] == 'reviews']
    latest = {}
    for record in reviews:
        meta = record['meta']
        if record['folder'] == 'items' and meta['status'] == 'complete':
            key = (meta['scope_type'], meta['scope'])
            previous = latest.get(key)
            if previous is None or (review_time(meta['reviewed_at']), meta['id']) > (review_time(previous['meta']['reviewed_at']), previous['meta']['id']):
                latest[key] = record
    lines = ['# Reviews ledger', '', '<!-- Generated by tools/ledgers/manage.py index; edit records, not rows. -->', '',
             'See [protocol](../PROTOCOL.md), [template](TEMPLATE.md), and [all ledgers](../README.md).', '',
             'Latest means the newest completed review of that exact scope, at its named revision.',
             'A section/feature review does not refresh the overall application review.', '']
    for scope_type in ('overall', 'section', 'feature'):
        selected = [r for key, r in sorted(latest.items()) if key[0] == scope_type]
        lines += [f'## Latest {scope_type} reviews', '']
        lines += review_table(selected) if selected else [f'No completed {scope_type} review yet.', '']
    lines += ['## Draft reviews', '']
    lines += review_table([r for r in reviews if r['meta']['status'] == 'draft'])
    lines += ['## Review history', '']
    history = sorted(reviews, key=lambda r: (review_time(r['meta']['reviewed_at']) if r['meta'].get('reviewed_at')
                                           else datetime.min.replace(tzinfo=timezone.utc), r['meta']['id']), reverse=True)
    lines += review_table(history)
    return '\n'.join(lines)


def review_table(records: list[dict]) -> list[str]:
    lines = ['| Scope | Review | Status | Reviewed at | Source revision |', '| --- | --- | --- | --- | --- |']
    for record in records:
        meta = record['meta']
        title = index_cell(meta['title']).replace('[', '\\[').replace(']', '\\]')
        link = f"[{title}]({record['folder']}/{record['path'].name})"
        scope = f"{meta['scope_type']}: {meta['scope']}"
        lines.append('| ' + ' | '.join([index_cell(scope), link, index_cell(meta['status']),
                                        index_cell(meta.get('reviewed_at')), index_cell(meta.get('source_revision'))]) + ' |')
    return [*lines, '']


def index_cell(value: object) -> str:
    return str(value or '—').replace('|', '\\|').replace('\n', ' ')


def render_index(kind: str, records: list[dict]) -> str:
    if kind == 'journeys':
        return _JOURNEYS.render_board(records, index_cell)
    if kind == 'reviews':
        return render_reviews(records)
    lines = [f'# {kind.title()} ledger', '', '<!-- Generated by tools/ledgers/manage.py index; edit records, not rows. -->', '',
             'See [protocol](../PROTOCOL.md), [template](TEMPLATE.md), and [all ledgers](../README.md).', '']
    for folder, label in (('items', 'Active records'), ('archive', 'Archived records')):
        lines += [f'## {label}', '', '| Record | Status | Owner | Branch | Updated |', '| --- | --- | --- | --- | --- |']
        for record in sorted(records, key=lambda r: str(r['meta']['id'])):
            if record['kind'] != kind or record['folder'] != folder:
                continue
            meta = record['meta']
            title = index_cell(meta['title']).replace('[', '\\[').replace(']', '\\]')
            link = f"[{title}]({folder}/{record['path'].name})"
            lines.append('| ' + ' | '.join([link] + [index_cell(meta.get(k)) for k in ('status', 'owner', 'branch', 'updated')]) + ' |')
        lines.append('')
    return '\n'.join(lines)


def validate(records: list[dict], root: Path) -> list[str]:
    errors, ids, scopes, paths = [], set(), set(), set()
    for record in records:
        rid = str(record['meta'].get('id', ''))
        if rid in ids:
            errors.append(f'duplicate record ID: {rid}')
        ids.add(rid)
    by_id = {str(r['meta'].get('id')): r for r in records}
    work_links = _JOURNEYS.work_links(records)
    for record in records:
        failures = check_metadata(record) + check_references(record, ids, root)
        failures.extend(_JOURNEYS.check_record_links(record, by_id))
        if record['kind'] == 'journeys':
            failures.extend(_JOURNEYS.check_journey(record, by_id, root, local_path, work_links))
        if record['kind'] == 'reviews':
            failures.extend(check_review_links(record, by_id))
        if record['kind'] == 'documents' and record['meta'].get('status') in {'current', 'review-needed'}:
            for key, seen in (('scope', scopes), ('path', paths)):
                value = record['meta'].get(key)
                if value in seen:
                    failures.append(f'duplicate active document {key}: {value}')
                seen.add(value)
        errors.extend(f"{record['path'].relative_to(root)}: {message}" for message in failures)
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('index', 'check'))
    args = parser.parse_args()
    try:
        records = read_records(ROOT)
        errors = validate(records, ROOT)
        if errors:
            raise ValueError('\n'.join(errors))
        for kind in STATES:
            path = ROOT / 'ledgers' / kind / 'README.md'
            expected = render_index(kind, records)
            if args.action == 'index':
                path.write_text(expected, encoding='utf-8')
            elif not path.exists() or path.read_text(encoding='utf-8') != expected:
                errors.append(f'stale index: {path.relative_to(ROOT)}; run index')
        if errors:
            raise ValueError('\n'.join(errors))
    except (ValueError, OSError, yaml.YAMLError) as exc:
        print(exc)
        return 1
    print(f'{args.action}: {len(records)} records across {len(STATES)} ledgers passed.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
