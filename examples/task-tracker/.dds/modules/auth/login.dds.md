---
id: modules-auth-login
type: module
status: active
dependencies: [architecture-core-database, product-constraints]
sources: [src/auth/**]
last_updated: 2026-09-18
description: Credential verification, lockout, and JWT issuance for LoginHandler.
---

# AUTH: Login

## [0] CONTEXT_AND_PURPOSE
The `LoginHandler` is responsible for verifying an email and password against `users.password_hash` and issuing the JWT that every other module requires, under constraint C1 of `product-constraints`.

## [1] TECHNICAL_CONSTRAINTS
<constraints>
- `LoginHandler` MUST verify passwords with Argon2id through `hashing.verify`; no other comparison path exists (C1).
- `LoginHandler` MUST lock an account for 15 minutes after 10 failed attempts and MUST answer a locked account with HTTP 423.
- `LoginHandler` MUST issue a JWT valid for 12 hours whose subject is `users.id`; the JWT never carries the email address.
</constraints>

## [2] LOGIC_FLOW
1. `LoginHandler` loads the user by email; a missing user takes the same code path and time as a wrong password.
2. `LoginHandler` calls `hashing.verify` and increments the failure counter on mismatch.
3. `LoginHandler` issues the JWT and resets the failure counter on success.

## Changelog
- [2026-09-18]: Promoted from draft after security review.
