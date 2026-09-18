---
id: architecture-email-gateway
type: architecture
status: deprecated
dependencies: [product-notifications]
last_updated: 2026-09-10
deprecated_date: 2026-09-10
original_path: .dds/architecture/email-gateway/email-gateway.dds.md
description: SMTP relay service and third-party email provider contract for the Notifications epic.
---

> ⚠️ DEPRECATED: This database schema / infrastructure was retired on 2026-09-10. Reason: constraint C3 of `product-constraints` (no third-party email provider under a signed data processing agreement); the in-app late list of `product-vision` replaces the digest.

# ARCHITECTURE: Email Gateway

## [0] CONTEXT_AND_ALIGNMENT
The email gateway relayed digest emails for the Notifications epic (`product-notifications`) through a third-party provider.

## [1] TECH_STACK_AND_INFRASTRUCTURE
- **SMTP relay container:** 1 replica - Queued outbound mail.
- **Third-party email API:** Provider contract never signed (C3).

## [2] DATA_MODELS_AND_SCHEMAS
<schema>
### [Email_Gateway] outbound_mail
- `id` (UUIDv4) - PRIMARY KEY.
- `recipient` (VARCHAR(254)) - NOT NULL - Personal data; the reason C3 applied.
- `sent_at` (TIMESTAMPTZ) - NULL until delivery.
</schema>

## [3] GLOBAL_BOUNDARIES_AND_API_CONTRACTS
- Only the Notifications module wrote to `outbound_mail`.

## Changelog
- [2026-09-10]: Retired in the Notifications cascade (`impact product-notifications --down`).
