from playwright.async_api import Page


class OrderConfirmationPage:
    def __init__(self, page: Page):
        self.page = page
        self.confirmation_header = self.page.get_by_test_id("complete-header")
        self.back_home_button = self.page.get_by_test_id("back-to-products")

    async def verify_confirmed(self):
        await self.confirmation_header.wait_for(state="visible")
        assert await self.confirmation_header.inner_text() == "Thank you for your order!"
