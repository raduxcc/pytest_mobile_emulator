import pytest
import yaml
from pathlib import Path
from utils.driver_factory import create_mobile_driver
from utils.driver_factory import create_web_driver
from pytest_html import extras


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default=None, help="Target environment")
    parser.addoption("--device", action="store", default=None, help="Mobile device name")
    parser.addoption("--headless", action="store_true", help="Run in headless mode")


@pytest.fixture(scope="session")
def config(request):
    # absolute path to this conftest.py
    base_dir = Path(__file__).resolve().parent
    config_path = base_dir / "config.yaml"

    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")

    with config_path.open() as f:
        cfg = yaml.safe_load(f)

    env_name = request.config.getoption("--env") or cfg["default_env"]
    env_cfg = cfg["environments"][env_name]

    device = request.config.getoption("--device") or cfg["mobile"]["default_device"]


    return {
        "env": env_name,
        "base_url": env_cfg["base_url"],
        "chrome_binary": env_cfg["chrome_binary"],
        "mobile_device": device,
        'default_browser': cfg["default_browser"],
        "headless": cfg["browser_mode"]["headless"],
        "window_width": cfg["window_size"]["width"],
        "window_height": cfg["window_size"]["height"],
        "grid_enabled": cfg["selenium"]["grid"]["enabled"],
        "grid_url": cfg["selenium"]["grid"]["url"],
        "timeout_implicit_wait": cfg["timeouts"]["implicit_wait"],
    }


@pytest.fixture(scope="session")
def web_driver(config):
    driver = create_web_driver(config)
    driver.get(config["base_url"])
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def mobile_driver(config):
    driver = create_mobile_driver(config)
    driver.get(config["base_url"])
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to detect test failure and attach screenshot.
    """
    outcome = yield
    report = outcome.get_result()

    if report.outcome == 'failed':
        driver = item.funcargs.get("web_driver") or item.funcargs.get("mobile_driver")
        if not driver:
            return
        if report.failed:
            screenshot = driver.get_screenshot_as_base64()
            extra = getattr(report, "extra", [])
            extra.append(extras.image(screenshot, 'failed test screenshot'))
            report.extra = extra

