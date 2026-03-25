from typing import Protocol
from abc import abstractmethod

from src.order.order_protocol import IOrder

class IOrderBook(Protocol):
    
    
    @abstractmethod
    def process_order(self, IOrder):
        raise NotImplementedError


