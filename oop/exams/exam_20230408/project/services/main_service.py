from project.services.base_service import BaseService


class MainService(BaseService):
    SERVICE_CAPACITY = 30

    def __init__(self, name: str):
        super().__init__(name, MainService.SERVICE_CAPACITY)

    def details(self) -> str:
        result = [f"{self.name} Main Service:", "Robots: none"]
        if self.robots:
            result[1] = f"Robots: {' '.join(r.name for r in self.robots)}"

        return '\n'.join(result)