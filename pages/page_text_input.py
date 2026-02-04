from playwright.sync_api import Page
from controls.text_input import Input
from controls.button_text_input import ButtonTextInput


class PageTextInput:
    def __init__(self, page: Page):
        self.page = page
        self.url = "http://uitestingplayground.com/textinput"
        self.input_field = Input(self.page)
        self.button_text_input = ButtonTextInput(self.page)

    def open(self):
        self.page.goto(self.url)

    def fill_new_text(self, new_text: str):
        self.input_field.fill(new_text)

    def click_button(self):
        self.button_text_input.click_button()

    def get_button_locator(self):
        return self.button_text_input.wrapper()

