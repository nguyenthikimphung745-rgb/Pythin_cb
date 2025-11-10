try:
    So = int(input("Nhap so: "))
except:
    print("Loi nhap lieu!")
else:
    if So%2 ==0:
        print(f"{So} La so chan!")
    else:
        print(f"{So} La so le!")