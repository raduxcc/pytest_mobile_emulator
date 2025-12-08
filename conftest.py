import pytest
from pytest_html import extras


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to detect test failure and attach screenshot.
    """
    outcome = yield
    report = outcome.get_result()

    # take screenshot on test failure
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")  # retrieve driver fixture
        if not driver:
            return
        if report.failed:
            screenshot = driver.get_screenshot_as_base64()
            extra = getattr(report, "extra", [])
            extra.append(extras.image(screenshot, 'failed test screenshot'))
            report.extra = extra

