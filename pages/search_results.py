from selenium.webdriver.common.by import By
from pages.base import BasePage

class SearchResultsPage(BasePage):

    RESULTS_STARCRAFTII = (By.XPATH, '//p[@title="StarCraft II"]')
    RESULTS_STREAMERS_PROFILE_PIC = (By.XPATH, '//article/div/div/div/a[contains(@class,"tw-link") and contains(@href,"/home")]')
    # RESULTS_STREAMERS_ALTERNATIVE = (By.XPATH, '//button[contains(@class,"ScCoreLink")]/div/div/following-sibling::*/div')
    RESULTS_STREAMERS_NAME = (By.XPATH, '//a[contains(@class,"tw-link") and contains(@href,"/home")]/div/div/../..') #dirty selector

    def select_nth_starcraftii_result(self, n: int):
        self.get_nth_element(self.RESULTS_STARCRAFTII, n).click()

    def scroll_down(self, times: int = 2, amount: float = 100):
        for _ in range(times):
            self.js_scroll_down(amount)
            self.wait_seconds(1)

    def get_streamer_title(self, n: int = 1):
        self.wait_for_visible(self.RESULTS_STREAMERS_NAME)
        el = self.get_nth_element(self.RESULTS_STREAMERS_NAME, n)

        return el.text.strip()


    def select_first_streamer(self, n: int = 1):
        self.wait_for_visible(self.RESULTS_STREAMERS_PROFILE_PIC)
        self.get_nth_element(self.RESULTS_STREAMERS_PROFILE_PIC, n).click()
