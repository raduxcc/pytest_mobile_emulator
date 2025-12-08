from selenium.webdriver.common.by import By
from pages.base import BasePage

class StreamerPage(BasePage):

    STREAMER_STREAMER_BANNER = (By.XPATH, '//img[@class="tw-image" and contains(@alt,"Profile banner for")]')
    STREAMER_STREAMER_NAME = (By.XPATH, '//h1[contains(@class,"tw-title")]')
    STREAMER_FIRST_VIDEO = (By.XPATH, '//button[@role="link"]/div/div/img')

    REQUIRED_ELEMENTS = [
        STREAMER_STREAMER_BANNER,
        STREAMER_STREAMER_NAME,
        STREAMER_FIRST_VIDEO
    ]

    def get_streamer_title(self):

        self.wait_for_page_ready()
        self.assert_element_exists(self.STREAMER_STREAMER_BANNER)
        self.assert_element_exists(self.STREAMER_STREAMER_NAME)

        title = self.find(self.STREAMER_STREAMER_NAME).text.strip()

        return title
