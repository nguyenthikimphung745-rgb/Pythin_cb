while True:
    try:
        n = int(input("Nhap so: "))
        if (n>0):
            break
    except ValueError:
        print("Loi nhap sai kieu du lieu")
print("====Cau 1 ====")
for i in range(1,n+1):
    if i%2==0:
        print(i,end=" ")

print("====Cau 2 ====")
tong=0
for i in range(1,n+1):
    if (i%2 !=0):
        tong+=i
print(f"Tong tu 1 den {n} la: {tong}")

print("====Cau 3 ====")
n=int(input("Nhap so: "))
for i in range(1,n+1):
    if i%3 == 0:
        print(f"Cac so la {i}")

print("====Cau 4 ====")
i = 1
dem = 0
while(i<=10):
    try:
        so = int(input(f"Nhap so thu {i}:"))
        i += 1
        if(so<0):
            dem +=1
    except ValueError:
        print("Loi nhap lieu sai kieu du lieu")
print(f"Co {dem} so am!")
    
print("====Cau 5 ====")
n=int(input("Nhap so: "))
for i in range(1,11):
    print(n,"x",i,"=",n*i)

print("====Cau 6 ====")
n=int(input("Nhap so: "))
for i in range(1, n + 1):
        if i == 5:
            continue  
        print(i, end=' ')

print("====Cau 8 ====")
while True:
    try:
        n = int(input("Nhap n:"))
        if(n>0):
            break
    except ValueError:
        print("Loi nhap sai kieu du lieu")
i = 1
max = -1000
min = 1000
while (i<=n):
    try:
        so = int(input(f"Nhap so thu {i}:"))
        i+=1
        if(so>max):
            max = so 
        if(so<min):
            min = so 
    except ValueError:
        print("Sai kieu du lieu")
print(f"Gia tri lon nhat la : {max}, nho nhat la : {min}")

print("====Cau 9 ====")
so = int(input("Nhap so :"))
So=so
dem = 0 
while(so!=0):
    so = so //10
    dem += 1
print(f"So {So} co {dem} chu so!")
print("====Cau 10 ====")
