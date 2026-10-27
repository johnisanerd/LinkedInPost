# Frozen items (need a new capability; not in this release)

### FRZ-001 P3 frozen/scope - Sidebar grouping, breadcrumbs from location, sidebar search, command palette, RouteGuard, recently viewed
- **Source IDs:** C01-1, C01-2, C01-3, C01-4, C01-5, C01-6, C01-9, C01-10
- **Why frozen:** Needs a new capability beyond the feature freeze (ledger entry FZ-001).
- **In-scope alternative:** Keep the flat sidebar; fix only labels and the dead tour/pill claims.

### FRZ-002 P3 frozen/scope - Feed redesign: thumbnails, masonry, source dedupe grouping, per-source mute/boost, compose-from-card CTA, search-description toggle, tablet trending
- **Source IDs:** C02-3, C02-5, C02-8, C02-9, C02-11, C02-14, C02-15, C02-17, C02-18
- **Why frozen:** Needs a new capability beyond the feature freeze (ledger entry FZ-002).
- **In-scope alternative:** Ship the current text-only feed; make existing actions touch-visible (see the touch-gap item).

### FRZ-003 P3 frozen/scope - Passage clipping from the stream card, bulk clip select, clip groups, drag-into-editor context blocks
- **Source IDs:** C03-5, C03-7, C03-10, D3-4, D3-6
- **Why frozen:** Needs a new capability beyond the feature freeze (ledger entry FZ-003).
- **In-scope alternative:** Keep passage clipping in the article detail view only.

### FRZ-004 P3 frozen/scope - Article detail redesign: single scrollable stack, lightbox, read-full primary
- **Source IDs:** C03-8, C03-9
- **Why frozen:** Needs a new capability beyond the feature freeze (ledger entry FZ-004).
- **In-scope alternative:** Leave the tab layout as is.

### FRZ-005 P3 frozen/scope - Multi-channel deliveryChannels[] per post and multi-channel chips
- **Source IDs:** C05-10, C07-8
- **Why frozen:** Needs a new capability beyond the feature freeze (ledger entry FZ-005).
- **In-scope alternative:** Document single channel per post; show the channel on the queue row.

### FRZ-006 P3 frozen/scope - Test connection per credential and a connection-health page
- **Source IDs:** C09-6, C05-11, C09-15
- **Why frozen:** Needs a new capability beyond the feature freeze (ledger entry FZ-006).
- **In-scope alternative:** Show getIntegrations status and needs_reauth state on /connections.

### FRZ-007 P3 frozen/scope - Undo-send window
- **Source IDs:** C07-7
- **Why frozen:** Needs a new capability beyond the feature freeze (ledger entry FZ-007).
- **In-scope alternative:** Use the editor publish confirmation instead.

### FRZ-008 P3 frozen/scope - Editor layout redesign: 3 tab groups, 60/40 flip, versions drawer, 2-up compare, selection toggle
- **Source IDs:** C06-1, C06-8, C06-9, C06-10, C06-11
- **Why frozen:** Needs a new capability beyond the feature freeze (ledger entry FZ-008).
- **In-scope alternative:** Leave layout unchanged; add tooltips only.

### FRZ-009 P3 frozen/scope - Newsletter full-page editor, CodeMirror, voice chip, dedicated issue view, subject A/B and segmentation
- **Source IDs:** C08-5, C08-8, C08-9, C08-10, C08-12
- **Why frozen:** Needs a new capability beyond the feature freeze (ledger entry FZ-009).
- **In-scope alternative:** Keep the drawer; fix send safety only.

### FRZ-010 P3 frozen/scope - Variant-pick logging and post-publish rating signals
- **Source IDs:** C11-1, C11-3
- **Why frozen:** Needs a new capability beyond the feature freeze (ledger entry FZ-010).
- **In-scope alternative:** No signal capture this release.

### FRZ-011 P3 frozen/scope - Admin panel search, sort, batch, audit log, CSV
- **Source IDs:** C12-3
- **Why frozen:** Needs a new capability beyond the feature freeze (ledger entry FZ-011).
- **In-scope alternative:** Keep the plain list with error handling.

### FRZ-012 P3 frozen/scope - zod validation of API responses
- **Source IDs:** C13-6
- **Why frozen:** Needs a new capability beyond the feature freeze (ledger entry FZ-012).
- **In-scope alternative:** Hand-written guards on bootstrap and getRows only.

### FRZ-013 P3 frozen/scope - Enrichment DAG page and re-run for standard users, run filters and metrics
- **Source IDs:** C10-4, C10-5, C10-6
- **Why frozen:** Needs a new capability beyond the feature freeze (ledger entry FZ-013).
- **In-scope alternative:** Leave admin-only; show failed nodes in progress panel.

### FRZ-014 P2 frozen/scope - Real per-user Gmail auto-reply and LinkedIn DM automation infrastructure
- **Source IDs:** WKB-031
- **Why frozen:** Needs a new capability beyond the feature freeze (ledger entry FZ-014).
- **In-scope alternative:** Hide the Gmail/LinkedIn automation UI for this release.
