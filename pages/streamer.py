from selenium.webdriver.common.by import By
from pages.base import BasePage

class StreamerPage(BasePage):

    STREAMER_STREAMER_BANNER = (By.XPATH, '//img[@class="tw-image" and contains(@alt,"Profile banner for")]')
    STREAMER_STREAMER_NAME = (By.XPATH, '//h1[contains(@class,"tw-title")]')

    # def sdefx(self, n: int):

    def get_streamer_title(self, n: int = 1):
        self.wait_for_visible(self.STREAMER_STREAMER_NAME)
        el = self.get_nth_element(self.STREAMER_STREAMER_NAME, n)

        return el.text.strip()
