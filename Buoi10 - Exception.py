print ("Three")
value = 10 / 2
print ("Two")
value = 10 / 1
print ("One")

d = 0
try: 
    value = 10/d
    print("value", value)

except ZeroDivisionError as e:
    print("Error: ", str(e))
    print("Ignore to continue...")
print ("Let's go")

def chia(a,b):
    try:
        x=int(a)
        y=int(b)
        z=x/y
        print(f'{x}/{y}={z}')
    except ValueError as e1:
        print('Lỗi chuyển kiểu dữ liệu!')
    except ZeroDivisionError as e2:
        print('Lỗi chia cho 0!')
    except:
        print('Chương trình có lỗi!')
    finally:
        print('Đã chạy xong')

a=input("Nhập a:")
b=input("Nhập b:")
chia(a,b)

# # Ví dụ sử dụng random Module:
#  import random
#  print(random.random())
# print(random.randint(1, 10))
