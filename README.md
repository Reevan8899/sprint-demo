# Sprint Demo: MVP интернет-магазина

[![PR checks](https://github.com/Reevan8899/sprint-demo/actions/workflows/pr-check.yml/badge.svg)](https://github.com/Reevan8899/sprint-demo/actions/workflows/pr-check.yml)

Практическая работа №4 по программной инженерии.
Индивидуальная имитация Scrum-спринта с GitHub.

## Возможности

### Аутентификация

Регистрация и вход по email; проверка пароля и защита от дубликатов.

### Каталог

Три товара с ценами и поиск по идентификатору.

### Корзина, заказ и история

Добавление товаров, расчёт суммы, заказ с адресом доставки, поиск и фильтрация истории. Снимки каталога, корзины и заказов не позволяют изменить внутреннее состояние извне.

## Запуск

Нужен Python 3.12 или новее. Данные хранятся в памяти процесса.

```console
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
python -m src.demo
python -m pytest --cov=src --cov-report=term-missing
python -m ruff check .
```

В Linux/macOS активация окружения: `source .venv/bin/activate`.
Все цены заданы в целых рублях, количество - положительное целое число.
Это учебная библиотека с консольной демонстрацией; данные после выхода не сохраняются.

## Работа с ветками

`main` - релиз; `sprint-1` - интеграция; `feature/*` - отдельные задачи.
Изменения принимаются через PR. Критерии готовности: [цель спринта](docs/sprint-1-goal.md).
Самопроверка индивидуального автора не считается независимым ревью.

## Лицензия

MIT, см. [LICENSE](LICENSE).
