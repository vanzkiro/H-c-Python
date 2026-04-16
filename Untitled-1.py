class SinhVien:
    def __init__(self, ho_ten = "",mssv = "", khoa = "", ngay_sinh = ""):
        self.ho_ten = ho_ten
        self.mssv = mssv
        self.khoa = khoa
        self.ngay_sinh = ngay_sinh
 
    def nhap(self):
        self.ho_ten = input("Nhap ho ten")
        self.mssv = input("Nhap ma")
        self.khoa = input("Nhap khoa")
        self.ngay_sinh = input("Nhap ntns")
    
    def hien(self):
        print(f"ten sv: {self.ho_ten} mssv: {self.mssv} khoa: {self.khoa} ngay sinh: {self.ngay_sinh}")
    
class QuanLySinhVien:
    def __init__(self):
        self.danh_sach_sv = []
    def them_sinh_vien(self):
        sv = SinhVien()
        sv.nhap()
        self.danh_sach_sv.append(sv)
        print("Them tc")
    def tim_sinh_vien(self, mssv):
        for sv in self.danh_sach_sv:
            if sv.mssv == mssv:
                return sv
        return None
    def xoa_sinh_vien(self):
        mssv = input("Nhap mssv can xoa")
        sv = self.tim_sinh_vien(mssv)

        if sv:
            self.danh_sach_sv.remove(sv)
            print("Xoa thanh cong")
        else:
            print("Khong tim thay sinh vien")

    def sua_sinh_vien(self):
        mssv = input("Nhap mssv can sua")
        sv = self.tim_sinh_vien(mssv)
        if sv:
            print("nhap")
            sv.ho_ten = input("nhap ho ten")
            sv.khoa = input("nhap khoa")
            sv.ngay_sinh = input("nhap ngay sinh")
            print("sua thanh cong")
        else:
            print("Khong tim thay sinh vien")

    def xem_ds_sv(self):
        if not self.danh_sach_sv:
            print("Danh sach rong")
        else:
            for sv in self.danh_sach_sv:
                sv.hien()
ql = QuanLySinhVien()
while True:
    print("nhap 1: de them sv")
    print("nhap 2: de xoa sv")
    print("nhap 3: sua sv")
    print("nhap 4: xem ds")
    print("nhap 0: break")

    chon = input("nhap lua chon")
    if chon == "1":
        ql.them_sinh_vien()
    elif chon == "2":
        ql.xoa_sinh_vien()
    elif chon == "3":
        ql.sua_sinh_vien()
    elif chon == "4":
        ql.xem_ds_sv()
    elif chon == "0":
        break
    else:
        print("nhap lai")


