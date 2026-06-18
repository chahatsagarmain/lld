"""
Strategy Pattern Explanation
============================
The Strategy Design Pattern is a behavioral design pattern that enables selecting an 
algorithm's behavior at runtime. Instead of implementing a single algorithm directly 
inside a class (or using complex conditional logic to choose among several algorithms), 
we define a family of algorithms, encapsulate each one as a separate class (Strategy), 
and make their objects interchangeable.

Problem / Alternative (Before Strategy):
----------------------------------------
Suppose we have a PaymentProcessor that needs to support multiple payment methods 
(e.g., Credit Card, Debit Card, PayPal, UPI). 
If we implement all payment handling directly in the PaymentProcessor class, we end up 
with a process_payment method filled with complex conditional branches:

    def process_payment(self, method_type):
        if method_type == "credit_card":
            # credit card processing logic
        elif method_type == "debit_card":
            # debit card processing logic
        elif method_type == "paypal":
            # paypal processing logic
        # ... and so on

This approach has major drawbacks:
1. Tight Coupling: The PaymentProcessor class depends directly on the implementation details 
   of all payment methods.
2. Code Bloat & Maintenance: The class becomes large and hard to maintain as more payment methods are added.
3. Violation of Open-Closed Principle: Every time a new payment method is introduced, we must 
   modify the existing PaymentProcessor class (specifically adding another `elif` branch), 
   which risks breaking existing working code.

Solution (With Strategy):
-------------------------
We define a common interface (`PaymentStrategy`) containing a unified method (`process_strategy`).
Each payment method is implemented as a standalone class (e.g., `CreditCardPayment`, `DebitCardPayment`) 
conforming to this interface.

The `PaymentProcessor` (called the Context) delegates the execution of the payment algorithm 
to a concrete strategy object passed to it (e.g., via method parameter). 

Benefits:
---------
- Open-Closed Principle: You can introduce new payment strategies without modifying the PaymentProcessor.
- Isolation of Code: The details of each payment algorithm are isolated within its own class.
- Swap at Runtime: The strategy can be swapped dynamically at runtime by passing different strategy objects.
"""

from payment_processor import PaymentProcessor
from credit_card import CreditCardPayment
from debit_card import DebitCardPayment

if __name__ == '__main__':
    p = PaymentProcessor("person1" , "person2" , 100)
    p.process_payement(CreditCardPayment())
    p.process_payement(DebitCardPayment())