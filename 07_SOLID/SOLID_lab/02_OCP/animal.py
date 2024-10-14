from abc import ABC, abstractmethod


class Animal(ABC):
    sound = None

    @staticmethod
    @abstractmethod
    def make_sound():
        return self.sound

    def get_species(self):
        return self.__class__.__name__


class Cat(Animal):
    sound = 'Meow'

    @staticmethod
    def make_sound():
        return Cat.sound


class Dog(Animal):
    sound = 'Bark'

    @staticmethod
    def make_sound():
        return Dog.sound


class Horse(Animal):
    sound = 'Horse sound....'

    @staticmethod
    def make_sound():
        return Horse.sound


dog = Dog()
cat = Cat()
horse = Horse()

animal_list = [dog,cat, horse]
for animal in animal_list:
    print(animal.make_sound())

