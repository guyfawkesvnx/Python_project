# 1. Viết chương trình tìm tất cả các số chia hết cho 7 nhưng không phải bội số của 5, nằm trong đoạn 2000 và 3200 (tính cả 2000 và 3200). Các số thu được sẽ được in thành chuỗi trên một dòng, cách nhau bằng dấu phẩy.
# j = []
# for i in range (2000, 3001):
# 	if ( i %7== 0) and ( i %5!= 0):
# 	    j.append(str(i))
# print(",".join(j))


# tinh giai thua 1 so nhap vao
# x = int(input(("nhap vao so can tinh :")))
# def fact(x):
#     if x == 0:
#         return 1
#     return (x * fact(x - 1))
# print(fact(x))

# bai3
# x = int(input("Nhap vao gia tri x :"))
# d = dict()
# for i in range(1, x+1):
#     d[i] = i * i
# print(d)

# bai4
# values = input("nhap vao gia tri :")
# l = values.split(".")   # nhân giá trị cách nhau bằng dấu .
# tuple = l
# print(tuple)
 
# bai 5
# class uppcaseString(object):
#     def __init__(self):
#         self.s = ""
#     def getString(self):
#         self.s = input("Nhap vao mot chuoi")
#     def printString(self):
#         print(self.s.upper())
# strObj = uppcaseString()
# strObj.getString()
# strObj.printString()

# bai 6 tính bình phuong 1 số
# x = int(input("Nhap vao gia tri :"))
# def square(num):
#     return num ** 2
# print (square(x))

# bai 7
# print(reversed.__doc__)
# print(Warning.__doc__)
# print(int.__doc__)
# x = int(input("nhap gia tri so nguyen :"))
# def square(num):
#     return num ** 2
# x = print(square(x))
# print(x.__doc__)

# bai 8
# class person:
#     name = "Person"
#     def __init__(self, name = None):
#         self.name = name
# jeffery = person("jeffery")
# print("%s name is %s" % (person.name, jeffery.name))

# nico = person()
# nico.name = "Nico"
# print("%s name is %s" % (person.name, nico.name))
# 
#

# bbai 9
# import math 
# c=50 
# h=30 
# value = [] 
# items=[x for x in input("Nhập giá trị của d: ").split(',')] 
# for d in items:     
#     value.append(str(int(round(math.sqrt(2*c*float(d)/h))))) # Code by Quantrimang.com 
# print (','.join(value))

# bai10
# input_str = input("nhap gia tri X, Y :")
# dimensions = [int(x) for x in input_str.split(',')]
# rowNum = dimensions[0]
# colNum = dimensions[1]
# multilist = [[0 for col in range(colNum)] for row in range(rowNum)]
# for row in range(rowNum):
#     for col in range(colNum):
#         multilist[row][col] = row*col
# print(multilist)


# bai11
# input_string = input("nhap chuoi gia tri gia tri vao :")
# string_split = [x for x in input_string.split(",")]
# string_split.sort()
# print(string_split)

# item = [x for x in input("nhap chuoi gia tri :").split(",")]
# item.sort()
# print(item)

# bai12
# lines = []
# while True:
#     x = input()
#     if x:
#         lines.append(x.upper())
#     else:
#         break
# for y in lines:
#     print(y)
    
# Bai 13 
# bien = input("Nhap gia tri vao: ")
# y = [x for x in bien.split(" ")]
# print(" ".join(sorted(list(set(y))))) 
# set dùng để loại bỏ trùng lập
# sorted dùng để sắp xếp 

# bai 14
# value = []
# items = [x for x in input("Nhap vao chuoi gia tri: ").split(",")]
# for p in items:
#     intp = int(p, 2)
#     if not intp % 5:
#         value.append(p)
# print(",".join(value))

#bai 15
# values = []
# for i in range(1000, 3000 + 1):
#     s = str(i)
#     if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
#         values.append(s)
# print("-".join(values))

#bai 16
# values = input("Nhap dau vao: ")
# s = {"chu":0, "so":0}
# for c in values:
#     if c.isdigit():
#         s["chu"]+=1
#     elif c.isalpha():
#         s["so"]+=1
#     else:
#         pass
# print("so chu la: " , s["chu"])
# print("so: ", s["so"])