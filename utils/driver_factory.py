from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def create_mobile_driver(config, device_name=None):
    chrome_options = Options()

    # Chrome binary per environment
    chrome_options.binary_location = config["chrome_binary"]

    # Mobile emulation
    device = device_name or config["mobile_device"]
    chrome_options.add_experimental_option(
        "mobileEmulation", {"deviceName": device}
    )


    chrome_options.add_argument(f"--window-size={config["window_width"]},{config["window_height"]}")
    if config["headless"]:
        chrome_options.add_argument("--headless=new")
        # chrome_options.add_argument("--window-size=412,915")

    # ---------- Driver Construction ----------
    if config["grid_enabled"]:
        driver = webdriver.Remote(
            command_executor=config["grid_url"],
            options=chrome_options
        )
    else:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)

    return driver


def create_web_driver(cfg):
    browser = cfg["default_browser"]
    if browser == "chrome":
        options = Options()
        if cfg["headless"]:
            options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()
    driver.implicitly_wait(cfg["timeout_implicit_wait"])

    return driver
