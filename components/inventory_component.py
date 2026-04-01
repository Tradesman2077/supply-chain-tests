class InventoryComponent:
    def __init__(self, page):
        self.page = page

    async def add_item_to_cart(self, item_index: int) -> tuple[str, str]:
        item = self.page.get_by_test_id("inventory-item").nth(item_index)
        name = await item.get_by_test_id("inventory-item-name").inner_text()
        price = await item.get_by_test_id("inventory-item-price").inner_text()
        await item.get_by_role("button", name="Add to cart").click()
        await item.get_by_role("button", name="Remove").wait_for(state="visible")
        return name, price
