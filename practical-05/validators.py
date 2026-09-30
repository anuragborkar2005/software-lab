import re

EMAIL_PATTERN = re.compile(
    r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}$"
)

def is_valid_email(email: str) -> bool:
    """Return True if 'email' looks like a valid email address."""
    if not isinstance(email, str):
        return False
    if len(email) > 254 or ".." in email:
        return False
    return bool(EMAIL_PATTERN.match(email))
