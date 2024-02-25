from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from BGG_Automation.utils.locator_builder.locator_builder import Locator


class Page:
    def __init__(self, driver):
        self.__driver = driverdadadada

    def send_keys(self, locator: Locator, value):
        self.__driver.find_element(locator.by, locator.value).send_keys(value)

    def click(self, locator: Locator):
        self.__driver.find_element(locator.by, locator.value).click()

    def submit(self, locator: Locator):
        self.__driver.find_element(locator.by, locator.value).submit()

    def refresh(self):
        self.__driver.refresh()

    def open_new_tab(self):
        self.__driver.execute_script("window.open('');")

    def find_element(self, locator: Locator):
        return self.__driver.find_element(locator.by, locator.value)

    def find_multiple_elements(self, locator: Locator):
        return self.__driver.find_elements(locator.by, locator.value)

    def quit(self):
        self.__driver.quit()

    def wait_until_element_clickable(self, locator: Locator, time=30):
        wait = WebDriverWait(self.__driver, time)
        element = wait.until(ec.element_to_be_clickable(locator))
        element.click()

    def wait_until_element_located(self, locator: Locator, time=30):
        wait = WebDriverWait(self.__driver, time)
        element = wait.until(ec.presence_of_element_located(locator))
        return element
    #test

    def get_texts(self, locator: Locator) -> str:
        elements = self.__driver.find_elements(locator.by, locator.value)
        texts = [element.text for element in elements]
        joined_texts = ' '.join(texts)
        return joined_texts

    def get_texts2(self, locator: Locator):
        elements = self.__driver.find_elements(locator.by, locator.value)
        texts = [element.text for element in elements]
        joined_texts = ' '.join(texts)
        return texts

    def get_link(self, locator: Locator) -> str:
        return self.__driver.find_element(locator.by, locator.value).get_attribute("href")
