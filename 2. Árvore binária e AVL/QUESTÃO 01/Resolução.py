# classe livro
class arvoresLivros:
    def __init__(self, chave=None, dir=None, esq=None):
        self.chave = chave
        self.dir = dir
        self.esq = esq

# função insere
def insere(nodo, raiz):
    if nodo is None:
        return
    elif raiz.chave is None:
        raiz.chave = nodo.chave
    elif nodo.chave < raiz.chave:
        if raiz.esq is None:
            raiz.esq = nodo
        else:
            insere(nodo, raiz.esq)
    else:
        if raiz.dir is None:
            raiz.dir = nodo
        else:
            insere(nodo, raiz.dir)

# função imprime
def imprime(raizb):
    sequencia = []
    if raizb is not None:
        sequencia.extend(imprime(raizb.esq))
        sequencia.append(raizb.chave)
        sequencia.extend(imprime(raizb.dir))
    return sequencia

# resultado arvore
def Result_Arvore():
    rec = arvoresLivros()
    recebeLivros = input()
    recebeLivros = recebeLivros.split(' ')
    
    for livro in recebeLivros:
        nodo = arvoresLivros(int(livro))
        insere(nodo, rec)

    resultado = imprime(rec)
    return resultado

# Executa a função
pegaFuncao = Result_Arvore()
print(*pegaFuncao)