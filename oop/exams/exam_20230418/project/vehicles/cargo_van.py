from project.vehicles.base_vehicle import BaseVehicle


class CargoVan (BaseVehicle):

    @property
    def get_max_mileage(self):
        return 180.00

    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, self.get_max_mileage)


    def drive(self, mileage: float) -> None:
        what_part_of_max_mileage_will__passed = int(mileage / self.get_max_mileage * 100) + 5 # reduce an additional 5% % because of the load.

        self.battery_level -= what_part_of_max_mileage_will__passed
        # self.battery_level = int(self.battery_level * 0.95) # reduce an additional 5% % because of the load.

