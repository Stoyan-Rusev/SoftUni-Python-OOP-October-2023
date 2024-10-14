from project.dough import Dough
from typing import Dict
from project.topping import Topping


class Pizza:
    def __init__(self, name: str, dough: Dough, max_number_of_toppings: int):
        self.name = name
        self.dough = dough
        self.max_number_of_toppings = max_number_of_toppings
        self.toppings: Dict[Topping.topping_type: Topping.weight] = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name == "":
            raise ValueError("The name cannot be an empty string")
        self.__name = name

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, dough):
        if not dough:
            raise ValueError("You should add dough to the pizza")
        self.__dough = dough

    @property
    def max_number_of_toppings(self):
        return self.__max_number_of_toppings

    @max_number_of_toppings.setter
    def max_number_of_toppings(self, max_number_of_toppings):
        if max_number_of_toppings <= 0 :
            raise ValueError("The maximum number of toppings cannot be less or equal to zero")
        self.__max_number_of_toppings = max_number_of_toppings

    def add_topping(self, topping: Topping):
        if len(self.toppings) == self.max_number_of_toppings:
            raise ValueError("Not enough space for another topping")

        _type = topping.topping_type
        quantity = topping.weight
        if _type not in self.toppings.keys():
            self.toppings[_type] = quantity
        else:
            self.toppings[_type] += quantity

    def calculate_total_weight(self):
        toppings_weight = sum(topping for topping in self.toppings.values())
        total_weight = self.dough.weight + toppings_weight
        return total_weight
