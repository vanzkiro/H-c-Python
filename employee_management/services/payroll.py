from models.employee import Employee


class PayrollService:
    @staticmethod
    def get_salary_report(employees: list) -> list:
        report = []
        for emp in employees:
            report.append({
                'emp_id': emp.emp_id,
                'name': emp.name,
                'role': emp.get_role(),
                'department': emp.department,
                'base_salary': emp.base_salary,
                'calculated_salary': emp.calculate_salary(),
                'performance': emp.performance_score
            })
        return sorted(report, key=lambda x: x['calculated_salary'], reverse=True)

    @staticmethod
    def format_currency(amount: float) -> str:
        return f"{amount:,.0f} VNĐ"
