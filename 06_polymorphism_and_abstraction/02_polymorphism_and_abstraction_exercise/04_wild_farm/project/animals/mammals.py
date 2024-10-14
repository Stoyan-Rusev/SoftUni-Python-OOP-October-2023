from project.animals.animal import Mammal
from project.food import Fruit, Vegetable, Meat


class Mouse(Mammal):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)
        self.sound = "Squeak"
        self.foods = [Vegetable, Fruit]
        self.gain_weight = 0.10


class Dog(Mammal):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)
        self.sound = "Woof!"
        self.foods = [Meat]
        self.gain_weight = 0.40


class Cat(Mammal):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)
        self.sound = "Meow"
        self.foods = [Vegetable, Meat]
        self.gain_weight = 0.30


class Tiger(Mammal):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)
        self.sound = "ROAR!!!"
        self.foods = [Meat]
        self.gain_weight = 1.00
