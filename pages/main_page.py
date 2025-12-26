import time
from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import MainPageLocators, HeaderLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class MainPage(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)  # наследование wait из BasePage
        self.wait_1s = WebDriverWait(browser, 1)

    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        #login_link.click()
        self.browser.execute_script("arguments[0].click();", login_link)

    def select_filter(self, filter_type):
        dropdown_select = self.wait.until(EC.element_to_be_clickable(MainPageLocators.FILTER_TYPE_DROPDOWN))
        dropdown_select.click()
        option_xpath = f"//ul[contains(@class,'p-dropdown-items')]//li[@role='option'][normalize-space(.//span | .)='{filter_type}']"
        target_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, option_xpath)))
        target_option.click()

    def assert_pets_type_current_page(self, expected_type: str):
        all_cards = self.wait.until(
            EC.presence_of_all_elements_located(MainPageLocators.PET_CARDS)
        )
        visible_cards = [card for card in all_cards if card.is_displayed()]
        assert visible_cards, "Отфильтрованный список пуст (нет видимых карточек)"

        expected = expected_type.strip()

        for card in visible_cards:
            pet_type = card.find_element(*MainPageLocators.PET_TYPE).text.strip()
            pet_name = card.find_element(*MainPageLocators.PET_NAME).text.strip()

            assert pet_type == expected, (f"Ожидали тип '{expected_type}', а в карточке '{pet_type}' (name='{pet_name}')")


    def filter_by_pet_name(self, name: str):
        field = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(MainPageLocators.NAME_FILTER))
        field.clear()
        field.send_keys(name + Keys.ENTER)

    def get_visible_pet_names(self):
        time.sleep(0.5)
        cards = WebDriverWait(self.browser, 10).until(EC.presence_of_all_elements_located(MainPageLocators.PET_CARDS))
        names = []
        for card in cards:
            if not card.is_displayed():
                continue
            name_el = card.find_element(*MainPageLocators.PET_NAME)
            names.append(name_el.text.strip())
        return names

    def get_card_by_name(self, pet_name):
        cards = self.browser.find_elements(*MainPageLocators.PET_CARDS)
        for card in cards:
            name = card.find_element(*MainPageLocators.PET_NAME).text
            if name == pet_name:
                return card
        raise AssertionError(f"Карточка с именем {pet_name} не найдена")

    def is_liked(self, card):
        like_pet = card.find_element(*MainPageLocators.LIKE_CONTAINER)
        classes = like_pet.get_attribute("class")
        return "liked" in classes

    def open_pet_details(self, pet_name):
        card = self.get_card_by_name(pet_name)
        details_button = card.find_element(*MainPageLocators.DETAILS_BUTTON)
        details_button.click()

    def click_quit(self):
        quit_button = self.wait.until(EC.element_to_be_clickable(HeaderLocators.QUIT_BUTTON))
        quit_button.click()


    def assert_pets_type_all_pages(self, pets_type):
        while True:
            self.assert_pets_type_current_page(pets_type)
            try:
                self.wait_1s.until_not(EC.element_to_be_clickable(MainPageLocators.NEXT_PAGE_BUTTON))
                break
            except:
                next_button = self.wait.until(EC.element_to_be_clickable(MainPageLocators.NEXT_PAGE_BUTTON))
                next_button.click()
                time.sleep(1)