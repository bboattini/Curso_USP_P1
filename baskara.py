
a=float(input("insira o valor de a: "))
b=float(input("insira o valor de b: "))
c=float(input("insira o valor de c: "))
delta=b**2 -(4*a*c)
if(delta < 0):
    print("esta equação não possui raízes reais")
if(delta == 0):
    x=-b/(2*a)
    print("a raiz desta equação é", x)
if(delta > 0):
    x1=(-b+delta**(1/2))/(2*a)
    x2=(-b-delta**(1/2))/(2*a)
    if x2>x1:
        print("as raizes são", x1,"e", x2)
    else:
        print("as raizes são", x2,"e", x1)
