import time
import pytest
from utils.driver_factory import create_mobile_driver
from pages.home import HomePage
from pages.search import SearchPage
from pages.search_results import SearchResultsPage
from pages.streamer import StreamerPage


@pytest.fixture
def driver():
    driver = create_mobile_driver(device_name="Pixel 7")
    yield driver
    driver.quit()


def test_twitch_homepage_failing(driver):
    home = HomePage(driver)
    home.open_home_page()

    current_url = home.get_current_url()
    # failing intentionally to test screenshot embedding into html report
    assert current_url == "https://m.twitch.tv"

def test_twitch_mobile_nav(driver):
    home = HomePage(driver)
    search = SearchPage(driver)
    results = SearchResultsPage(driver)
    streamer = StreamerPage(driver)

    # 1. go to twitch.tv
    home.open_home_page()

    # assert redirect to mobile site version
    current_url = home.get_current_url()
    assert current_url == "https://m.twitch.tv/?desktop-redirect=true"

    # 2. click in the search icon / open search bar
    home.open_search_bar()

    # 3. Input StarCraft II
    search.enter_search_text("StarCraft II")

    # select first result
    search.select_starcraftii_category()
    assert results.get_current_url() == "https://m.twitch.tv/directory/category/starcraft-ii"
    # 4. Scroll down two times
    results.scroll_down(times=2)

    # 5. Select first streamer
    results_streamer_name = results.get_streamer_title()
    results.select_first_streamer()

    # Streamer page validations
    streamer_streamer_name = streamer.get_streamer_title()
    assert results_streamer_name == streamer_streamer_name
    results.take_screenshot("end-of-test")
