"""Password hashing — governed by modules-auth-login (constraint C1 of product-constraints). Illustrative code, never run."""


def hash_password(password: str) -> str:
    """Argon2id via the argon2-cffi PasswordHasher; the only hashing path in the codebase."""
    from argon2 import PasswordHasher
    return PasswordHasher().hash(password)


def verify(password_hash: str, password: str) -> bool:
    from argon2 import PasswordHasher
    from argon2.exceptions import VerifyMismatchError
    try:
        return PasswordHasher().verify(password_hash, password)
    except VerifyMismatchError:
        return False
