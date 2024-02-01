# class No arvore
class noArvorConhec:
    def __init__(self, valor):
        self.valor = valor
        self.filhos = []

#função contrução da arvores conhecimento
def construir_arvore_conhecimento(licoes):
    raiz = noArvorConhec(licoes[0])
    for aula in licoes[1:]:
        no_atual = raiz
        while True:
            if aula < no_atual.valor:
                if not no_atual.filhos or not no_atual.filhos[0]:
                    no_atual.filhos.insert(0, noArvorConhec(aula))
                    break
                else:
                    no_atual = no_atual.filhos[0]
            else:
                if not no_atual.filhos or not no_atual.filhos[-1]:
                    no_atual.filhos.append(noArvorConhec(aula))
                    break
                else:
                    no_atual = no_atual.filhos[-1]
    return raiz
# função de conhecimento total
def conhecTotal(no, profundidade):
    if not no or profundidade == 0:
        return 0
    total = no.valor
    for filho in no.filhos:
        total += conhecTotal(filho, profundidade - 1)
    return total

# Entrada
n, m = [int(x) for x in input().split()]
licoes_hogwarts = [int(x) for x in input().split()]
licoes_cin = [int(x) for x in input().split()]
profundidade = int(input())

#chamada
arvore_hogwarts = construir_arvore_conhecimento(licoes_hogwarts)
arvore_cin = construir_arvore_conhecimento(licoes_cin)
conhecimento_total = conhecTotal(arvore_hogwarts, profundidade) + conhecTotal(arvore_cin, profundidade)

#print final
print(f"valor total de conhecimento: {conhecimento_total}")