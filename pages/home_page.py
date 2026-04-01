from playwright.async_api import Page
from config import UI_BASE_URL
from components.inventory_component import InventoryComponent


class HomePage:
    def __init__(self, page: Page, inventory_component: InventoryComponent):
        self.page = page
        self.inventory_component = inventory_component

    async def navigate(self):
        await self.page.goto(UI_BASE_URL)

    async def add_inventory_item_to_cart(self, menu_item: int) -> tuple[str, str]:
        name, price = await self.inventory_component.add_item_to_cart(menu_item)
        await self.page.get_by_test_id("shopping-cart-link").get_by_test_id("shopping-cart-badge").wait_for(state="visible")
        return name, price

    async def select_checkout(self):
        await self.page.get_by_test_id("shopping-cart-link").click()
        