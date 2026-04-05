import os
filepath = 'testRead.txt'
# r read only
# open(filepath)
# print('Open file with default mode.')

# r+ read and write
file = open(filepath, 'r+')
print('Open file with read and write mode.')

str = file.read()
print('file content:', str)

# s1 = file.readline()
# print('file content:', s1)
# s2 = file.readline()
# print('file content:', s2)

#write file 
info = \
'Name: Cntt\n' + \
'mail: it@example.com\n' + \
'address: Hanoi'
f = open('testRead.txt', 'w')
f.write(info)
#khi chay co can dong file khong? - co, neu khong dong thi file se bi loi va khong the mo lai duoc
f.close()