from playwright.sync_api import Page, expect
import pytest

from pages.home import homePage
from pages.results import resultsPage

@pytest.mark.regression
def test_resultsUI(page: Page, navigation):
    homePageObj = homePage(page)
    resultsPageObj = resultsPage(page)
    homePageObj.enterproduct()
    homePageObj.clickOnSearchBtn()
    resultsPageObj.valdiateTheVisibilityOfresultstext()
    resultsPageObj.valdiateTheVisibilityOffreeDeliverytext()
    