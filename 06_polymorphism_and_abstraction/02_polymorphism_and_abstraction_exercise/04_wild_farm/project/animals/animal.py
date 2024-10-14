from abc import ABC, abstractmethod
from project.food import Food


class Animal(ABC):
    @abstractmethod
    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight
        self.food_eaten = 0
        self.sound = None
        self.foods = None
        self.gain_weight = None

    def make_sound(self):
        return self.sound

    def feed(self, food: Food):
        for food_class in self.foods:
            if isinstance(food, food_class):
                self.weight += food.quantity * self.gain_weight
                self.food_eaten += food.quantity
                return None
        return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


class Bird(Animal, ABC):
    @abstractmethod
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return (f"{self.__class__.__name__} [{self.name}, {self.wing_size}, "
                f"{self.weight}, {self.food_eaten}]")


class Mammal(Animal, ABC):
    @abstractmethod
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return (f"{self.__class__.__name__} [{self.name}, {self.weight}, "
                f"{self.living_region}, {self.food_eaten}]")
