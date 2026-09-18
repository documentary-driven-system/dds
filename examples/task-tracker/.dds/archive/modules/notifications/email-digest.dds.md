---
id: modules-notifications-email-digest
type: module
status: deprecated
dependencies: [architecture-email-gateway, product-notifications]
sources: [src/notifications/**]
last_updated: 2026-09-10
deprecated_date: 2026-09-10
original_path: .dds/modules/notifications/email-digest.dds.md
description: The daily digest job that built and queued one late-task email per Team Lead.
---

> ⚠️ DEPRECATED: This module was removed from the system on 2026-09-10. Reason: constraint C3 of `product-constraints` (no third-party email provider under a signed data processing agreement); the in-app late list of `product-vision` replaces the digest.

# NOTIFICATIONS: Email Digest

## [0] CONTEXT_AND_PURPOSE
The `DigestJob` was responsible for building one late-task email per Team Lead at 08:00 and queueing the email through the email gateway (`architecture-email-gateway`).

## [1] TECHNICAL_CONSTRAINTS
<constraints>
- `DigestJob` MUST run once per workday per Team Lead and skip Team Leads with no late tasks.
</constraints>

## [2] LOGIC_FLOW
1. `DigestJob` queried late tasks grouped by Team Lead.
2. `DigestJob` rendered the digest and inserted one `outbound_mail` row per Team Lead.

## Changelog
- [2026-09-10]: Removed in the Notifications cascade; `src/notifications/` deleted in the same commit.
