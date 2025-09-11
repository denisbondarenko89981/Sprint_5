from selenium.webdriver.common.by import By

class StellarLocators:
    # кнопки хедера
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, '//p[text()="Личный Кабинет"]') # кнопка Личный кабинет
    CONSTRUCTOR_BUTTON = (By.XPATH, '//p[text()="Конструктор"]') # кнопка Конструктор
    LOGO_BUTTON = (By.XPATH, '//header//a[contains(@href, "/")]') # Логотип сайта

    # вкладки конструктора
    BUNS_TAB = (By.XPATH, '//span[text()="Булки"]/..') # булки
    SAUCES_TAB = (By.XPATH, '//span[text()="Соусы"]/..') # соусы
    FILLINGS_TAB = (By.XPATH, '//span[text()="Начинки"]/..') # начинки
    CONSTRUCTOR_TABS = (By.XPATH, "//div[contains(@class, 'tab_tab')]") # все вкладки конструктора

    # https://stellarburgers.nomoreparties.site/register (Страница регистрации)
    REGISTER_NAME = (By.XPATH, '//label[text()="Имя"]/following-sibling::input') # поле Имя для регистрации
    REGISTER_EMAIL = (By.XPATH, '//label[text()="Email"]/following-sibling::input') # поле Email для регистрации
    REGISTER_PASSWORD = (By.XPATH, '//input[@type="password"]') # поле Пароль для регистрации
    REGISTER_SUBMIT = (By.XPATH, '//button[text()="Зарегистрироваться"]') # кнопка Зарегестрироваться на странице регистрации
    LOGIN_LINK = (By.XPATH, '//a[text()="Войти"]') # линк Войти на странице регистрации
    REGISTER_ERROR = (By.XPATH, '//p[@class="input__error text_type_main-default"]') # текст Некорректный пароль на странице регистрации

    # https://stellarburgers.nomoreparties.site/login (Личный кабинет для ненавторизованного пользователя)
    LOGIN_EMAIL = (By.XPATH, '//label[text()="Email"]/following-sibling::input') # поле Email для входа в лк
    LOGIN_PASSWORD = (By.XPATH, '//input[@type="password"]') # поле Пароль для входа в лк
    LOGIN_SUBMIT = (By.XPATH, '//button[text()="Войти"]') # кнопка Войти для входа в лк
    REGISTER_LINK = (By.XPATH, '//a[text()="Зарегистрироваться"]') # кнопка Регистрация в лк
    RESTORE_LINK = (By.XPATH, '//a[text()="Восстановить пароль"]') # линк Восстановить пароль в лк

    # https://stellarburgers.nomoreparties.site/forgot-password (Страница восстановления пароля)
    LINK_LOGIN = (By.XPATH, '//a[text()="Войти"]') # кнопка Войти на странице восстановления пороля

    # главная страница 
    LOGIN_ACCOUNT = (By.XPATH, '//button[text()="Войти в аккаунт"]') # кнопка Войти в аккаунт на главной

    # https://stellarburgers.nomoreparties.site/account/profile (Личный кабинет авторизированного пользователя)
    LOGOUT_BUTTON = (By.XPATH, '//button[text()="Выход"]') # кнопка выхода из лк
