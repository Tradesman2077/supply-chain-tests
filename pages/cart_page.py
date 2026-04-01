from playwright.async_api import Page


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.item_name = self.page.get_by_test_id("inventory-item-name")
        self.checkout_button = self.page.get_by_test_id("checkout")

    async def verify_item_in_summary(self, item_name: str, item_price: str):
        await self.item_name.filter(has_text=item_name).wait_for(state="visible")
        await self.page.get_by_test_id("inventory-item-price").filter(has_text=item_price).wait_for(state="visible")

    async def select_checkout(self):
        await self.checkout_button.click()
