import tkinter as tk
root = tk.Tk()
root.title("Tính cửa sổ BML")

def tinh_BMI():
    try:
        Chieucao = float(ent_Chieucao.get())
        Cannang = float(ent_Cannang.get())
        BMI = Cannang/(Chieucao**2)
        if BMI <18.5:
            loai = "Thiếu cân"
        elif BMI < 25:
            loai = "Bình thường"
        elif BMI < 30:
            loai = " Thừa cân"
        else:
            loai = "Quá béo"
        lblKetQua.config(text=f"BMI của bạn là{BMI:.1f} - Bạn{loai}")
        
    except:
        lblKetQua.config(text="Vui lòng nhập đúng giá trị.")
    

lblTitle = tk.Label(root,text="TÍNH CHỈ SỐ BMI",font=("Arial,18,bold"))
lblTitle.grid(row= 0, column= 0 , columnspan=2)
lbl_Chieucao = tk.Label(root,text= "Chieu cao (m)")
lbl_Chieucao.grid(row=1,column=0)
ent_Chieucao = tk.Entry(root)
ent_Chieucao.grid(row=1,column=1)

lbl_Cannang = tk.Label(root,text= "Cân nặng (kg)")
lbl_Cannang.grid(row=2,column=0)
ent_Cannang = tk.Entry(root)
ent_Cannang.grid(row=2,column=1)

btntinhBMI = tk.Button(root, text="Tính BMI", command=tinh_BMI)
btntinhBMI.grid(row= 3,column= 0,columnspan=2)

lblKetQua=tk.Label(root,text="")
lblKetQua.grid(row= 4,column= 0,columnspan=2)



root.mainloop()








