import time
import pytest
from utils.driver_factory import create_mobile_driver
from pages.home import HomePage
from pages.search_results import SearchResultsPage
from pages.streamer import StreamerPage


@pytest.fixture
def driver():
    driver = create_mobile_driver(device_name="Pixel 7")
    yield driver
    driver.quit()


def test_twitch_mobile_nav(driver):
    home = HomePage(driver)
    results = SearchResultsPage(driver)
    streamer = StreamerPage(driver)

    # 1. go to twitch.tv
    home.open_home_page()
    results.take_screenshot("home-page")
    time.sleep(2)

    # 2. click in the search icon / open search bar
    home.open_search_bar()

    # 3. Input StarCraft II
    home.enter_search_text("StarCraft II")
    time.sleep(2)

    # select first result
    results.select_nth_starcraftii_result(1)
    time.sleep(2)

    # 4. Scroll down two times
    results.scroll_down(times=2)
    time.sleep(2)

    # 5. Select first streamer
    results_streamer_name = results.get_streamer_title()
    results.select_first_streamer()
    time.sleep(2)

    # Streamer page validations
    streamer_streamer_name = streamer.get_streamer_title()
    assert results_streamer_name == streamer_streamer_name
    results.take_screenshot("end-of-test")
