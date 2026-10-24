"""Управляемая демонстрация: ошибочный тест обязан заблокировать PR."""


def test_ci_failure_demonstration():
    assert False, "Intentional failure for additional assignment B"
