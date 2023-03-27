n=int(input("Digite um número inteiro: "))
d=n
primo=True
while d>2:
    d=d-1
    if n%d==0:
        primo=False
        print("não primo")
        break
if primo==True:
    print("primo")
