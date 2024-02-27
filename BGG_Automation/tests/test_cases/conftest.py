import allure
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import time


@allure.title('setup')
@pytest.fixture(autouse=True)
def setup(request):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get('https://boardgamegeek.com/')
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.quit()


def pytest_exception_interact(node, call, report):
    if report.failed:
        if hasattr(node.instance, "driver"):
            driver = node.instance.driver
            take_screenshot_allure(driver, node.nodeid)


def take_screenshot_allure(driver, name):
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    file_name = f"./BGG_Automation/reports/screenshot_{timestamp}.png"
    driver.save_screenshot(file_name)
    allure.attach.file(file_name, name=f"Screenshot on Failure: {name}", attachment_type=allure.attachment_type.PNG)