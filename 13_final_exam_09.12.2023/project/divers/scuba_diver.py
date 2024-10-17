from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):
    INITIAL_OXYGEN_LEVEL = 540

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_OXYGEN_LEVEL)

    def miss(self, time_to_catch: int):
        oxygen_decrease = round(0.3 * time_to_catch)
        if self.oxygen_level - oxygen_decrease < 0:
            self.oxygen_level = 0
        else:
            self.oxygen_level -= oxygen_decrease

    def renew_oxy(self):
        self.oxygen_level = self.INITIAL_OXYGEN_LEVEL
