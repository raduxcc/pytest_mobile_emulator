import pytest
from pytest_html import extras

def pytest_configure(config):
    pytest.extra_data = []

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to detect test failure and attach screenshot.
    """

    outcome = yield
    report = outcome.get_result()

    # Only take screenshot on test failure
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")  # retrieve driver fixture

        # if driver:
        #     timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        #     test_name = item.name.replace(" ", "_")
        #
        #     os.makedirs("test_runs", exist_ok=True)
        #     os.makedirs(f"test_runs/{driver.session_id}", exist_ok=True)
        #
        #     filename = f"test_runs/{driver.session_id}/FAILURE_on_{test_name}_{timestamp}.png"
        #     # failed_ss_path = filename
        #
        #     driver.save_screenshot(filename)
        #
        #     print(f"\n[TEST FAIL SCREENSHOT SAVED] @ {filename}")
        if not driver:
            return
        if report.failed:
            screenshot = driver.get_screenshot_as_base64()
            extra = getattr(report, "extra", [])
            extra.append(extras.image(screenshot, '^ failure screenshot ^'))
            # extra.append(extras.image("/" + failed_ss_path, 'Screenshot on Failure'))
            report.extra = extra

