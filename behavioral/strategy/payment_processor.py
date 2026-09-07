from payment_strategy import PaymentStrategy

class PaymentProcessor:
    """
    The Context.
    Maintains a reference to a Strategy object and delegates the actual 
    payment execution to the current Strategy interface.
    """
    def __init__(self, sender, receiver, amount):
        self._sender = sender
        self._receiver = receiver
        self._amount = amount

    def process_payement(self, payment_strategy: PaymentStrategy):
        """Execute payment using the passed-in payment strategy."""
        payment_strategy.process_strategy(self._sender, self._receiver, self._amount)


