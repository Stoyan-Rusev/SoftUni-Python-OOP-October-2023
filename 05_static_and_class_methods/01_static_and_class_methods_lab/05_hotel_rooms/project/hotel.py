from typing import List
from project.room import Room


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms: List[Room] = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for current_room in self.rooms:
            if (current_room.number == room_number
                    and not current_room.is_taken
                    and current_room.capacity >= people):
                current_room.is_taken = True
                current_room.guests = people
                self.guests += people
                break

    def free_room(self, room_number):
        for current_room in self.rooms:
            if current_room.number == room_number:
                if not current_room.is_taken:
                    return f"Room number {room_number} is not taken"
                current_room.is_taken = False
                self.guests -= current_room.guests
                current_room.guests = 0
                break

    def status(self):
        free_rooms_nums = []
        taken_room_nums = []
        for room in self.rooms:
            if room.is_taken:
                taken_room_nums.append(str(room.number))
            else:
                free_rooms_nums.append(str(room.number))

        return (f"Hotel {self.name} has {self.guests} total guests\n"
                f"Free rooms: {', '.join(free_rooms_nums)}\n"
                f"Taken rooms: {', '.join(taken_room_nums)}")
