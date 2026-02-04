from playwright.sync_api import Page


class ButtonTextInput:
    def __init__(self, page: Page):
        self.page = page
        self.button_locator = page.get_by_role("button", name="Button That Should Change it's Name Based on Input Value")

    def wrapper(self):
        return self.button_locator

    def click_button(self):
        self.wrapper().click()

