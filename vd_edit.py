import sqlite3
def sua_tuoi_sinh_vien(ma_sv, tuoi_moi):
 
    conn = sqlite3.connect('quanly_sinhvien.db')
    cur = conn.cursor()
    sql_update = "UPDATE Sinhvien SET tuoi = ? WHERE id = ?"
    du_lieu = (tuoi_moi,ma_sv)
    cur.execute(sql_update, du_lieu)
    conn.commit()
    print(f" Đã cập nhật mới cho sinh viên có mã: {ma_sv}")
    conn.close()

sua_tuoi_sinh_vien()