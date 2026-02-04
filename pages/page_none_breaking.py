from playwright.async_api import Page
from controls.my_button import MyButton


class PageNoneBreaking:
    def __init__(self, page: Page):
        self.page = page
        self.url = "http://uitestingplayground.com/nbsp"
        self.button = MyButton(self.page)

    def open(self):
        self.page.goto(self.url)

    def click_button(self):
        self.button.click()

