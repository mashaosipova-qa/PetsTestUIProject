import pytest
import time
from pages.main_page import MainPage
from data.test_data import PET_TYPES, URLS
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.skip
def test_go_to_login_page(browser):
    page = MainPage(browser, URLS['main_page'])
    page.open()
    page.go_to_login_page()
    browser.save_screenshot('result1.png')

# Проверка фильтрации по типу (type = hamster) под авторизованным пользователем
@pytest.mark.regression
def test_filter_pet_category(main_page):
    hamster_type = PET_TYPES['hamster']
    main_page.select_filter(hamster_type)
    time.sleep(1)
    main_page.assert_pets_type_all_pages(hamster_type)

#  Проверка фильтрации по имени питомца (Filter by pet name)
@pytest.mark.regression
def test_filter_by_pet_name(main_page, browser, created_pet):
    pet_name = created_pet["name"]  # cоздание питомца через фикстуру created_pet
    browser.get(URLS['main_page'])
    main_page.filter_by_pet_name(pet_name)
    time.sleep(1)
    names = main_page.get_visible_pet_names()
    print("VISIBLE NAMES:", names)
    assert names, "Отфильтрованный список не содержит питомца с таким именем"
    assert pet_name in names, "В списке нет питомца с таким именем"

# Проверка добавления лайка питомцу
@pytest.mark.smoke
def test_add_like_pet_by_name(main_page, browser, created_pet):
    pet_name = created_pet["name"]  # cоздание питомца через фикстуру created_pet
    browser.get(URLS['main_page'])
    main_page.filter_by_pet_name(pet_name)
    time.sleep(1)
    card = main_page.get_card_by_name(pet_name)
    like_pet = card.find_element(By.CSS_SELECTOR, "span.product-price")
    like_pet.click()
    names = main_page.get_visible_pet_names()
    print("VISIBLE NAMES:", names)
    assert "liked" in like_pet.get_attribute("class"), "Лайк не поставлен"

# Проверка что по клику на кнопку Details пользователь переходит на страницу Pet Details
@pytest.mark.regression
def test_open_pet_details(main_page, browser, created_pet):
    pet_name = created_pet["name"]  # cоздание питомца через фикстуру created_pet
    browser.get(URLS['main_page'])
    main_page.filter_by_pet_name(pet_name)
    time.sleep(1)
    main_page.open_pet_details(pet_name)
    assert "/details/" in browser.current_url
    browser.save_screenshot('details.png')

# Проверка, что по клику на кнопку Quit происходит перенаправление на страницу логина
@pytest.mark.regression
def test_quit_redirects_to_login(browser, logged_user, main_page):
    browser.get(URLS["main_page"])
    main_page.click_quit()
    WebDriverWait(browser, 10).until(EC.url_to_be(URLS['login_page']))
    assert browser.current_url == URLS['login_page']




