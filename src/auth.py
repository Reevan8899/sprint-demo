"""Регистрация и вход с PBKDF2-HMAC-SHA256 и случайной солью."""
import hashlib
import hmac
import re
import secrets

_users: dict[str, str] = {}


def _normalize_email(email: str) -> str:
    if not isinstance(email, str):
        raise ValueError("Некорректный email")
    email = email.strip().lower()
    if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email):
        raise ValueError("Некорректный email")
    return email


def _hash_password(password: str, salt: bytes | None = None) -> str:
    salt = secrets.token_bytes(16) if salt is None else salt
    digest = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 600000).hex()
    return f"pbkdf2_sha256$600000${salt.hex()}${digest}"


def _verify_password(password: str, stored: str) -> bool:
    try:
        algorithm, rounds, salt_hex, _digest = stored.split("$")
        if algorithm != "pbkdf2_sha256" or rounds != "600000":
            return False
        salt = bytes.fromhex(salt_hex)
        if len(salt) != 16:
            return False
    except ValueError:
        return False
    return hmac.compare_digest(stored, _hash_password(password, salt))


def register(email: str, password: str) -> bool:
    """Зарегистрировать email; дубликат и неверные данные вызывают ValueError."""
    email = _normalize_email(email)
    if not isinstance(password, str) or len(password) < 8:
        raise ValueError("Пароль должен содержать минимум 8 символов")
    if email in _users:
        raise ValueError("Пользователь с таким email уже существует")
    _users[email] = _hash_password(password)
    return True


def login(email: str, password: str) -> bool:
    """Проверить учётные данные; неверные данные возвращают False."""
    try:
        email = _normalize_email(email)
    except ValueError:
        return False
    if not isinstance(password, str) or email not in _users:
        return False
    return _verify_password(password, _users[email])


def reset_users() -> None:
    """Очистить память между демонстрациями и тестами."""
    _users.clear()
