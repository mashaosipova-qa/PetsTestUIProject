from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.test_data import URLS


class LoginPage(BasePage):
    def __init__(self, browser, timeout=10):
        super().__init__(browser, URLS['login_page'], timeout)
        self.wait = WebDriverWait(self.browser, timeout)

    def enter_login(self, login_text):
        login_email = self.wait.until(EC.presence_of_element_located(LoginPageLocators.LOGIN_EMAIL))
        login_email.clear()
        login_email.send_keys(login_text)

    def enter_password(self, password_text):
        input_password = self.wait.until(EC.presence_of_element_located(LoginPageLocators.LOGIN_PASS))
        input_password.clear()
        input_password.send_keys(password_text)

    def submit_login(self):
        login_button = self.wait.until(EC.element_to_be_clickable(LoginPageLocators.LOGIN_BTN))
        login_button.submit()

    def login(self, email, password):
        self.open()
        self.enter_login(email)
        self.enter_password(password)
        self.submit_login()