"""LoginHandler — governed by modules-auth-login."""
from datetime import timedelta
from . import hashing

LOCK_AFTER = 10
LOCK_FOR = timedelta(minutes=15)
TOKEN_TTL = timedelta(hours=12)


class LoginHandler:
    def __init__(self, users, tokens, clock):
        self.users, self.tokens, self.clock = users, tokens, clock

    def login(self, email: str, password: str) -> str:
        user = self.users.by_email(email)
        if user is not None and user.locked_until and user.locked_until > self.clock.now():
            raise Locked()                                      # HTTP 423
        ok = user is not None and hashing.verify(user.password_hash, password)
        if not ok:
            if user is not None:
                self.users.record_failure(user.id, LOCK_AFTER, LOCK_FOR)
            raise Unauthorized()                                # same path and timing for unknown user
        self.users.reset_failures(user.id)
        return self.tokens.issue(subject=user.id, ttl=TOKEN_TTL)  # subject is users.id, never the email


class Locked(Exception):
    pass


class Unauthorized(Exception):
    pass
