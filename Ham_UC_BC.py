import tinhUCBC
while True:
    try:
        A = int(input("Nhap A:"))
        B = int(input("Nhap B:"))
        if A>0 and B>0:
            break
    except ValueError:
        print("Loi nhap lieu!")

print(f"USCLN cua {A}v a {B} la {tinhUCBC.USCLN(A,B)}")
