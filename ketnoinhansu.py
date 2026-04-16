import sys
import sqlite3
from PyQt6.QtWidgets import *
from nhansu import Ui_Dialog


class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.con = sqlite3.connect("nhansu.db")
        self.cur = self.con.cursor()

        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS nhansu (
            CCCD TEXT PRIMARY KEY,
            HoTen TEXT,
            NgaySinh TEXT,
            GioiTinh TEXT,
            DiaChi TEXT
        )
        """)

        self.load_data()

        self.ui.btnThem.clicked.connect(self.them)
        self.ui.btnSua.clicked.connect(self.sua)
        self.ui.btnXoa.clicked.connect(self.xoa)
        self.ui.btnTim.clicked.connect(self.tim)

        self.ui.tableWidget.cellClicked.connect(self.fill_data)


    def load_data(self):
        self.ui.tableWidget.setRowCount(0)

        dataset = self.cur.execute("SELECT * FROM nhansu")
        rows = dataset.fetchall()

        for i, row in enumerate(rows):
            self.ui.tableWidget.insertRow(i)
            for j, val in enumerate(row):
                self.ui.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))

    def them(self):
        cccd = self.ui.txt_cccd.text()
        ten = self.ui.txt_ten.text()
        ns = self.ui.txt_ns.text()
        gt = self.ui.cb_gt.currentText()
        dc = self.ui.txt_dc.text()

        if cccd == "" or ten == "":
            QMessageBox.warning(self, "Lỗi", "Thiếu dữ liệu")
            return

        try:
            self.cur.execute("INSERT INTO nhansu VALUES (?,?,?,?,?)",
                             (cccd, ten, ns, gt, dc))
            self.con.commit()

            self.load_data()
            QMessageBox.information(self, "OK", "Đã thêm")
        except:
            QMessageBox.warning(self, "Lỗi", "CCCD đã tồn tại")

    def sua(self):
        cccd = self.ui.txt_cccd.text()
        ten = self.ui.txt_ten.text()
        ns = self.ui.txt_ns.text()
        gt = self.ui.cb_gt.currentText()
        dc = self.ui.txt_dc.text()

        self.cur.execute("""
        UPDATE nhansu
        SET HoTen=?, NgaySinh=?, GioiTinh=?, DiaChi=?
        WHERE CCCD=?
        """, (ten, ns, gt, dc, cccd))

        self.con.commit()
        self.load_data()
        QMessageBox.information(self, "OK", "Đã sửa")


    def xoa(self):
        row = self.ui.tableWidget.currentRow()

        if row == -1:
            QMessageBox.warning(self, "Lỗi", "Chọn dòng cần xóa")
            return

        cccd = self.ui.tableWidget.item(row, 0).text()

        self.cur.execute("DELETE FROM nhansu WHERE CCCD=?", (cccd,))
        self.con.commit()

        self.load_data()
        QMessageBox.information(self, "OK", "Đã xóa")

    def tim(self):
        key = self.ui.txt_tim.text()

        self.ui.tableWidget.setRowCount(0)

        dataset = self.cur.execute("""
        SELECT * FROM nhansu
        WHERE CCCD LIKE ? OR HoTen LIKE ? OR DiaChi LIKE ?
        """, (f"%{key}%", f"%{key}%", f"%{key}%"))

        rows = dataset.fetchall()

        for i, row in enumerate(rows):
            self.ui.tableWidget.insertRow(i)
            for j, val in enumerate(row):
                self.ui.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))

    def fill_data(self, row, col):
        self.ui.txt_cccd.setText(self.ui.tableWidget.item(row, 0).text())
        self.ui.txt_ten.setText(self.ui.tableWidget.item(row, 1).text())
        self.ui.txt_ns.setText(self.ui.tableWidget.item(row, 2).text())
        self.ui.cb_gt.setCurrentText(self.ui.tableWidget.item(row, 3).text())
        self.ui.txt_dc.setText(self.ui.tableWidget.item(row, 4).text())


# ===== RUN =====
app = QApplication(sys.argv)
window = Main()
window.show()
sys.exit(app.exec())