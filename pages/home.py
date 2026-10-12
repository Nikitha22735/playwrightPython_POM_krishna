import allure
from playwright.sync_api import Page, expect


class homePage:
    @allure.step("__init__")
    def __init__(self, page: Page) -> None:
        self.amazonLogo = page.get_by_role("link", name="Amazon.in")
        self.accountAndLists = page.get_by_role(
            "link", name="Hello, sign in Account & Lists"
        )
        self.cartLink = page.get_by_role("link", name="items in cart")
        self.searchBar = page.get_by_role("searchbox", name="Search Amazon.in")
        self.searchBtn = page.locator('#nav-search-submit-button')

    @allure.step("validateAmazonLogoVisibility")
    def validateAmazonLogoVisibility(self) -> None:
        expect(self.amazonLogo).to_be_visible()

    @allure.step("validateAccountAndListsVisibility")
    def validateAccountAndListsVisibility(self) -> None:
        expect(self.accountAndLists).to_be_visible()

    @allure.step("validateCartLinkVisibility")
    def validateCartLinkVisibility(self) -> None:
        expect(self.cartLink).to_be_visible()

    @allure.step("validateSearchBarVisibility")
    def validateSearchBarVisibility(self) -> None:
        expect(self.searchBar).not_to_be_visible()

    @allure.step("enterproduct")
    def enterproduct(self):
        self.searchBar.fill("iphone")

    @allure.step("clickOnSearchBtn")
    def clickOnSearchBtn(self):
        self.searchBtn.click()