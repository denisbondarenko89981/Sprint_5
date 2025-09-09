# Автотесты Stellar Burgers

![Python](https://img.shields.io/badge/python-3.13-blue)
![Selenium](https://img.shields.io/badge/selenium-4.11.2-green)
![Pytest](https://img.shields.io/badge/pytest-8.4.1-orange)
![Build](https://img.shields.io/badge/build-passing-brightgreen)
![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)

Автоматизированные тесты для [Stellar Burgers](https://stellarburgers.nomoreparties.site/), написанные на **Python** с использованием **Selenium** и **pytest**.

---

## Структура проекта

```
.
├── locators/
│   └── stellar_locators.py        # Локаторы элементов страниц
├── tests/
│   ├── test_click_header.py       # Тесты хедера
│   ├── test_constructor.py        # Тесты конструктора
│   ├── test_enter_lc.py           # Тесты входа в ЛК
│   ├── test_login.py              # Тесты разных способов логина
│   ├── test_profile_navigation.py # Тест выхода из ЛК
│   └── test_registration.py       # Тесты регистрации
├── conftest.py                    # Фикстуры pytest
└── utils.py                       # Утилиты (BASE_URL, login)
```

---

## Установка

```bash
git clone <репозиторий>
cd <папка проекта>
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

> В `requirements.txt` должны быть: `selenium`, `pytest`.

---

## Запуск тестов

- Все тесты  
  ```bash
  pytest -v
  ```

- Конкретный файл  
  ```bash
  pytest -v tests/test_login.py
  ```

- С HTML-отчётом  
  ```bash
  pytest --html=report.html -v
  ```

- С покрытием кода  
  ```bash
  pytest --cov=./
  ```

---

## Локаторы

| Раздел              | Локаторы                                                                 |
|---------------------|--------------------------------------------------------------------------|
| **Хедер**           | `PERSONAL_ACCOUNT_BUTTON`, `CONSTRUCTOR_BUTTON`, `LOGO_BUTTON`           |
| **Конструктор**     | `BUNS_TAB`, `SAUCES_TAB`, `FILLINGS_TAB`                                 |
| **Регистрация / Вход** | `REGISTER_NAME`, `REGISTER_EMAIL`, `REGISTER_PASSWORD`, `REGISTER_SUBMIT`, `LOGIN_EMAIL`, `LOGIN_PASSWORD`, `LOGIN_SUBMIT`, `LOGIN_LINK`, `REGISTER_LINK`, `RESTORE_LINK`, `LINK_LOGIN` |
| **Личный кабинет**  | `LOGOUT_BUTTON`                                                          |

---

## Фикстуры

- **`driver`** — Chrome WebDriver  
- **`unique_user_data`** — генерация уникальных данных для регистрации  

---

## Примеры тестов

- Личный кабинет: вход через разные кнопки  
- Хедер: переходы по логотипу и кнопке «Конструктор»  
- Конструктор: переключение вкладок «Булки», «Соусы», «Начинки»  
- Регистрация: успешная регистрация и ошибка при коротком пароле  
- Личный кабинет: выход из аккаунта  

---

## Утилиты

Файл `utils.py` содержит `login(driver)` для авторизации:

```python
from locators.stellar_locators import StellarLocators as SL

TEST_EMAIL = "denis_bondarenko_28_123@yandex.ru"
TEST_PASSWORD = "denisbondarenko28"
BASE_URL = "https://stellarburgers.nomoreparties.site/"

def login(driver):
    driver.find_element(*SL.LOGIN_EMAIL).send_keys(TEST_EMAIL)
    driver.find_element(*SL.LOGIN_PASSWORD).send_keys(TEST_PASSWORD)
    driver.find_element(*SL.LOGIN_SUBMIT).click()
```

---

## Пример отчёта pytest

| Тест                                      | Статус |
|-------------------------------------------|--------|
| `test_login_via_personal_account`         | ✅ PASS |
| `test_success_registration`               | ✅ PASS |
| `test_registration_with_short_password`   | ❌ FAIL |

---

## Автор

Денис • QA Engineer
