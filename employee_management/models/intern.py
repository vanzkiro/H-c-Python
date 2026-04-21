from models.employee import Employee

class Intern(Employee):
    INTERN_RATE = 0.50  # 50% of base salary

    def __init__(self, emp_id, name, age, email, base_salary, department="", school=""):
        super().__init__(emp_id, name, age, email, base_salary, department)
        self.school = school

    def calculate_salary(self) -> float:
        return self.base_salary * self.INTERN_RATE

    def get_role(self) -> str:
        return "Intern"

    def to_dict(self) -> dict:
        d = super().to_dict()
        d['school'] = self.school
        d['extra_info'] = self.school
        return d
