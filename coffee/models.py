from abc import ABC, abstractmethod


# Strategy
class Coffee(ABC):

    @abstractmethod
    def add_espresso_shots(self, barista_drink):
        """ Print the number and return """


# Strategy concrete
class Latte(Coffee):

    def add_espresso_shots(self, barista_drink):
        print(f"{barista_drink.customer_name} will get cold brew with 1 shots")
        return 1


# Strategy concrete
class ColdBrew(Coffee):

    def add_espresso_shots(self, barista_drink):
        print(f"{barista_drink.customer_name} will get cold brew with 2 shots")
        return 2


# context
class BaristaDrink:
    def __init__(self, customer_name, coffee=None):
        self.customer_name = customer_name
        self.coffee = coffee

    def prepare(self):
        return self.coffee.add_espresso_shots(self)

    def prepare_with_function(self):
        return self.coffee(self)


def add_espresso_shots_to_latte(barista_drink):
    print(f"{barista_drink.customer_name} will get cold brew with 1 shots")


def add_espresso_shots_to_cold_brew(barista_drink):
    print(f"{barista_drink.customer_name} will get cold brew with 2 shots")
