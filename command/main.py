"""
Command Pattern Explanation
===========================
The Command Pattern is a behavioral design pattern that turns a request into a stand-alone 
object containing all information about the request. This transformation lets you parameterize 
methods with different requests, queue or log requests, and support undoable operations.

Pattern Participants:
--------------------
1. **Command** (Order): Declares an interface for executing an operation.
2. **Concrete Command** (OrderPizza, OrderBurger): Defines a binding between a Receiver object 
   and an action. Implements execute_order() by invoking the corresponding operation(s) on the Receiver.
3. **Receiver** (Chef): Knows how to perform the operations associated with carrying out a request.
4. **Invoker** (Waiter): Asks the command to carry out the request.
5. **Client** (main.py): Creates a Concrete Command object and sets its Receiver.

Why Decouple?
-------------
Without this pattern, the Waiter would need direct knowledge of the Chef's methods (e.g. chef.cook_pizza()). 
If the Chef learned to cook a new dish, the Waiter class would have to be modified to support it, leading 
to tight coupling. 

With the Command Pattern, the Waiter only depends on the abstract `Order` interface. If the Chef learns 
a new recipe, we only need to write a new subclass of `Order`. The Waiter remains unchanged, adhering 
to the Open-Closed Principle.
"""

from waiter import Waiter 
from chef import Chef
from order_pizza import OrderPizza
from order_burger import OrderBurger

if __name__ == "__main__":
    w = Waiter()
    c = Chef()
    op = OrderPizza(c)
    pb = OrderBurger(c)
    w.take_order(op)
    w.take_order(pb)