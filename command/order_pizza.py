from order import Order 
from chef import Chef

class OrderPizza(Order):
    """
    Concrete Command for ordering a pizza.
    Encapsulates the action of cooking a pizza by delegation to the Chef.
    """

    def __init__(self, chef: Chef):
        self._chef = chef

    def execute_order(self):
        """Execute the order by delegating to the Chef's cook_pizza method."""
        self._chef.cook_pizza()