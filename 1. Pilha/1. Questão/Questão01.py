def pilha_Itens(pilha):
    # criação dos arrays
    nomeJogadoresDict = {"endrick", "neymar", "cr7", "messi"}
    marcasDict = {"new balance":"endrick", "puma":"neymar", "nike":"cr7", "adidas":"messi"}
    # entradas vinda do input
    subPilhas = pilha.split('-')
    listaJogador = []

    for i in subPilhas:
        if i in nomeJogadoresDict:
            listaJogador.append(i)
        elif i in marcasDict:
            if marcasDict[i] not in listaJogador:
                return "Incorreto"
            elif len(listaJogador) > 0:
                listaJogador.pop()
        else:
            return "Incorreto"
    # condição de chek - jogador    
    if not listaJogador:
        return "Correto"
    else:
        return "Incorreto"

resultPilha = input()
print(pilha_Itens(resultPilha))