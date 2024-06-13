from typing import List

from project.robots.base_robot import BaseRobot
from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.base_service import BaseService
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    VALID_SERVICE_TYPE = {"MainService": MainService,
                          "SecondaryService": SecondaryService,
                          }

    VALID_ROBOT_TYPE = {"FemaleRobot": [FemaleRobot, 'SecondaryService'],
                        "MaleRobot": [MaleRobot, 'MainService'],
                        }

    def __init__(self):
        self.robots: List[BaseRobot] = []
        self.services: List[BaseService] = []

    def add_service(self, service_type: str, name: str) -> str:
        service = self.VALID_SERVICE_TYPE.get(service_type)

        if not service:
            raise Exception("Invalid service type!")

        service = self.VALID_SERVICE_TYPE[service_type](name)
        self.services.append(service)

        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        robot = self.VALID_ROBOT_TYPE.get(robot_type)

        if not robot:
            raise Exception("Invalid robot type!")

        robot = self.VALID_ROBOT_TYPE[robot_type][0](name, kind, price)
        self.robots.append(robot)

        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = self._find_robot(robot_name)
        service = self._find_service(service_name)
        robot_class = robot.__class__.__name__
        service_class = service.__class__.__name__

        if self.VALID_ROBOT_TYPE[robot_class][1] != service_class:
            return "Unsuitable service."

        if service.capacity <= len(service.robots):
            raise Exception("Not enough capacity for this robot!")

        self.robots.remove(robot)
        service.robots.append(robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str) -> str:
        robot = self._find_robot(robot_name)
        service = self._find_service(service_name)

        try:
            robot = next(filter(lambda r: r.name == robot_name, service.robots))
        except StopIteration:
            raise Exception("No such robot in this service!")

        service.robots.remove(robot)
        self.robots.append(robot)

        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str) -> str:
        service = self._find_service(service_name)
        [r.eating() for r in service.robots]

        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name: str):
        service = self._find_service(service_name)
        total_price = sum(r.price for r in service.robots)

        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        result = [serv.details() for serv in self.services]

        return '\n'.join(result)

    # my methods

    def _find_robot(self, name: str) -> BaseRobot:
        try:
            return next(filter(lambda r: r.name == name, self.robots))
        except StopIteration:
            pass

    def _find_service(self, name: str) -> BaseService:
        try:
            return next(filter(lambda s: s.name == name, self.services))
        except StopIteration:
            pass

