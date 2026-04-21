def format_currency(amount: float) -> str:
    return f"{amount:,.0f} VNĐ"

def format_employee_info(emp) -> str:
    lines = [
        f"ID         : {emp.emp_id}",
        f"Họ tên     : {emp.name}",
        f"Tuổi       : {emp.age}",
        f"Email      : {emp.email}",
        f"Chức vụ    : {emp.get_role()}",
        f"Phòng ban  : {emp.department}",
        f"Lương CB   : {format_currency(emp.base_salary)}",
        f"Lương TT   : {format_currency(emp.calculate_salary())}",
        f"Hiệu suất  : {emp.performance_score}/10 ({emp.get_performance_rating()})",
        f"Dự án      : {', '.join(emp.projects) if emp.projects else 'Chưa có'}",
    ]
    return '\n'.join(lines)
