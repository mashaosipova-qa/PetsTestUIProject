from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage
from pages.locators import ProfilePageLocators
from data.test_data import URLS
from selenium.common.exceptions import TimeoutException


class ProfilePage(BasePage):
    def __init__(self, browser, timeout=10):
        super().__init__(browser, URLS['profile_page'], timeout)
        self.profile_locators = ProfilePageLocators()
        self.wait = WebDriverWait(self.browser, timeout)

    # Нажатие на кнопку "+"
    def click_add_button(self):
        add_button = self.wait.until(EC.element_to_be_clickable(self.profile_locators.ADD_BUTTON))
        add_button.click()

    # Возвращает количество питомцев на странице профиля
    def get_pets_count(self):
        cards = self.browser.find_elements(*self.profile_locators.PET_CARD)
        return len(cards)

    # Проверяет есть ли на странице элемент с текстом = {pet_name}
    def is_new_pet_displayed(self, pet_name):
        pet_xpath = ProfilePageLocators.NEW_PET_XPATH.format(pet_name=pet_name)
        pet_locator = (By.XPATH, pet_xpath)

        pet = self.wait.until(EC.presence_of_element_located(pet_locator))
        return pet.is_displayed()

    def open_pet_edit_form(self, pet_name):
        edit_xpath = ProfilePageLocators.PET_EDIT_BUTTON_XPATH.format(pet_name=pet_name)
        edit_locator = (By.XPATH, edit_xpath)

        edit_button = self.wait.until(EC.element_to_be_clickable(edit_locator))
        edit_button.click()

    def get_pet_type(self, pet_name):
        # Находим элемент по имени питомца
        pet_xpath = ProfilePageLocators.PET_BY_NAME_XPATH.format(pet_name=pet_name)
        pet_elem = self.wait.until(EC.presence_of_element_located((By.XPATH, pet_xpath)))
        # Находим карточку этого питомца
        pet_card = pet_elem.find_element(By.XPATH, ProfilePageLocators.PET_CARD_BY_PET_ELEMENT)
        # Ищем тип питомца внутри карточки
        type_elements = pet_card.find_elements(By.XPATH, ProfilePageLocators.PET_TYPE_IN_CARD_XPATH)
        for elem in type_elements:
            pet_type = elem.text.strip().lower()
            return pet_type

    def delete_pet1(self, pet_name):
        delete_button = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH,
             f"//button[@aria-label='Delete' and ancestor::div[contains(@class, 'product-list-item')][.//div[contains(@class, 'product-name') and contains(., '{pet_name}')]]]")
        ))
        delete_button.click()

    def delete_pet(self, pet_name):
        delete_xpath = ProfilePageLocators.PET_DELETE_BUTTON_XPATH.format(pet_name=pet_name)
        delete_locator = (By.XPATH, delete_xpath)

        delete_button = self.wait.until(EC.element_to_be_clickable(delete_locator))
        delete_button.click()

    def wait_for_confirm_dialog(self):
        self.wait.until(EC.presence_of_element_located(self.profile_locators.CONFIRM_DELETE_LOCATOR))

    def confirm_delete_pet(self, pet_name):
        confirm_delete_button = self.wait.until(EC.element_to_be_clickable(self.profile_locators.CONFIRM_DELETE_LOCATOR))
        confirm_delete_button.click()

    def is_pet_not_displayed1(self, pet_name):
        pet_locator = (By.XPATH, f"//*[normalize-space(text())='{pet_name}']")
        try:
            pet = self.wait.until(EC.element_to_be_clickable(pet_locator))
            return not pet.is_displayed()
        except TimeoutException:
            return True # Питомец не найден т.е удален

    def is_pet_not_displayed(self, pet_name):
        pet_xpath = ProfilePageLocators.PET_BY_NAME_XPATH.format(pet_name=pet_name)
        pet_locator = (By.XPATH, pet_xpath)

        try:
            pet = self.wait.until(EC.element_to_be_clickable(pet_locator))
            return not pet.is_displayed()
        except TimeoutException:
            # Элемент так и не появился — считаем, что питомец удалён
            return True





