import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store_true", default="chrome", help="browser selection"
    )


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--guest")   # Add this option to avoid  " Change your password notification in the Google "


@pytest.fixture(scope="function")
def browser_instance(request):
    browser_name = request.config.getoption("--browser_name")
    if browser_name  == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    elif browser_name == "edge":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    yield driver
    driver.close()


