from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from pages.locators import PetEditPageLocators, ProfilePageLocators, PetNewPageLocators
from data.test_data import URLS
from pages.base_page import BasePage



class PetEditPage(BasePage):
    def __init__(self, browser, timeout=10):
        super().__init__(browser, URLS["pet_edit_page"], timeout)
        self.locators = PetEditPageLocators()
        self.profile_locators = ProfilePageLocators()
        self.pet_new_page_locators = PetNewPageLocators()
        self.wait = WebDriverWait(self.browser, timeout)

    def select_pet_type(self, pet_type):
        dropdown_select = self.wait.until(EC.element_to_be_clickable(self.pet_new_page_locators.PET_TYPE_DROPDOWN))
        dropdown_select.click()

        option_xpath = self.pet_new_page_locators.PET_TYPE_OPTION_XPATH.format(pet_type=pet_type)
        target_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, option_xpath)))
        target_option.click()


    def save_pet(self):
        save_button = self.wait.until(EC.element_to_be_clickable(self.locators.SAVE_BUTTON))
        save_button.click()
