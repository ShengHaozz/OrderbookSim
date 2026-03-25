from order_protocol import IOrder, IOrderFactory
from src.util import OrderTypeEnum

from dataclasses import dataclass
from uuid import UUID

@dataclass(frozen = True)
class Order(IOrder):
    order_type: OrderTypeEnum
    order_qty: int
    order_owner: UUID

@dataclass
class OrderFactory(IOrderFactory):
    order_owner: UUID

    def make_buy_order(self, qty: int):
        return Order(OrderTypeEnum.BUY, qty, self.order_owner)
    
    def make_sell_order(self, qty):
        return Order(OrderTypeEnum.SELL, qty, self.order_owner)