Feature: Storefront Orders

	As a supply chain operator
	I want to create an item / buyer account in the inventory system
	So that I can process an order in the storefront

	# Data handover: inventory_item_id and buyer_id are returned from the API and
	# combined as the postal code ({buyer_id}_{inventory_item_id}) during checkout.
	# The buyer's first and last name from the API response populate the checkout form.
	# No UI step uses hardcoded values — all data originates from API responses.
	Scenario: Place storefront order using inventory system data
		Given an item is created in the inventory system with the following details
			| name             | status    |
			| ladys blue jeans | available |
		And a buyer account is created in the inventory system with the following details
			| username     | firstName   | lastName |
			| chris1231989 | christopher | wright   |
		And I login to the storefront
		When I add item 1 from the inventory system to my cart
		And I retrieve the buyer account details from the inventory system
		And I select the check out button on the home page
		Then I should see the selected product in my order summary with the correct name and price
		When I select the checkout button on the cart page
		And I input the buyer account details and confirm the order
		Then the order details should be correct on the checkout overview page
		And the order should be confirmed on the confirmation page