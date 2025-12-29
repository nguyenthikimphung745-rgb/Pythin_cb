#Câu 2 : Trò chơi “Nạp năng lượng”
import random
def tro_choi_nap_nang_luong():
    nang_luong = 0
    toida_lan_nap = 5
    print("-"*30)
    print("BAT DAU TRO CHOI BAN MUC TIEU")
    print("-"*30)   
    for lan_nap in range(1,toida_lan_nap+1):
        if(random.random()<0.5):
            diem_cong = random.randint(15,40)
            nang_luong += diem_cong
            ket_qua = f"TRÚNG! Tăng {diem_cong} điểm "
        else:
            diem_cong = random.randint(5, 15)
            nang_luong -= diem_cong
            if nang_luong < 0:
                nang_luong = 0
            ket_qua = f"THAT BAI (-{diem_cong})"
        print(f"Phát thứ {lan_nap}: {ket_qua}. Tổng điểm: {nang_luong}")
        if nang_luong >= 120:
            print("\n KẾT THÚC. BẠN ĐÃ THẮNG! (Tổng >= 120)")
            return
        print("\n KẾT THÚC. BẠN ĐÃ THUA! (Tổng điểm < 120)")

tro_choi_nap_nang_luong()

# Cau 