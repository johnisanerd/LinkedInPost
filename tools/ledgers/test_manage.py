"""Behavior checks for ledger claims, identity, references, and derived indexes."""
from __future__ import annotations

import contextlib
import io
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import yaml

from tools.ledgers import manage


class LedgerChecks(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for kind in manage.STATES:
            for folder in ('items', 'archive'):
                (self.root / 'ledgers' / kind / folder).mkdir(parents=True)

    def record(self, **overrides) -> dict:
        meta = dict(id='2026-10-26-example-gap', title='Example gap', status='open',
                    created='2026-10-26', updated='2026-10-26', related=[], docs=[])
        meta.update(overrides)
        body = '\n\n'.join(f'## {name}\n\nContent.' for name in manage.SECTIONS['backlog'])
        return dict(kind='backlog', folder='items',
                    path=self.root / 'ledgers/backlog/items/2026-10-26-example-gap.md',
                    meta=meta, body=body)

    def test_claim_requires_agent_branch_worktree_and_timestamp(self) -> None:
        record = self.record(status='in-progress')
        errors = '\n'.join(manage.validate([record], self.root))
        for field in ('owner', 'branch', 'worktree', 'claimed_at'):
            self.assertIn(f'claim requires {field}', errors)

    def test_complete_claim_is_valid_and_naive_time_is_rejected(self) -> None:
        record = self.record(status='in-progress', owner='agent/session', branch='codex/example',
                             worktree='/tmp/example-worktree', claimed_at='2026-10-26T05:00:00+05:30')
        record['body'] = record['body'].replace('## Attempts\n\nContent.',
                                               '## Attempts\n\n- 2026-10-26 — Claimed by agent/session.')
        self.assertEqual(manage.validate([record], self.root), [])
        record['meta']['claimed_at'] = '2026-10-26T05:00:00'
        self.assertIn('timezone offset', '\n'.join(manage.validate([record], self.root)))

    def test_unknown_relationship_and_missing_document_are_rejected(self) -> None:
        record = self.record(related=['2026-10-26-missing'], docs=['missing.md'])
        errors = '\n'.join(manage.validate([record], self.root))
        self.assertIn('unknown record IDs', errors)
        self.assertIn('missing document', errors)

    def test_document_cannot_escape_repository(self) -> None:
        record = self.record(docs=['../outside.md'])
        self.assertIn('repository-relative', '\n'.join(manage.validate([record], self.root)))

    def test_duplicate_record_identity_is_rejected(self) -> None:
        record = self.record()
        self.assertIn('duplicate record ID', '\n'.join(manage.validate([record, record], self.root)))

    def test_duplicate_canonical_scope_is_rejected(self) -> None:
        (self.root / 'design.md').write_text('# Design\n')
        first = self.record()
        first.update(kind='documents', body='\n'.join(f'## {s}\nText.' for s in manage.SECTIONS['documents']))
        first['meta'].update(status='current', scope='example', path='design.md', owner='maintainer', role='design')
        second = dict(first, path=first['path'].with_name('2026-10-26-another-doc.md'),
                      meta=dict(first['meta'], id='2026-10-26-another-doc'))
        self.assertIn('duplicate active document scope', '\n'.join(manage.validate([first, second], self.root)))

    def test_closure_requires_archive_resolution_and_evidence(self) -> None:
        record = self.record(status='closed')
        record['body'] = record['body'].replace('## Verification\n\nContent.', '## Verification\n')
        errors = '\n'.join(manage.validate([record], self.root))
        self.assertIn('closed backlog belongs in archive', errors)
        self.assertIn('requires resolution', errors)
        self.assertIn('nonempty Verification', errors)

    def test_blocked_claim_requires_reason(self) -> None:
        record = self.record(status='blocked')
        self.assertIn('blocked_reason', '\n'.join(manage.validate([record], self.root)))

    def test_indexes_are_regenerated_and_staleness_fails_check(self) -> None:
        record = self.record()
        record['path'].write_text('---\n' + yaml.safe_dump(record['meta']) + '---\n' + record['body'])
        with patch.object(manage, 'ROOT', self.root), contextlib.redirect_stdout(io.StringIO()):
            with patch('sys.argv', ['manage.py', 'index']):
                self.assertEqual(manage.main(), 0)
            with patch('sys.argv', ['manage.py', 'check']):
                self.assertEqual(manage.main(), 0)
            index = self.root / 'ledgers/backlog/README.md'
            index.write_text(index.read_text() + '\nManual stale row.\n')
            with patch('sys.argv', ['manage.py', 'check']):
                self.assertEqual(manage.main(), 1)


    def review(self, slug='review-one', **overrides) -> dict:
        meta = dict(id=f'2026-10-26-{slug}', title=slug, status='complete',
                    created='2026-10-26', updated='2026-10-26', related=[], docs=[],
                    scope_type='overall', scope='application', reviewer='reviewer/session',
                    reviewed_at='2026-10-26T07:30:00+05:30', source_revision='abc123', previous_review=None)
        meta.update(overrides)
        body = '\n\n'.join(f'## {name}\n\nEvidence for this section.' for name in manage.SECTIONS['reviews'])
        return dict(kind='reviews', folder='items', meta=meta, body=body,
                    path=self.root / f"ledgers/reviews/items/{meta['id']}.md")

    def test_completed_review_requires_evidence_and_reviewer_revision_time(self) -> None:
        record = self.review(reviewer=None, reviewed_at=None, source_revision=None)
        record['body'] = record['body'].replace('## Evidence and limitations\n\nEvidence for this section.',
                                               '## Evidence and limitations\n')
        errors = '\n'.join(manage.validate([record], self.root))
        for field in ('reviewer', 'source_revision', 'reviewed_at'):
            self.assertIn(f'completed review requires {field}', errors)
        self.assertIn('nonempty Evidence and limitations', errors)

    def test_review_timestamp_needs_timezone(self) -> None:
        record = self.review(reviewed_at='2026-10-26T07:30:00')
        self.assertIn('timestamp with timezone', '\n'.join(manage.validate([record], self.root)))

    def test_review_latest_uses_timestamp_per_scope_and_ignores_drafts(self) -> None:
        old = self.review('z-older', reviewed_at='2026-10-26T08:00:00+05:30')
        new = self.review('a-newer', reviewed_at='2026-10-26T03:00:00+00:00')
        draft = self.review('draft-newest', status='draft', reviewed_at='2026-10-26T12:00:00+00:00')
        section = self.review('section-state', scope_type='section', scope='runtime')
        retired = self.review('superseded-newest', status='superseded', reviewed_at='2026-10-27T12:00:00+00:00')
        records = [old, new, draft, section, retired]
        self.assertEqual(manage.validate(records, self.root), [])
        board = manage.render_index('reviews', records)
        overall = board.split('## Latest overall reviews')[1].split('## Latest section reviews')[0]
        self.assertIn('a-newer', overall)
        for hidden in ('z-older', 'draft-newest', 'section-state', 'superseded-newest'):
            self.assertNotIn(hidden, overall)
        self.assertIn('section-state', board.split('## Latest section reviews')[1].split('## Latest feature reviews')[0])
        self.assertIn('z-older', board.split('## Review history')[1])

    def test_review_cannot_reference_another_scope_as_previous(self) -> None:
        prior = self.review('prior', scope_type='section', scope='runtime')
        current = self.review(previous_review=prior['meta']['id'])
        self.assertIn('same scope_type and scope', '\n'.join(manage.validate([prior, current], self.root)))

    def test_review_previous_must_exist_and_be_older(self) -> None:
        current = self.review(previous_review='2026-10-26-absent')
        self.assertIn('another review record', '\n'.join(manage.validate([current], self.root)))
        prior = self.review('future', reviewed_at='2026-10-27T03:00:00+00:00')
        current['meta']['previous_review'] = prior['meta']['id']
        self.assertIn('must be older', '\n'.join(manage.validate([prior, current], self.root)))

    def test_feature_review_resolves_feature_record(self) -> None:
        feature = self.record()
        feature.update(kind='features', body='\n'.join(f'## {s}\nEvidence.' for s in manage.SECTIONS['features']))
        feature['meta']['status'] = 'planned'
        record = self.review(scope_type='feature', scope=feature['meta']['id'])
        self.assertEqual(manage.validate([feature, record], self.root), [])
        self.assertIn('existing feature record ID', '\n'.join(manage.validate([record], self.root)))

    def test_no_completed_overall_review_is_not_filled_from_section(self) -> None:
        section = self.review(scope_type='section', scope='runtime')
        board = manage.render_index('reviews', [section])
        self.assertIn('No completed overall review yet.', board)
        archived = self.review('old-overall')
        archived['folder'] = 'archive'
        board = manage.render_index('reviews', [section, archived])
        self.assertIn('No completed overall review yet.', board)
        self.assertIn('old-overall', board.split('## Review history')[1])


    def journey(self, slug='journey-one', **overrides) -> dict:
        meta = dict(id=f'2026-10-26-{slug}', title=slug, status='partial',
                    created='2026-10-26', updated='2026-10-26', related=[], docs=[],
                    journey_type='workflow', scope_type='section', scope='runtime',
                    actor='operator', trigger='runtime mismatch', verification_owner='supervisor',
                    source_revision='abc123', checked_at='2026-10-26T08:00:00+05:30',
                    modules=['runtime'], code_paths=['src'])
        meta.update(overrides)
        (self.root / 'src').mkdir(exist_ok=True)
        body = '\n\n'.join(f'## {name}\n\nEvidence and explicit limits.' for name in manage.SECTIONS['journeys'])
        return dict(kind='journeys', folder='items', meta=meta, body=body,
                    path=self.root / f"ledgers/journeys/items/{meta['id']}.md")

    def test_journey_links_are_typed_and_must_resolve(self) -> None:
        task = self.record(journeys=['2026-10-26-unknown'])
        self.assertIn('unknown or non-journey', '\n'.join(manage.validate([task], self.root)))
        task['meta']['journeys'] = 'not-a-list'
        self.assertIn('must be a list', '\n'.join(manage.validate([task], self.root)))
        task['meta']['journeys'] = [task['meta']['id']]
        self.assertIn('unknown or non-journey', '\n'.join(manage.validate([task], self.root)))

    def test_verified_journey_requires_all_linked_backlog_closed(self) -> None:
        journey = self.journey(status='verified')
        task = self.record(journeys=[journey['meta']['id']])
        for state in ('open', 'in-progress', 'blocked'):
            task['meta']['status'] = state
            self.assertIn('unresolved linked backlog', '\n'.join(manage.validate([task, journey], self.root)))
        task['meta'].update(status='closed', resolution='fixed')
        task['folder'] = 'archive'
        self.assertEqual(manage.validate([task, journey], self.root), [])
        task['meta']['status'] = 'open'
        task['folder'] = 'items'
        self.assertIn('unresolved linked backlog', '\n'.join(manage.validate([task, journey], self.root)))

    def test_closed_work_does_not_replace_journey_verification_evidence(self) -> None:
        journey = self.journey(status='verified', checked_at=None, source_revision=None)
        journey['body'] = journey['body'].replace('## Verification evidence\n\nEvidence and explicit limits.', '## Verification evidence\n')
        errors = '\n'.join(manage.validate([journey], self.root))
        self.assertIn('verified journey requires source_revision', errors)
        self.assertIn('verified journey requires checked_at', errors)
        self.assertIn('nonempty Verification evidence', errors)

    def test_journey_code_paths_allow_directories_but_not_escapes_or_missing_paths(self) -> None:
        journey = self.journey()
        self.assertEqual(manage.validate([journey], self.root), [])
        journey['meta']['code_paths'] = ['missing.py', '../outside']
        errors = '\n'.join(manage.validate([journey], self.root))
        self.assertIn('code path does not exist', errors)
        self.assertIn('repository-relative', errors)

    def test_journey_board_groups_scope_and_derives_linked_ticket_state(self) -> None:
        journey = self.journey()
        overall = self.journey('overall-flow', scope_type='overall', scope='application')
        task = self.record(journeys=[journey['meta']['id']])
        board = manage.render_index('journeys', [overall, journey, task])
        self.assertIn('## Overall journeys', board)
        self.assertIn('### runtime', board)
        self.assertIn('Open tickets', board)
        self.assertIn('Example gap', board)
        self.assertIn('| partial | 1 |', board)
        task['meta']['status'] = 'closed'
        board = manage.render_index('journeys', [journey, task])
        self.assertIn('| partial | 0 |', board)

    def test_feature_journey_requires_a_real_feature_record(self) -> None:
        journey = self.journey(scope_type='feature', scope='2026-10-26-absent')
        self.assertIn('feature record ID', '\n'.join(manage.validate([journey], self.root)))

    def test_journey_checked_time_needs_timezone(self) -> None:
        journey = self.journey(checked_at='2026-10-26T08:00:00')
        self.assertIn('checked_at requires an ISO timestamp with timezone', '\n'.join(manage.validate([journey], self.root)))

    def test_related_cannot_bypass_typed_journey_ticket_linkage(self) -> None:
        journey = self.journey(status='verified')
        task = self.record(related=[journey['meta']['id']])
        self.assertIn('must use journeys', '\n'.join(manage.validate([journey, task], self.root)))
        task['meta']['related'] = []
        journey['meta']['related'] = [task['meta']['id']]
        self.assertIn('ticket journeys link', '\n'.join(manage.validate([journey, task], self.root)))

    def test_all_linked_tickets_must_close_not_just_the_first(self) -> None:
        journey = self.journey(status='verified')
        first = self.record(status='closed', resolution='fixed', journeys=[journey['meta']['id']])
        first['folder'] = 'archive'
        second = self.record(id='2026-10-26-second-gap', journeys=[journey['meta']['id']])
        second['path'] = second['path'].with_name('2026-10-26-second-gap.md')
        errors = '\n'.join(manage.validate([journey, first, second], self.root))
        self.assertIn('unresolved linked backlog: 2026-10-26-second-gap', errors)


if __name__ == '__main__':
    unittest.main()
