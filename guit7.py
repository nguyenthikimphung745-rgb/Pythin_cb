import tkinter as tk 
root = tk.Tk()
# 1 Tạo một biến chung cho cả nhóm
var_gender = tk.StringVar()
var_gender.set("Nam") # Đặt giá trị mặt định
# 2 Các radiobutton dùng chung 'variable' nhưng khác 'value'
rad_male = tk.Radiobutton(root,text="Nam", variable=var_gender,value="Nam")
rad_male.pack(anchor=tk.W)
rad_female = tk.Radiobutton(root,text="Nữ", variable=var_gender,value="Nữ")
rad_female.pack(anchor=tk.W)
def xem_gioi_tinh():
    print("GIỚI TÍNH ĐÃ CHỌN:", var_gender.get())
tk.Button(root,text="Xác nhận", command=xem_gioi_tinh).pack()
root.mainloop()
