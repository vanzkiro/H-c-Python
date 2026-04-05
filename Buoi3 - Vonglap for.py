
# for _i in range(1, 12):
#     print(f"Giá trị của _i: {_i}")
#     if _i % 2 == 0: print(f"{_i} là số chẵn")
#     else: print(f"{_i} là số lẻ")
    
# for _i in range(1, 6):
#     print(_i * _i)

# for _i in range(1, 6): # 5 khoi lenh (1*3, 1*4, 2*3, 2*4; 3*3, 3*4, 4*3, 4*4, 4*5; 5*3, 5*4)
#     for _j in range(3, 5): # 2 khoi lenh  #tong cong co 10 khoi lenh
#         _a = _i * _j
#         print(_a)



from cmath import sqrt
from math import *


n = int(input("Nhập số nguyên n: "))
for i in range(1, n + 1):
    print(f"{2 * i} = 2 * {i}")
#---------------------------------------------------------
n = int(input("Nhập số nguyên n: "))
if n> 10:
    print("so phai lon hon or bang 10")
else:
    print("nhung so chan nho hon n")
    for i in range(1, n + 1):
        if i %2 == 0:
            print(i)



n = int(input("Nhập số nguyên n: "))
if n > 10:
    print("Số nhập vào phải bé hơn hoặc bằng 10")  
else:
    print(f"Số chẵn trong khoảng từ 1 đến {n}:")
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(i)
#---------------------------------------------------------

print("Các số từ 80 đến 100 chia hết cho 2 và 3:")
for i in range(80, 101):
    if i % 2 == 0 and i % 3 == 0:
        print(i)
#--------------------------------------------------------

n = int(input("Nhập số nguyên n: "))
if n < 20:
    print("So chia het cho 5 or 7:")
    for i in range(1, n + 1):
        if i % 5 == 0 or i % 7 == 0:
            print(i)



def snt(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True
    
# DOC NOI DUNG FILE A GHI SANG FILE B
file_a = open('file_a.txt', 'r')   
file_b = open('file_b.txt', 'w')
for line in file_a:
    file_b.write(line)
file_a.close()
file_b.close()

# w co tac 



n = int(input("Nhập N: "))

if n <= 1:
    print("Không phải số nguyên tố")
else:
    for i in range(2, n):
        if n % i == 0:
            print("Không phải số nguyên tố")
            break
    else:
        print("Là số nguyên tố")


