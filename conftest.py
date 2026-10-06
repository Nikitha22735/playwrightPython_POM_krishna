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
