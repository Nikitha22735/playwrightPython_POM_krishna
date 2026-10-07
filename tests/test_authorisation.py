import os

import pytest
from playwright.sync_api import Page

from pages.authorisation import authorisationPage


def test_authorisation_success(page: Page, navigation: None) -> None:
    email = "trainingplaywright@gmail.com"
    password = "Welcome@04"
   

    authorisation_page = authorisationPage(page)
    authorisation_page.openSignIn()
    authorisation_page.continueWithEmail(email)
    authorisation_page.submitPassword(password)
    authorisation_page.validateSignedIn()


def test_authorisation_rejects_empty_email(page: Page, navigation: None) -> None:
    authorisation_page = authorisationPage(page)
    authorisation_page.openSignIn()
    authorisation_page.continueButton.click()
    authorisation_page.validateEmailRequiredError()


def test_authorisation_rejects_empty_password(
    page: Page, navigation: None
) -> None:
    email = os.getenv("AMAZON_EMAIL")
    if not email:
        pytest.skip(
            "Set AMAZON_EMAIL to run the empty-password validation test."
        )

    authorisation_page = authorisationPage(page)
    authorisation_page.openSignIn()
    authorisation_page.continueWithEmail(email)
    authorisation_page.signInButton.click()
    authorisation_page.validatePasswordRequiredError()
