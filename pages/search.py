from selenium.webdriver.common.by import By
from pages.base import BasePage

class SearchPage(BasePage):

    BROWSE_BUTTON = (By.XPATH, '//div[contains(text(),"Browse")]/..')
    SEARCH_BAR = (By.XPATH, '//input[@type="search"]')
    SEARCH_CATEGORY_STARCRAFTII = (By.XPATH,'//a[contains(@href,"/directory/category/starcraft-ii")]')

    REQUIRED_ELEMENTS = [
        SEARCH_BAR,
        BROWSE_BUTTON
    ]

    def enter_search_text(self, text):
        self.wait_for_page_ready()
        self.assert_element_exists(self.SEARCH_BAR)
        self.click(self.SEARCH_BAR)

        self.type_text(self.SEARCH_BAR, text)
        # self.wait_seconds(1)


    def select_starcraftii_category(self):
        self.wait_for_visible(self.SEARCH_CATEGORY_STARCRAFTII)
        self.assert_element_exists(self.SEARCH_CATEGORY_STARCRAFTII)
        self.click(self.SEARCH_CATEGORY_STARCRAFTII)
        # self.wait_seconds(1)

