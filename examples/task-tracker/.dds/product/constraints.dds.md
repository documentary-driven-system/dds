---
id: product-constraints
type: product
status: active
dependencies: []
last_updated: 2026-09-18
description: Non-negotiable security, legal, and compliance constraints; no KPI or tier overrides them.
---

# PRODUCT: Non-Negotiable Constraints

## [0] BUSINESS_VISION_AND_VALUE
The constraints in this document protect TaskTracker users and the company regardless of any KPI. No tier, KPI, or business goal overrides an entry; a conflict stops the work and goes to a human (manifesto [1].0).

## [1] CONSTRAINTS
<constraints>
- **C1 Credential protection (security):** The system MUST store user passwords only as salted hashes produced by a purpose-built password hashing function. Source: company security policy SEC-04.
- **C2 Personal data erasure (legal):** The system MUST erase or anonymise a user's personal data within 30 days of an erasure request. Source: GDPR Article 17.
- **C3 Third-party processors (legal):** The system MUST NOT send personal data to a third-party service without a signed data processing agreement. Source: GDPR Article 28.
- **C4 Deletion audit (compliance):** The system MUST keep an audit record of every task deletion for 12 months. Source: internal audit standard AUD-2.
</constraints>

## [2] KEY_PERFORMANCE_INDICATORS (KPIs)
None. Constraints are rules, not targets (manifesto [1].2).

## Changelog
- [2026-09-18]: Promoted from draft after legal review.
- [2026-09-10]: C3 invoked to retire the Notifications epic; see the Tombstones in the product, architecture, and modules trees.
