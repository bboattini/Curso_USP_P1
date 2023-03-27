
def maior_primo(n):
    d=n
    r=n
    primo=True
    while n>2:
        while d>2:
            d=d-1
            primo=True
            if n%d==0:
                primo=False
                break
        if primo==True:
            r=n
            break
        n=n-1
    return r
        
