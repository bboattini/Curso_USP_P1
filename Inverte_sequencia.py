

n=1
L=[]
N=-1
while n!=0:
    n=int(input('Digite um número: '))
    if n!=0:
        L.append(n)
print()
while (-1*N) <= len(L):
    print(L[N])
    N=N-1
