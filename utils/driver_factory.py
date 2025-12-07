from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def create_mobile_driver(device_name):
    chrome_options = Options()
    chrome_options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    mobile_emulation = {"deviceName": device_name}
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

    # get latest chromedriver
    service = Service(ChromeDriverManager().install())

    # construct the WebDriver
    driver = webdriver.Chrome(
        service=service,
        options=chrome_options
    )

    return driver
