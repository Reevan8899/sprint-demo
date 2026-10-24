"""Регистрация и вход: первоначальный учебный вариант хеширования."""
import hashlib
import hmac
import re

_users: dict[str, str] = {}


def _normalize_email(email: str) -> str:
    if not isinstance(email, str):
        raise ValueError("Некорректный email")
    email = email.strip().lower()
    if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email):
        raise ValueError("Некорректный email")
    return email


def _hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


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
    return hmac.compare_digest(_users[email], _hash_password(password))


def reset_users() -> None:
    """Очистить память между демонстрациями и тестами."""
    _users.clear()
