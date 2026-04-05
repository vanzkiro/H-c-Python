#viet chuong trinh chuan hoa ho va ten
name = input("Nhap ho va ten: ")
name = name.title()
print(name)

#---------------------------------
_str = "Nước Việt Nam là một, dân tộc Việt Nam là một. Sông có thể cạn núi có thể mòn, song chân lý ấy không bao giờ thay đổi. (HỒ CHÍ MINH, 1890 - 1969)"
print(len(_str))

text = _str.lower() # chuyen chuoi thanh chuoi thuong
print("hồ chí minh" in text)
print("non sông" in text)

text = _str.split(".") # chia chuoi theo dau cham
print(text)

text = _str.isalnum() # kiem tra xem co phai la ki tu va so hay khong
print(text) 
special = [c for c in text if not c.isalnum() and not c.isspace()]

print("Ký tự đặc biệt:", set(special))

text = _str.replace ("Việt Nam", "VIỆT NAM")
print(text)

#---------------------------------
s = input("Nhập chuỗi số (vd: 1,2,3,4): ")
# Tách chuỗi thành list số
numbers = list(map(int, s.split(',')))

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Lọc số nguyên tố
primes = [n for n in numbers if is_prime(n)]
print( primes)

#----------------------------------
password = input("Nhập mật khẩu: ")

# Kiểm tra điều kiện
letter = any(c.isalpha() for c in password)
no_space = ' ' not in password
digit = any(c.isdigit() for c in password)
special = any(c in '(){}!@#$%' for c in password)
length = 8 <= len(password) <= 12

if letter and digit and special and no_space and length:
    print("Mật khẩu mạnh!")
else:
    print("Mật khẩu yếu!")

#-----------------------------------
n = int(input("Nhập n: "))
word = input("Nhập danh sách từ (cách nhau bằng dấu cách): ").split()
result = [w for w in word if len(w) > n]

print( result)

#-----------------------------------    
lst = ['abc', 'xyz', 'aba', '1221', 'ii', 'ii2', '5yhy5']
n = int(input("Nhập độ dài tối thiểu: "))

count = 0
for s in lst:
    if len(s) >= n and s[0] == s[-1]:
        count += 1

print(count)