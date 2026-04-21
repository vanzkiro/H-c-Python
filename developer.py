from models.employee import Employee

class Developer(Employee):
    TECH_BONUS = 0.20  # 20% bonus

    def __init__(self, emp_id, name, age, email, base_salary, department="", tech_stack=""):
        super().__init__(emp_id, name, age, email, base_salary, department)
        self.tech_stack = tech_stack

    def calculate_salary(self) -> float:
        return self.base_salary * (1 + self.TECH_BONUS)

    def get_role(self) -> str:
        return "Developer"

    def to_dict(self) -> dict:
        d = super().to_dict()
        d['tech_stack'] = self.tech_stack
        d['extra_info'] = self.tech_stack
        return d
