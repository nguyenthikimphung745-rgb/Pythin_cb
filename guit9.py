
import tkinter as tk
from tkinter import ttk,messagebox

def calculate_and_oder():
    
root = tk.Tk()
root.title("Hệ Thống Đặt Trà Sữa - KIMPHUNG")
root.geometry("400x600")
lblTitle = tk.Label(
    root, 
    text="MILK TEA ORDER FORM", 
    fg="#A0522D",                 # fg là foreground color (màu chữ)
    font=("Arial", 20, "bold")     # Cấu trúc: ("Tên Font", Cỡ, "Kiểu")
)



lblTitle.grid(pady=20)

lbl_user = tk.Label(root,text="Tên khách hàng:")
lbl_user.grid(row=1, column=0,sticky=tk.W,padx=5,pady=5)
# 1 Tên
txt_user = tk.Entry(root)
txt_user.grid(row=1,column=0,padx=10,pady=10)
# 2 size
tk.Label(root,text="Chọn size ly:").grid(row=2, column=0,sticky=tk.W,padx=5,pady=5)

var_size = tk.StringVar(value="S")
f_size = tk.Frame(root)
f_size.grid(row=2, column=1,sticky="w")
tk.Radiobutton(f_size,text="Nhỏ(S)(+0đ)",variable=var_size,value="S").pack(anchor="w")
tk.Radiobutton(f_size,text="Vừa(M)(+5k)",variable=var_size,value="M").pack(anchor="w")
tk.Radiobutton(f_size,text="Lớn(L)(+10k)",variable=var_size,value="L").pack(anchor="w")
# 3 topping
tk.Label(root,text="Thêm Topping:").grid(row=3, column=0,sticky=tk.W,padx=5,pady=5)
var_t1,var_t2,var_t3 =tk.IntVar(),tk.IntVar(),tk.IntVar()
f_topping = tk.Frame(root)
f_topping.grid(row=3, column=1,sticky="w")
tk.Checkbutton(f_topping,text="Trân Châu",variable=var_t1).pack(anchor="w")
tk.Checkbutton(f_topping,text="Thạch",variable=var_t2).pack(anchor="w")
tk.Checkbutton(f_topping,text="Kem Cheese",variable=var_t3).pack(anchor="w")

# 4 Thanh toán 
tk.Label(root,text="Thanh toán:").grid(row=4, column=0,sticky=tk.W,padx=5,pady=5)
combo_payment = ttk.Combobox(root)
combo_payment['values']=("Tiền mặt","Chuyển khoản")
combo_payment['state']="readonly"
combo_payment.current(0)
combo_payment.grid(row=4,column=1,sticky="w", pady= 30 )


#5 Nút đặt hàng
btn = tk.Button(root,text="Đặt hàng", width=20, command=calculate_and_oder)
btn.grid(row=5, column=0,columnspan=2,pady=30)


root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

root.mainloop()
