import math
try:
    NamDL = int(input("Nhap nam)"))
except:
    print("Loi nhap lieu!")
else:
    Ducan = NamDL%10
    Duchi = NamDL%12
    can=''
    chi=''
match Ducan:
    case 0: can= "Canh"
    case 1: can= "Tan"
    case 2: can= "Nhâm"
    case 3: can= "Quý"
    case 4: can= "Giáp"
    case 5: can= "Ất"
    case 6: can= "Bính"
    case 7: can= "Đinh"
    case 8: can= "Mậu"
    case 9: can= "Kỷ"
match Duchi:
    case 0: chi= "Thân"
    case 1: chi= "Dậu"
    case 2: chi= "Tuất"
    case 3: chi= "Hợi"
    case 4: chi= "Tí"
    case 5: chi= "Sửu"
    case 6: chi= "Dần"
    case 7: chi= "Mẹo"
    case 8: chi= "Thìn"
    case 9: chi= "Tỵ"
    case 10: chi= "Ngọ"
    case 11: chi= "Mùi"
print(can,chi)