from BGG_Automation.base.base_driver import Page
from BGG_Automation.pages.bgg_pages.common_pages.common_locators import CommonPageLocators as Locs


class CommonPage(Page):

    def fill_and_go_next(self):
        self.accept_cookies()
        self.browse_dropdown()
        self.all_boardgames_button()
        # self.privacy_accept()

    def browse_dropdown(self):
        self.wait_until_element_clickable(Locs.BROWSE_DROPDOWN)

    def all_boardgames_button(self):
        self.wait_until_element_clickable(Locs.ALL_BOARDGAMES_BUTTON)

    def accept_cookies(self):
        self.wait_until_element_clickable(Locs.COOKIES_ACCEPT)

    def privacy_accept(self):
        self.wait_until_element_clickable(Locs.PRIVACY_ACCEPT)
