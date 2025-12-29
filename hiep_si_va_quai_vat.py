#Câu 2 
import random
def tro_choi_hiep_si_va_quai_vat():
    tong_diem = 0
    toida_luot = 10
    print("--- BẮT ĐẦU TRÒ CHƠI ---")
    for so_luot in range(1,toida_luot+1):
        if(random.random()<0.7):
            diem_cong = random.randint(50,100)
            tong_diem += diem_cong
            ket_qua = f"TRÚNG! Cộng {diem_cong} điểm "
        else:
            diem_thay_doi = -20
            tong_diem += diem_thay_doi
            if tong_diem < 0:
                tong_diem = 0
            ket_qua = f"THẤT BẠI. (-20)"
        print(f"Phát thứ {so_luot}: {ket_qua}. Tổng điểm: {tong_diem}")
        if tong_diem >= 400:
            print("\n KẾT THÚC. BẠN ĐÃ THẮNG! (Tổng >= 400)")
            return
        print("\n KẾT THÚC. BẠN ĐÃ THUA! (Tổng điểm < 400)")

tro_choi_hiep_si_va_quai_vat()
#Câu 1
try:
    Van = float(input(" Nhap diem van:"))
    Toan = float(input(" Nhap diem toan:"))
    Anh = float(input(" Nhap diem anh:"))
except ValueError:
    print("Loi sai nhap lieu!")
else:
    tb = ( Toan*2+Van+Anh)/4
    if Van < 0 or Van > 10 or Toan < 0 or Toan > 10 or Anh < 0 or Anh > 10 :
        print(" Nhap diem khong dung")
    else:
        if (tb>=9.0):
            loai,tien,bac ="Xuất sắc",5000000,3
        elif (8.0<=tb<9.0):
            loai,tien,bac ="Giỏi",3000000,2
        elif (tb>=7.0):
           loai,tien,bac ="Khá",1000000,1
        else :
           loai,tien,bac ="Trung bình",0,0 
        if (Toan < 4 or Van < 4 or Anh < 4) and bac > 0:
            bac -= 1
            danh_sach_loai = ["Trung bình", "Khá", "Giỏi", "Xuất sắc"]
            danh_sach_tien = [0, 1000000, 3000000, 5000000]
            loai = danh_sach_loai[bac]
            tien = danh_sach_tien[bac]

        print(f"ĐTK: {tb}")
        print(f"Xếp loại: {loai}")
        print(f"Học bổng: {tien} VNĐ")
#Câu 3 