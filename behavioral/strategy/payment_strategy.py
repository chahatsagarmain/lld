from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    """
    Abstract Strategy Interface.
    Declares the interface for executing a payment algorithm.
    """

    @abstractmethod
    def process_strategy(self, sender, reciever, amound):
        """Execute the payment transaction strategy."""
        pass