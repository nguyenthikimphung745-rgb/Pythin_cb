# Câu 2 (3,0 điểm): Trò chơi “Bắn mục tiêu”
import random
def tro_choi_ban_muc_tieu():
    tong_diem = 0
    toida_phat_ban = 7
    print("-"*30)
    print("BAT DAU TRO CHOI BAN MUC TIEU")
    print("-"*30)   
    for phat_ban in range(1,toida_phat_ban+1):
        if(random.random()<0.4):
            diem_cong = random.randint(10,25)
            tong_diem =+ diem_cong
            ket_qua = f"TRÚNG! Cộng {diem_cong} điểm "
        else:
            diem_cong = 0
            ket_qua = f"TRƯỢT. Cộng 0 điểm"
        print(f"Phát thứ {phat_ban}: {ket_qua}. Tổng điểm: {tong_diem}")
        if tong_diem >= 90:
            print("\n KẾT THÚC. BẠN ĐÃ THẮNG! (Tổng >= 90)")
            return
        print("\n KẾT THÚC. BẠN ĐÃ THUA! (Tổng điểm < 90)")

tro_choi_ban_muc_tieu()