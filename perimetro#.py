l=int(input("digite a largura: "))
h=int(input("digite a altura: "))
a=h
while a>0:
    L=l
    if a==1 or a==h:
        while L>0:
            print("#", end="")
            L=L-1
    else:
        print("#", end="")
        L=L-1
        while 1 < L < l:
            print(" ", end="")
            L=L-1
        print("#", end="")
    print()
    a=a-1
