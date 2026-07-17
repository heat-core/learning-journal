from dataclasses import dataclass, field


@dataclass
class Student:
    name: str
    age: int
    grades: list[float] = field(default_factory=list)

    def average_grade(self) -> float:
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)


if __name__ == "__main__":
    student1 = Student(name="Farbod", age=32)
    student1.grades.append(18.5)
    student1.grades.append(19.0)
    student1.grades.append(17.5)

    print(f"Student: {student1.name}, Age: {student1.age}")
    print(f"Grades: {student1.grades}")
    print(f"Average: {student1.average_grade():.2f}")

    student2 = Student(name="Ali", age=28, grades=[16.0, 18.0])
    print(f"\nStudent: {student2.name}")
    print(f"Average: {student2.average_grade():.2f}")