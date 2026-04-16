from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        
        # --- Phần khởi tạo Widget (giữ nguyên của bạn) ---
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(70, 50, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 110, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=Dialog)
        self.label_3.setGeometry(QtCore.QRect(70, 160, 47, 13))
        self.label_3.setObjectName("label_3")
        self.btnTinhTong = QtWidgets.QPushButton(parent=Dialog)
        self.btnTinhTong.setGeometry(QtCore.QRect(160, 230, 75, 23))
        self.btnTinhTong.setObjectName("btnTinhTong")
        
        # Các ô nhập liệu kiểu QTextEdit
        self.txtN1 = QtWidgets.QTextEdit(parent=Dialog)
        self.txtN1.setGeometry(QtCore.QRect(140, 40, 104, 31))
        self.txtN1.setObjectName("txtN1")
        self.txtN2 = QtWidgets.QTextEdit(parent=Dialog)
        self.txtN2.setGeometry(QtCore.QRect(140, 100, 104, 31))
        self.txtN2.setObjectName("txtN2")
        self.txtKetQua = QtWidgets.QTextEdit(parent=Dialog)
        self.txtKetQua.setGeometry(QtCore.QRect(140, 150, 104, 31))
        self.txtKetQua.setObjectName("txtKetQua")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # --- BỔ SUNG: Kết nối sự kiện Click ---
        self.btnTinhTong.clicked.connect(self.xu_ly_tinh_tong)

    # --- BỔ SUNG: Hàm xử lý logic ---
    def xu_ly_tinh_tong(self):
        try:
            # Lấy dữ liệu từ QTextEdit bằng .toPlainText()
            str_n1 = self.txtN1.toPlainText()
            str_n2 = self.txtN2.toPlainText()
            
            # Chuyển sang số và tính toán
            tong = float(str_n1) + float(str_n2)
            
            # Hiển thị kết quả
            self.txtKetQua.setPlainText(str(tong))
        except ValueError:
            self.txtKetQua.setPlainText("Lỗi: Nhập số!")

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Tính Tổng"))
        self.label.setText(_translate("Dialog", "Số 1"))
        self.label_2.setText(_translate("Dialog", "Số 2"))
        self.label_3.setText(_translate("Dialog", "Tổng"))
        self.btnTinhTong.setText(_translate("Dialog", "Tính"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())