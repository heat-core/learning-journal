class Drug:
    def __init__(self, name: str, amount: int, price: int):
        self.name = name
        self.amount = amount
        self.price = price





class Pharmacy:
    def __init__(self, name: str):
        self.drugs = []
        self.employees = []

    def add_drug(self, drug: Drug):
        self.drugs.append(drug)

    def add_employee(self, first_name: str, last_name: str, age: int):
        self.employees.append({
            "first_name": first_name,
            "last_name": last_name,
            "age": age
        })

    def total_value(self) -> int:
        for drug in self.drugs:
            value = drug.amount * drug.price
            total += value
        return total

    def employees_summary(self) -> str:
        print("Employees:\n")
        for i in range(self.employee):
            return print("\nThe employee number {i} is {first_name} {last_name} who is {age} years old.")
