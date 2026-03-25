from typing import Protocol
from abc import abstractmethod
from uuid import uuid4, UUID
from enum import Enum
from collections.abc import Collection, Sequence

from src.order.order_protocol import IOrder
from src.util import OrderTypeEnum


class IOrderStatus(Enum):
    FILLED = 1
    PARTIALLY_FILLED = 2
    OPEN = 3


class IOrderBookOrder(Protocol):
    """
    Orderbook Order that is attributed to an owner
    """

    order_type: OrderTypeEnum
    order_qty: int # set to int for now
    order_owner: UUID

    @abstractmethod
    def fill_order(self, IOrder) -> 'IOrderBookOrder':
        raise NotImplementedError

class IOrderBookSlice(Protocol):
    """
    Aggregation of IOrderBookOrder at a specific price
    """
    orders: Sequence[IOrderBookOrder]
    # Orders in slice must have some ordering to determine which order to fill first

    @abstractmethod
    def fill_order(self, IOrder) -> 'IOrderBookSlice':
        raise NotImplementedError


class IOrderBook(Protocol):
    open_orders: Collection[IOrderBookSlice]
    
    @abstractmethod
    def process_order(self, IOrder) -> IOrderStatus:
        raise NotImplementedError

    @abstractmethod
    def get_bid(self) -> IOrderBookSlice:
        raise NotImplementedError
    
    @abstractmethod
    def get_ask(self) -> IOrderBookSlice:
        raise NotImplementedError
    

