from order import Order
from chef import Chef

class OrderBurger(Order):
    """
    Concrete Command for ordering a burger.
    Encapsulates the action of cooking a burger by delegation to the Chef.
    """

    def __init__(self, chef: Chef):
        self._chef = chef

    def execute_order(self):
        """Execute the order by delegating to the Chef's cook_burger method."""
        self._chef.cook_burger()

        