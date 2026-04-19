![DDS Banner](docs/dds-banner.png)

# DDS

## Documentary Driven System

DDS (Documentary Driven System) is an enterprise documentation methodology that transforms documentation from a passive reference into a governing system layer across the software lifecycle. In this model, documentation is not only descriptive; it is the primary mechanism for decision-making, change control, and implementation consistency.

## Executive Summary

DDS provides a shared truth framework for projects where human teams and AI agents collaborate. It manages business rules, architectural boundaries, and module-level implementation decisions through a clear hierarchy.

The core proposition of this model is:
- Documentation guides code.
- Conflicts across layers are resolved through a strict priority order.
- Changes are not considered release-ready until they are atomically documented and traceable.

## What Is DDS?

DDS is a documentation operating model that organizes project knowledge into three core tiers:
- Product: Business goals, personas, KPIs, and requirements.
- Architecture: Data models, infrastructure, global APIs, and technical boundaries.
- Modules: Feature-level implementation rules and behaviors.

These tiers operate like a state machine with routing protocols under `.dds/meta`. Teams or agents first identify intent, then route to the correct domain, and execute according to the relevant write/update/deprecate protocols.

## What Does DDS Enable?

- Establishes a Single Source of Truth (SSoT) at enterprise scale.
- Reduces misalignment across business, architecture, and module layers.
- Delivers machine-perceivable, chunkable, and consistent knowledge structures for AI agents.
- Provides traceability, locking, log rotation, and dependency analysis for change management.
- Prevents knowledge loss during feature retirement through the Tombstone protocol.

## Core Principles

- SSoT: The `.dds/` content is the primary reference for system behavior.
- Truth Hierarchy: Product > Architecture > Modules priority is enforced.
- Threshold-Based Sync: Commit/deploy should not proceed before corresponding documentation is updated.
- Cascade Effect: Changes at upper tiers are propagated to lower tiers through impact analysis.

## Documentation Links

### Core Guides (`docs/`)

- DDS framework overview: [docs/dds-main.md](docs/dds-main.md)
- Product tier: [docs/dds-product.md](docs/dds-product.md)
- Architecture tier: [docs/dds-architecture.md](docs/dds-architecture.md)
- Modules tier: [docs/dds-modules.md](docs/dds-modules.md)
- AI system routing: [docs/llms.txt](docs/llms.txt)

### Meta Routing and Rules (`.dds/meta/`)

- Master manifesto: [.dds/meta/manifesto.dds.md](.dds/meta/manifesto.dds.md)

Product domain:
- [.dds/meta/dds.product/rules.dds.md](.dds/meta/dds.product/rules.dds.md)
- [.dds/meta/dds.product/write.dds.md](.dds/meta/dds.product/write.dds.md)
- [.dds/meta/dds.product/update.dds.md](.dds/meta/dds.product/update.dds.md)
- [.dds/meta/dds.product/deprecate.dds.md](.dds/meta/dds.product/deprecate.dds.md)

Architecture domain:
- [.dds/meta/dds.architecture/rules.dds.md](.dds/meta/dds.architecture/rules.dds.md)
- [.dds/meta/dds.architecture/write.dds.md](.dds/meta/dds.architecture/write.dds.md)
- [.dds/meta/dds.architecture/update.dds.md](.dds/meta/dds.architecture/update.dds.md)
- [.dds/meta/dds.architecture/deprecate.dds.md](.dds/meta/dds.architecture/deprecate.dds.md)

Modules domain:
- [.dds/meta/dds.modules/rules.dds.md](.dds/meta/dds.modules/rules.dds.md)
- [.dds/meta/dds.modules/write.dds.md](.dds/meta/dds.modules/write.dds.md)
- [.dds/meta/dds.modules/update.dds.md](.dds/meta/dds.modules/update.dds.md)
- [.dds/meta/dds.modules/deprecate.dds.md](.dds/meta/dds.modules/deprecate.dds.md)

## Operating Approach

1. Define the business need or change intent.
2. Route to the correct domain through the master manifesto.
3. Apply the write/update/deprecate protocol based on action type.
4. Validate cross-tier consistency through impact analysis.
5. Keep documentation and code synchronized as a single delivery unit.

## Conclusion

DDS does more than improve documentation quality. It systematically strengthens decision quality, change safety, and governance for AI-assisted software delivery in enterprise environments.
