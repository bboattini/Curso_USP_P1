
def partida():
    n=int(input('Quantas peças?'))
    M=int(input('Limite de peças por jogada?'))
    print()
    while n<=0:
        print("Oops! Jogada inválida! Tente de novo.")
        n=float(input('Quantas peças?'))
        M=float(input('Limite de peças por jogada?'))
    if (M+1)%n==0 or M>n or ((n==5 or n==11) and M==3):
        print('Computador começa!')
        print() 
        while n!=0:
            v=0
            if n==1:
                break
            n=n - computador_escolhe_jogada(n, M)
            if n==0:
                break
            n=n - usuario_escolhe_jogada(n, M)
    else:
        print('Voce começa!')
        print()
        while n!=0:
            v=0
            n=n - usuario_escolhe_jogada(n, M)
            if n==1:
                break
            n=n - computador_escolhe_jogada(n, M)
            if n==0:
                break
    print('Fim do jogo! O computador ganhou!')
    print()
    
def usuario_escolhe_jogada(n, M):
    if n<=0:
        print("Oops! Jogada inválida! Tente de novo.")
        print()
    x=int(input('Quantas peças vc vai tirar?'))
    while x > M or x<=0:
        print("Oops! Jogada inválida! Tente de novo.")
        print()
        x=int(input('Quantas peças vc vai tirar?'))
    print('Voce tirou',x ,'peças')
    n=n-x
    if n==1:
        print('agora resta apenas uma peça no tabuleiro')
        print()
        print('O Computador tirou uma peça')
    else:
        print('agora restam',n ,'peças no tabuleiro')
        print()
    return x

def computador_escolhe_jogada(n, M):
    while n!=0:
        v=0
        if n<=M:
            v=n
            break
        while((M+1)%n!=0 or n==1):
            v=v+1
            n=n-1
            if v>M:
                v=M
            if n==0:
                break
        if n==0:
            print('O Computador tirou', v,'peças')
            break
        if v==0:
            v=v+1
            n=n-1
            if v>M:
                v=M
        while ((M+1)%n!=0 or n==1):
            v=v+1
            n=n-1
            if v>M:
                v=M
            if n==0:
                break
        print('O Computador tirou', v,'peças')
        if n!=0:
            print('agora restam',n ,'peças no tabuleiro')
            print()
            break
        else:
            break
    return v

def campeonato():
    print('Voce escolheu um campeonato!')
    print()
    r=0
    while r<3:
        r=r+1
        print('**** Rodada', r,'****')
        print()
        p=partida()
    print("**** Final do campeonato! ****")
    print()
    print("Placar: Você 0 X 3 Computador")
print("Bem-vindo ao jogo do NIM! Escolha:")
print()
print("1 - para jogar uma partida isolada")
o=int(input("2 - para jogar um campeonato! "))
if o==1:
    p=partida()
    print(p)
if o==2:
    p=campeonato()






    


