# fruitlist = ["apple", "apricot", "banana", "coconut", "lemon"]
# otherlist = [100, "one", "two", 3]
# print(fruitlist)
# print(otherlist)
# print("---------------------------")
# print(fruitlist)
# print(otherlist)

# for fruit in fruitlist:
#     print("Fruit: ", fruit)

# print("count: ", len(fruit))

# for i in range(0, len(fruit)):
#     print("element at ", i, "=", fruit[i])

# sublist = fruit[1:4] #tạo danh sách con

# print("Sub list [1:4] ", sublist)


# print("Chua cap nhat", fruitlist)
# fruitlist[0] = 2000
# print("Sau khi cap nhat: ", fruitlist)

# fruitlist[3:5] = ["banana"]
# print("Sau khi cap nhat nhieu phan tu",fruitlist)

# fruitlist.append("orange")
# fruitlist.append("grape")
# print(fruitlist)

# fruitlist.insert(0, "Van")
# print(fruitlist)

# #del xoa 1 or nhieu phan tu , remove
# del fruitlist[6]
# print("Xoa 1 phan tu", fruitlist)

# del fruitlist[1:4]
# print("Xoa nhieu phan tu",fruitlist)

# fruitlist.remove("Van")
# print(fruitlist)

heights = [1.65, 1.72, 1.68, 1.75, 1.70, 1.68, 1.73, 1.69, 1.76, 1.71]

print("Tong so sinh vien: ", len(heights))
print("Danh sach chieu cao sinh vien: ", heights)

max_height = max(heights)
print(f"Chieu cao cao nhat: {max_height} (m)")

min_height = min(heights)
print(f"Chieu cao thap nhat: {min_height} (m)")

height_tb = sum(heights) / len(heights)
print(f"Chieu cao trung binh: {height_tb} (m)")

count_cao_lon_tb = 0
for height in heights:
    if height >= height_tb:
        count_cao_lon_tb += 1
print(f"So luong sinh vien co chieu cao >= trung binh: {count_cao_lon_tb}")


_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sum = 0
for i in range(len(_list)):
    sum += i
    print(sum)