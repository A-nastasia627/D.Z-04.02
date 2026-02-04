import re
import allure
from playwright.sync_api import Page, expect
from pages.page_none_breaking import PageNoneBreaking
from pages.page_main import MainPage


@allure.title("Тест: нажатие кнопки My Button.")
def test_click_button(page: Page):
    page_none_breaking = PageNoneBreaking(page)
    page_main = MainPage(page)

    with allure.step("Открытие главной страницы."):
        page_main.open_main_page()

    with allure.step("Переход по ссылке Non-Breaking Space."):
        page_main.click_link_none_breaking()

    with allure.step("Проверка URL при переходе по ссылке"):
        new_url = "http://uitestingplayground.com/nbsp"
        expect(page).to_have_url(new_url)

    with allure.step("Нажатие кнопки."):
        page_none_breaking.click_button()


# pytest --alluredir test_results
# allure serve test_results
# allure generate

# с интерфейс- pytest --headed
# в разные браузеры- pytest --browser webkit
# конкретный тест- pytest test_login.py
# конкретный тест, передайте имя функции теста- pytest -k test_add_a_todo_item