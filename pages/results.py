from playwright.sync_api import Page, expect
class resultsPage:
    def __init__(self, page):
        self.resultsText = page.get_by_role("heading", name="Results", exact=True)
        self.freeDeliverytext = page.get_by_text("Eligible for Free Delivery")

    def valdiateTheVisibilityOfresultstext(self):
        expect(self.resultsText).to_be_visible()

    def valdiateTheVisibilityOffreeDeliverytext(self):
        expect( self.freeDeliverytext).to_be_visible()