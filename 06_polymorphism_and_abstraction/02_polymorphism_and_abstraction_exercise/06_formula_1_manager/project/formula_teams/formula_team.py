from abc import ABC, abstractmethod
from typing import Dict, Optional


class FormulaTeam(ABC):
    EXPENSES: Optional[int] = None
    SPONSORS: Optional[Dict] = None

    @abstractmethod
    def __init__(self, budget: int):
        self.budget = budget

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        if value < 1_000_000:
            raise ValueError("F1 is an expensive sport, find more sponsors!")
        self.__budget = value

    def calculate_revenue_after_race(self, race_pos: int):
        revenue = -self.EXPENSES

        for award_dict in self.SPONSORS.values():
            for place in award_dict.keys():
                if race_pos <= place:
                    revenue += award_dict[place]
                    break
        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
