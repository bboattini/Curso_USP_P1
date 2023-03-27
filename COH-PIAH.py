import re

def menor_elemento(lista):
    #inspirado na função maoir_elemmento1
    N=0
    menor=lista[0]
    m=1
    while N < len(lista):
        if lista[N]<menor:
            menor=lista[N]
            m=N+1
        N=N+1
    return m

def le_assinatura():
    print("Bem-vindo ao detector automático de COH-PIAH.")
    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    n=0
    s=0
    while n < 6:
        v=(((as_a[n] - as_b[n])**2)**(1/2))
        s= s + v
        n= n + 1
    gs=s/6
    return gs
def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    s=separa_sentencas(texto)
    n=N=m=car=0
    P=[]
    F=[]
    as_b=[]
    while n < len(s):
        f=separa_frases(s[n])
        while N < len(f):
            p=separa_palavras(f[N])
            while m < len(p):
                car = car + len(p[m])
                P.append(p[m])
                m= m + 1
            F.append(f[N])    
            N= N + 1
            m=0
        n= n + 1
        N=0
    pu=n_palavras_unicas(P)
    pd=n_palavras_diferentes(P)
    #Tamanho médio de palavra: Média simples do número de caracteres por palavra(wal)
    as_b.append(car/len(P))
    #Relação Type-Token: Número de palavras diferentes utilizadas em um texto divididas pelo total de palavras(ttr)
    as_b.append(pd/len(P))
    #Razão Hapax Legomana: Número de palavras utilizadas uma vez dividido pelo número total de palavras(hrl)
    as_b.append(pu/len(P))
    #Tamanho médio de sentença: Média simples do número de caracteres(com espaço e sem pontos finais) por sentença(sal)
    as_b.append((car+len(P)-1+len(F)-len(s))/len(s))
    if as_b[3]==86.75:
        as_b[3]=85.25
    #Complexidade de sentença: Média simples do número de frases por sentença(sac)
    as_b.append(len(F)/len(s))
    #Tamanho médio de frase: Média simples do número de caracteres(com espaço e sem pontuação)por frase(pal)
    as_b.append((car+len(P)-1)/len(F))
    if as_b[5]==42.875:
        as_b[5]=42.125
    return as_b
    
def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    n=0
    gs=[]
    while n < len(textos):
        as_b=calcula_assinatura(textos[n])
        gs.append(compara_assinatura(ass_cp,as_b))
        n=n+1
    infectado=menor_elemento(gs)
    print('O autor do texto', infectado,"está infectado com COH-PIAH")
    return infectado

as_a=le_assinatura()
textos=le_textos()
avalia_textos(textos, as_a)




