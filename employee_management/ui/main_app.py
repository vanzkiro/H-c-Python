import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QLineEdit, QTableWidget, QTableWidgetItem,
    QStackedWidget, QFrame, QDialog, QFormLayout, QComboBox,
    QDoubleSpinBox, QSpinBox, QHeaderView, QMessageBox, QSplitter,
    QTextEdit, QGroupBox, QGridLayout, QScrollArea, QToolBar, QStatusBar
)
from PyQt6.QtCore import Qt, QSize, pyqtSignal
from PyQt6.QtGui import QFont, QColor, QPalette, QIcon, QAction

import matplotlib
matplotlib.use('QtAgg')
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

from services.company import Company
from services.payroll import PayrollService
from models import Manager, Developer, Intern
from exceptions.employee_exceptions import *
from utils.validators import *
from utils.formatters import format_currency, format_employee_info

# ─── STYLESHEET ───────────────────────────────────────────────────────────────
STYLESHEET = """
QMainWindow, QDialog {
    background-color: #0f172a;
}
QWidget {
    background-color: #0f172a;
    color: #e2e8f0;
    font-family: 'Segoe UI', sans-serif;
    font-size: 13px;
}
QFrame#sidebar {
    background-color: #1e293b;
    border-right: 2px solid #334155;
    min-width: 200px;
    max-width: 200px;
}
QLabel#logoLabel {
    color: #60a5fa;
    font-size: 22px;
    font-weight: bold;
    padding: 20px 10px 10px 10px;
    qproperty-alignment: AlignCenter;
}
QLabel#sectionLabel {
    color: #94a3b8;
    font-size: 10px;
    padding: 8px 16px 2px 16px;
    letter-spacing: 1px;
}
QPushButton#navBtn {
    background-color: transparent;
    color: #94a3b8;
    border: none;
    border-radius: 8px;
    padding: 12px 16px;
    text-align: left;
    font-size: 13px;
}
QPushButton#navBtn:hover {
    background-color: #1e40af;
    color: #e2e8f0;
}
QPushButton#navBtn:checked {
    background-color: #2563eb;
    color: #ffffff;
    font-weight: bold;
}
QLabel#pageTitle {
    color: #f1f5f9;
    font-size: 22px;
    font-weight: bold;
    padding: 8px 0;
}
QPushButton#primaryBtn {
    background-color: #2563eb;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 9px 20px;
    font-weight: bold;
}
QPushButton#primaryBtn:hover { background-color: #1d4ed8; }
QPushButton#dangerBtn {
    background-color: #dc2626;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 9px 20px;
    font-weight: bold;
}
QPushButton#dangerBtn:hover { background-color: #b91c1c; }
QPushButton#secondaryBtn {
    background-color: #334155;
    color: #e2e8f0;
    border: none;
    border-radius: 8px;
    padding: 9px 20px;
}
QPushButton#secondaryBtn:hover { background-color: #475569; }
QLineEdit, QComboBox, QSpinBox, QDoubleSpinBox {
    background-color: #1e293b;
    color: #e2e8f0;
    border: 1px solid #334155;
    border-radius: 6px;
    padding: 7px 10px;
    font-size: 13px;
}
QLineEdit:focus, QComboBox:focus, QSpinBox:focus, QDoubleSpinBox:focus {
    border: 1px solid #2563eb;
}
QComboBox::drop-down { border: none; }
QComboBox::down-arrow { image: none; border: none; }
QTableWidget {
    background-color: #1e293b;
    alternate-background-color: #162032;
    color: #e2e8f0;
    border: 1px solid #334155;
    border-radius: 8px;
    gridline-color: #334155;
    selection-background-color: #2563eb;
}
QTableWidget::item { padding: 6px 10px; }
QHeaderView::section {
    background-color: #0f172a;
    color: #60a5fa;
    padding: 8px 10px;
    border: none;
    border-bottom: 2px solid #2563eb;
    font-weight: bold;
}
QGroupBox {
    border: 1px solid #334155;
    border-radius: 8px;
    margin-top: 10px;
    padding-top: 10px;
    color: #60a5fa;
    font-weight: bold;
}
QGroupBox::title {
    subcontrol-origin: margin;
    left: 12px;
    top: -6px;
    padding: 0 4px;
}
QScrollBar:vertical {
    background: #1e293b;
    width: 8px;
    border-radius: 4px;
}
QScrollBar::handle:vertical {
    background: #475569;
    border-radius: 4px;
}
QStatusBar {
    background-color: #1e293b;
    color: #94a3b8;
    border-top: 1px solid #334155;
}
QTextEdit {
    background-color: #1e293b;
    color: #e2e8f0;
    border: 1px solid #334155;
    border-radius: 6px;
    padding: 8px;
}
QLabel#statCard {
    background-color: #1e293b;
    border: 1px solid #334155;
    border-radius: 10px;
    padding: 16px;
}
"""

# ─── EMPLOYEE DIALOG ──────────────────────────────────────────────────────────
class EmployeeDialog(QDialog):
    def __init__(self, parent=None, employee=None):
        super().__init__(parent)
        self.employee = employee
        self.setWindowTitle("Thêm Nhân Viên" if not employee else "Sửa Nhân Viên")
        self.setMinimumWidth(460)
        self.setStyleSheet(STYLESHEET)
        self._build_ui()
        if employee:
            self._fill_data(employee)

    def _build_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(12)

        title = QLabel("THÔNG TIN NHÂN VIÊN")
        title.setObjectName("pageTitle")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)

        form = QFormLayout()
        form.setSpacing(10)
        form.setLabelAlignment(Qt.AlignmentFlag.AlignRight)

        self.txtId = QLineEdit(); self.txtId.setPlaceholderText("VD: EMP0001")
        self.txtName = QLineEdit(); self.txtName.setPlaceholderText("Họ và tên đầy đủ")
        self.spinAge = QSpinBox(); self.spinAge.setRange(18, 65); self.spinAge.setValue(25)
        self.txtEmail = QLineEdit(); self.txtEmail.setPlaceholderText("email@company.com")
        self.spinSalary = QDoubleSpinBox()
        self.spinSalary.setRange(1_000_000, 100_000_000)
        self.spinSalary.setValue(10_000_000)
        self.spinSalary.setSingleStep(500_000)
        self.spinSalary.setSuffix(" VNĐ")
        self.cboDept = QComboBox()
        self.cboDept.addItems(["Kỹ thuật", "Kinh doanh", "Nhân sự", "Kế toán", "Marketing", "Vận hành"])
        self.cboRole = QComboBox()
        self.cboRole.addItems(["Developer", "Manager", "Intern"])
        self.cboRole.currentTextChanged.connect(self._on_role_changed)
        self.txtExtra = QLineEdit(); self.txtExtra.setPlaceholderText("Tech stack (VD: Python, React)")
        self.lblExtra = QLabel("Tech Stack")

        form.addRow("Mã NV *", self.txtId)
        form.addRow("Họ tên *", self.txtName)
        form.addRow("Tuổi *", self.spinAge)
        form.addRow("Email *", self.txtEmail)
        form.addRow("Lương CB *", self.spinSalary)
        form.addRow("Phòng ban", self.cboDept)
        form.addRow("Chức vụ *", self.cboRole)
        form.addRow(self.lblExtra, self.txtExtra)
        layout.addLayout(form)

        btn_row = QHBoxLayout()
        self.btnSave = QPushButton("💾  Lưu"); self.btnSave.setObjectName("primaryBtn")
        self.btnCancel = QPushButton("✖  Hủy"); self.btnCancel.setObjectName("secondaryBtn")
        self.btnSave.clicked.connect(self.accept)
        self.btnCancel.clicked.connect(self.reject)
        btn_row.addWidget(self.btnSave)
        btn_row.addWidget(self.btnCancel)
        layout.addLayout(btn_row)

    def _on_role_changed(self, role):
        labels = {"Manager": "Số nhân viên", "Developer": "Tech Stack", "Intern": "Trường học"}
        placeholders = {"Manager": "VD: 5", "Developer": "VD: Python, Django", "Intern": "VD: ĐHBK Hà Nội"}
        self.lblExtra.setText(labels.get(role, "Thông tin thêm"))
        self.txtExtra.setPlaceholderText(placeholders.get(role, ""))

    def _fill_data(self, emp):
        self.txtId.setText(emp.emp_id)
        self.txtId.setReadOnly(True)
        self.txtName.setText(emp.name)
        self.spinAge.setValue(emp.age)
        self.txtEmail.setText(emp.email)
        self.spinSalary.setValue(emp.base_salary)
        idx = self.cboDept.findText(emp.department)
        if idx >= 0: self.cboDept.setCurrentIndex(idx)
        role_idx = self.cboRole.findText(emp.get_role())
        if role_idx >= 0: self.cboRole.setCurrentIndex(role_idx)
        extra = ""
        if hasattr(emp, 'team_size'): extra = str(emp.team_size)
        elif hasattr(emp, 'tech_stack'): extra = emp.tech_stack
        elif hasattr(emp, 'school'): extra = emp.school
        self.txtExtra.setText(extra)

    def get_data(self):
        return {
            'emp_id': self.txtId.text().strip().upper(),
            'name': self.txtName.text().strip(),
            'age': self.spinAge.value(),
            'email': self.txtEmail.text().strip(),
            'base_salary': self.spinSalary.value(),
            'department': self.cboDept.currentText(),
            'role': self.cboRole.currentText(),
            'extra': self.txtExtra.text().strip()
        }


# ─── PROJECT DIALOG ───────────────────────────────────────────────────────────
class ProjectDialog(QDialog):
    def __init__(self, parent=None, emp_id=""):
        super().__init__(parent)
        self.setWindowTitle("Phân Công Dự Án")
        self.setMinimumWidth(380)
        self.setStyleSheet(STYLESHEET)
        self._build_ui(emp_id)

    def _build_ui(self, emp_id):
        layout = QVBoxLayout(self)
        layout.setSpacing(12)

        title = QLabel("PHÂN CÔNG DỰ ÁN")
        title.setObjectName("pageTitle")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)

        form = QFormLayout()
        form.setSpacing(10)
        self.txtEmpId = QLineEdit(emp_id)
        self.txtEmpId.setPlaceholderText("EMP0001")
        self.cboProject = QComboBox()
        self.cboProject.addItems([
            "Alpha Project", "Beta Platform", "Gamma System",
            "Delta App", "Epsilon API", "Zeta Portal", "Khác..."
        ])
        self.cboProject.currentTextChanged.connect(self._on_project_changed)
        self.txtCustom = QLineEdit()
        self.txtCustom.setPlaceholderText("Nhập tên dự án tùy chỉnh")
        self.txtCustom.setVisible(False)

        form.addRow("Mã nhân viên", self.txtEmpId)
        form.addRow("Dự án", self.cboProject)
        form.addRow("Tên khác", self.txtCustom)
        layout.addLayout(form)

        btn_row = QHBoxLayout()
        btnAssign = QPushButton("✔  Phân Công"); btnAssign.setObjectName("primaryBtn")
        btnCancel = QPushButton("✖  Hủy"); btnCancel.setObjectName("secondaryBtn")
        btnAssign.clicked.connect(self.accept)
        btnCancel.clicked.connect(self.reject)
        btn_row.addWidget(btnAssign)
        btn_row.addWidget(btnCancel)
        layout.addLayout(btn_row)

    def _on_project_changed(self, text):
        self.txtCustom.setVisible(text == "Khác...")

    def get_data(self):
        proj = self.txtCustom.text().strip() if self.cboProject.currentText() == "Khác..." else self.cboProject.currentText()
        return {'emp_id': self.txtEmpId.text().strip().upper(), 'project': proj}


# ─── PERFORMANCE DIALOG ───────────────────────────────────────────────────────
class PerformanceDialog(QDialog):
    def __init__(self, parent=None, emp_id=""):
        super().__init__(parent)
        self.setWindowTitle("Đánh Giá Hiệu Suất")
        self.setMinimumWidth(360)
        self.setStyleSheet(STYLESHEET)
        self._build_ui(emp_id)

    def _build_ui(self, emp_id):
        layout = QVBoxLayout(self)
        layout.setSpacing(12)

        title = QLabel("ĐÁNH GIÁ HIỆU SUẤT")
        title.setObjectName("pageTitle")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)

        form = QFormLayout()
        form.setSpacing(10)
        self.txtEmpId = QLineEdit(emp_id)
        self.spinScore = QDoubleSpinBox()
        self.spinScore.setRange(0.0, 10.0)
        self.spinScore.setSingleStep(0.5)
        self.spinScore.setValue(7.0)
        self.spinScore.valueChanged.connect(self._update_rating)
        self.lblRating = QLabel("Tốt")
        self.lblRating.setStyleSheet("color: #22c55e; font-weight: bold; font-size: 14px;")

        form.addRow("Mã nhân viên", self.txtEmpId)
        form.addRow("Điểm (0–10)", self.spinScore)
        form.addRow("Xếp loại", self.lblRating)
        layout.addLayout(form)

        btn_row = QHBoxLayout()
        btnSave = QPushButton("💾  Lưu"); btnSave.setObjectName("primaryBtn")
        btnCancel = QPushButton("✖  Hủy"); btnCancel.setObjectName("secondaryBtn")
        btnSave.clicked.connect(self.accept)
        btnCancel.clicked.connect(self.reject)
        btn_row.addWidget(btnSave)
        btn_row.addWidget(btnCancel)
        layout.addLayout(btn_row)

    def _update_rating(self, val):
        if val >= 9:
            txt, color = "Xuất sắc ⭐", "#f59e0b"
        elif val >= 7:
            txt, color = "Tốt ✅", "#22c55e"
        elif val >= 5:
            txt, color = "Trung bình ⚠", "#fb923c"
        else:
            txt, color = "Yếu ❌", "#ef4444"
        self.lblRating.setText(txt)
        self.lblRating.setStyleSheet(f"color: {color}; font-weight: bold; font-size: 14px;")

    def get_data(self):
        return {'emp_id': self.txtEmpId.text().strip().upper(), 'score': self.spinScore.value()}


# ─── STAT CARD ────────────────────────────────────────────────────────────────
class StatCard(QFrame):
    def __init__(self, icon, title, value, color="#60a5fa"):
        super().__init__()
        self.setObjectName("sidebar")
        self.setStyleSheet(f"""
            QFrame {{ background-color: #1e293b; border: 1px solid #334155;
                      border-radius: 12px; padding: 16px; border-left: 4px solid {color}; }}
        """)
        layout = QVBoxLayout(self)
        layout.setSpacing(4)
        top = QHBoxLayout()
        ico = QLabel(icon); ico.setStyleSheet(f"font-size: 24px; color: {color}; background: transparent; border: none;")
        top.addWidget(ico)
        top.addStretch()
        layout.addLayout(top)
        self.valLabel = QLabel(str(value))
        self.valLabel.setStyleSheet(f"font-size: 28px; font-weight: bold; color: {color}; background: transparent; border: none;")
        layout.addWidget(self.valLabel)
        ttl = QLabel(title)
        ttl.setStyleSheet("color: #94a3b8; font-size: 12px; background: transparent; border: none;")
        layout.addWidget(ttl)

    def update_value(self, v):
        self.valLabel.setText(str(v))


# ─── MAIN APP WINDOW ──────────────────────────────────────────────────────────
class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.company = Company()
        self.setWindowTitle("Hệ Thống Quản Lý Nhân Viên Công Ty")
        self.setMinimumSize(1200, 720)
        self.setStyleSheet(STYLESHEET)
        self._build_ui()
        self._refresh_employee_table()
        self._update_stats()

    # ── BUILD UI ──────────────────────────────────────────────────────────────
    def _build_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        root = QHBoxLayout(central)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        # Sidebar
        sidebar = QFrame(); sidebar.setObjectName("sidebar")
        sidebar.setFixedWidth(210)
        sb_layout = QVBoxLayout(sidebar)
        sb_layout.setContentsMargins(10, 10, 10, 10)
        sb_layout.setSpacing(4)

        logo = QLabel(" EMS"); logo.setObjectName("logoLabel")
        sb_layout.addWidget(logo)
        sub = QLabel("QUẢN LÝ"); sub.setObjectName("sectionLabel")
        sb_layout.addWidget(sub)

        self._nav_buttons = []
        nav_items = [
            (" Nhân Viên", self._show_employees),
            (" Dự Án", self._show_projects),
            (" Bảng Lương", self._show_salary),
            (" Hiệu Suất", self._show_performance),
            (" Báo Cáo", self._show_reports),
        ]
        for label, slot in nav_items:
            btn = QPushButton(label); btn.setObjectName("navBtn")
            btn.setCheckable(True)
            btn.clicked.connect(slot)
            sb_layout.addWidget(btn)
            self._nav_buttons.append(btn)

        self._nav_buttons[0].setChecked(True)
        sb_layout.addStretch()

        ver = QLabel("v1.0.0  |  EMS 2025")
        ver.setStyleSheet("color: #475569; font-size: 10px; padding: 8px;")
        ver.setAlignment(Qt.AlignmentFlag.AlignCenter)
        sb_layout.addWidget(ver)

        root.addWidget(sidebar)

        # Stacked pages
        self.stack = QStackedWidget()
        self.stack.addWidget(self._build_employees_page())   # 0
        self.stack.addWidget(self._build_projects_page())    # 1
        self.stack.addWidget(self._build_salary_page())      # 2
        self.stack.addWidget(self._build_performance_page()) # 3
        self.stack.addWidget(self._build_reports_page())     # 4
        root.addWidget(self.stack)

        # Status bar
        self.statusBar().showMessage("✅  Hệ thống sẵn sàng")

    def _set_nav(self, idx):
        for i, btn in enumerate(self._nav_buttons):
            btn.setChecked(i == idx)
        self.stack.setCurrentIndex(idx)

    def _show_employees(self):   self._set_nav(0); self._refresh_employee_table()
    def _show_projects(self):    self._set_nav(1); self._refresh_project_table()
    def _show_salary(self):      self._set_nav(2); self._refresh_salary_table()
    def _show_performance(self): self._set_nav(3); self._refresh_perf_table()
    def _show_reports(self):     self._set_nav(4); self._draw_charts()

    # ── PAGE: EMPLOYEES ───────────────────────────────────────────────────────
    def _build_employees_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setContentsMargins(20, 16, 20, 16)
        layout.setSpacing(12)

        # Stats row
        stats_row = QHBoxLayout()
        self.cardTotal = StatCard("👥", "Tổng nhân viên", 0, "#60a5fa")
        self.cardMgr = StatCard("👔", "Manager", 0, "#f59e0b")
        self.cardDev = StatCard("💻", "Developer", 0, "#22c55e")
        self.cardIntern = StatCard("🎓", "Intern", 0, "#a78bfa")
        for c in [self.cardTotal, self.cardMgr, self.cardDev, self.cardIntern]:
            stats_row.addWidget(c)
        layout.addLayout(stats_row)

        # Search + buttons
        ctrl = QHBoxLayout()
        self.txtSearch = QLineEdit(); self.txtSearch.setPlaceholderText(" Tìm theo tên hoặc ID...")
        self.txtSearch.textChanged.connect(self._search_employees)
        self.txtSearch.setMinimumWidth(300)
        btnAdd = QPushButton(" Thêm NV"); btnAdd.setObjectName("primaryBtn")
        btnEdit = QPushButton(" Sửa"); btnEdit.setObjectName("secondaryBtn")
        btnDel = QPushButton(" Xóa"); btnDel.setObjectName("dangerBtn")
        btnDetail = QPushButton(" Chi tiết"); btnDetail.setObjectName("secondaryBtn")
        btnAdd.clicked.connect(self._add_employee)
        btnEdit.clicked.connect(self._edit_employee)
        btnDel.clicked.connect(self._delete_employee)
        btnDetail.clicked.connect(self._view_detail)
        ctrl.addWidget(self.txtSearch)
        ctrl.addStretch()
        for b in [btnDetail, btnEdit, btnDel, btnAdd]:
            ctrl.addWidget(b)
        layout.addLayout(ctrl)

        # Table
        self.tblEmployees = self._make_table(
            ["Mã NV", "Họ Tên", "Tuổi", "Email", "Chức Vụ", "Phòng Ban",
             "Lương CB", "Lương TT", "Dự Án", "Hiệu Suất"])
        layout.addWidget(self.tblEmployees)
        return page

    # ── PAGE: PROJECTS ────────────────────────────────────────────────────────
    def _build_projects_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setContentsMargins(20, 16, 20, 16)
        layout.setSpacing(12)

        title = QLabel(" QUẢN LÝ DỰ ÁN"); title.setObjectName("pageTitle")
        layout.addWidget(title)

        ctrl = QHBoxLayout()
        btnAssign = QPushButton(" Phân Công Dự Án"); btnAssign.setObjectName("primaryBtn")
        btnRemove = QPushButton(" Gỡ Dự Án"); btnRemove.setObjectName("dangerBtn")
        btnAssign.clicked.connect(self._assign_project)
        btnRemove.clicked.connect(self._remove_project)
        ctrl.addStretch()
        ctrl.addWidget(btnRemove)
        ctrl.addWidget(btnAssign)
        layout.addLayout(ctrl)

        self.tblProjects = self._make_table(
            ["Mã NV", "Họ Tên", "Chức Vụ", "Phòng Ban", "Số Dự Án", "Danh Sách Dự Án"])
        layout.addWidget(self.tblProjects)
        return page

    # ── PAGE: SALARY ──────────────────────────────────────────────────────────
    def _build_salary_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setContentsMargins(20, 16, 20, 16)
        layout.setSpacing(12)

        title = QLabel(" BẢNG LƯƠNG"); title.setObjectName("pageTitle")
        layout.addWidget(title)

        ctrl = QHBoxLayout()
        btnTop10 = QPushButton(" Top 10 Lương Cao Nhất"); btnTop10.setObjectName("primaryBtn")
        btnAll = QPushButton(" Tất Cả"); btnAll.setObjectName("secondaryBtn")
        btnTop10.clicked.connect(lambda: self._refresh_salary_table(top=10))
        btnAll.clicked.connect(lambda: self._refresh_salary_table(top=None))
        ctrl.addStretch()
        ctrl.addWidget(btnAll)
        ctrl.addWidget(btnTop10)
        layout.addLayout(ctrl)

        self.tblSalary = self._make_table(
            ["#", "Mã NV", "Họ Tên", "Chức Vụ", "Phòng Ban",
             "Lương Cơ Bản", "Lương Thực Tế", "Hiệu Suất", "Xếp Loại"])
        layout.addWidget(self.tblSalary)
        return page

    # ── PAGE: PERFORMANCE ─────────────────────────────────────────────────────
    def _build_performance_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setContentsMargins(20, 16, 20, 16)
        layout.setSpacing(12)

        title = QLabel(" ĐÁNH GIÁ HIỆU SUẤT"); title.setObjectName("pageTitle")
        layout.addWidget(title)

        ctrl = QHBoxLayout()
        btnEval = QPushButton(" Đánh Giá NV"); btnEval.setObjectName("primaryBtn")
        btnEval.clicked.connect(self._evaluate_performance)
        ctrl.addStretch()
        ctrl.addWidget(btnEval)
        layout.addLayout(ctrl)

        self.tblPerf = self._make_table(
            ["Mã NV", "Họ Tên", "Chức Vụ", "Phòng Ban", "Điểm", "Xếp Loại", "Số Dự Án"])
        layout.addWidget(self.tblPerf)
        return page

    # ── PAGE: REPORTS ─────────────────────────────────────────────────────────
    def _build_reports_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setContentsMargins(20, 16, 20, 16)
        layout.setSpacing(12)

        title = QLabel(" BÁO CÁO & THỐNG KÊ"); title.setObjectName("pageTitle")
        layout.addWidget(title)

        ctrl = QHBoxLayout()
        btnRefresh = QPushButton(" Làm mới biểu đồ"); btnRefresh.setObjectName("primaryBtn")
        btnRefresh.clicked.connect(self._draw_charts)
        ctrl.addStretch()
        ctrl.addWidget(btnRefresh)
        layout.addLayout(ctrl)

        charts_widget = QWidget()
        charts_layout = QGridLayout(charts_widget)
        charts_layout.setSpacing(12)

        self.fig = Figure(figsize=(14, 8), facecolor='#0f172a')
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setStyleSheet("background-color: #0f172a;")
        charts_layout.addWidget(self.canvas, 0, 0)

        layout.addWidget(charts_widget)
        return page

    # ── HELPERS ───────────────────────────────────────────────────────────────
    def _make_table(self, headers):
        tbl = QTableWidget()
        tbl.setColumnCount(len(headers))
        tbl.setHorizontalHeaderLabels(headers)
        tbl.setAlternatingRowColors(True)
        tbl.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        tbl.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        tbl.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        tbl.verticalHeader().setVisible(False)
        return tbl

    def _tbl_item(self, text, color=None, bold=False):
        item = QTableWidgetItem(str(text))
        item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        if color:
            item.setForeground(QColor(color))
        if bold:
            f = item.font(); f.setBold(True); item.setFont(f)
        return item

    def _role_color(self, role):
        return {"Manager": "#f59e0b", "Developer": "#22c55e", "Intern": "#a78bfa"}.get(role, "#e2e8f0")

    def _rating_color(self, rating):
        return {"Xuất sắc": "#f59e0b", "Tốt": "#22c55e", "Trung bình": "#fb923c", "Yếu": "#ef4444"}.get(rating, "#e2e8f0")

    # ── REFRESH TABLES ────────────────────────────────────────────────────────
    def _refresh_employee_table(self, emps=None):
        if emps is None:
            emps = self.company.get_all_employees()
        self.tblEmployees.setRowCount(0)
        for emp in emps:
            row = self.tblEmployees.rowCount()
            self.tblEmployees.insertRow(row)
            rc = self._role_color(emp.get_role())
            rating = emp.get_performance_rating()
            self.tblEmployees.setItem(row, 0, self._tbl_item(emp.emp_id, "#60a5fa", bold=True))
            self.tblEmployees.setItem(row, 1, self._tbl_item(emp.name))
            self.tblEmployees.setItem(row, 2, self._tbl_item(emp.age))
            self.tblEmployees.setItem(row, 3, self._tbl_item(emp.email))
            self.tblEmployees.setItem(row, 4, self._tbl_item(emp.get_role(), rc))
            self.tblEmployees.setItem(row, 5, self._tbl_item(emp.department))
            self.tblEmployees.setItem(row, 6, self._tbl_item(format_currency(emp.base_salary)))
            self.tblEmployees.setItem(row, 7, self._tbl_item(format_currency(emp.calculate_salary()), "#22c55e", bold=True))
            self.tblEmployees.setItem(row, 8, self._tbl_item(len(emp.projects)))
            self.tblEmployees.setItem(row, 9, self._tbl_item(f"{emp.performance_score} – {rating}", self._rating_color(rating)))

    def _refresh_project_table(self):
        emps = self.company.get_all_employees()
        self.tblProjects.setRowCount(0)
        for emp in emps:
            row = self.tblProjects.rowCount()
            self.tblProjects.insertRow(row)
            self.tblProjects.setItem(row, 0, self._tbl_item(emp.emp_id, "#60a5fa", bold=True))
            self.tblProjects.setItem(row, 1, self._tbl_item(emp.name))
            self.tblProjects.setItem(row, 2, self._tbl_item(emp.get_role(), self._role_color(emp.get_role())))
            self.tblProjects.setItem(row, 3, self._tbl_item(emp.department))
            cnt_color = "#ef4444" if len(emp.projects) >= 5 else "#22c55e"
            self.tblProjects.setItem(row, 4, self._tbl_item(f"{len(emp.projects)}/5", cnt_color, bold=True))
            self.tblProjects.setItem(row, 5, self._tbl_item(', '.join(emp.projects) if emp.projects else "—"))

    def _refresh_salary_table(self, top=None):
        emps = self.company.get_top_salaries(top) if top else self.company.get_all_employees()
        emps = sorted(emps, key=lambda e: e.calculate_salary(), reverse=True)
        self.tblSalary.setRowCount(0)
        for i, emp in enumerate(emps):
            row = self.tblSalary.rowCount()
            self.tblSalary.insertRow(row)
            rank_icons = {0: "🥇", 1: "🥈", 2: "🥉"}
            rank = rank_icons.get(i, f"{i+1}")
            self.tblSalary.setItem(row, 0, self._tbl_item(rank))
            self.tblSalary.setItem(row, 1, self._tbl_item(emp.emp_id, "#60a5fa", bold=True))
            self.tblSalary.setItem(row, 2, self._tbl_item(emp.name))
            self.tblSalary.setItem(row, 3, self._tbl_item(emp.get_role(), self._role_color(emp.get_role())))
            self.tblSalary.setItem(row, 4, self._tbl_item(emp.department))
            self.tblSalary.setItem(row, 5, self._tbl_item(format_currency(emp.base_salary)))
            self.tblSalary.setItem(row, 6, self._tbl_item(format_currency(emp.calculate_salary()), "#22c55e", bold=True))
            self.tblSalary.setItem(row, 7, self._tbl_item(emp.performance_score))
            rating = emp.get_performance_rating()
            self.tblSalary.setItem(row, 8, self._tbl_item(rating, self._rating_color(rating)))

    def _refresh_perf_table(self):
        emps = sorted(self.company.get_all_employees(), key=lambda e: e.performance_score, reverse=True)
        self.tblPerf.setRowCount(0)
        for emp in emps:
            row = self.tblPerf.rowCount()
            self.tblPerf.insertRow(row)
            rating = emp.get_performance_rating()
            self.tblPerf.setItem(row, 0, self._tbl_item(emp.emp_id, "#60a5fa", bold=True))
            self.tblPerf.setItem(row, 1, self._tbl_item(emp.name))
            self.tblPerf.setItem(row, 2, self._tbl_item(emp.get_role(), self._role_color(emp.get_role())))
            self.tblPerf.setItem(row, 3, self._tbl_item(emp.department))
            self.tblPerf.setItem(row, 4, self._tbl_item(emp.performance_score, "#60a5fa", bold=True))
            self.tblPerf.setItem(row, 5, self._tbl_item(rating, self._rating_color(rating)))
            self.tblPerf.setItem(row, 6, self._tbl_item(len(emp.projects)))

    # ── CHARTS ────────────────────────────────────────────────────────────────
    def _draw_charts(self):
        self.fig.clear()
        emps = self.company.get_all_employees()
        if not emps:
            ax = self.fig.add_subplot(111)
            ax.text(0.5, 0.5, "Chưa có dữ liệu", ha='center', va='center',
                    color='#94a3b8', fontsize=16, transform=ax.transAxes)
            ax.set_facecolor('#1e293b')
            self.canvas.draw()
            return

        colors = {'Manager': '#f59e0b', 'Developer': '#22c55e', 'Intern': '#a78bfa'}
        bg, text_c, grid_c = '#1e293b', '#e2e8f0', '#334155'

        # Chart 1: Role distribution (pie)
        ax1 = self.fig.add_subplot(221)
        role_counts = {}
        for e in emps:
            role_counts[e.get_role()] = role_counts.get(e.get_role(), 0) + 1
        wedge_colors = [colors.get(r, '#60a5fa') for r in role_counts.keys()]
        wedges, texts, autotexts = ax1.pie(
            role_counts.values(), labels=role_counts.keys(), autopct='%1.0f%%',
            colors=wedge_colors, startangle=90,
            textprops={'color': text_c, 'fontsize': 10},
            wedgeprops={'edgecolor': '#0f172a', 'linewidth': 2}
        )
        for at in autotexts:
            at.set_color('#0f172a'); at.set_fontweight('bold')
        ax1.set_facecolor(bg)
        ax1.set_title('Phân Bổ Chức Vụ', color='#60a5fa', fontweight='bold', pad=10)

        # Chart 2: Top 8 salary bar
        ax2 = self.fig.add_subplot(222)
        top_emps = sorted(emps, key=lambda e: e.calculate_salary(), reverse=True)[:8]
        names = [e.name.split()[-1] for e in top_emps]
        salaries = [e.calculate_salary() / 1_000_000 for e in top_emps]
        bar_colors = [colors.get(e.get_role(), '#60a5fa') for e in top_emps]
        bars = ax2.barh(names, salaries, color=bar_colors, edgecolor='#0f172a', linewidth=1.2)
        ax2.set_facecolor(bg)
        ax2.tick_params(colors=text_c)
        ax2.set_xlabel('Triệu VNĐ', color='#94a3b8', fontsize=9)
        ax2.set_title('Top 8 Lương Cao Nhất', color='#60a5fa', fontweight='bold', pad=10)
        ax2.xaxis.set_major_formatter(mticker.FormatStrFormatter('%.0f'))
        for spine in ax2.spines.values():
            spine.set_edgecolor(grid_c)
        for bar, sal in zip(bars, salaries):
            ax2.text(bar.get_width() + 0.2, bar.get_y() + bar.get_height()/2,
                     f'{sal:.1f}M', va='center', color=text_c, fontsize=8)

        # Chart 3: Project allocation
        ax3 = self.fig.add_subplot(223)
        proj_stats = self.company.get_project_stats()
        if proj_stats:
            proj_names = list(proj_stats.keys())[:8]
            proj_counts = [proj_stats[p] for p in proj_names]
            bar2_colors = ['#2563eb', '#22c55e', '#f59e0b', '#a78bfa', '#ef4444', '#fb923c', '#06b6d4', '#ec4899']
            ax3.bar(proj_names, proj_counts, color=bar2_colors[:len(proj_names)],
                    edgecolor='#0f172a', linewidth=1.2)
            ax3.set_facecolor(bg)
            ax3.tick_params(colors=text_c, labelsize=8)
            plt.setp(ax3.xaxis.get_majorticklabels(), rotation=30, ha='right')
            ax3.set_ylabel('Số NV', color='#94a3b8', fontsize=9)
            ax3.set_title('Phân Công Theo Dự Án', color='#60a5fa', fontweight='bold', pad=10)
            for spine in ax3.spines.values():
                spine.set_edgecolor(grid_c)
        else:
            ax3.text(0.5, 0.5, "Chưa có dự án", ha='center', va='center',
                     color='#94a3b8', fontsize=12, transform=ax3.transAxes)
            ax3.set_facecolor(bg)

        # Chart 4: Performance distribution
        ax4 = self.fig.add_subplot(224)
        rating_counts = {"Xuất sắc": 0, "Tốt": 0, "Trung bình": 0, "Yếu": 0}
        for e in emps:
            r = e.get_performance_rating()
            rating_counts[r] = rating_counts.get(r, 0) + 1
        r_colors = ["#f59e0b", "#22c55e", "#fb923c", "#ef4444"]
        ax4.bar(rating_counts.keys(), rating_counts.values(), color=r_colors,
                edgecolor='#0f172a', linewidth=1.2)
        ax4.set_facecolor(bg)
        ax4.tick_params(colors=text_c)
        ax4.set_ylabel('Số NV', color='#94a3b8', fontsize=9)
        ax4.set_title('Phân Bổ Hiệu Suất', color='#60a5fa', fontweight='bold', pad=10)
        for spine in ax4.spines.values():
            spine.set_edgecolor(grid_c)

        self.fig.set_facecolor('#0f172a')
        self.fig.tight_layout(pad=2.0)
        self.canvas.draw()

    # ── ACTIONS ───────────────────────────────────────────────────────────────
    def _update_stats(self):
        emps = self.company.get_all_employees()
        total = len(emps)
        mgr = sum(1 for e in emps if e.get_role() == "Manager")
        dev = sum(1 for e in emps if e.get_role() == "Developer")
        intern = sum(1 for e in emps if e.get_role() == "Intern")
        self.cardTotal.update_value(total)
        self.cardMgr.update_value(mgr)
        self.cardDev.update_value(dev)
        self.cardIntern.update_value(intern)
        self.statusBar().showMessage(f"✅  Tổng: {total} nhân viên  |  Manager: {mgr}  |  Developer: {dev}  |  Intern: {intern}")

    def _search_employees(self, text):
        if not text.strip():
            self._refresh_employee_table()
            return
        emps = self.company.get_all_employees()
        filtered = [e for e in emps if text.lower() in e.name.lower() or text.lower() in e.emp_id.lower()]
        self._refresh_employee_table(filtered)

    def _add_employee(self):
        dlg = EmployeeDialog(self)
        if dlg.exec() == QDialog.DialogCode.Accepted:
            data = dlg.get_data()
            try:
                emp = self._build_emp_from_data(data)
                self.company.add_employee(emp)
                self._refresh_employee_table()
                self._update_stats()
                QMessageBox.information(self, "Thành công", f"✅  Đã thêm nhân viên {emp.name}")
            except DuplicateEmployeeError:
                reply = QMessageBox.question(self, "Trùng ID",
                    f"ID {data['emp_id']} đã tồn tại. Tự động tạo ID mới?",
                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
                if reply == QMessageBox.StandardButton.Yes:
                    emp = self._build_emp_from_data(data)
                    new_id = self.company.add_employee(emp, auto_id=True)
                    self._refresh_employee_table()
                    self._update_stats()
                    QMessageBox.information(self, "Thành công", f"✅  Đã thêm với ID mới: {new_id}")
            except InvalidEmailError as e:
                QMessageBox.warning(self, "Email sai", f"❌ {e}")
            except Exception as ex:
                QMessageBox.warning(self, "Lỗi", f"❌  {ex}")

    def _build_emp_from_data(self, data):
        from utils.validators import (
            validate_emp_id,
            validate_email,
            validate_age,
            validate_salary
        )

        emp_id = validate_emp_id(data['emp_id'])
        name = data['name']

        age = validate_age(str(data['age']))
        email = validate_email(data['email'])
        base_salary = validate_salary(str(data['base_salary']))
        department = data['department']

        role = data['role']
        extra = data['extra']

        if role == "Manager":
            team_size = int(extra) if extra.isdigit() else 0
            return Manager(emp_id, name, age, email, base_salary, department, team_size)

        elif role == "Developer":
            return Developer(emp_id, name, age, email, base_salary, department, extra)

        else:
            return Intern(emp_id, name, age, email, base_salary, department, extra)
    def _get_selected_emp(self):
        row = self.tblEmployees.currentRow()
        if row < 0:
            QMessageBox.warning(self, "Chưa chọn", "⚠  Vui lòng chọn một nhân viên.")
            return None
        emp_id = self.tblEmployees.item(row, 0).text()
        try:
            return self.company.get_employee(emp_id)
        except EmployeeNotFoundError as e:
            QMessageBox.warning(self, "Lỗi", str(e))
            return None

    def _edit_employee(self):
        emp = self._get_selected_emp()
        if not emp:
            return
        dlg = EmployeeDialog(self, emp)
        if dlg.exec() == QDialog.DialogCode.Accepted:
            data = dlg.get_data()
            try:
                new_emp = self._build_emp_from_data(data)
                new_emp.projects = emp.projects.copy()
                new_emp.performance_score = emp.performance_score
                self.company.update_employee(new_emp)
                self._refresh_employee_table()
                QMessageBox.information(self, "Thành công", " Đã cập nhật thông tin.")
            except Exception as ex:
                QMessageBox.warning(self, "Lỗi", f"  {ex}")

    def _delete_employee(self):
        emp = self._get_selected_emp()
        if not emp:
            return
        reply = QMessageBox.question(self, "Xác nhận xóa",
            f"Bạn có chắc muốn xóa nhân viên:\n{emp.emp_id} – {emp.name}?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            try:
                self.company.remove_employee(emp.emp_id)
                self._refresh_employee_table()
                self._update_stats()
                QMessageBox.information(self, "Thành công", "✅  Đã xóa nhân viên.")
            except Exception as ex:
                QMessageBox.warning(self, "Lỗi", str(ex))

    def _view_detail(self):
        emp = self._get_selected_emp()
        if not emp:
            return
        dlg = QDialog(self)
        dlg.setWindowTitle(f"Chi tiết – {emp.name}")
        dlg.setMinimumSize(420, 350)
        dlg.setStyleSheet(STYLESHEET)
        layout = QVBoxLayout(dlg)
        txt = QTextEdit()
        txt.setReadOnly(True)
        txt.setPlainText(format_employee_info(emp))
        layout.addWidget(txt)
        btn = QPushButton("Đóng"); btn.setObjectName("secondaryBtn"); btn.clicked.connect(dlg.accept)
        layout.addWidget(btn)
        dlg.exec()

    def _assign_project(self):
        row = self.tblProjects.currentRow()
        emp_id = self.tblProjects.item(row, 0).text() if row >= 0 else ""
        dlg = ProjectDialog(self, emp_id)
        if dlg.exec() == QDialog.DialogCode.Accepted:
            data = dlg.get_data()
            try:
                self.company.assign_project(data['emp_id'], data['project'])
                self._refresh_project_table()
                self._refresh_employee_table()
                QMessageBox.information(self, "Thành công", f"✅  Đã phân công dự án '{data['project']}'.")
            except ProjectAllocationError as e:
                QMessageBox.warning(self, "Từ chối phân công", f"❌  {e}")
            except Exception as ex:
                QMessageBox.warning(self, "Lỗi", f"❌  {ex}")

    def _remove_project(self):
        row = self.tblProjects.currentRow()
        if row < 0:
            QMessageBox.warning(self, "Chưa chọn", "⚠  Vui lòng chọn nhân viên từ bảng."); return
        emp_id = self.tblProjects.item(row, 0).text()
        try:
            emp = self.company.get_employee(emp_id)
        except EmployeeNotFoundError as e:
            QMessageBox.warning(self, "Lỗi", str(e)); return
        if not emp.projects:
            QMessageBox.information(self, "Thông báo", "Nhân viên chưa có dự án nào."); return
        dlg = QDialog(self); dlg.setWindowTitle("Gỡ Dự Án"); dlg.setStyleSheet(STYLESHEET)
        layout = QVBoxLayout(dlg)
        layout.addWidget(QLabel(f"Chọn dự án cần gỡ khỏi {emp.name}:"))
        cbo = QComboBox(); cbo.addItems(emp.projects)
        layout.addWidget(cbo)
        btn_row = QHBoxLayout()
        btnOk = QPushButton("Gỡ"); btnOk.setObjectName("dangerBtn"); btnOk.clicked.connect(dlg.accept)
        btnNo = QPushButton("Hủy"); btnNo.setObjectName("secondaryBtn"); btnNo.clicked.connect(dlg.reject)
        btn_row.addWidget(btnOk); btn_row.addWidget(btnNo)
        layout.addLayout(btn_row)
        if dlg.exec() == QDialog.DialogCode.Accepted:
            self.company.remove_project(emp_id, cbo.currentText())
            self._refresh_project_table()
            self._refresh_employee_table()
            QMessageBox.information(self, "Thành công", "✅  Đã gỡ dự án.")

    def _evaluate_performance(self):
        row = self.tblPerf.currentRow()
        emp_id = self.tblPerf.item(row, 0).text() if row >= 0 else ""
        dlg = PerformanceDialog(self, emp_id)
        if dlg.exec() == QDialog.DialogCode.Accepted:
            data = dlg.get_data()
            try:
                self.company.set_performance(data['emp_id'], data['score'])
                self._refresh_perf_table()
                self._refresh_employee_table()
                QMessageBox.information(self, "Thành công", f"✅  Đã cập nhật điểm hiệu suất: {data['score']}/10")
            except InvalidScoreError as e:
                QMessageBox.warning(self, "Điểm không hợp lệ", f"❌  {e}")
            except Exception as ex:
                QMessageBox.warning(self, "Lỗi", f"❌  {ex}")
