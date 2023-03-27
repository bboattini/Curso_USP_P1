t=input("Por favor, entre com o número de segundos que deseja converter: ")
s=int(t)
D=s//86400
H=(s%86400)//3600
M=((s%86400)%3600)//60
S=((s%86400)%3600)%60
print(D,"dias,",H,"horas,",M,"minutos e",S,"segundos.")
