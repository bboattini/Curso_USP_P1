n=int(input("Digite o valor de n: "))
f=1
if n==0:
    print("1")
else:
    while n>0:
        f=f*n
        n=n-1
    print(f)
