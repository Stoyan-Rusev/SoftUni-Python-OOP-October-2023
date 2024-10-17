from typing import List

from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.horse import Horse
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    VALID_HORSE_BREEDS = {"Appaloosa": Appaloosa,
                          "Thoroughbred": Thoroughbred}

    def __init__(self):
        self.horses: List[Horse] = []
        self.jockeys: List[Jockey] = []
        self.horse_races: List[HorseRace] = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        for h in self.horses:
            if h.name == horse_name:
                raise Exception(f"Horse {horse_name} has been already added!")

        if horse_type in self.VALID_HORSE_BREEDS:
            new_horse = self.VALID_HORSE_BREEDS[horse_type](horse_name, horse_speed)
            self.horses.append(new_horse)
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        for j in self.jockeys:
            if j.name == jockey_name:
                raise Exception(f"Jockey {jockey_name} has been already added!")

        new_jockey = Jockey(jockey_name, age)
        self.jockeys.append(new_jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        for r in self.horse_races:
            if r.race_type == race_type:
                raise Exception(f"Race {race_type} has been already created!")

        new_race = HorseRace(race_type)
        self.horse_races.append(new_race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = next((j for j in self.jockeys if j.name == jockey_name), None)
        if jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        horse = next((h for h in reversed(self.horses) if h.__class__.__name__ == horse_type and not h.is_taken), None)
        if horse is None:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if jockey.horse is not None:
            return f"Jockey {jockey_name} already has a horse."

        jockey.horse = horse
        horse.is_taken = True
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        race = next((r for r in self.horse_races if r.race_type == race_type), None)
        if race is None:
            raise Exception(f"Race {race_type} could not be found!")

        jockey = next((j for j in self.jockeys if j.name == jockey_name), None)
        if jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        for j in race.jockeys:
            if j.name == jockey_name:
                return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        race = next((r for r in self.horse_races if r.race_type == race_type), None)
        if race is None:
            raise Exception(f"Race {race_type} could not be found!")
        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        winner = self.jockeys[0]
        for j in self.jockeys:
            if j.horse.speed > winner.horse.speed:
                winner = j
        return (f"The winner of the {race_type} race, "
                f"with a speed of {winner.horse.speed}km/h is {winner.name}! "
                f"Winner's horse: {winner.horse.name}.")
