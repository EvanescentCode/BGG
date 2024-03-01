from BGG_Automation.pages.bgg_pages.all_boardgames_page.all_boardgames_page import AllBoardsPage
from BGG_Automation.pages.bgg_pages.common_pages.common_page import CommonPage
from BGG_Automation.pages.bgg_pages.login_page.login_page import LoginPage


class CommonPathBgg:
    def __init__(self, driver):
        self.driver = driver
        self.login = LoginPage(driver)
        self.browse_menu = CommonPage(driver)
        self.all_boardgames = AllBoardsPage(driver)

    def test_browse_menu(self):
        self.browse_menu.accept_cookies()
        self.login.fill_and_go_next()
        self.browse_menu.fill_and_go_next()
        self.all_boardgames.fill_and_go_next()
