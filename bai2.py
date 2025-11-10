import math
try:
    thang= int(input("Nhap thang 1-12)"))
except:
    print("Loi nhap lieu!")
else:
    match thang:
        case 2:
         print("Co 28 hay 29 ngay")
        case 1|3|5|7|9|12:
         print("Co 31 ngay")
        case 5|6|8|10|11:
         print("Co 30 ngay")
        case _:
         print("Sai thang")