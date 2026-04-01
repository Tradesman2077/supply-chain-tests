from behave import given, when, then
from config import API_BASE_URL
from context import SupplyChainContext
from models import Buyer
from utils import get_with_retry, post_with_retry


@given('an item is created in the inventory system with the following details')
def step_create_inventory_item(context: SupplyChainContext):
    row = dict(zip(context.table.headings, context.table[0]))
    response = post_with_retry(f"{API_BASE_URL}/pet", json=row)
    context.inventory_item_id = response.json()["id"]

@given('a buyer account is created in the inventory system with the following details')
def step_create_buyer_account(context: SupplyChainContext):
    row = dict(zip(context.table.headings, context.table[0]))
    post_with_retry(f"{API_BASE_URL}/user", json=row)
    context.buyer = Buyer(**row)

@given('I login to the storefront')
def step_navigate_login_page(context: SupplyChainContext):
    context.loop.run_until_complete(context.login_page.navigate())
    context.loop.run_until_complete(context.login_page.login())

@when('I add item {item_index:d} from the inventory system to my cart')
def step_add_item_to_cart(context: SupplyChainContext, item_index: int):
    (context.selected_item_name, context.selected_item_price) = context.loop.run_until_complete(context.home_page.add_inventory_item_to_cart(item_index))

@when('I retrieve the buyer account details from the inventory system')
def step_retrieve_buyer_details(context: SupplyChainContext):
    response = get_with_retry(f"{API_BASE_URL}/user/{context.buyer.username}")
    context.buyer_id = response.json()['id']

@when('I select the check out button on the home page')
def step_checkout(context: SupplyChainContext):
    context.loop.run_until_complete(context.home_page.select_checkout())

@when('I select the checkout button on the cart page')
def step_select_checkout_on_cart(context: SupplyChainContext):
    context.loop.run_until_complete(context.cart_page.select_checkout())

@when('I input the buyer account details and confirm the order')
def step_confirm_order(context: SupplyChainContext):
    context.loop.run_until_complete(context.checkout_page.input_buyer_details(
        context.buyer.firstName,
        context.buyer.lastName,
        context.buyer_id,
        context.inventory_item_id
    ))

@then('the order details should be correct on the checkout overview page')
def step_verify_order_overview(context: SupplyChainContext):
    context.loop.run_until_complete(context.checkout_overview_page.verify_items_and_confirm(
        context.selected_item_name,
        context.selected_item_price
    ))

@then('I should see the selected product in my order summary with the correct name and price')
def step_verify_item_in_summary(context: SupplyChainContext):
    context.loop.run_until_complete(context.cart_page.verify_item_in_summary(context.selected_item_name, context.selected_item_price))

@then('the order should be confirmed on the confirmation page')
def step_verify_order_confirmation(context: SupplyChainContext):
    context.loop.run_until_complete(context.order_confirmation_page.verify_confirmed())