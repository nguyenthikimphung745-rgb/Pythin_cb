import tkinter as tk #Buoc 1
#Buoc 2: Tạo cửa sổ chính
root = tk.Tk()
root.title("Ung dung dau tien")
root.geometry("300x200") # Rộng x cao

#Bước 3: Tạo và đặt widget lên cửa sổ
lbl_hello = tk.Label(root,text="Hello,Gui world!",font=("Arial",14))
lbl_hello.pack(pady=50)# Đưa nhãn vào giữa

#Bước 4: Chạy vòng lập sự kiện
root.mainloop()