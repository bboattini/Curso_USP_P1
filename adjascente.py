n=int(input("Digite um numero inteiro: "))
a=False
r=-1
if n<0:
    n=-1*n
while n != 0:
    if n%10==r:
        a=True
        print("sim")
        break
    r=n%10
    n=n//10
if a==False:
    print("não")
        
        
