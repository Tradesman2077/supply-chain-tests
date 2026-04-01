import asyncio
from typing import Protocol
from playwright.async_api import Browser, BrowserContext, Page, Playwright
from behave.model import Table
from pages import LoginPage
from pages import HomePage
from pages import CartPage
from pages import CheckoutPage
from pages import CheckoutOverviewPage
from pages import OrderConfirmationPage


class AppContext(Protocol):
    loop: asyncio.AbstractEventLoop
    playwright_instance: Playwright
    browser: Browser
    browser_context: BrowserContext
    page: Page
    home_page: HomePage
    login_page: LoginPage
    cart_page: CartPage
    checkout_page: CheckoutPage
    checkout_overview_page: CheckoutOverviewPage
    order_confirmation_page: OrderConfirmationPage
    scenario_name: str
    table: Table