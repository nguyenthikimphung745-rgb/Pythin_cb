def get_city(event):
    print("Thành phố:", combo_city.get())

import tkinter as tk
from tkinter import ttk # Bắt buộc import ttk
root = tk.Tk()
tk.Label(root,text="Chọn thành phố:").pack()
# 1 Khởi tạo combobox
combo_city = ttk.Combobox(root,width=20)
# 2 Cung cấp các danh sách lựa chọn
combo_city['values'] = ("Hà Nội","Đà Nẵng","TP.Hồ Chí Minh","Cần Thơ")
# 3 cài đặt chế độ chỉ được chọn, không cho gõ bậy bạ
combo_city['state'] = 'readonly'
combo_city.pack()
# Lấy dữ liệu đã chọn
combo_city.bind("<<Comboboxselected>>", get_city)

root.mainloop()