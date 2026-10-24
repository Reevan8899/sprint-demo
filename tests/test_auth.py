import pytest

from src.auth import login, register, reset_users


@pytest.fixture(autouse=True)
def clean_users():
    reset_users()
    yield
    reset_users()


def test_registration_and_login():
    assert register("user@example.com", "securepass123") is True
    assert login("user@example.com", "securepass123") is True


@pytest.mark.parametrize("email", ["", "invalid", "a@b", "a b@example.com", None])
def test_reject_invalid_email(email):
    with pytest.raises(ValueError, match="email"):
        register(email, "securepass123")


@pytest.mark.parametrize("password", ["short", "", None])
def test_reject_short_password(password):
    with pytest.raises(ValueError, match="минимум 8"):
        register("user@example.com", password)


def test_duplicate_ignores_email_case_and_surrounding_spaces():
    register(" User@Example.com ", "securepass123")
    with pytest.raises(ValueError, match="уже существует"):
        register("user@example.com", "otherpass123")
    assert login("USER@EXAMPLE.COM", "securepass123")


@pytest.mark.parametrize("email,password", [
    ("unknown@example.com", "securepass123"),
    ("user@example.com", "wrongpass"),
    ("user@example.com", None), (None, "securepass123")])
def test_wrong_credentials(email, password):
    register("user@example.com", "securepass123")
    assert login(email, password) is False


def test_reset_removes_user():
    register("user@example.com", "securepass123")
    reset_users()
    assert not login("user@example.com", "securepass123")
