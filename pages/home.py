from selenium.webdriver.common.by import By
from pages.base import BasePage

class HomePage(BasePage):

    BASE_URL = 'https://www.twitch.tv/'

    ACCEPT_COOKIE = (By.XPATH, '//button[@data-a-target="consent-banner-accept"]')
    BROWSE_BUTTON = (By.XPATH, '//div[contains(text(),"Browse")]/..')
    SEARCH_BAR = (By.XPATH, '//input[@type="search"]')

    def open_home_page(self):
        self.visit(self.BASE_URL)

        # somewhat necessary artificial waiting time
        # @todo: find better way
        self.wait_seconds(3)

        # cookie policy
        self.wait_for_visible(self.ACCEPT_COOKIE)
        self.assert_element_exists(self.ACCEPT_COOKIE)
        self.click(self.ACCEPT_COOKIE)

        # browse button should be visible on home page
        self.wait_for_visible(self.BROWSE_BUTTON)
        self.assert_element_exists(self.BROWSE_BUTTON)
        self.click(self.BROWSE_BUTTON)

    def open_search_bar(self):
        self.wait_for_visible(self.SEARCH_BAR)
        self.click(self.SEARCH_BAR)

    def enter_search_text(self, text):
        # self.click(self.SEARCH_INPUT)
        self.type_text(self.SEARCH_BAR, text)
