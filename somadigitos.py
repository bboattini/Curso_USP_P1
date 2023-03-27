n=int(input("Digite um número inteiro: "))
s=0
if n<0:
    n=n*(-1)
while n!=0:
    s=s+(n%10)
    n=n//10
print(s)
