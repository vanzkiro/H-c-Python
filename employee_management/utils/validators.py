import re
from exceptions.employee_exceptions import (
    InvalidAgeError,
    InvalidSalaryError,
    InvalidScoreError,
    InvalidEmailError  
)


def validate_age(age_str: str) -> int:
    try:
        age = int(age_str)
    except ValueError:
        raise ValueError(f"Tuổi phải là số nguyên, nhận được: '{age_str}'")
    if not (18 <= age <= 65):
        raise InvalidAgeError(age)
    return age


def validate_salary(salary_str: str) -> float:
    try:
        salary = float(salary_str.replace(',', ''))
    except ValueError:
        raise ValueError(f"Lương phải là số, nhận được: '{salary_str}'")
    if salary <= 0:
        raise InvalidSalaryError(salary)
    return salary


def validate_email(email: str) -> str:
    pattern = r'^[^@\s]+@[^@\s]+\.[^@\s]+$'
    if not re.match(pattern, email):
        raise InvalidEmailError(email) 
    return email


def validate_score(score_str: str) -> float:
    try:
        score = float(score_str)
    except ValueError:
        raise ValueError(f"Điểm phải là số, nhận được: '{score_str}'")
    if not (0 <= score <= 10):
        raise InvalidScoreError(score)
    return score


def validate_emp_id(emp_id: str) -> str:
    if not emp_id.strip():
        raise ValueError("ID nhân viên không được để trống.")
    return emp_id.strip().upper()