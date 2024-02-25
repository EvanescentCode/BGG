from pytest import fixture
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from BGG_Automation.tests.common_path.common_path_bgg import CommonPathBgg
import time


class TestBgg:

    @fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('https://boardgamegeek.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        yield
        time.sleep(5)
        self.driver.quit()

    def test_bgg(self):
        CommonPathBgg(self.driver).test_browse_menu()
