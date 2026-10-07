from playwright.sync_api import Page, expect


class authorisationPage:
    def __init__(self, page: Page) -> None:
        self.signInLink = page.get_by_role(
            "link", name="Hello, sign in Account & Lists"
        )
        self.emailInput = page.get_by_role(
            "textbox", name="Enter mobile number or email"
        )
        self.continueButton = page.get_by_role("button", name="Continue")
        self.passwordInput = page.get_by_role("textbox", name="Password")
        self.signInButton = page.get_by_role("button", name="Sign in")
        self.searchBox = page.get_by_role("searchbox", name="Search Amazon.in")
        self.accountGreeting = page.locator("#nav-link-accountList-nav-line-1")
        self.emailRequiredError = page.get_by_role("alert").filter(
            has_text="Enter your mobile number or email"
        )
        self.passwordRequiredError = page.locator("#auth-password-missing-alert")

    def openSignIn(self) -> None:
        self.signInLink.click()

    def continueWithEmail(self, email: str) -> None:
        self.emailInput.fill(email)
        self.continueButton.click()

    def submitPassword(self, password: str) -> None:
        self.passwordInput.fill(password)
        self.signInButton.click()

    def validateSignedIn(self) -> None:
        expect(self.searchBox).to_be_visible()
        expect(self.accountGreeting).to_be_visible()
        expect(self.accountGreeting).not_to_have_text("Hello, sign in")

    def validateEmailRequiredError(self) -> None:
        expect(self.emailRequiredError).to_be_visible()

    def validatePasswordRequiredError(self) -> None:
        expect(self.passwordRequiredError).to_be_visible()
