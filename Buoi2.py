# _a = 14
# _b = 2
# _c = 4
# _d = 2
# print(_a + _b)
# print(_a - _b)
# print(_a * _b)
# print(_a // _c)
# print(_a % _c)
# print(_a / _c)
# print(_b ** _c)

#Toan tu so sanh
# print(_b < _a)
# print(_b > _a)
# print(_b <= _a)
# print(_b >= _a)
# print(_b == _d)
# print(_b != _a)

#Toan tu gan 
# _e = 10;
# print(_e)
# _e += 5
# print(_e)
# _e -= 5
# print(_e)
# _e *= 2
# print(_e)
# _e /= 2
# print(_e)
# _e %= 3
# print(_e)
# _e //= 2
# print(_e)
# _e **= 2
# print(_e)

#-----------------------------------------------------
#Toan tu logic
# _a = 5 > 4 and 3 > 2
# print(_a)
# _b = 5 > 4 or 3 < 2
# print(_b)
# _c = not (5 > 4) 
# print(_c)

#-------------------------------------------------------
#Toan tu bitwise
#and bang 1 khi ca 2 bang 1
#or bang 0 khi ca 2 bang 0
#xor bang 1 khi 2 bit khac nhau
#not bang 1 khi bit bang 0 va nguoc lai
#shift left dich bit sang trai, shift right dich bit sang phai

#---------------------------------------------------------------
# _n = int(input("Nhap so keo: "))
# _m = int(input("Nhap so hoc sinh: "))
# _result = _n // _m
# print("So keo moi hoc sinh duoc la: ", _result)
# _result = _n % _m
# print("So keo con lai la: ", _result)


# _a = str(input("Nhap ho ten: "))
# _b = int(input("Nhap nam sinh: "))
# _c = 2024 - _b
# print("Ban", _a, "nam nay ", _c, " tuoi!")

    
# _x = int(input("Nhap so thang: "))
# _c = 2**(_x + 1)
# print("So tho la: ", _c)

# option = 2 
# if option == 1:
#     print("Hello")
# elif option == 2:
#     print("Hi")
# else:
#     print("Goodbye")
# # Neu khac 0 thi la True, bang 0 thi la False
# _var1 = -100
# _var2 = 100
# if _var1:
#     print("1.1 Bien co gia tri True")
#     print("Gia tri cua _var1:", _var1)
# elif True:
#     print("1.2 Bien co gia tri True")
#     print("Gia tri cua _var2:", _var2)  
# else:
#     print("1.3 Bien co gia tri False")
#     print(_var1 +_var2)

# _var3 = 0
# if _var3:
#     print("2.1 Bien co gia tri True")
#     print("Gia tri cua _var3:", _var3)
# else:
#     print("2.2 Bien co gia tri False")
#     print("Gia tri cua _var3:", _var3)

# _number = 10
# if _number < 15:
#     print("Nho hon 15")
#     if _number == 15:
#         print("Bang 15")
#     elif _number == 10:
#         print("Bang 10")
#     elif _number == 5:
#         print("Bang 5")
# elif _number < 5:
#         print("Nho hon 5")
# else:
#     print("Lon hon hoac bang 15")


# n = int(input("Nhập diem: "))
# if n >= 0 and n <= 10:
#     if n >= 9:
#         print("Xuat sac")
#     elif n >= 7 and n < 9:
#         print("Gioi")
#     elif n >= 5 and n < 7:
#         print("Trung binh")
#     elif n >= 0 and n < 5:
#         print("Dat")
# else:
#     print("Diem khong hop le")

n = int(input("Nhap so: "))
if n % 2 == 0:
    print("Day la so chan")
else:
    print("Day la so le")

_a = int(input("Nhap a: "))
_b = int(input("Nhap b: "))
_c = int(input("Nhap c: "))
if _a + _b > _c and _a + _c > _b and _b + _c > _a:
    print("Do dai 3 canh cua tam giac")
else:
    print("Day khong phai la do dai 3 canh cua tam giac")

_n = int(input("Nhap nam sinh: "))
import time
x = time.localtime()
year = x[0]
age = year - _n
print("Nam nay ban", age, "tuoi")
