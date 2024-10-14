from project.food.main_dish import MainDish


class Salmon(MainDish):
    GRAMS = 22

    def __init__(self, name, price):
        super().__init__(name, price, self.GRAMS)
        self.__grams = Salmon.GRAMS

    @property
    def grams(self):
        return self.__grams
