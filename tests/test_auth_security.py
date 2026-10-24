"""Регрессионные тесты дефекта хеширования из учебного примера."""
import pytest

from src import auth


@pytest.fixture(autouse=True)
def clean_users():
    auth.reset_users()
    yield
    auth.reset_users()


def test_equal_passwords_have_different_salted_hashes():
    auth.register("one@example.com", "same-password")
    auth.register("two@example.com", "same-password")
    assert auth._users["one@example.com"] != auth._users["two@example.com"]
    assert auth.login("one@example.com", "same-password")
    assert not auth.login("one@example.com", "wrong-password")


@pytest.mark.parametrize("stored", ["broken", "x$600000$ab$cd",
    "pbkdf2_sha256$1$ab$cd", "pbkdf2_sha256$600000$nothex$00"])
def test_malformed_stored_hash_does_not_authenticate(stored):
    auth.register("user@example.com", "same-password")
    auth._users["user@example.com"] = stored
    assert auth.login("user@example.com", "same-password") is False



def test_short_salt_is_rejected():
    auth.register("user@example.com", "same-password")
    auth._users["user@example.com"] = "pbkdf2_sha256$600000$ab$cd"
    assert auth.login("user@example.com", "same-password") is False
