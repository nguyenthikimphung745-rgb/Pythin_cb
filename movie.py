import tkinter as tk
from tkinter import ttk,messagebox
class MovieBookingApp:
    def __init__(self,root):
        self.root=root
        self.root.title("He Thong Dat Ve Xem Phim")
        self.root.geometry("500x650")
        self.root.configure(bg="white") 
        self.base_price = 70000
        self.seat_price={
            "Thuong": 0,
            "VIP": 30000,
            "Doi": 60000
        }
        self.service_price={
            "Bap": 25000,
            "Nuoc": 15000,
            "Combo": 35000
        }
        self.create_widgets()

    def create_widgets(self):
        title=tk.Label(self.root,text="MOVIE TICKET BOOKING",
                            font=("Arial",22,"bold"),
                            fg="brown",
                            bg="white")
        title.pack(pady=20)
        frame=tk.Frame(self.root,bg="white")
        frame.pack(padx=20,pady=10)
        lbl_name=tk.Label(frame,text="Tên khách hàng:",
                            font=("Arial",14),
                            bg="white")
        lbl_name.grid(row=0,column=0,sticky="W",pady=10)

        self.entry_name=tk.Entry(frame,font=("Arial",14),bg="white")
        self.entry_name.grid(row=0,column=1,pady=10)

        lbl_seat=tk.Label(frame,text="Loại ghế:",
                       font=("Arial",14),
                            bg="white" )
        lbl_seat.grid(row=1,column=0,sticky="W",pady=15)
        seat_frame=tk.LabelFrame(frame,text="Chọn ghế",bg="white")
        seat_frame.grid(row=1,column=1)

        self.seat_var = tk.StringVar(value="VIP")
        tk.Radiobutton(seat_frame,
                       text="Thường (+0đ)",
                       variable=self.seat_var,
                       value="Thuong",
                       bg="white").pack(anchor="w")
        tk.Radiobutton(seat_frame,
                        text="VIP (+30k)",
                        variable=self.seat_var,
                        value="VIP",
                        bg="white").pack(anchor="w")
        
        tk.Radiobutton(seat_frame,
                        text="Doi (+60k)",
                        variable=self.seat_var,
                        value="Đôi",
                        bg="white").pack(anchor="w")
        
        lbl_service=tk.Label(frame,text="Dịch vụ thêm:",
                             font=("Arial",14),
                             bg="white" )
        lbl_service.grid(row=2,column=0,sticky="W",pady=15)
        service_frame=tk.LabelFrame(frame,bg="white")
        service_frame.grid(row=2,column=1)

        self.bap_var = tk.BooleanVar()
        self.nuoc_var = tk.BooleanVar()
        self.combo_var = tk.BooleanVar()
        tk.Checkbutton(
            service_frame,
            text="Bắp rang (+25k)",
            variable=self.bap_var,
            bg="white"
        ).pack(anchor="w")
        tk.Checkbutton(
            service_frame,
            text="Nước ngọt (+15k)",
            variable=self.nuoc_var,
            bg="white"
        ).pack(anchor="w")
        tk.Checkbutton(
            service_frame,
            text="Combo (+35k)",
            variable=self.combo_var,
            bg="white"
        ).pack(anchor="w")

        tk.Label(frame,text="Suất chiếu:",
                             font=("Arial",14),
                             bg="white" ).grid(row=3,column=0,sticky="W",pady=15)
        self.time_var = tk.StringVar()
        combo_time = ttk.Combobox(
            frame,textvariable= self.time_var,
            state="readonly"
        )
        combo_time["values"] = ("8.00","13.00","18.00","21.00")
        combo_time.current(0)
        combo_time.grid(row=3,column=1)
        tk.Label(frame,text="Số lượng vé:",
                            font=("Arial",14),
                            bg="white").grid(row=4,column=0,sticky="W",pady=15)
        self.entry_ticket= tk.Entry(frame)
        self.entry_ticket.grid(row=4,column=1)

        btn = tk.Button(self.root,text="Đặt vé", font=("Arial",16,"bold"),bg="brown",fg="white",width=20,command=self.book_ticket)
        btn.pack(pady=30)
    def book_ticket(self):
        name = self.entry_name.get().strip()
        if name =="":
            messagebox.showwarning("Lỗi","Vui lòng nhập tên.")
        try:
            quantity=int(self.entry_ticket.get())
            if quantity<=0:
                messagebox.showwarning("Lỗi","Phải nhập số >0")
                return
        except:
            messagebox.showwarning("Lỗi","Số lượng vé phải là số nguyên dương.")
            return
        
        seat = self.seat_var.get()
        ticket_price = self.base_price + self.seat_price[seat]
        total = ticket_price*quantity

        services=[]
        if(self.bap_var.get()):
            total += self.service_price["Bap"]
            services.append("Bắp rang")
        if(self.nuoc_var.get()):
            total += self.service_price["Nuoc"]
            services.append("Nước ngọt")
        if(self.combo_var.get()):
            total += self.service_price["Combo"]
            services.append("Combo")
        
        time = self.time_var.get()
        services_text = ",".join(services) if services else"Không"
        result =(
            f"Khách hàng:{name}\n"
            f"Suất chiếu:{time}\n"
            f"Loại ghế:{seat}\n"
            f"Số lượng vé:{quantity}\n"
            f"Dịch vụ:{services_text}\n\n"
            f"Tổng tiền:{total:,}đ"
        )
        messagebox.showinfo("Đặt vé thành công",result)

if __name__=="__main__":
    root =tk.Tk()
    app =MovieBookingApp(root)
    root.mainloop()