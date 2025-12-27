import pytest
from data.test_data import LOGIN_DATA

@pytest.mark.skip
def test_go_to_login_page(login_page): # открытие страницы, login_page - функция-фикстура
    login_page.browser.save_screenshot('result2.png')

@pytest.mark.skip
def test_input_login(login_page):   # ввод логина
    login_page.enter_login(LOGIN_DATA["valid_email"]) # Метод из LoginPage

@pytest.mark.skip
def test_input_password(login_page):
    login_page.enter_password(LOGIN_DATA["valid_password"])  # Метод из LoginPage

@pytest.mark.skip
def test_submit_button(login_page):
    login_page.submit_login()  # Метод из LoginPage

@pytest.mark.skip
def test_login(login_page):
    login_page.enter_login(LOGIN_DATA["valid_email"])
    login_page.enter_password(LOGIN_DATA["valid_password"])
    login_page.submit_login()
    login_page.browser.save_screenshot('result3.png')





