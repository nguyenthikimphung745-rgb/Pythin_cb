try:
    Van = float(input(" Nhap diem van:"))
    Toan = float(input(" Nhap diem toan:"))
    Anh = float(input(" Nhap diem anh:"))
except ValueError:
    print("Loi sai nhap lieu!")
else:
    tb = ( Van + Toan + Anh)/3
    if Van < 0 or Van > 10 or Toan < 0 or Toan > 10 or Anh < 0 or Anh > 10 :
        print(" Nhap diem khong dung")
    else:
        if (tb>=9):
            print("Xep loai Xuat Sac")
        elif (tb>=8):
            print("Xep loai Gioi")
        elif (tb>=7):
            print("Xep loai Kha")
        elif (tb>=5):
            print("Xep loai Trung Binh")
        else:
            print("Xep loai Yeu")