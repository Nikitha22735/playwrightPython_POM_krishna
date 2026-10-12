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
    report = outcome.get_result()

    if report.failed:
        page = item.funcargs.get("page")
        # page.screenshot()
        if page:
            allure.attach(page.screenshot(), 
                          name="failedpage", 
                          attachment_type=allure.attachment_type.PNG)