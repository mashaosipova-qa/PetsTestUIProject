from selenium.webdriver.common.by import By

class HeaderLocators:
    QUIT_BUTTON = (By.XPATH, "//a[contains(@class,'p-menuitem-link')][.//span[@class='p-menuitem-text' and normalize-space()='Quit']]")

class MainPageLocators:
    LOGIN_LINK = (By.XPATH, '//*[@id="app"]/header/div/ul/li[1]/a')
    FILTER_TYPE_DROPDOWN = (By.XPATH, "//div[contains(@class,'p-dropdown') and .//span[contains(@class,'p-dropdown-label')]]")
    PET_CARDS = (By.XPATH, "//div[contains(@class,'product-grid-item') and contains(@class,'card') and not(contains(@style,'display: none'))]")
    PET_TYPE = (By.CSS_SELECTOR, "span.product-category")
    PET_NAME = (By.CSS_SELECTOR, "div.product-name")
    NAME_FILTER = (By.CSS_SELECTOR, "input#petName")
    LIKE_CONTAINER = (By.CSS_SELECTOR, "span.product-price")
    DETAILS_BUTTON = (By.CSS_SELECTOR, "button[aria-label='Details']")
    NEXT_PAGE_BUTTON = (By.CSS_SELECTOR, "button.p-paginator-next")
    PAGINATOR_PAGES_CONTAINER = (By.CSS_SELECTOR, "span.p-paginator-pages")
    #Динамический локатор
    # @staticmethod
    # def pet_card_by_name(name: str):
    #     return (By.XPATH, f"//div[contains(@class,'product-grid-item') and contains(@class,'card')]" f"//div[contains(@class,'product-name') and text()='{name}']")

class LoginPageLocators:
    LOGIN_EMAIL = (By.ID, "login")
    LOGIN_PASS = (By.CSS_SELECTOR, "#password > input")
    LOGIN_BTN = (By.CLASS_NAME, "p-button-label")

class ProfilePageLocators:
    ADD_BUTTON = (By.XPATH, "//button[@type='button']")
    PET_CARD = (By.CSS_SELECTOR, ".col-12")
    EDIT_BUTTON = (By.XPATH, ".//button[contains(@aria-label,'Edit')]")
    CONFIRM_DELETE_LOCATOR = (By.CSS_SELECTOR, "body > div.p-confirm-popup.p-component.p-ripple-disabled > div.p-confirm-popup-footer > button.p-button.p-component.p-confirm-popup-accept.p-button-sm")
    NEW_PET_XPATH = "//*[normalize-space(text())='{pet_name}']"
    PET_EDIT_BUTTON_XPATH = ("//button[@aria-label='Edit' and " "ancestor::div[contains(@class, 'product-list-item')]" "[.//div[contains(@class, 'product-name') and contains(., '{pet_name}')]]]")
    PET_BY_NAME_XPATH = "//*[normalize-space(text())='{pet_name}']"
    PET_CARD_BY_PET_ELEMENT = "./ancestor::div[contains(@class, 'product-list-detail')][1]"
    PET_TYPE_IN_CARD_XPATH = (".//*[contains(text(), 'cat') or contains(text(), 'hamster') or " "contains(text(), 'dog') or contains(text(), 'reptile') or " "contains(text(), 'parrot')]")
    PET_DELETE_BUTTON_XPATH = ("//button[@aria-label='Delete' and " "ancestor::div[contains(@class, 'product-list-item')]" "[.//div[contains(@class, 'product-name') and contains(., '{pet_name}')]]]")
    PET_BY_NAME_XPATH = "//*[normalize-space(text())='{pet_name}']"

class PetNewPageLocators:
    PET_NAME_INPUT = (By.ID, "name")
    PET_AGE_INPUT = (By.XPATH, "//span[@id='age']//input")
    PET_TYPE_DROPDOWN = (By.ID, "typeSelector")
    PET_GENDER_DROPDOWN = (By.ID, "genderSelector")
    PET_TYPE_OPTION = (By.XPATH, "//div[@id='pv_id_4_list']//li[@role='option' and normalize-space(text())='{pet_type}']")
    PET_GENDER_OPTION_MALE = (By.XPATH, "//ul[contains(@class,'p-dropdown-items')]//li[@role='option' and @aria-label='Male']")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
    CANCEL_BUTTON = (By.CSS_SELECTOR, '[aria-label="Cancel"]')
    PET_TYPE_OPTION_XPATH = "//div[contains(@class,'p-dropdown-panel')]//li[@role='option'][normalize-space(.//span | .)='{pet_type}']"

class PetEditPageLocators:
    SAVE_BUTTON = (By.XPATH, "//button[@type='submit']")


