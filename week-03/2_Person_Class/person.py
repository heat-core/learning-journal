import math


class Consts:
    BASE_PRICE = {'worker': 1200, 'teacher': 1500, 'engineer': 2000}
    BASE_COST = {'worker': 200, 'teacher': 150, 'engineer': 300}
    BASE_INCOME = {'worker': {'mine': 800}, 'teacher': {'mine': 300}, 'engineer': {'mine': 1000}}
    MIN_AGE = 15
    AGE_MUL = 10

class Person:
    instances = []

    def __init__(self, name: str, age: int) -> None:
        ...

    def do_level(self, income: int) -> float:
        ...

    def calc_income(self):
        pass

    def calc_life_cost(self):
        pass

    def calc(self) -> float:
        ...

    def get_job(self) -> str:
        ...

    def upgrade(self) -> None:
        ...

    @staticmethod
    def calc_all() -> float:
        ...
