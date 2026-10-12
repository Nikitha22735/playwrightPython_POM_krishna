from playwright.sync_api import Page
import pytest

from pages.home import homePage


@pytest.mark.regression
def test_validateHomeUI(page: Page, navigation):
    homePageObj = homePage(page)
    homePageObj.validateAmazonLogoVisibility()
    homePageObj.validateAccountAndListsVisibility()
    homePageObj.validateCartLinkVisibility()
    homePageObj.validateSearchBarVisibility()