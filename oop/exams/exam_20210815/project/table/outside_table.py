from project.table.table import Table


class OutsideTable(Table):
    def __init__(self, table_number: int, capacity: int):
        super().__init__(table_number, capacity)

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if not (51 <= value <= 100):
            raise ValueError("Outside table's number must be between 51 and 100 inclusive!")
        self.__capacity = value
