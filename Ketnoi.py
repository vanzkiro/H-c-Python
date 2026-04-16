#Khoi tao ket noi csdl
import sqlite3
con = sqlite3.connect("quanlysinhvien.db")
cur = con.cursor()

#tao cau truc bang du lieu------
#cur.execute("CREATE TABLE sinhvien (MaSinhVien text PRIMARY KEY, HoVaTen text, GioiTinh integer, NgaySinh text, QueQuan text)")

#---- Them du lieu vao bang du lieu
# cur.execute("INSERT INTO sinhvien VALUES ('SV001','Nguyễn Văn Minh',0,'2000-01-10','Hà Nội')")
# cur.execute("INSERT INTO sinhvien VALUES ('SV002','Phạm Thị Lan',1,'2000-06-02','Thái Bình')")
# cur.execute("INSERT INTO sinhvien VALUES ('SV003','Lê Xuân Lan',1,'2001-05-02','Hà Nội')")
# cur.execute("INSERT INTO sinhvien VALUES ('SV004','Nguyễn Như Quỳnh',1,'2001-01-04','Hải Phòng')")

#------------------
#lay ra danh sach sinh vien ho "Phạm"
dataset = cur.execute("SELECT * FROM sinhvien WHERE HoVaTen LIKE '%Phạm%'")
for row in dataset:
    print(row) #hien thi tung dong

dataset = cur.execute("SELECT * FROM sinhvien WHERE HoVaTen LIKE '%Phạm%'")
for row in dataset:
    for col in row:
        print(col) #hien thi tung cot 

#----dataset = cur.execute("SELECT name FROM sqlite_master WHERE type = 'table' AND name = 'sinhvien'")
if dataset.rowcount == 0:
    print("Khong ton tai bang sinh vien")
else:
    print("Da ton tai ")

#------------------
dataset1 = cur.execute("SELECT typeof(MaSinhVien), typeof(HoVaTen), typeof(GioiTinh), typeof(NgaySinh), typeof(QueQuan) FROM sinhvien")
for row in dataset1:
    print(row) 

# cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
# tables = cur.fetchall() print("Các bảng trong DB:", tables)

#------------------
cur.execute("UPDATE sinhvien SET HoVaTen = 'Nguyễn Văn An' WHERE MaSinhVien = 'SV001'")
print("da cap nhat")


cur.execute("DELETE FROM sinhvien WHERE MaSinhVien = 'SV004'")
cur.execute("DELETE FROM sinhvien WHERE MaSinhVien = 'SV003'")
print("da xoa")

cur.execute("SELECT * FROM sinhvien")
for row in dataset:
    print(row) #hien thi tung dong

#cap nhat thay doi vao database
con.commit()
#dong ket noi
con.close()



# tao cau truc bang du lieu xep loai, co khoa ngoai la MaSinhVien
# cur.execute("CREATE TABLE xeploai (MaSinhVien text NOT NULL, HocKy integer, XL text, FOREIGN KEY (MaSinhVien) REFERENCES sinhvien(MaSinhVien))")

