from typing import Protocol
from abc import abstractmethod

from order.iorder import IOrder

class IOrderBook(Protocol):
    def __init__(self):
        raise NotImplementedError
    
    @abstractmethod
    def process_order(self, IOrder):
        raise NotImplementedError
    

