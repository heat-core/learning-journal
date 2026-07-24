# IMPORTS
from work_place import WorkPlace, Consts



class Company(WorkPlace):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.expertise = "company"
        self.calc_capacity()

    def calc_capacity(self) -> None:
        self.capacity = int(self.level)

    def calc_costs(self) -> int:
        return int(Consts.BASE_PLACE_COST * self.level)
