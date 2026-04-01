from playwright.async_api import Page


class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.first_name_input = self.page.get_by_test_id("firstName")
        self.last_name_input = self.page.get_by_test_id("lastName")
        self.postal_code_input = self.page.get_by_test_id("postalCode")
        self.continue_button = self.page.get_by_test_id("continue")

    async def input_buyer_details(self, first_name: str, last_name: str, buyer_id: int, inventory_item_id: int):
        postal_code = f"{buyer_id}_{inventory_item_id}"
        await self.first_name_input.fill(first_name)
        await self.last_name_input.fill(last_name)
        await self.postal_code_input.fill(postal_code)
        await self.continue_button.click()
