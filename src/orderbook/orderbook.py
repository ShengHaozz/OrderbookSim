from orderbook_protocol import IOrderBookOrder, IOrder, IOrderBook, IOrderBookSlice, IOrderBookView, OrderStatus, OrderTypeEnum

from dataclasses import dataclass
from uuid import UUID

@dataclass
class OrderBookOrder(IOrderBook):   
    order_type: OrderTypeEnum
    order_qty: int
    order_owner: UUID

    def fill_order(self, order: IOrder) -> 'OrderBookOrder':
        pass

class OrderBookSlice(IOrderBookSlice):

    def __init__(self):
        self._orders: list[IOrderBookOrder] = list()
    
    def fill_order(self, order: IOrder) -> 'OrderBookSlice':
        pass
        
    def remove_order(self, order_owner: UUID) -> 'OrderBookSlice':
        pass
    
    def add_orderbook_order(self, orderbook_order: IOrderBookOrder) -> 'OrderBookSlice':
        pass


class OrderBook(IOrderBook):
    
    def __init__(self):
        self._open_orders: list[IOrderBookSlice] = list()
    
    def process_order(self, order: IOrder) -> 'OrderStatus':
        pass

    def get_bid(self) -> 'OrderBookSlice':
        pass
    
    def get_ask(self) -> 'OrderBookSlice':
        pass
    
    def get_orderbook(self) -> 'OrderBookView':
        pass
    

class OrderBookView(IOrderBookView):
    pass