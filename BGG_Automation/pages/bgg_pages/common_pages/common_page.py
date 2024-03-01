import allure
from selenium.common import WebDriverException

from BGG_Automation.base.base_driver import Page
from BGG_Automation.pages.bgg_pages.common_pages.common_locators import CommonPageLocators as Locs
import time


class CommonPage(Page):
    @allure.step('Common')
    def fill_and_go_next(self):
        self.browse_dropdown()
        self.all_boardgames_button()

    def browse_dropdown(self):
        try:
            self.wait_until_element_clickable(Locs.BROWSE_DROPDOWN)
        except Exception as e:
            time.sleep(2)
            self.wait_until_element_clickable(Locs.BROWSE_DROPDOWN)

    def all_boardgames_button(self):
        self.wait_until_element_clickable(Locs.ALL_BOARDGAMES_BUTTON)

    def accept_cookies(self):
        self.wait_until_element_clickable(Locs.COOKIES_ACCEPT)

    def privacy_accept(self):
        self.wait_until_element_clickable(Locs.PRIVACY_ACCEPT)
