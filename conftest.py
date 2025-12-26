# запуск браузера и логин
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from pages.pet_new_page import PetNewPage
from pages.main_page import MainPage
from data.test_data import LOGIN_DATA, URLS, PET_DATA

#открывает и закрывает браузер для каждого теста
@pytest.fixture(scope="function")
def browser():
    # отключение pop_up о сохранении/смены пароля
    options = Options()
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.default_content_setting_values.notifications": 2,
    }
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--disable-features=PasswordLeakDetection")
    options.add_argument("--password-store=basic")

    # Важные флаги для менеджера паролей
    options.add_argument("--disable-save-password-bubble")
    options.add_argument("--disable-features=AutofillServerCommunication,PasswordManagerOnboarding")
    options.add_argument("--password-store=basic")

    driver = webdriver.Chrome(options=options)
    # разворачивает окно браузера на весь экран, чтобы все элементы страницы были видны о время теста
    driver.maximize_window()
    yield driver
    driver.quit()

#Залогиненный пользователь
@pytest.fixture(scope="function")
def logged_user(browser):
    page = LoginPage(browser)
    page.login(LOGIN_DATA['valid_email'], LOGIN_DATA['valid_password'])

    return browser


@pytest.fixture(scope="function")
def profile_page(logged_user):
    """Страница профиля для уже авторизованного пользователя."""
    page = ProfilePage(logged_user)   # logged_user == браузер после логина
    page.open()                       # открываем URL профиля
    return page


@pytest.fixture(scope="function")
def created_pet(logged_user, browser):
    """Создаёт нового уникального питомца на основе PET_DATA['pet3']"""

    # открыть форму создания
    browser.get(URLS['profile_page'])
    profile_page = ProfilePage(browser)
    profile_page.click_add_button()

    # уникальные данные на основе pet3
    pet = PET_DATA['pet3']
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")  # 20251223_064756
    pet_name = f"{pet['name']}_{timestamp}"

    pet_new_page = PetNewPage(browser)
    pet_new_page.fill_pet_name(pet_name)
    pet_new_page.fill_pet_age(pet['age'])
    pet_new_page.select_pet_type(pet['type'])
    pet_new_page.save_pet()

    return {
        "name": pet_name,  # Карамелька_20251223_064756
        "age": pet['age'],
        "type": pet['type'],
    }
@pytest.fixture(scope="function")
def main_page(logged_user):
    # открыть main_page
    logged_user.get(URLS['main_page'])
    return MainPage(logged_user, URLS['main_page'])

