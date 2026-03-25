from typing import Protocol
from abc import abstractmethod
from uuid import uuid4, UUID
from enum import Enum

from src.order.order_protocol import IOrder
from src.util import OrderTypeEnum


class IOrderStatus(Enum):
    FILLED = 1
    PARTIALLY_FILLED = 2
    OPEN = 3


class IOrderBookOrder(Protocol):
    order_type: OrderTypeEnum
    order_qty: int # set to int for now
    order_owner: UUID

    @abstractmethod
    def fill_order(self, IOrder) -> 'IOrderBookOrder':
        raise NotImplementedError


class IOrderBook(Protocol):
    
    
    @abstractmethod
    def process_order(self, IOrder) -> IOrderStatus:
        raise NotImplementedError


