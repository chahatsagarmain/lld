from payment_strategy import PaymentStrategy

class CreditCardPayment(PaymentStrategy):
    """
    Concrete Strategy for Credit Card payments.
    Implements the payment processing via credit card.
    """

    def process_strategy(self, sender, reciever, amount):
        """Process the transaction via credit card."""
        print(f"sending {amount} from {sender} to {reciever} via card")