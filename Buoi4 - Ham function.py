def sayHello(name):  # def ten_ham(tham_so): #goi ham ten_ham(gia_tri_tham_so)
    """
    Ham truyen vao ten nguoi va tra ve mot chuoi
    """
    return "Hello, " + name

text = sayHello("Nguyen Van A")
print(text) 

def tonghieu(x,y):
    tong = x + y
    hieu = x - y
    return tong, hieu
t,h = tonghieu(10, 8)
print("Tong:", t)  
print("Hieu:", h)

#bien cuc bo - khai bao ben trong ham, chi su dung duoc trong ham do

b = 20
def msg():
    a = 10
    print("Gia tri a:", a)
    print("Gia tri b:", b)

    return
msg()
#print(a)  # loi vi a la bien cuc bo, chi su dung duoc trong ham msg()
print(b)

#tham so bat buoc, tham so mac dinh, 
def sum(_a, _b):
    _c = _a + _b
    print("Tong:", _c)
sum(5, 10)

#tham so mac dinh
def msg(_id, _name, _age = 23):
    print("ID:", _id)
    print("Name:", _name)
    print("Age:", _age)
    return
msg(1, "Nguyen Van A", 30)
msg(_id = 2, _name = "Nguyen Van B", _age = 25)
msg(_id = 3, _name = "Nguyen Van C")  # age mac dinh la 23

#tham so tu khoa 
def msg(_id, _name):
    print("ID:", _id)
    print("Name:", _name)
    return
msg(_id = 1, _name = "Nguyen Van A")
msg(_name = "Nguyen Van A", _id = 1)

#tham so thay doi  #def ten_ham(tham_so_chinh_thuc, *var):  #tham so thay doi se duoc truyen vao dang tuple
def printinfo(argl, *var):
    print("Output is: ")
    print(argl)
    for v in var:
        print(v)
    return

# viet chuong chinh ham tinh tong cho cac so 
def sum(*var):
    sum = 0
    for n in var:
        sum = sum + n
    return sum 
print("Tong:", sum(0, 1, 2, 3, 4, 5))


