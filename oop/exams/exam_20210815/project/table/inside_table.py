from project.table.table import Table


class InsideTable(Table):
    def __init__(self, table_number: int, capacity: int):
        super().__init__(table_number, capacity)

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if not (1 <= value <= 50):
            raise ValueError("Inside table's number must be between 1 and 50 inclusive!")
        self.__capacity = value
