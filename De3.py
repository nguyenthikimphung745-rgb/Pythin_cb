# Câu 3 : List – thuật toán (không dùng sum/max/min/sort)
# --- a) Tính nhiệt độ trung bình ---
NhietDo = [30, 28, 35, 33, 29, 31, 27, 34]
n = len(NhietDo)
tong = 0
for t in NhietDo:
    tong += t
trung_binh = tong / n
print(f"a) Nhiệt độ trung bình: {trung_binh}")

# --- b) Tìm nhiệt độ lớn nhất ---
max_val = NhietDo[0] 
for t in NhietDo:
    if t > max_val:
        max_val = t
print(f"b) Nhiệt độ lớn nhất: {max_val}")

# --- c) Đếm số ngày nóng (>= 32) và không nóng (< 32) ---
ngay_nong = 0
ngay_khong_nong = 0
for t in NhietDo:
    if t >= 32:
        ngay_nong += 1
    else:
        ngay_khong_nong += 1
print(f"c) Số ngày nóng: {ngay_nong}, Số ngày không nóng: {ngay_khong_nong}")

# --- d) Sắp xếp tăng dần  ---

NhietDo_SapXep = NhietDo[:] 

for i in range(n):
    for j in range(0, n - i - 1):
        if NhietDo_SapXep[j] > NhietDo_SapXep[j + 1]:
            
            NhietDo_SapXep[j], NhietDo_SapXep[j + 1] = NhietDo_SapXep[j + 1], NhietDo_SapXep[j]

print(f"d) Danh sách nhiệt độ tăng dần: {NhietDo_SapXep}")
# Câu 2
import random

def tro_choi_ban_muc_tieu():
    tong_diem = 0
    so_phat_ban = 7
    thang = False

    print("--- BẮT ĐẦU TRÒ CHƠI ---")

    for i in range(1, so_phat_ban + 1):
        trung_muc_tieu = random.random() <= 0.40
        if trung_muc_tieu:
            diem_moi = random.randint(10, 25)
            tong_diem += diem_moi
            print(f"Phát {i}: TRÚNG! (+{diem_moi} điểm). Tổng hiện tại: {tong_diem}")
        else:
            print(f"Phát {i}: TRƯỢT. Tổng hiện tại: {tong_diem}")

        
        if tong_diem >= 90:
            print(f"\nCHÚC MỪNG! Bạn đạt {tong_diem} điểm và THẮNG sớm ở phát thứ {i}.")
            thang = True
            break

    if not thang:
        print(f"\nKẾT THÚC: Bạn chỉ đạt {tong_diem} điểm. Rất tiếc, bạn đã THUA!")


tro_choi_ban_muc_tieu()