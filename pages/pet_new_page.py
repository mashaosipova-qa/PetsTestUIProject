from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.locators import PetNewPageLocators
from data.test_data import URLS


class PetNewPage(BasePage):
    def __init__(self, browser, timeout=10):
        super().__init__(browser, URLS["pet_new_page"], timeout)
        self.locators = PetNewPageLocators()
        self.wait = WebDriverWait(self.browser, timeout)

    def fill_pet_name(self, name):
        name_input = self.wait.until(EC.presence_of_element_located(self.locators.PET_NAME_INPUT))
        name_input.clear()
        name_input.send_keys(name)

    def fill_pet_age(self, age):
        name_input = self.wait.until(EC.presence_of_element_located(self.locators.PET_AGE_INPUT))
        name_input.clear()
        name_input.send_keys(age)

    def select_pet_type(self, pet_type: str):
        dropdown_select = self.wait.until(EC.element_to_be_clickable(self.locators.PET_TYPE_DROPDOWN))
        dropdown_select.click()

        option_xpath = self.locators.PET_TYPE_OPTION_XPATH.format(pet_type=pet_type)
        target_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, option_xpath)))
        target_option.click()

    def select_pet_gender_male(self):
        type_select = self.wait.until(EC.element_to_be_clickable(self.locators.PET_GENDER_DROPDOWN))
        type_select.click()
        male_option = self.wait.until(EC.element_to_be_clickable(self.locators.PET_GENDER_OPTION_MALE))
        male_option.click()

    def save_pet(self):
        submit_button = self.wait.until(EC.element_to_be_clickable(self.locators.SUBMIT_BUTTON))
        submit_button.click()

    def cancel_create_pet(self):
        cancel_button = self.wait.until(EC.element_to_be_clickable(self.locators.CANCEL_BUTTON))
        cancel_button.click()
