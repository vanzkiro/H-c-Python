from models.employee import Employee

class Manager(Employee):
    MANAGEMENT_BONUS = 0.30  # 30% bonus

    def __init__(self, emp_id, name, age, email, base_salary, department="", team_size=0):
        super().__init__(emp_id, name, age, email, base_salary, department)
        self.team_size = team_size

    def calculate_salary(self) -> float:
        team_bonus = self.team_size * 500_000
        return self.base_salary * (1 + self.MANAGEMENT_BONUS) + team_bonus

    def get_role(self) -> str:
        return "Manager"

    def to_dict(self) -> dict:
        d = super().to_dict()
        d['team_size'] = self.team_size
        d['extra_info'] = str(self.team_size)
        return d
