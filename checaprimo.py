primo=True
n=int(input("Insira um inteiro positivo: "))
d=n
while d>2:
    d=d-1
    if n%d==0:
        primo=False
        break
print(primo)
