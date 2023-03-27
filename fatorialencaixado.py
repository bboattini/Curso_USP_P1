a=False
while a==False:
    n=int(input("Digite o valor de n: "))
    f=1
    if n==0:
        a=True
    while n>0:
        f=f*n
        n=n-1
    print(f)
