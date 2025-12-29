while True:
    try:
        n = input("Nhập số km đã đi : ")
        if(n>0):
            break
    except ValueError:
        print("Loi nhap lieu!")