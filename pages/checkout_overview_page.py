from playwright.async_api import Page


class CheckoutOverviewPage:
    def __init__(self, page: Page):
        self.page = page
        self.item_name = self.page.get_by_test_id("inventory-item-name")
        self.finish_button = self.page.get_by_test_id("finish")

    async def verify_items_and_confirm(self, item_name: str, item_price: str):
        await self.item_name.filter(has_text=item_name).wait_for(state="visible")
        await self.page.get_by_test_id("inventory-item-price").filter(has_text=item_price).wait_for(state="visible")
        await self.finish_button.click()
