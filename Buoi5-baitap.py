_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sum = 0
for i in _list:
    sum += i
print(sum)
# print("Tong: ", sum(_list))

_list1 = [1, 2, 3, 4, 5]
tich = 1 
for i in _list1:
    tich = tich * i 
print(tich)


_list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sc = []
sl = []
for i in _list2:
    if i % 2 == 0:
        sc.append(i) #append là thêm phần tử vào cuối list
    else:
        sl.append(i)
print(sc)
print(sl)

_list3 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
_new = _list3[2:4]
print(_new)

_list4 = ['zero', 'three'] #cho one two vao giua list
_list4.insert(1,'one')
_list4.insert(2,'two') #insert là thêm phần tử vào vị trí bất kỳ
print(_list4)

_list5 = [11, 2, 23, 45, 6, 9]
print(max(_list5))
print(min(_list5))

#Viết chương trình copy một list cho trước thành một list mới
_list6 = [11, 2, 23, 45, 6, 9] + [11, 2, 23,]
_list6 = _list6 * 2
print(_list6)

#Nhập vào từ bàn phím số n và list cho trước, tim các từ có độ dài lớn hơn n từ list đó
n = input("Nhap so nguyen n: ")
_list7 = [11, 2, 23, 45, 6, 9]
for i in _list7:
    if len(i) > n:
        print(i)

