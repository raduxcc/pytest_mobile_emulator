from selenium.webdriver.common.by import By
from pages.base import BasePage

class SearchResultsPage(BasePage):

    BROWSE_BUTTON = (By.XPATH, '//div[contains(text(),"Browse")]/..')
    RESULTS_STREAMERS_PROFILE_PIC = (By.XPATH, '//article/div/div/div/a[contains(@class,"tw-link") and contains(@href,"/home")]')
    RESULTS_STREAMERS_NAMES = (By.XPATH, '//a[contains(@class,"tw-link") and contains(@href,"/home") and not(@aria-hidden="true")]')
    RESULTS_VIDEOS = (By.XPATH, '//div[@role="list"]//img[contains (@class, "tw-image" ) and contains(@sizes, "max-width")]')

    REQUIRED_ELEMENTS = [
        BROWSE_BUTTON
    ]

    def scroll_down(self, times: int = 2, amount: float = 200):
        for _ in range(times):
            self.wait_seconds(2)
            self.js_scroll_down(amount)
            # self.wait_seconds(2)

    def get_current_url(self):
        return self.driver.current_url

    def get_streamer_title(self, n: int = 1):
        self.wait_for_visible(self.RESULTS_STREAMERS_NAMES)
        self.assert_element_exists(self.RESULTS_STREAMERS_NAMES)

        title = self.get_nth_element(self.RESULTS_STREAMERS_NAMES, n).text.strip()

        return title


    def select_first_streamer(self, n: int = 1):
        # self.wait_for_visible(self.RESULTS_STREAMERS_PROFILE_PIC)

        self.wait_for_visible(self.RESULTS_VIDEOS)
        self.assert_element_exists(self.RESULTS_STREAMERS_PROFILE_PIC)
        self.wait_seconds(1)
        self.get_nth_element(self.RESULTS_STREAMERS_PROFILE_PIC, n).click()
