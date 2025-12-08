
def tinhcvdt(cd,cr):
            dt = cd*cr
            cv = (cd+cr)*2
            return cv,dt
while True:
    try:
        cd= int(input("Nhap chieu dai:"))
        cr= int(input("Nhap chieu rong:"))
        break
    except ValueError:
        print("Loi nhap lieu!")

    
    
        
        
        