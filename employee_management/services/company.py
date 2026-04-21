import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from models import Employee, Manager, Developer, Intern

from exceptions.employee_exceptions import (
    EmployeeNotFoundError, DuplicateEmployeeError,
    ProjectAllocationError, InvalidScoreError
)
from database.db_manager import get_connection
from datetime import datetime


class Company:
    def __init__(self):
        self._employees: dict[str, Employee] = {}
        self._load_from_db()

    def _load_from_db(self):
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("SELECT emp_id, name, age, email, base_salary, department, role, extra_info, performance_score FROM employees")
            rows = cur.fetchall()
            for row in rows:
                emp_id, name, age, email, base_salary, dept, role, extra_info, perf = row
                try:
                    emp = self._create_employee_obj(emp_id, name, age, email, base_salary, dept, role, extra_info)
                    emp.performance_score = perf or 0.0
                    # Load projects
                    cur2 = conn.cursor()
                    cur2.execute("SELECT project_name FROM project_assignments WHERE emp_id=?", (emp_id,))
                    for (proj,) in cur2.fetchall():
                        emp.projects.append(proj)
                    self._employees[emp_id] = emp
                except Exception:
                    pass
            conn.close()
        except Exception:
            pass

    def _create_employee_obj(self, emp_id, name, age, email, base_salary, dept, role, extra_info):
        if role == "Manager":
            team_size = int(extra_info) if extra_info and extra_info.isdigit() else 0
            return Manager(emp_id, name, age, email, base_salary, dept, team_size)
        elif role == "Developer":
            return Developer(emp_id, name, age, email, base_salary, dept, extra_info or "")
        elif role == "Intern":
            return Intern(emp_id, name, age, email, base_salary, dept, extra_info or "")
        else:
            raise ValueError(f"Unknown role: {role}")

    def _generate_id(self) -> str:
        i = 1
        while True:
            new_id = f"EMP{i:04d}"
            if new_id not in self._employees:
                return new_id
            i += 1

    def add_employee(self, emp: Employee, auto_id: bool = False) -> str:
        if emp.emp_id in self._employees:
            if auto_id:
                emp.emp_id = self._generate_id()
            else:
                raise DuplicateEmployeeError(emp.emp_id)
        self._employees[emp.emp_id] = emp
        self._save_employee_to_db(emp)
        return emp.emp_id

    def _save_employee_to_db(self, emp: Employee):
        conn = get_connection()
        cur = conn.cursor()
        d = emp.to_dict()
        extra = d.get('extra_info', '')
        cur.execute("""
            INSERT OR REPLACE INTO employees
            (emp_id, name, age, email, base_salary, department, role, extra_info, performance_score)
            VALUES (?,?,?,?,?,?,?,?,?)
        """, (emp.emp_id, emp.name, emp.age, emp.email, emp.base_salary,
              emp.department, emp.get_role(), extra, emp.performance_score))
        conn.commit()
        conn.close()

    def get_employee(self, emp_id: str) -> Employee:
        if emp_id not in self._employees:
            raise EmployeeNotFoundError(emp_id)
        return self._employees[emp_id]

    def remove_employee(self, emp_id: str):
        if emp_id not in self._employees:
            raise EmployeeNotFoundError(emp_id)
        del self._employees[emp_id]
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM employees WHERE emp_id=?", (emp_id,))
        cur.execute("DELETE FROM project_assignments WHERE emp_id=?", (emp_id,))
        conn.commit()
        conn.close()

    def update_employee(self, emp: Employee):
        if emp.emp_id not in self._employees:
            raise EmployeeNotFoundError(emp.emp_id)
        self._employees[emp.emp_id] = emp
        self._save_employee_to_db(emp)

    def assign_project(self, emp_id: str, project_name: str):
        emp = self.get_employee(emp_id)

        if len(emp.projects) >= 5: 
            raise ProjectAllocationError(emp_id)

        emp.add_project(project_name)

        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO project_assignments (emp_id, project_name, assigned_date) VALUES (?,?,?)",
            (emp_id, project_name, datetime.now().strftime("%Y-%m-%d"))
        )
        conn.commit()
        conn.close()

    def remove_project(self, emp_id: str, project_name: str):
        emp = self.get_employee(emp_id)
        emp.remove_project(project_name)
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM project_assignments WHERE emp_id=? AND project_name=?", (emp_id, project_name))
        conn.commit()
        conn.close()

    def set_performance(self, emp_id: str, score: float):
        from utils.validators import validate_score

        score = validate_score(str(score)) 

        emp = self.get_employee(emp_id)
        emp.set_performance_score(score)

        conn = get_connection()
        cur = conn.cursor()
        cur.execute("UPDATE employees SET performance_score=? WHERE emp_id=?", (score, emp_id))
        conn.commit()
        conn.close()

    def get_all_employees(self) -> list:
        return list(self._employees.values())

    def search_by_name(self, keyword: str) -> list:
        return [e for e in self._employees.values() if keyword.lower() in e.name.lower()]

    def get_top_salaries(self, n: int = 10) -> list:
        emps = sorted(self._employees.values(), key=lambda e: e.calculate_salary(), reverse=True)
        return emps[:n]

    def get_project_stats(self) -> dict:
        stats = {}
        for emp in self._employees.values():
            for proj in emp.projects:
                stats[proj] = stats.get(proj, 0) + 1
        return stats

    def save_salary_record(self, month: str):
        conn = get_connection()
        cur = conn.cursor()
        for emp in self._employees.values():
            cur.execute("INSERT INTO salaries (emp_id, calculated_salary, month) VALUES (?,?,?)",
                        (emp.emp_id, emp.calculate_salary(), month))
        conn.commit()
        conn.close()
