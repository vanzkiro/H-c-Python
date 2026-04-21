class InvalidAgeError(Exception):
    def __init__(self, age):
        super().__init__(f"Tuổi không hợp lệ: {age}. Tuổi phải từ 18 đến 65.")
        self.age = age


class InvalidSalaryError(Exception):
    def __init__(self, salary):
        super().__init__(f"Lương không hợp lệ: {salary}. Lương phải lớn hơn 0.")
        self.salary = salary


class InvalidEmailError(Exception): 
    def __init__(self, email):
        super().__init__(f"Email không hợp lệ: {email}")
        self.email = email


class EmployeeNotFoundError(Exception):
    def __init__(self, emp_id):
        super().__init__(f"Không tìm thấy nhân viên với ID: {emp_id}")
        self.emp_id = emp_id


class DuplicateEmployeeError(Exception):
    def __init__(self, emp_id):
        super().__init__(f"Nhân viên với ID {emp_id} đã tồn tại.")
        self.emp_id = emp_id


class ProjectAllocationError(Exception):
    def __init__(self, emp_id):
        super().__init__(f"Nhân viên {emp_id} đã được phân công 5 dự án. Không thể thêm.")
        self.emp_id = emp_id


class InvalidScoreError(Exception):
    def __init__(self, score):
        super().__init__(f"Điểm không hợp lệ: {score}. Điểm phải từ 0 đến 10.")
        self.score = score