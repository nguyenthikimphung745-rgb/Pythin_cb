def USCLN(A,B):
    if B==0:
        return A
    while B!=0:
        temp= B
        B=A%B
        A=temp
    return A