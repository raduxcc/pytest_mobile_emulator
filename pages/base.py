import time
import os
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
from pytest_html import extras


class BasePage:

    def __init__(self, driver, timeout = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.timeout = timeout
        self.actions = ActionChains(driver)


    def visit(self, url):
        self.driver.get(url)


    def find(self, locator: tuple):
        return self.driver.find_element(*locator)


    def click(self, locator: tuple):
        self.find(locator).click()


    def type_text(self, locator: tuple, text: str):
        self.find(locator).send_keys(text)


    # # @todo: apparently broken in mobile emulator. If necessary, check other sources
    # def scroll_down(self, amount=200):
    #     self.actions.scroll_by_amount(0, amount).perform()


    def js_scroll_down(self, amount=200):
        self.driver.execute_script("window.scrollBy(0, arguments[0]);", amount)


    def wait_seconds(self, seconds: float):
        time.sleep(seconds)


    # reliable DOM ready state conditional wait
    def wait_for_page_ready(self, timeout : int = 10):
        timeout = timeout or self.timeout
        for locator in self.REQUIRED_ELEMENTS:
            try:
                WebDriverWait(self.driver, timeout).until(
                    EC.presence_of_element_located(locator)
                )
            except TimeoutException:
                raise AssertionError(
                    f"Page did not load required element: {locator} on {self.__class__.__name__}"
                )
        return True


    def wait_for_visible(self, locator: tuple):
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            raise AssertionError(f"Element not visible: {locator}")


    def is_visible(self, locator: tuple):
        try:
            return self.find(locator).is_displayed()
        except NoSuchElementException:
            return False


    # @todo: add selector aliases
    def assert_element_exists(self, locator, message=""):
        elements = self.driver.find_elements(*locator)
        if len(elements) == 0:
            msg = message or f"Expected element to exist: {locator}"
            self._fail_with_screenshot(msg)

        self.step_pass(f"Element exists: {locator}")
        return True


    # returns the n-th WebElement from a list of elements matching the provided xpath
    def get_nth_element(self, locator: tuple, n: int):
        elements = self.wait.until(EC.presence_of_all_elements_located(locator))

        if n < 1 or n > len(elements):
            raise IndexError(
                f"Index {n} out of range. Found only {len(elements)} elements for: {locator}"
            )

        return elements[n - 1]


    def take_screenshot(self, name_prefix: str = "screenshot"):
        os.makedirs("test_report", exist_ok=True)
        os.makedirs(f"test_report/assets", exist_ok=True)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filepath = f"test_report/assets/{name_prefix}_{timestamp}.png"

        self.driver.save_screenshot(filepath)
        return filepath

    # STEP LOGGING

    def _add_report_extra(self, extra):
        if not hasattr(self.driver, "_pytest_report_extras"):
            self.driver._pytest_report_extras = []
        self.driver._pytest_report_extras.append(extra)

    def step(self, message: str):
        page = self.__class__.__name__
        log_msg = f"[STEP PASS] {message} on {page}"
        print(log_msg)
        self._add_report_extra(extras.text(log_msg))

        return True


    def step_pass(self, message: str = "Assertion passed"):
        return self.step(message)


    def _fail_with_screenshot(self, message: str):
        test_report_older_path = "test_report"
        assets_folder_path = "test_report/assets"
        os.makedirs(test_report_older_path, exist_ok=True)
        os.makedirs(assets_folder_path, exist_ok=True)

        filename = f"assert_fail_{int(time.time())}.png"
        filepath = os.path.join(assets_folder_path, filename)

        self.driver.save_screenshot(filepath)

        # append to html report
        from pytest_html import extras
        self._add_report_extra(extras.image(filepath))

        raise AssertionError(message)
