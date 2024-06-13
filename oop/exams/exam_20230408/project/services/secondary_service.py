from project.services.base_service import BaseService


class SecondaryService(BaseService):
    SERVICE_CAPACITY = 15

    def __init__(self, name: str):
        super().__init__(name, SecondaryService.SERVICE_CAPACITY)

    def details(self) -> str:
        result = [f"{self.name} Secondary Service:", "Robots: none"]
        if self.robots:
            result[1] = f"Robots: {' '.join(r.name for r in self.robots)}"

        return '\n'.join(result)