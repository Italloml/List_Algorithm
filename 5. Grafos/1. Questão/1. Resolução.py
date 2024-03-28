def buskTeso(lugar): #função buscar Tesouro
    visitado = set()  
    bloco = [(0, 0)]  
    while bloco:
        salAtua, nivAtua = bloco.pop(0)
        if lugar[salAtua] == "Tesouro":
            return "TESOURO :)"
        visitado.add(salAtua)
        for chave in lugar[salAtua]:
            if chave not in visitado and chave < len(lugar):
                bloco.append((chave, nivAtua + 1))
    return "SEM TESOURO :("
def entrada(): #entrada do input
    lugar = []
    while True:
        entrada = input().strip()
        if entrada == "Tesouro":
            lugar.append(entrada)
            break
        lugar.append(list(map(int, entrada.split())))
    return lugar
lugar = entrada()
resultado = buskTeso(lugar)
print(resultado)