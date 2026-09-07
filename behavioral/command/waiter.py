from order import Order

class Waiter:
    """
    The Invoker.
    Responsible for initiating command execution. It triggers the command by 
    calling execute_order() without knowing details about the concrete request.
    """

    def __init__(self):
        pass

    def take_order(self, order: Order):
        """Take an order and trigger its execution."""
        order.execute_order()