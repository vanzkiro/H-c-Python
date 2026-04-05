#viet ham tinh tong 2 so truyen vao 
def tong(_a, _b):
    return _a + _b
print("Tong:", tong(5, 10))
#viet ham tinh tong cac so truyen vao
def tong(*var):
    _sum = 0
    for n in var:
        _sum = _sum + n
    return _sum
print("Tong:", tong(0, 1, 2, 3, 4, 5))


def snt(_n):
    if _n < 2:
        return False
    else:
        i = 2
        while i <= _n // 2:
            if _n % i == 0:
                return False
            i = i + 1
        return True
#tim so nguyen to trong khoang [a, b]
def snt_khoang(_a, _b):
    for n in range(_a, _b + 1):
        if snt(n):
            print(n)
            
#tim so hoan hao 
def hoanhao(_n):
    tong = 0
    for i in range(1, _n):
        if _n % i == 0:
            tong = tong + i
    return tong == _n
# tim so hoan hao trong khoang [a, b]
def hoanhao_khoang(_a, _b):
    for n in range(_a, _b + 1):
        if hoanhao(n):
            print(n)








#viet menu chon thuc thi 
def menu():
    print(" 1: tinh tong 2 so")
    print(" 2: tinh tong cac so")
    print(" 3: kiem tra so nguyen to")
    print(" 0: thoat")
    return int(input("Nhap lua chon: "))
while True:
    choice = menu()
    if choice == 1:
        _a = int(input("Nhap a: "))
        _b = int(input("Nhap b: "))
        print("Tong:", tong(_a, _b))
    elif choice == 2:
        n = int(input("Nhap so luong so: "))
        var = []
        for i in range(n):
            var.append(int(input(f"Nhap so thu {i + 1}: ")))
        print("Tong:", tong(*var))
    elif choice == 3:
        n = int(input("Nhap n: "))
        if snt(n):
            print(f"{n} La so nguyen to")
        else:
            print(f"{n} Khong phai la so nguyen to")
    elif choice == 0:
        print("Thoat chuong trinh")
        break

