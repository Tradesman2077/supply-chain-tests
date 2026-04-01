from typing import Protocol
from context import AppContext
from models import Buyer


class SupplyChainContext(AppContext, Protocol):
    inventory_item_id: int
    buyer: Buyer
    buyer_id: int
    selected_item_name: str
    selected_item_price: str
