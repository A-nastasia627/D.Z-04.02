from playwright.sync_api import Page


class Section:
    def __init__(self, page: Page, title: str):
        self.page = page
        self.title = title

    def get_section_link(self, title):
        return self.page.locator(f'//section[@id="overview"]//a[contains(text(), "{title}")]')

    def click_text_input(self, title: str):
        self.get_section_link(title).click()
