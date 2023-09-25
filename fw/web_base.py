from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WebBase:

    driver = None

    def get_driver(self):
        if self.driver is None:
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
        return self.driver

    def quit_driver(self):
        try:
            self.driver.quit()
            self.driver = None
        except:
            self.driver = None

    def click_element(self, locator):
        web_element = self.find_element(locator)
        web_element.click()

    def send_keys(self, locator, text):
        web_element = self.find_element(locator)
        web_element.send_keys(text)

    def get_tag_text(self, locator):
        text = self.find_element(locator).getText()
        return text

    def find_element(self, locator, wait=None):
        if wait is None:
            wait = 30
        web_element = WebDriverWait(self.driver, wait).until(EC.presence_of_element_located(locator))
        return web_element

    def check_is_there_element_on_the_page(self, locator):
        try:
            self.find_element(locator)
        except NoSuchElementException:
            return False
        return True
