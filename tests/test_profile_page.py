import pytest
from pages.profile_page import ProfilePage
from data.test_data import PET_DATA, URLS, PET_TYPES
from pages.pet_new_page import PetNewPage
from pages.pet_edit_page import PetEditPage
from selenium.webdriver.common.by import By
import time

# 1. Проверка добавления нового питомца pet 1 c заполнением только обязательных полей
@pytest.mark.smoke
def test_add_new_pet(profile_page, browser):
    pet_name = PET_DATA['pet1']['name']
    pet_type = PET_DATA['pet1']['type']
    initial_pets_count = profile_page.get_pets_count()
    print(f'Количество питомцев до прохождения теста: {initial_pets_count}')
    profile_page.click_add_button()
    pet_new_page = PetNewPage(browser)
    print('Открыта страница создания нового питомца')
    pet_new_page.fill_pet_name(pet_name)
    print('Заполнено поле Name')
    pet_new_page.select_pet_type(pet_type)
    print('Выбрана категория (type=cat)')
    pet_new_page.save_pet()
    time.sleep(1)
    browser.get(URLS['profile_page'])
    print('Создан новый питомец')
    time.sleep(1)
    current_pet_count = profile_page.get_pets_count()
    print(f'Количество питомцев после прохождения теста: {current_pet_count}')

    assert current_pet_count == initial_pets_count + 1, (f"Ожидалось питомцев: {initial_pets_count + 1}, "f"но на странице сейчас: {current_pet_count}")
    assert profile_page.is_new_pet_displayed(pet_name), (f"Питомец с именем '{pet_name}' не отображается в профиле")

# 2. Проверка добавления нового питомца pet2 c заполнением обязательных и необязательных полей на странице pet_new_page
@pytest.mark.regression
def test_add_new_pet_with_optional_fields(profile_page, browser):
    pet_name = PET_DATA['pet2']['name']
    pet_type = PET_DATA['pet2']['type']
    pet_age = PET_DATA['pet2']['age']
    initial_pets_count = profile_page.get_pets_count()
    print(f'Количество питомцев до прохождения теста: {initial_pets_count}')
    profile_page.click_add_button()
    pet_new_page = PetNewPage(browser)
    print('Открыта страница создания нового питомца')
    pet_new_page.fill_pet_name(pet_name)
    print('Заполнено поле Name')
    pet_new_page.select_pet_type(pet_type)
    print('Выбрана категория (type=cat)')
    pet_new_page.fill_pet_age(pet_age)
    print('Заполнено поле Age')
    pet_new_page.select_pet_gender_male()
    print('Выбран gender Male')
    pet_new_page.save_pet()
    time.sleep(1)
    browser.get(URLS['profile_page'])
    print('Создан новый питомец')
    time.sleep(1)
    current_pet_count = profile_page.get_pets_count()
    print(f'Количество питомцев после прохождения теста: {current_pet_count}')

    assert current_pet_count == initial_pets_count + 1, (f"Ожидалось питомцев: {initial_pets_count + 1}, "f"но на странице сейчас: {current_pet_count}")
    assert profile_page.is_new_pet_displayed(pet_name), (f"Питомец с именем '{pet_name}' не отображается в профиле")

# 3. Проверка сохранения данных при отмене(кнопка Cancel)
@pytest.mark.smoke
def test_add_new_pet_with_cancel(profile_page, browser):
    pet_name = PET_DATA['pet4']['name']
    pet_type = PET_DATA['pet4']['type']
    initial_pets_count = profile_page.get_pets_count()
    print(f'Количество питомцев до прохождения теста: {initial_pets_count}')
    profile_page.click_add_button()
    pet_new_page = PetNewPage(browser)
    print('Открыта страница создания нового питомца')
    pet_new_page.fill_pet_name(pet_name)
    print('Заполнено поле Name')
    pet_new_page.select_pet_type(pet_type)
    print('Выбрана категория (type=cat)')
    pet_new_page.cancel_create_pet()
    time.sleep(1)
    browser.get(URLS['profile_page'])

    time.sleep(1)
    current_pet_count = profile_page.get_pets_count()
    print(f'Количество питомцев после прохождения теста: {current_pet_count}')

    assert current_pet_count == initial_pets_count, (f"Ожидалось питомцев: {initial_pets_count}, "f"но на странице сейчас: {current_pet_count}")


# 4. Редактирование категории питомца (с cat на hamster)
# @pytest.mark.smoke
def test_edit_pet_type_cat_to_hamster(browser, profile_page, created_pet):
    pet_name = created_pet["name"] # cоздание питомца через фикстуру created_pet
    time.sleep(3)
    browser.get(URLS['profile_page'])
    time.sleep(1)
    profile_page.open_pet_edit_form(pet_name)
    pet_edit_page = PetEditPage(browser)
    pet_type = PET_DATA['pet3_edited']['type']
    pet_edit_page.select_pet_type(pet_type)  # меняем на hamster
    pet_edit_page.save_pet()
    time.sleep(5)
    assert profile_page.get_pet_type(pet_name) == PET_TYPES['hamster']

# 5. Удаление элемента из списка
# @pytest.mark.smoke
def test_delete_pet(browser, profile_page, created_pet):
    pet_name = created_pet["name"] # cоздание питомца через фикстуру created_pet
    time.sleep(3)
    browser.get(URLS['profile_page'])
    profile_page.delete_pet(pet_name)
    profile_page.wait_for_confirm_dialog()
    profile_page.confirm_delete_pet(pet_name)
    browser.refresh()
    time.sleep(5)
    assert profile_page.is_pet_not_displayed(pet_name), (f"Питомец с именем '{pet_name}' отображается в профиле")



