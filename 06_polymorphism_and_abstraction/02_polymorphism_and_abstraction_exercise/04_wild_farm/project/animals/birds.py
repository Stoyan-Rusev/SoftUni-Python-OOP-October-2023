from project.animals.animal import Bird
from project.food import Food, Meat


class Owl(Bird):
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)
        self.sound = "Hoot Hoot"
        self.foods = [Meat]
        self.gain_weight = 0.25


class Hen(Bird):
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)
        self.sound = "Cluck"
        self.foods = [Food]
        self.gain_weight = 0.35
