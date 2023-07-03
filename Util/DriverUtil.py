from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Setup driver
class DriverUtil:
    @staticmethod
    def get_instance(browser: str, mode = "--headless=new"):
        if browser == 'chrome':
            options = webdriver.ChromeOptions()
            options.add_argument(mode)
            return webdriver.Chrome(service=Service(ChromeDriverManager().install()),options = options)
