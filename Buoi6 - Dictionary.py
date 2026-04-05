# _info = {"name": "Pham Quang Van", "Age": 21, "Country": "Vietnam"}
# print(_info)

# _dict = dict()
# _dict["Name"] = "Pham Quang Van B "
# _dict["Age"] = "22"
# print("dictionary: ", _dict)


# _dict = {1: "One", 2: 'Two', 2: "Three"}
# print("Dictionary: ", _dict)

# _dict2 = {'Name': "Python", "2": 'Two', 2: "Three", 4: 'Four', 5: 'Five'}
# print("Dictionary: ", _dict2['Name']) #dict(key)
# print("Dictionary: ", _dict2['2']) #dict(key)

# _info.update({"name": "Phạm Quang Văn", "Age": 23})
# print(_info )

# del _info["Country"] #xoa 1 phan tu trong dictionary
# print(_dict)

# _info.clear() #xoa toan bo dictionary

# _dict.keys() #tra ve cac key trong dictionary
# _dict.values() #tra ve cac value trong dictionary


# _dict3 = {
#     20231249: ("Pham Quang Van", 9.5), 
#     20231177: ("Ta Van Tung", 8.5),
#     20231221: ("Le Xuan Huynh", 7.5),
#     20231166: ("Hua Duc Luong", 6.5),
# }
# n = int(input("nhap sbd ")) #nhap sbd neu ton tai thi dua ra ho ten va diem
# if n in _dict3:
#     name, diem = _dict3[n]  # Giải nén tuple
#     print(f"Tên: {name}, Điểm: {diem}")
# else:
#     print("khong ton tai")


#---------------------------------------------

khoa = {"a":"!", "b": "@", "c": "#", "d": "$"}
ban_ro = input("Nhap ban ro: ")
ban_ma = []
for i in ban_ro:
    if i in khoa:
        ban_ma.append(khoa.get(i))
    else:
        ban_ma.append(i)
print(ban_ma)
