from abc import ABC, abstractmethod
from typing import Any, NamedTuple, List
from datetime import datetime


class Order(NamedTuple):
    datetime: datetime
    purchase_price: float
    quantity: int
    symbol: str
    order_type: int


class TimeSeriesData(NamedTuple):
    timestamp: datetime
    data_type: str
    data: Any


class PriceData(NamedTuple):
    open: float
    high: float
    low: float
    volume: int
    close: float


DATE_TYPE_MAPPING = {
    PriceData.__name__: PriceData
}


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
