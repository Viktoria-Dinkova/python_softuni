from typing import List

from project.route import Route
from project.user import User
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:

    VALID_VEHICLE_TYPE = {'PassengerCar': PassengerCar,
                          'CargoVan': CargoVan
                          }

    def __init__(self):
        self.users: List[User] = []
        self.vehicles: List[BaseVehicle] = []
        self.routes: List[Route] = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        user = self._find_user(driving_license_number)
        if user:
            return f"{driving_license_number} has already been registered to our platform."

        user = User(first_name, last_name, driving_license_number)
        self.users.append(user)

        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        vehicle = self.VALID_VEHICLE_TYPE.get(vehicle_type)
        if not vehicle:
            return f"Vehicle type {vehicle_type} is inaccessible."

        vehicle = self._find_vehicle(license_plate_number)
        if vehicle:
            return f"{license_plate_number} belongs to another vehicle."

        vehicle = self.VALID_VEHICLE_TYPE[vehicle_type](brand, model, license_plate_number)
        self.vehicles.append(vehicle)
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        route = self._find_route(start_point, end_point)
        if route:
            if route.length == length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."

            if route.length < length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."

            if route.length > length:
                route.is_locked = True

        r_id = len(self.routes) + 1
        route = Route(start_point, end_point, length, r_id)
        self.routes.append(route)

        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened: bool):
        user = self._find_user(driving_license_number)
        vehicle = self._find_vehicle(license_plate_number)
        route = next(filter(lambda r: r.route_id == route_id, self.routes))

        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        if is_accident_happened:
            vehicle.is_damaged = True
            user.decrease_rating()
        else:
            user.increase_rating()

        vehicle.drive(route.length)
        return vehicle.__str__()

    def repair_vehicles(self, count: int):
        damaged_vehicles = filter(lambda dv: dv.is_damaged, self.vehicles)
        sorted_damaged_vehicles = sorted(damaged_vehicles, key=lambda dv: (dv.brand, dv.model))
        for i in range(count if count < len(sorted_damaged_vehicles) else len(sorted_damaged_vehicles)):
            sorted_damaged_vehicles[i].is_damaged = False
            sorted_damaged_vehicles[i].recharge()

        return f"{len(sorted_damaged_vehicles)} vehicles were successfully repaired!"

    def users_report(self):
        result = ["*** E-Drive-Rent ***"]
        sorted_users = sorted( self.users, key=lambda u: -u.rating)
        for su in sorted_users:
            result.append(su.__str__())

        return '\n'.join(result)

    def _find_user(self, driving_license_number) -> User:
        try:
            return next(filter(lambda u: u.driving_license_number == driving_license_number, self.users))
        except StopIteration:
            return None

    def _find_vehicle(self, license_plate_number) -> BaseVehicle:
        try:
            return next(filter(lambda v: v.license_plate_number == license_plate_number, self.vehicles))
        except StopIteration:
            return None

    def _find_route(self, start_point: str, end_point: str) -> Route:
        try:
            return next(filter(lambda r: r.start_point == start_point and r.end_point == end_point, self.routes))
        except StopIteration:
            return None
