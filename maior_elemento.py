def maior_elemento(lista):
    L1=[lista[0]]
    N=0
    while N < len(lista):
        n=0
        item=True
        while n < len(L1):
            if L1[n] == lista[N]:
                item=False
                break
            n=n+1
        if item == True:
            L1.append(lista[N])
        N=N+1
    N=0
    while N < len(L1):
        n=0
        while n < len(L1):
            if L1[N]>L1[n] and n!=N and n>N:
                aux=L1[N]
                L1[N]=L1[n]
                L1[n]=aux
            n=n+1
        N=N+1
    return L1[N-1]

def maior_elemento1(lista):
    N=0
    maior=lista[0]
    m=1
    while N < len(lista):
        if lista[N]>maior:
            maior=lista[N]
            m=N+1
        N=N+1
    return m
