from abc import ABC, abstractmethod

class Order(ABC):
    """
    Abstract Command Interface.
    Declares the interface for executing an order/command.
    """

    @abstractmethod
    def execute_order(self):
        """Execute the target command action."""
        pass