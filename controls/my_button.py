from playwright.sync_api import Page


class MyButton:
    def __init__(self, page: Page):
        self.page = page

        self.button = page.get_by_role("button", name="My&nbsp;Button")
        # self.button = page.get_by_role("button", name="My Button")

    def click(self):
        self.button.click()


