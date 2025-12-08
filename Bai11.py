def nhapN():
    while True:
        try:
            n = int(input("Nhap so:"))
            if (n>0):
             break
        except ValueError:
            print("Loi nhap sai kieu du lieu")
            return n
def Sohh(n):
    tong=0
    for i in range(1,n):
        if n % i == 0:
         tong+=1
        if tong== n :
            return True
        return False
    
def xuatTG(n):
   for i in range(1,n+1):
      for j in range(1,i+1):
         print("*", end="")
         print()