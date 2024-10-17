from typing import List

from project.booths.booth import Booth
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.delicacy import Delicacy
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    DELICACY_TYPES = {"Gingerbread": Gingerbread,
                      "Stolen": Stolen}
    BOOTH_TYPES = {"Open Booth": OpenBooth,
                   "Private Booth": PrivateBooth}

    def __init__(self):
        self.booths: List[Booth] = []
        self.delicacies: List[Delicacy] = []
        self.income: float = 0.0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        for d in self.delicacies:
            if d.name == name:
                raise Exception(f"{name} already exists!")

        if type_delicacy not in self.DELICACY_TYPES:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        new_delicacy = self.DELICACY_TYPES[type_delicacy](name, price)
        self.delicacies.append(new_delicacy)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        for b in self.booths:
            if b.booth_number == booth_number:
                raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth not in self.BOOTH_TYPES:
            raise Exception(f"{type_booth} is not a valid booth!")

        new_booth = self.BOOTH_TYPES[type_booth](booth_number, capacity)
        self.booths.append(new_booth)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        free_booth = next((b for b in self.booths if not b.is_reserved and b.capacity >= number_of_people), None)
        if free_booth is None:
            raise Exception(f"No available booth for {number_of_people} people!")
        free_booth.reserve(number_of_people)
        return f"Booth {free_booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        booth = next((b for b in self.booths if b.booth_number == booth_number), None)
        delicacy = next((d for d in self.delicacies if d.name == delicacy_name), None)
        if booth is None:
            raise Exception(f"Could not find booth {booth_number}!")
        if delicacy is None:
            raise Exception(f"No {delicacy_name} in the pastry shop!")
        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = next((b for b in self.booths if b.booth_number == booth_number), None)
        booth_bill = booth.price_for_reservation + sum([d.price for d in booth.delicacy_orders])
        self.income += booth_bill

        booth.is_reserved = False
        booth.price_for_reservation = 0
        booth.delicacy_orders = []
        return f"Booth {booth_number}:\nBill: {booth_bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."
