from selenium.webdriver.common.by import By
from pages.base import BasePage

class HomePage(BasePage):

    BASE_URL = 'https://www.twitch.tv/'

    COOKIE_OVERLAY = (By.XPATH, '//div[@data-a-target="consent-banner"]')
    ACCEPT_COOKIE = (By.XPATH, '//button[@data-a-target="consent-banner-accept"]')
    BROWSE_BUTTON = (By.XPATH, '//div[contains(text(),"Browse")]/..')
    SEARCH_BAR = (By.XPATH, '//input[@type="search"]')

    REQUIRED_ELEMENTS = [
        COOKIE_OVERLAY
    ]

    def open_home_page(self):
        self.visit(self.BASE_URL)
        # self.wait_seconds(3)
        self.wait_for_page_ready()
        # handle cookie policy
        self.assert_element_exists(self.ACCEPT_COOKIE)
        self.click(self.ACCEPT_COOKIE)

    def get_current_url(self):
        return self.driver.current_url

    def open_search_bar(self):
        self.wait_for_visible(self.BROWSE_BUTTON)
        self.assert_element_exists(self.BROWSE_BUTTON)
        self.click(self.BROWSE_BUTTON)

