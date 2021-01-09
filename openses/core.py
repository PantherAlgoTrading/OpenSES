from abc import ABC, abstractmethod
from typing import NamedTuple, List
from datetime import datetime


class Order(NamedTuple):
    datetime: datetime
    purchase_price: float
    quantity: int
    symbol: str
    order_type: int


class Strategy(ABC):
    @abstractmethod
    def retrieve_data(self):
        """Retrieve data from OpenSES hub that will be used by strategy"""
        pass

    @abstractmethod
    def send_orders(self, orders):
        """After iterating through data, send a List of Order objects back to OpenSES hub"""
        pass


class PipelineScript(ABC):
    @abstractmethod
    def retrieve_data(self):
        """Retrieve the initial source of data that the pipeline function will modify (if necessary)"""
        pass

    @abstractmethod
    def update_hub(self, data):
        """Update the hub's data store after retrieving and/or processing data."""
        pass
