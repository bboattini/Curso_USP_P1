def maximo(a, b, c):
    if a>b:
        m=a
        if a<c:
            m=c
    else:
        m=b
        if b<c:
            m=c
    return m
