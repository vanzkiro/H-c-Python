import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QFont
from database.db_manager import initialize_db
from ui.main_app import MainApp


def seed_sample_data(company):
    """Thêm dữ liệu mẫu nếu chưa có nhân viên."""
    from models import Manager, Developer, Intern
    if company.get_all_employees():
        return

    samples = [
        Manager("EMP0001", "Nguyễn Văn An", 38, "an.nguyen@company.com", 25_000_000, "Kỹ thuật", 8),
        Manager("EMP0002", "Trần Thị Bình", 42, "binh.tran@company.com", 28_000_000, "Kinh doanh", 5),
        Developer("EMP0003", "Lê Quang Chiến", 29, "chien.le@company.com", 18_000_000, "Kỹ thuật", "Python, Django, React"),
        Developer("EMP0004", "Phạm Thị Dung", 27, "dung.pham@company.com", 16_000_000, "Kỹ thuật", "Java, Spring Boot"),
        Developer("EMP0005", "Hoàng Minh Đức", 31, "duc.hoang@company.com", 20_000_000, "Kỹ thuật", "Go, Kubernetes"),
        Developer("EMP0006", "Vũ Thị Hà", 26, "ha.vu@company.com", 15_000_000, "Marketing", "JavaScript, Vue"),
        Developer("EMP0007", "Đặng Văn Hùng", 33, "hung.dang@company.com", 22_000_000, "Kỹ thuật", "C++, Embedded"),
        Intern("EMP0008", "Nguyễn Thị Lan", 22, "lan.nguyen@company.com", 5_000_000, "Kỹ thuật", "ĐH Bách Khoa HN"),
        Intern("EMP0009", "Trần Văn Minh", 21, "minh.tran@company.com", 5_000_000, "Kinh doanh", "ĐH Kinh tế QD"),
        Developer("EMP0010", "Bùi Thị Nga", 28, "nga.bui@company.com", 17_000_000, "Nhân sự", "Python, SQL"),
    ]

    projects_data = {
        "EMP0001": ["Alpha Project", "Beta Platform", "Gamma System"],
        "EMP0002": ["Delta App"],
        "EMP0003": ["Alpha Project", "Epsilon API"],
        "EMP0004": ["Beta Platform", "Gamma System"],
        "EMP0005": ["Alpha Project", "Zeta Portal"],
        "EMP0006": ["Delta App", "Epsilon API"],
        "EMP0007": ["Gamma System"],
        "EMP0008": ["Alpha Project"],
        "EMP0009": [],
        "EMP0010": ["Beta Platform"],
    }

    perf_scores = {
        "EMP0001": 9.0, "EMP0002": 8.5, "EMP0003": 8.0,
        "EMP0004": 7.5, "EMP0005": 9.5, "EMP0006": 6.0,
        "EMP0007": 7.0, "EMP0008": 5.5, "EMP0009": 4.0,
        "EMP0010": 8.2,
    }

    for emp in samples:
        try:
            company.add_employee(emp)
        except Exception:
            pass

    for emp_id, projects in projects_data.items():
        for proj in projects:
            try:
                company.assign_project(emp_id, proj)
            except Exception:
                pass

    for emp_id, score in perf_scores.items():
        try:
            company.set_performance(emp_id, score)
        except Exception:
            pass


def main():
    initialize_db()
    app = QApplication(sys.argv)
    app.setFont(QFont("Segoe UI", 10))
    app.setApplicationName("Employee Management System")

    window = MainApp()
    seed_sample_data(window.company)
    window._refresh_employee_table()
    window._update_stats()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
