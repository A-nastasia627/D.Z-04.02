import re
import allure
from playwright.sync_api import Page, expect
from pages.page_text_input import PageTextInput
from pages.page_main import MainPage


@allure.title("Тест: изменение текста кнопки .")
def test_new_text_button(page: Page):
    page_text = PageTextInput(page)
    page_main = MainPage(page)

    with allure.step("Открытие главной страницы."):
        page_main.open_main_page()

    with allure.step("Пролистывание страницы."):
        page.evaluate("window.scrollBy(0,500);")

    with allure.step("Переход по ссылке Input text."):
        page_main.click_link_text_input()

    with allure.step("Проверка URL при переходе по ссылке"):
        new_url = "http://uitestingplayground.com/textinput"
        expect(page).to_have_url(new_url)

    with (allure.step("Ввод текста кнопка.")):
        new_text = "new text button"
        page_text.fill_new_text(new_text)

    with allure.step("Нажатие кнопки."):
        page_text.click_button()
