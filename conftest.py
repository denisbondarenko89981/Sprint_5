import pytest
import uuid
import random
import string
from selenium import webdriver

@pytest.fixture
def driver():
    """Фикстура для инициализации и закрытия браузера"""
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1400,900")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture
def unique_user_data():
    """Фикстура для генерации уникальных данных пользователя"""
    name = f"User_{uuid.uuid4().hex[:6]}"
    email = f"{uuid.uuid4().hex[:6]}@example.com"
    chars = string.ascii_letters + string.digits
    password = ''.join(random.choices(chars, k=8))
    return {"name": name, "email": email, "password": password}
