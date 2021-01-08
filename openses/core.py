from abc import ABC, abstractmethod

# TODO: Finalize parameters for abstract methods send_orders() and update_hub()


class Strategy(ABC):
    @abstractmethod
    def retrieve_data():
        """Retrieve data from OpenSES hub that will be used by strategy"""
        pass

    @abstractmethod
    def send_orders():
        """After iterating through data, send orders back to OpenSES hub"""
        pass


class PipelineScript(ABC):
    @abstractmethod
    def retrieve_data():
        """Retrieve the initial source of data that the pipeline function will modify (if necessary)"""
        pass

    @abstractmethod
    def update_hub():
        """Update the hub's data store after retrieving and/or processing data."""
        pass
