import allure
import softest
from BGG_Automation.tests.common_path.common_path_bgg import CommonPathBgg
import pytest


class TestBgg(softest.TestCase):
    @allure.epic("test_browse_menu")
    @pytest.mark.usefixtures("setup")
    def test_bgg(self):
        CommonPathBgg(self.driver).test_browse_menu()

    def __driver_mark(self, driver):  # Does nothing and do not touch
        self.driver = driver
