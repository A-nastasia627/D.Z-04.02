from playwright.sync_api import Page


class Input:
    def __init__(self, page: Page):
        self.page = page
        self.locator_input = page.get_by_placeholder('MyButton')

    def fill(self, text: str):
        self.locator_input.fill(text)
