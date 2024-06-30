from project.equipment.base_equipment import BaseEquipment


class ElbowPad(BaseEquipment):
    
    @property
    def get_protection(self):
        return 90

    @property
    def get_price(self):
        return 25.0

    def __init__(self):
        super().__init__(self.get_protection, self.get_price)

    def increase_price(self):
        return self.get_price * 1.1 # increase price with 10%

