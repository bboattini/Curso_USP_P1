def soma_hipotenusas(N):
    s=0
    while N>1:
        n=N
        while n>1:
            n=n-1
            c=float(((N**2)-(n**2))**(1/2))
            if c ==int(c):
                s=s+N
                break
        N=N-1
    return s
