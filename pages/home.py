class homePage:
    def __init__(self, page):
        self.searchBar = page.get_by_role("searchbox", name="Search Amazon.in")
        self.searchBtn = page.locator('#nav-search-submit-button')


    def enterproduct(self):
        self.searchBar.fill("iphone")

    def clickOnSearchBtn(self):
        self.searchBtn.click()