from typing import List

from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    VALID_MUSICIAN_TYPES = {"Guitarist": Guitarist,
                            "Drummer": Drummer,
                            "Singer": Singer}

    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Musician] = []
        self.concerts: List[Concert] = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.VALID_MUSICIAN_TYPES:
            raise ValueError("Invalid musician type!")

        m = next((m for m in self.musicians if m.name == name), None)
        if m is not None:
            raise Exception(f"{name} is already a musician!")

        new_musician = self.VALID_MUSICIAN_TYPES[musician_type](name, age)
        self.musicians.append(new_musician)
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        b = next((b for b in self.bands if b.name == name), None)
        if b is not None:
            raise Exception(f"{name} band is already created!")

        new_b = Band(name)
        self.bands.append(new_b)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        c = next((c for c in self.concerts if c.place == place), None)
        if c is not None:
            raise Exception(f"{place} is already registered for {genre} concert!")

        new_concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(new_concert)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = next((m for m in self.musicians if m.name == musician_name), None)
        if musician is None:
            raise Exception(f"{musician_name} isn't a musician!")

        band = next((b for b in self.bands if b.name == band_name), None)
        if band is None:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_bands(self, musician_name: str, band_name: str):
        band = next((b for b in self.bands if b.name == band_name), None)
        if band is None:
            raise Exception(f"{band_name} isn't a band!")

        member = next((m for m in band.members if m.name == musician_name), None)
        if member is None:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members.remove(member)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        concert = next(c for c in self.concerts if c.place == concert_place)
        band = next(b for b in self.bands if b.name == band_name)
        singer = next((s for s in band.members if s.__class__.__name__ == 'Singer'), None)
        guitarist = next((g for g in band.members if g.__class__.__name__ == 'Guitarist'), None)
        drummer = next((d for d in band.members if d.__class__.__name__ == 'Drummer'), None)
        if not all([singer, guitarist, drummer]):
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        if concert.genre == 'Rock':
            drummer_required_skills = ['play the drums with drumsticks']
            singer_required_skills = ['sing high pitch notes']
            guitarist_required_skills = ['play rock']

            is_drummer_ready = True if all(s in drummer.skills for s in drummer_required_skills) else False
            is_singer_ready = True if all(s in singer.skills for s in singer_required_skills) else False
            is_guitarist_ready = True if all(s in guitarist.skills for s in guitarist_required_skills) else False
            if not all([is_drummer_ready, is_singer_ready, is_guitarist_ready]):
                raise Exception(f"The {band_name} band is not ready to play at the concert!"
)
        elif concert.genre == 'Metal':
            drummer_required_skills = ['play the drums with drumsticks']
            singer_required_skills = ['sing low pitch notes']
            guitarist_required_skills = ['play metal']

            is_drummer_ready = True if all(s in drummer.skills for s in drummer_required_skills) else False
            is_singer_ready = True if all(s in singer.skills for s in singer_required_skills) else False
            is_guitarist_ready = True if all(s in guitarist.skills for s in guitarist_required_skills) else False
            if not all([is_drummer_ready, is_singer_ready, is_guitarist_ready]):
                raise Exception(f"The {band_name} band is not ready to play at the concert!")

        elif concert.genre == 'Jazz':
            drummer_required_skills = ['play the drums with drum brushes']
            singer_required_skills = ['sing low pitch notes', 'sing high pitch notes ']
            guitarist_required_skills = ['play jazz']

            is_drummer_ready = True if all(s in drummer.skills for s in drummer_required_skills) else False
            is_singer_ready = True if all(s in singer.skills for s in singer_required_skills) else False
            is_guitarist_ready = True if all(s in guitarist.skills for s in guitarist_required_skills) else False
            if not all([is_drummer_ready, is_singer_ready, is_guitarist_ready]):
                raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = (concert.audience * concert.ticket_price) - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert.place}."
