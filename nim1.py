
def partida():
    v=0
    N=
    M=
    if (M+1)%N==0:
        print('Voce começa!')
        print()
        while n!=0:
            x=usuario_escolhe_jogada(N, M)
            print('Voce tirou',x ,'peças')
            n=N-x
            if n==1
                print('agora resta apenas uma peça no tabuleiro')
            else
                print('agora restam',n ,'peças no tabuleiro')
            while (M+1)%n!=0:
                v=v+1
                n=n-1
            if v==0:
                v=1
            while (M+1)%n!=0:
                v=v+1
                n=n-1
            print('O Computador tirou',v ,'peças')
            if n!=0:
                print('agora restam',n ,'peças no tabuleiro')
    else:
        print('Computador começa!')
        print() 
        while n!=0:
            while (M+1)%n!=0:
                v=v+1
                n=n-1
            if v==0:
                v=1
            while (M+1)%n!=0:
                v=v+1
                n=n-1
            print('O Computador tirou',v ,'peças')
            if n!=0:
                print('agora restam',n ,'peças no tabuleiro')
            if n==0:
                break
            x=usuario_escolhe_jogada(N, M)
            print('Voce tirou',x ,'peças')
            n=N-x
            if n==1
                print('agora resta apenas uma peça no tabuleiro')
            else
                print('agora restam',n ,'peças no tabuleiro')
    print('Fim do jogo! O computador ganhou!')
    
def usuario_escolhe_jogada(N, M):
x=int(input('Quantas peças vc vai tirar?'))
    while x > M:
        print("Oops! Jogada inválida! Tente de novo.")
        print()
        x=int(input('Quantas peças vc vai tirar?'))
         print('Voce tirou',x ,'peças')
            n=N-x
            if n==1
                print('agora resta apenas uma peça no tabuleiro')
            else
                print('agora restam',n ,'peças no tabuleiro')
    return n






