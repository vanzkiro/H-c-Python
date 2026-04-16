

class Person:
    def __init__(self, name, age = 21, gender = "Male"):
        self.name = name
        self.age = age
        self.gender = gender
    
    def showInfo(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)

eva = Person("Eva", 20, "Female")
eva.showInfo()
print("---------")

adam = Person("Adam")
adam.showInfo()
print("---------")

cain = Person("Cain", 1)
cain.showInfo()

#--------------------------------------------------
class Hoc_Vien:
    def __init__(self, ten, ns, email, dt, dc, lop):
        self.ten = ten
        self.ns = ns
        self.email = email
        self.dt = dt
        self.dc = dc
        self.lop = lop
    def show_info(self):
        print("Ten: ", self.ten)
        print("Ngay sinh", self.ns)
        print("Email", self.dt)
        print("SDT", self.dc)
        print("Dia chi", self.lop)
        print("Lop", self.dt)

    def chang_info(self): #thay doi thong tin voi tham so mac finh truyen vao
        self.dc = "Ha Noi"
        self.lop = "IT14.3"

v = Hoc_Vien("Pham Quang Van", "2005-03-19", "abc@.com", "0123456789", "Thai Binh", "IT14.x")
v.show_info()
print("-------------")
v.chang_info()
v.show_info()

#---------------------------------------
class Phan_So:
    def __init__(self, tu_so, mau_so=1):
        if mau_so == 0:
            print("Mau so khong the bang 0")
        self.tu_so = tu_so
        self.mau_so = mau_so

    def nhan(self, other):
        result = Phan_So(self.tu_so * other.tu_so, self.mau_so * other.mau_so)
        return result

    def chia(self, other):
        if other.tu_so == 0:
            print("Khong the chia cho phan so co tu so bang 0")
        result = Phan_So(self.tu_so * other.mau_so, self.mau_so * other.tu_so)
        return result

    def cong(self, other):
        result = Phan_So(self.tu_so * other.mau_so + other.tu_so * self.mau_so, self.mau_so * other.mau_so)
        return result

    def tru(self, other):
        result = Phan_So(self.tu_so * other.mau_so - other.tu_so * self.mau_so, self.mau_so * other.mau_so)
        return result
    
    def toi_gian(self):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        ucln = gcd(abs(self.tu_so), abs(self.mau_so))
        self.tu_so //= ucln
        self.mau_so //= ucln
        if self.mau_so < 0:
            self.tu_so = -self.tu_so
            self.mau_so = -self.mau_so

    def __str__(self):
        return f"{self.tu_so}/{self.mau_so}"

ps1 = Phan_So(1, 2)
ps2 = Phan_So(3, 4)
pps1 = ps1.nhan(ps2)
pps2 = ps1.chia(ps2)
pps3 = ps1.cong(ps2)
pps4 = ps1.tru(ps2)
print(pps1)
print(pps2)
print(pps3)
print(pps4)