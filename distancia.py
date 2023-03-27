x=float(input("Insira x1: "))
y=float(input("Insira y1: "))
X=float(input("Insira x2: "))
Y=float(input("Insira y2: "))
d=((x-X)**2+(y-Y)**2)**(1/2)
if d<10:
    print("perto")
else:
    print("longe")
