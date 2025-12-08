#Bai 1
n = input("Nhap vao mot chuoi:")
print("Do dai cua chuoi la :", len(n))
#Bai 2
s = "Python Programming"
print("Ky tu dau:", s[0])
print("Ky tu cuoi:", s[17])
print("Ky tu giua:", s[7])
#Bai 3
n = input("Nhap vao mot chuoi:")
print("3 ký tự đầu tiên:",n[:3])
print("3 ký tự đầu tiên:",n[-3:])
#Bai 4
n = input("Nhap ten nguoi:")
print(n.upper())
print(n.lower())
#Bai 5 
a = input("Nhap Ho:")
b = input("Nhap Ten dem:")
c = input("Nhap Ten:")
d = a + " " +b +" "+ c
print(d)
#Bai 6
a = input("Nhap mot cau:")
b = "Python"
print(a in b)