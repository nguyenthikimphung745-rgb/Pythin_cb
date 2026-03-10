import tkinter as tk
root = tk.Tk()
root.title("Phương trình bậc 2")

lblTitle = tk.Label(root,text="TÍNH PHƯƠNG TRÌNH BẬC 2",font=("Arial,18,bold"))
lblTitle.grid(row= 0, column= 0 , columnspan=2)
lblCt = tk.Label(root,text=" ax² + bx + c = 0",font=("Arial,18,bold"))
lblCt.grid(row= 2, column= 0 , columnspan=2)

lbl_A = tk.Label(root,text= "A")
lbl_A.grid(row=3,column=0,padx=5,pady=10)
ent_A = tk.Entry(root)
ent_A.grid(row=3,column=1)

lbl_B = tk.Label(root,text= "B")
lbl_B.grid(row=3,column=2,padx=5,pady=10)
ent_B = tk.Entry(root)
ent_B.grid(row=3,column=3)

lbl_C = tk.Label(root,text= "C")
lbl_C.grid(row=3,column=4,padx=5)
ent_C = tk.Entry(root)
ent_C.grid(row=3,column=4)

root.mainloop()