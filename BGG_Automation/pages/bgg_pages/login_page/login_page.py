import allure
from BGG_Automation.base.base_driver import Page
from BGG_Automation.pages.bgg_pages.login_page.login_enum import LoginEnum
from BGG_Automation.pages.bgg_pages.login_page.login_locators import LoginLocators as Locs


class LoginPage(Page):
    @allure.step('Login')
    def fill_and_go_next(self, username=LoginEnum.USERNAME, password=LoginEnum.PASSWORD):
        self.open_login_window()
        self.login(username, password)

    def open_login_window(self):
        self.wait_until_element_clickable(Locs.SIGN_IN_INITIALIZE_BUTTON)

    def login(self, username, password):
        self.send_keys(Locs.USERNAME_INPUT, username)
        self.send_keys(Locs.PASSWORD_INPUT, password)
        self.wait_until_element_clickable(Locs.SIGN_IN_FINISH_BUTTON)
