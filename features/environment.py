import asyncio
from playwright.async_api import async_playwright
from context import AppContext
from pages.checkout_page import CheckoutPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.order_confirmation_page import OrderConfirmationPage
from components.inventory_component import InventoryComponent


def init_pages(context: AppContext):
    context.home_page = HomePage(context.page, InventoryComponent(context.page))
    context.login_page = LoginPage(context.page)
    context.cart_page = CartPage(context.page)
    context.checkout_page = CheckoutPage(context.page)
    context.checkout_overview_page = CheckoutOverviewPage(context.page)
    context.order_confirmation_page = OrderConfirmationPage(context.page)

def before_all(context):
    context.loop = asyncio.new_event_loop()
    asyncio.set_event_loop(context.loop)

def before_scenario(context: AppContext, scenario):
    async def setup():
        context.playwright_instance = await async_playwright().start()
        context.playwright_instance.selectors.set_test_id_attribute("data-test")
        context.browser = await context.playwright_instance.chromium.launch(headless=False, slow_mo=200)
        context.browser_context = await context.browser.new_context()
        await context.browser_context.tracing.start(screenshots=True, snapshots=True, sources=True)
        context.page = await context.browser_context.new_page()

        init_pages(context)

        context.scenario_name = scenario.name

    context.loop.run_until_complete(setup())

def after_scenario(context, _scenario):
    async def teardown():
        trace_name = context.scenario_name.replace(" ", "_")
        await context.browser_context.tracing.stop(path=f"test-results/trace_{trace_name}.zip")
        await context.browser_context.close()
        await context.browser.close()
        await context.playwright_instance.stop()

    context.loop.run_until_complete(teardown())

def after_all(context):
    context.loop.close()