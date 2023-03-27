
def n_primos(N):
    n=N
    d=n
    r=1
    primo=True
    while n>2:
        d=n
        while d>2:
            d=d-1
            if n%d==0:
                primo=False
                break
            else:
                primo=True
        if primo==True:
            r=r+1
        n=n-1
    return r

