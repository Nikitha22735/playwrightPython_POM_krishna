from playwright.sync_api import Page, expect
# Page, Context, Playwright, Browser

def test_validateHomeUI(page: Page, navigation):
    expect(page.get_by_role("link", name="Amazon.in")).to_be_visible()
    expect(page.get_by_role("link", name="Hello, sign in Account & Lists")).to_be_visible()
    expect(page.get_by_role("link", name="items in cart")).to_be_visible()
    expect(page.get_by_role("searchbox", name="Search Amazon.in")).to_be_visible()