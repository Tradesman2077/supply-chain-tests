from playwright.async_api import Page
from config import UI_BASE_URL, STOREFRONT_TEST_USERNAME, STOREFRONT_TEST_PASSWORD


class LoginPage:
    def __init__(self, page : Page):
        self.page = page
        self.username_input = self.page.get_by_role("textbox", name="Username")
        self.password_input = self.page.get_by_placeholder("Password")
        self.login_button = self.page.get_by_role("button", name="Login")

    async def navigate(self):
        await self.page.goto(UI_BASE_URL)

    async def login(self):
        await self.username_input.fill(STOREFRONT_TEST_USERNAME)
        await self.password_input.fill(STOREFRONT_TEST_PASSWORD)
        await self.login_button.click()