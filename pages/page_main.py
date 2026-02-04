from playwright.sync_api import Page
from components.section import Section


class MainPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "http://uitestingplayground.com/"
        self.section_input = Section(page, "Text Input")
        self.section_none_breaking = Section(page, "Non-Breaking Space")

    def open_main_page(self):
        self.page.goto(self.url)

    def click_link_text_input(self):
        self.section_input.click_text_input("Text Input")

    def click_link_none_breaking(self):
        self.section_input.click_text_input("Non-Breaking Space")
