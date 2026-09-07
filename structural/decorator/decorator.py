# decorator pattern is strucutural pattern to extend behavior of a concerte implementation 
# usually to extend the behaviour you would use inheritence but for small extensions this can get quite messy 
# you need to come up with names , extend the functionaltiy , check the implementations and you end you creating a long chain of inhereince 

# imagine you have coffee class , you need coffee with milk and you would end up creating a new class 
# for coffee with sugar another class 
# for coffee with milk and sugar another class 

# hence we create a decorator , which is used to create deocrators which extend functioanlities of the original coffee class 

from abc import ABC , abstractmethod

class Beverage(ABC):

    @abstractmethod
    def get_description(self):
        pass 

    @abstractmethod 
    def get_price(self):
        pass 

class Coffee(Beverage):

    def get_description(self):
        return "coffe it is"

    def get_price(self):
        return int(100)

# the decorator has to implement the orignal interface but with a change

class CoffeeDecorator(Beverage):

    def __init__(self , coffee : Coffee):
        # it needs a coffee to decorate 
        self.coffee = coffee

    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_price(self):
        pass 

class MilkDecorator(CoffeeDecorator):

    def get_description(self):
        return f"{self.coffee.get_description()}  , Milk "

    def get_price(self):
        return int(self.coffee.get_price() + 20)

class SugarDecorator(CoffeeDecorator):

    def get_description(self):
        return f"{self.coffee.get_description()} , Sugar"

    def get_price(self):
        return int(self.coffee.get_price() + 5)

def main():
    coffee = Coffee()
    print(coffee.get_description())
    print(coffee.get_price())
    coffee_with_milk = MilkDecorator(coffee)
    print(coffee_with_milk.get_description())
    print(coffee_with_milk.get_price())
    coffee_with_sugar = SugarDecorator(coffee)
    print(coffee_with_sugar.get_description())
    print(coffee_with_sugar.get_price())
    coffee_with_milk_and_sugar = SugarDecorator(coffee_with_milk)
    print(coffee_with_milk_and_sugar.get_description())
    print(coffee_with_milk_and_sugar.get_price())

if __name__ == "__main__":
    main()