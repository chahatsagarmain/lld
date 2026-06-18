from payment_strategy import PaymentStrategy

class DebitCardPayment(PaymentStrategy):
    """
    Concrete Strategy for Debit Card payments.
    Implements the payment processing via debit card.
    """

    def process_strategy(self, sender, reciever, amount):
        """Process the transaction via debit card."""
        print(f"process {amount} from {sender} to {reciever} via debit card")