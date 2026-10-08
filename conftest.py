import allure
from playwright.sync_api import sync_playwright
import pytest

@pytest.fixture()
def navigation(page):
     page.goto("https://www.amazon.in/")
# @pytest.fixture()
# def page():
#     with sync_playwright() as p:
#             browser = p.chromium.launch(headless=False)
#             context = browser.new_context()
#             page = context.new_page()
#             yield page


# @pytest.fixture()
# def context():
#     with sync_playwright() as p:
#             browser = p.chromium.launch(headless=False)
#             context = browser.new_context()
#             yield context


# @pytest.fixture()
# def browser():
#     with sync_playwright() as p:
#             browser = p.chromium.launch(headless=False)
#             yield browser

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    status = outcome.get_result()
    if status.failed:
        page = item.funcargs['page']
        screenshot_path = f"screenshots/{item.name}.png"
        page.screenshot(path=screenshot_path)  
        allure.attach.file(screenshot_path, name="screenshot", attachment_type=allure.attachment_type.PNG)    
