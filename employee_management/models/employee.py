class Employee:
    def __init__(self, emp_id, name, age, email, base_salary, department):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.email = email
        self.base_salary = base_salary
        self.department = department

        self.projects = []
        self.performance_score = 0.0

    def calculate_salary(self):
        return self.base_salary  # mặc định, class con sẽ override

    def add_project(self, project):
        if project not in self.projects:
            self.projects.append(project)

    def remove_project(self, project):
        if project in self.projects:
            self.projects.remove(project)

    def set_performance_score(self, score):
        if 0 <= score <= 10:
            self.performance_score = score
        else:
            raise ValueError("Score must be between 0 and 10")

    def get_role(self):
        return "Employee"

    def get_performance_rating(self):
        if self.performance_score >= 9:
            return "Xuất sắc"
        elif self.performance_score >= 7:
            return "Tốt"
        elif self.performance_score >= 5:
            return "Trung bình"
        else:
            return "Yếu"

    def to_dict(self):
        return {
            "emp_id": self.emp_id,
            "name": self.name,
            "age": self.age,
            "email": self.email,
            "base_salary": self.base_salary,
            "department": self.department,
            "role": self.get_role(),
            "extra_info": ""
        }