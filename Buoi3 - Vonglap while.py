# count = 0
# n = 0
# while (count < 9):
#     print('So thu', n , 'la:', count)
#     n = n + 1
#     count = count + 1
# print("Finish")

# n = int(input("Nhập số nguyên n: "))
# tong = 0
# i = 1
# while i <= n:
#     tong = tong + i
#     i = i + 1
# print("sum:", tong)

# _dem = 0
# while _dem < 3:
#     print("dang nam trong while", _dem)
#     _dem = _dem + 1
# else:
#     print("dang nam trong else", _dem)

#while True: chi quan tam den khoi o trong while (nhung gi dieu kien dung); chay lap lai den khi nao dung thi break

#nhap vao bang cuu chuong muon in (1 - 10), hien thi bang cuu chuong tuong ung voi so vua nhap
for i in range(1, 11):
    print(f"Bang cuu chuong {i}:")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print()  



#-------------------------------------
tich = 1
i = 1
while i <= 10:
    tich = tich * i
    i = i + 1
print("Tich:", tich)

#---------------------------------------
n = int(input("Nhap n: "))
tich = 1
i = 1
while i <= n:
    tich = tich * i
    i = i + 1
print(f"{n}! = {tich}")

#---------------------------------------
n = int(input("Nhap n: "))
if n < 2:
    print("Khong phai SNT")
else:
    snt = True
    i = 2
    while i <= n // 2:
        if n % i == 0:
            snt = False
            break
        i = i + 1
    if snt:
        print(f"{n} La so nguyen to")
    else:
        print(f"{n} Khong phai la so nguyen to")

#---------------------------------------
n = int(input("Nhap n: "))
tong = 0
i = 1
while i < n:
    if i % 2 == 0:
        tong = tong + i
    i = i + 1
print("tong:", tong)

#-------------------
import math

n = int(input("Nhập số nguyên dương N: "))

if n <= 1:
    print("Số", n, "không phải là số nguyên tố!")
elif n == 2 or n == 3:
    print("Số", n, "là số nguyên tố!")
elif n % 2 == 0 or n % 3 == 0:
    print("Số", n, "không phải là số nguyên tố!")
else:
    check = True
    i = 5
    while i <= math.sqrt(n):
        if n % i == 0 or n % (i + 2) == 0:
            check = False
            break
        i += 6

    if check:
        print("Số", n, "là số nguyên tố!")
    else:
        print("Số", n, "không phải là số nguyên tố!")