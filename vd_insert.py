import sqlite3
def them_sinh_vien_moi(ten_sv, tuoi_sv, nganh_sv):

    conn = sqlite3.connect('quanly_sinhvien.db')
    cur = conn.cursor()



    sql_insert = " INSERT INTO SinhVien (ho_ten,tuoi,nganh_hoc) VALUES (?,?,?)"


    du_lieu = (ten_sv,  tuoi_sv, nganh_sv)


    cur.execute(sql_insert, du_lieu)
    conn.commit()

    print(f"Đã thêm sinh viên: {ten_sv}")

    conn.close()
them_sinh_vien_moi("Trần Văn A",25,"CNTT")

    