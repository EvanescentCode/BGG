from selenium.webdriver.common.by import By
from typing import NamedTuple


class Locator(NamedTuple):
    by: str
    value: str


class LocatorBuilder:

    @staticmethod
    def id(value) -> Locator:
        return Locator(By.ID, value)

    @staticmethod
    def name(value) -> Locator:
        return Locator(By.NAME, value)

    @staticmethod
    def css(value) -> Locator:
        return Locator(By.CSS_SELECTOR, value)

    @staticmethod
    def xpath(value) -> Locator:
        return Locator(By.XPATH, value)

    @staticmethod
    def link_text(value) -> Locator:
        return Locator(By.LINK_TEXT, value)

    @staticmethod
    def partial_link_text(value) -> Locator:
        return Locator(By.PARTIAL_LINK_TEXT, value)

    @staticmethod
    def tag_name(value) -> Locator:
        return Locator(By.TAG_NAME, value)

    @staticmethod
    def class_name(value) -> Locator:
        return Locator(By.CLASS_NAME, value)
