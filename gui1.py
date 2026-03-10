import tkinter as tk
root = tk.Tk()
root.geometry("300x100")
# Tạo nút bấm 
btn1 = tk.Button(root, text="Nút Trái")
btn2 = tk.Button(root, text="Nút Giữa")
btn3 = tk.Button(root, text="Nút Phải")

# Sắp xếp bằng pack()
btn1.pack(side=tk.LEFT, padx=10)
btn2.pack(side=tk.LEFT, padx=10)
btn3.pack(side=tk.LEFT, padx=10)

root.mainloop()