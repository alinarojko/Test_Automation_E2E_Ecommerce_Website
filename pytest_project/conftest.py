import os
import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
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
    wait = WebDriverWait(driver, 5)
    yield driver


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    outcome = yield
    report = outcome.get_result()

    if report.when == 'call':
        feature_request = item.funcargs['request']
        driver = feature_request.getfixturevalue('browser_instance')  # must match fixture name

        screenshot_dir = os.path.join("tests", "reports")
        os.makedirs(screenshot_dir, exist_ok=True)

        # Save screenshot
        screenshot_filename = f"{timestamp}.png"
        screenshot_path = os.path.join(screenshot_dir, screenshot_filename)
        driver.save_screenshot(screenshot_path)

        # Compute relative path from HTML file (assumed saved in same 'reports' dir)
        relative_path = screenshot_filename

        # Add to report
        extra = getattr(report, 'extra', [])
        pytest_html = item.config.pluginmanager.getplugin('html')
        extra.append(pytest_html.extras.image(relative_path))
        extra.append(pytest_html.extras.url('http://www.example.com/'))

        if report.failed and not hasattr(report, 'wasxfail'):
            extra.append(pytest_html.extras.html('<div>Test failed. Screenshot attached.</div>'))

        report.extra = extra
