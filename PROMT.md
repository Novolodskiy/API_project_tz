**📌 Промт для Codex (создание проекта автотестов API на Python + Pytest + Requests + Allure):**

Создай проект автотестирования API на Python с использованием:

* `pytest` для тестирования,
* `requests` для отправки HTTP-запросов,
* `allure-pytest` для генерации отчётов,
* архитектуры **Endpoint Object**.

🔧 Проект должен соответствовать следующим требованиям:

---

### 🔹 1. Структура проекта:

```
api_tests/
│
├── endpoints/
│   ├── __init__.py
│   ├── base_endpoint.py         # базовый класс для всех эндпоинтов
│   ├── get_users.py             # /api/test/users
│   └── get_user_by_id.py        # /api/test/user/{id}
│
├── tests/
│   ├── __init__.py
│   ├── test_get_users.py        # тесты для TC01–TC09
│   └── test_get_user_by_id.py   # тесты для TC010–TC015
│
├── conftest.py                  # фикстуры: инициализация классов, предусловия
├── requirements.txt             # зависимости
├── pytest.ini                   # настройки pytest и Allure
└── README.md
```

---

### 🔹 2. Эндпоинты и классы

* Для каждого эндпоинта создать отдельный класс в `endpoints/`.
* Каждый класс должен содержать:

  * Метод `send_request(...)` — вызов запроса.
  * Методы-проверки (`check_status_code`, `check_schema`, `check_error_message` и т.д.).
  * Ассерты и проверки должны быть частью методов классов.
* Общие проверки типа Content-Type, формат ошибки, пустые поля — выносить в `base_endpoint.py`.

---

### 🔹 3. Тесты

* Каждый TC должен быть отдельной функцией в `tests/`.
* Каждый тест вызывает соответствующий метод класса эндпоинта и использует Allure-steps.
* Название и содержание тестов соответствуют следующей логике:

  * TC01: `gender=male`
  * TC02: `gender=magic`
  * TC03: `gender=McCloud`
  * TC04: `gender=female`
  * TC05: `gender=robot`
  * TC06: без параметра gender
  * TC07: gender=""
  * TC08: gender=MALE
  * TC09: POST вместо GET
  * TC010: существующий id
  * TC011: POST вместо GET по id
  * TC012: несуществующий id
  * TC013: id как строка
  * TC014: id=0
  * TC015: id=-1

---

### 🔹 4. Фикстуры (`conftest.py`)

* Фикстура `get_existing_ids()` — получает список всех id (по 4 корректным gender).
* Фикстура `get_non_existing_id()` — возвращает id, которого нет в списке.
* Фикстура `get_endpoint_class()` — инициализирует классы эндпоинтов.
* Все фикстуры имеют scope "session" или "function" по необходимости.

---

### 🔹 5. Allure

* Использовать `@allure.title`, `@allure.step`, `@allure.description`.
* Все шаги проверок (assert'ов) оформлять как `@allure.step`.

---

### 🔹 6. Обработка ошибок

* Никаких `assert` в теле теста — только вызовы методов класса.
* В случае исключений/ошибок возвращать понятное описание и поднимать кастомные исключения, если нужно.
* Проверки: HTTP status, структура тела, типы данных, формат `Content-Type`, код и текст ошибок.

---

### 🔹 7. Пример requirements.txt:

```
pytest
requests
allure-pytest
```

---

### 🔹 8. Пример вызова эндпоинта в тесте

```python
@allure.title("TC01 — Корректный запрос с gender=male")
def test_tc01_get_users_male(get_endpoint_class):
    endpoint = get_endpoint_class("get_users")
    response = endpoint.send_request(gender="male")
    endpoint.check_status_code(response, 200)
    endpoint.check_content_type(response)
    endpoint.check_success_true(response)
    endpoint.check_idlist_is_array(response)
```

---

Сгенерируй весь проект в соответствии с этими требованиями. Учитывай всю архитектуру и порядок исполнения. Не упускай ни одной проверки, описанной выше.
