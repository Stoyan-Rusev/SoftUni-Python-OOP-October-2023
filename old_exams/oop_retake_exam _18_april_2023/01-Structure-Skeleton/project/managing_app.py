from typing import List

from project.route import Route
from project.user import User
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    def __init__(self):
        self.users: List[User] = []
        self.vehicles: List[BaseVehicle] = []
        self.routes: List[Route] = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        for current_user in self.users:
            if current_user.driving_license_number == driving_license_number:
                return f"{driving_license_number} has already been registered to our platform."

        user = User(first_name, last_name, driving_license_number)
        self.users.append(user)
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        vehicle_types = {'PassengerCar': PassengerCar,
                         'CargoVan': CargoVan}

        if vehicle_type not in vehicle_types:
            return f"Vehicle type {vehicle_type} is inaccessible."

        for vehicle in self. vehicles:
            if vehicle.license_plate_number == license_plate_number:
                return f"{license_plate_number} belongs to another vehicle."

        new_vehicle = vehicle_types[vehicle_type](brand, model, license_plate_number)
        self.vehicles.append(new_vehicle)
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        for route in self.routes:
            if route.start_point == start_point and route.end_point == end_point and route.length == length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."

        for route in self.routes:
            if route.start_point == start_point and route.end_point == end_point and route.length < length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."

        new_route = Route(start_point, end_point, length, len(self.routes) + 1)
        self.routes.append(new_route)
        for route in self.routes:
            if route.start_point == start_point and route.end_point == end_point and route.length > length:
                route.is_locked = True
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int, is_accident_happened: bool):
        user = next((u for u in self.users if u.driving_license_number == driving_license_number), None)
        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."
        vehicle = next((v for v in self.vehicles if v.license_plate_number == license_plate_number))
        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."
        route = next((r for r in self.routes if r.route_id == route_id))
        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)
        if is_accident_happened:
            vehicle.change_status()
            user.decrease_rating()
        else:
            user.increase_rating()

        return str(vehicle)

    def repair_vehicles(self, count: int):
        damaged_vehicles = [v for v in self.vehicles if v.is_damaged]
        selected_vehicles = sorted(damaged_vehicles, key=lambda v: (v.brand, v.model))[:count]

        for v in selected_vehicles:
            v.is_damaged = False
            v.recharge()

        return f"{len(selected_vehicles)} vehicles were successfully repaired!"

    def users_report(self):
        result = ["*** E-Drive-Rent ***"]
        sorted_users = sorted(self.users, key=lambda x: -x.rating)

        for user in sorted_users:
            result.append(user.__str__())
        return "\n".join(result)
