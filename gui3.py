import tkinter as tk
root = tk.Tk()
root.title("Login Form")
root.geometry("300x200")
# Label Username
lbl_user = tk.Label(root, text="Username:")
lbl_user.place(x=40, y=50)
# Ô nhập username
entry_user = tk.Entry(root)
entry_user.place(x=120, y=50, width=120)
#Label Password
lbl_pass = tk.Label(root, text="Password:")
lbl_pass.place(x=40, y=90)
# Ô nhập password
entry_pass = tk.Entry(root, show="*")
entry_pass.place(x=120, y=90, width=120)
# Nút Login
btn_login = tk.Button(root, text="Login")
btn_login.place(x=120,y=130, width=80)

root.mainloop()