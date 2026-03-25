from typing import Protocol
from abc import abstractmethod

from src.util import OrderTypeEnum
from uuid import UUID

class IOrder(Protocol):
    order_type: OrderTypeEnum
    order_qty: int
    order_owner: UUID


class IOrderFactory(Protocol):
    order_owner: UUID

    @abstractmethod
    def make_buy_order(self, qty: int) -> 'IOrder':
        raise NotImplementedError

    @abstractmethod
    def make_sell_order(self, qty: int) -> 'IOrder':
        raise NotImplementedError