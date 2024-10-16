from project.fish.base_fish import BaseFish


class PredatoryFish(BaseFish):
    TIME_TO_CATH = 90

    def __init__(self, name: str, points: float):
        super().__init__(name, points, self.TIME_TO_CATH)

    def fish_details(self):
        return (f"{self.__class__.__name__}: {self.name} "
                f"[Points: {self.points}, Time to Catch: {self.time_to_catch} seconds]")
