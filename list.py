# Câu 3 : Thuật toán trên List (không dùng sum/max/min/sort)
# a) Tinh diem trung binh
Diem = [7.5, 8.0, 6.0, 9.0, 5.5, 8.5, 7.0, 6.5]
Tong = 0
for value in Diem:
    Tong += value
Diem_TB = Tong/len(Diem)
print(f"Diem trung binh la: {Diem_TB}")
# b) Tinh diem cao nhat
max = Diem[0]
for value in Diem:
    if value > max:
        max = value
print(f"Diem cao nhat la:{max}")
# c) Đếm số điểm >= 8.0 và < 8.0 
D_lonhon = 0
D_nhohon = 0
for value in Diem:
    if value >= 8.0:
      D_lonhon += 1
    else:
      D_nhohon += 1
print(f"So diem (>= 8.0) la: {D_lonhon}")
print(f"So diem (< 8.0) la: {D_nhohon}")
# d) Sắp xếp danh sách tăng dần bằng thuật toán tự chọn và in ra 
for i in range(len(Diem)-1):
   for j in range(i+1,len(Diem)):
      if (Diem[i])>(Diem[j]):
         Diem[i],Diem[j] = Diem[j],Diem[i]
print(f"Danh sach tang dan: {Diem}")
# Câu 2 : Trò chơi “Săn kho báu” (random)
import random
def tro_choi_san_kho_bau():
    tong_diem = 0
    toida_luot = 7
    print("--- BẮT ĐẦU TRÒ CHƠI ---")
    for so_luot in range(1,toida_luot+1):
        if(random.random()<0.6):
            diem_cong = random.randint(5,30)
            tong_diem += diem_cong
            ket_qua = f"TRÚNG! Cộng {diem_cong} điểm "
        else:
            diem_thay_doi = -2
            tong_diem += diem_thay_doi
            if tong_diem < 0:
                tong_diem = 0
            ket_qua = f"THẤT BẠI. (-2)"
        print(f"Phát thứ {so_luot}: {ket_qua}. Tổng điểm: {tong_diem}")
        if tong_diem >= 80:
            print("\n KẾT THÚC. BẠN ĐÃ THẮNG! (Tổng >= 80)")
            return
        print("\n KẾT THÚC. BẠN ĐÃ THUA! (Tổng điểm < 80)")

tro_choi_san_kho_bau()
# Câu 1 Đề 1 : Tính tiền nước theo bậc thang
def tinh_tien_nuoc():
    
    try:
        x = float(input("Nhập số m3 nước tiêu thụ (x > 0): "))
        if x <= 0:
            print("Lỗi: Số m3 nước phải lớn hơn 0.")
            return
    except ValueError:
        print("Lỗi: Vui lòng nhập một số thực hợp lệ.")
        return

   
    tien_chua_phi = 0
    
    if x <= 10:
        tien_chua_phi = x * 7000
    elif x <= 20:
        
        tien_chua_phi = (10 * 7000) + (x - 10) * 9000
    else:
        
        tien_chua_phi = (10 * 7000) + (10 * 9000) + (x - 20) * 12000

   
    tong_tien = tien_chua_phi * 1.05

    
    print("-" * 30)
    print(f"Tiền nước chưa phí: {tien_chua_phi:,.0f} đ")
    print(f"Tổng tiền phải trả (gồm 5% phí BVMT): {tong_tien:,.0f} đ")
    print("-" * 30)


tinh_tien_nuoc()