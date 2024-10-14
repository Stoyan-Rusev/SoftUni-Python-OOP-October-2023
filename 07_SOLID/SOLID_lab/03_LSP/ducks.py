from abc import abstractmethod, ABC


class Duck(ABC):
    @staticmethod
    @abstractmethod
    def quack():
        pass

    @staticmethod
    def walk():
        raise Exception('I cannot walk by myself')

    @staticmethod
    def fly():
        raise Exception('I cannot fly by myself')


class RubberDuck(Duck):
    @staticmethod
    def quack():
        return "Squeek"


class RobotDuck(Duck):
    MAX_HEIGHT = 50

    def __init__(self):
        self.height = 0

    @staticmethod
    def quack():
        return 'Robotic quacking'

    @staticmethod
    def walk():
        return 'Robotic walking'

    def fly(self):
        """can only fly to specific height but
        when it reaches it starts landing automatically"""
        if self.height == RobotDuck.MAX_HEIGHT:
            self.land()
        else:
            self.height += 1

    def land(self):
        self.height = 0


duck1 = RobotDuck()
duck2 = RubberDuck()

# print(duck2.fly())
# print(duck2.walk())

# for _ in range(51):
#     duck1.fly()
#     print(duck1.height)
