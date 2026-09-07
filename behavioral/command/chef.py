class Chef:
    """
    The Receiver.
    Knows how to perform the actual business logic/operations associated with 
    carrying out a request (cooking specific dishes).
    """

    def __init__(self):
        pass

    def cook_pizza(self):
        """Perform action to cook a pizza."""
        print(f"chef cooked a pizza")

    def cook_burger(self):
        """Perform action to cook a burger."""
        print(f"chef cooked a burger")