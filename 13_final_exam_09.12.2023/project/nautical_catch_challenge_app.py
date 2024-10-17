from typing import List

from project.divers.base_diver import BaseDiver
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.base_fish import BaseFish
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:
    DIVER_TYPES = {'ScubaDiver': ScubaDiver,
                   'FreeDiver': FreeDiver}

    FISH_TYPES = {'PredatoryFish': PredatoryFish,
                  'DeepSeaFish': DeepSeaFish}

    def __init__(self):
        self.divers: List[BaseDiver] = []
        self.fish_list: List[BaseFish] = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        if diver_type not in self.DIVER_TYPES:
            return f"{diver_type} is not allowed in our competition."

        for d in self.divers:
            if d.name == diver_name:
                return f"{diver_name} is already a participant."

        diver = self.DIVER_TYPES[diver_type](diver_name)
        self.divers.append(diver)
        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type not in self.FISH_TYPES:
            return f"{fish_type} is forbidden for chasing in our competition."

        for f in self.fish_list:
            if f.name == fish_name:
                return f"{fish_name} is already permitted."

        fish = self.FISH_TYPES[fish_type](fish_name, points)
        self.fish_list.append(fish)
        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        diver = next((d for d in self.divers if d.name == diver_name), None)
        if diver is None:
            return f"{diver_name} is not registered for the competition."

        fish = next((f for f in self.fish_list if f.name == fish_name), None)
        if fish is None:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            if diver.oxygen_level == 0:
                diver.has_health_issue = True
            return f"{diver_name} missed a good {fish_name}."

        if diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish)
                if diver.oxygen_level == 0:
                    diver.has_health_issue = True
                return f"{diver_name} hits a {fish.points}pt. {fish_name}."

            if not is_lucky:
                diver.miss(fish.time_to_catch)
                if diver.oxygen_level == 0:
                    diver.has_health_issue = True
                return f"{diver_name} missed a good {fish_name}."

        if diver.oxygen_level > fish.time_to_catch:
            diver.hit(fish)
            if diver.oxygen_level == 0:
                diver.has_health_issue = True
            return f"{diver_name} hits a {fish.points}pt. {fish_name}."

    def health_recovery(self):
        count = 0
        for d in self.divers:
            if d.has_health_issue:
                d.has_health_issue = False
                d.oxygen_level = d.INITIAL_OXYGEN_LEVEL
                count += 1
        return f"Divers recovered: {count}"

    def diver_catch_report(self, diver_name: str):
        result = [f'**{diver_name} Catch Report**']
        diver = next((d for d in self.divers if d.name == diver_name), None)
        for f in diver.catch:
            result.append(f.fish_details())
        return '\n'.join(result)

    def competition_statistics(self):
        result = ['**Nautical Catch Challenge Statistics**']
        good_condition_divers = [d for d in self.divers if not d.has_health_issue]
        sorted_divers = sorted(good_condition_divers, key=lambda diver: (-diver.competition_points, len(diver.catch), diver.name))
        for d in sorted_divers:
            result.append(str(d))
        return '\n'.join(result)
