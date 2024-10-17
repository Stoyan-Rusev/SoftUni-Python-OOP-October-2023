rom typing import List

from project.equipment.base_equipment import BaseEquipment
from project.teams.base_team import BaseTeam
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    VALID_EQUIPMENT_TYPES = {"KneePad": KneePad, "ElbowPad": ElbowPad}
    VALID_TEAM_TYPES = {"OutdoorTeam": OutdoorTeam, "IndoorTeam": IndoorTeam}

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment: List[BaseEquipment] = []
        self.teams: List[BaseTeam] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = value

    def add_equipment(self, equipment_type: str):
        if equipment_type not in Tournament.VALID_EQUIPMENT_TYPES:
            raise ValueError("Invalid equipment type!")
        self.equipment.append(Tournament.VALID_EQUIPMENT_TYPES[equipment_type]())
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type not in Tournament.VALID_TEAM_TYPES:
            raise Exception("Invalid team type!")
        if self.capacity == len(self.teams):
            return "Not enough tournament capacity."
        self.teams.append(Tournament.VALID_TEAM_TYPES[team_type](team_name, country, advantage))
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        searched_equipment = next((e for e in reversed(self.equipment) if e.__class__.__name__ == equipment_type), None)
        searched_team = next((t for t in self.teams if t.name == team_name), None)

        if searched_equipment.price > searched_team.budget:
            return "Budget is not enough!"
        searched_team.budget -= searched_equipment.price
        searched_team.equipment.append(searched_equipment)
        self.equipment.remove(searched_equipment)
        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        searched_team = next((t for t in self.teams if t.name == team_name), None)
        if not searched_team:
            raise Exception("No such team!")

        if searched_team.wins:
            raise Exception(f"The team has {searched_team.wins} wins! Removal is impossible!")

        self.teams.remove(searched_team)
        return f"Successfully removed {searched_team.name}."

    def increase_equipment_price(self, equipment_type: str):
        count = 0
        for current_e in self.equipment:
            if current_e.__class__.__name__ == equipment_type:
                current_e.increase_price()
                count += 1
        return f"Successfully changed {count}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        team1 = next((t for t in self.teams if t.name == team_name1), None)
        team2 = next((t for t in self.teams if t.name == team_name2), None)
        if team1.__class__.__name__ != team2.__class__.__name__:
            raise Exception("Game cannot start! Team types mismatch!")

        team1_score = team1.advantage + sum([e.protection for e in team1.equipment])
        team2_score = team2.advantage + sum([e.protection for e in team2.equipment])

        if team1_score == team2_score:
            return "No winner in this game."
        winner = team1 if team1_score > team2_score else team2
        winner.win()
        return f"The winner is {winner.name}."

    def get_statistics(self):
        teams = sorted(self.teams, key=lambda x: -x.wins)
        result = [f"Tournament: {self.name}", f"Number of Teams: {len(self.teams)}", "Teams:"]
        [result.append(team.get_statistics()) for team in teams]
        return '\n'.join(result)
