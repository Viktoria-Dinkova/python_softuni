from project.equipment.base_equipment import BaseEquipment


class KneePad(BaseEquipment):

    @property
    def get_protection(self):
        return 120

    @property
    def get_price(self):
        return 15.0

    def __init__(self):
        super().__init__(self.get_protection, self.get_price)

    def increase_price(self):
        return self.get_price * 1.2  # increase price with 20%

