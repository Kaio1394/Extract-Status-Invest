
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Util.DriverUtil import DriverUtil


class Helper:
    def __init__(self):
        self.driver = DriverUtil.get_instance('chrome')

    def get_url(self, value):
        self.driver.get(value)

    def send_keys(self, options_by, by_value, value):
        match str(options_by).lower():
            case 'name':
                self.driver.find_element(By.NAME, by_value).send_keys(value)
            case 'xpath':
                self.driver.find_element(By.XPATH, by_value).send_keys(value)
            case 'id':
                self.driver.find_element(By.ID, by_value).send_keys(value)

    def send_click(self, options_by, by_value):
        match str(options_by).lower():
            case 'name':
                self.driver.find_element(By.NAME, by_value).click()
            case 'xpath':
                self.driver.find_element(By.XPATH, by_value).click()
            case 'id':
                self.driver.find_element(By.ID, by_value).click()

    def close(self):
        self.driver.close()
    
    def get_text_element(self, options_by, by_value):
        match str(options_by).lower():
            case 'name':
                return self.driver.find_element(By.NAME, by_value).text
            case 'xpath':
                return self.driver.find_element(By.XPATH, by_value).text
            case 'id':
                return self.driver.find_element(By.ID, by_value).text
    
    
    def get_url_browser(self):
        return self.driver.current_url

    def wait_until(self, timeout, options_by, value):
        match str(options_by).lower():
            case 'name':
                WebDriverWait(self.driver, timeout)\
                    .until(EC.presence_of_element_located((By.NAME, value)))
            case 'xpath':
                WebDriverWait(self.driver, timeout) \
                    .until(EC.presence_of_element_located((By.XPATH, value)))
            case 'id':
                WebDriverWait(self.driver, timeout) \
                    .until(EC.presence_of_element_located((By.ID, value)))