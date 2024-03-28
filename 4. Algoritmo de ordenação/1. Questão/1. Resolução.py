def funcBubbleSort(compri):# Bubble Sort
    n = len(compri)
    for i in range(n):
        for j in range(0, n-i-1):
            numero1 = int(compri[j].split(':')[0].split()[1])
            numero2 = int(compri[j+1].split(':')[0].split()[1])
            if numero1 > numero2:
                compri[j], compri[j+1] = compri[j+1], compri[j]
    for i, praca in enumerate(compri, start=1):
        numero = praca.split(':')[0].split()[1] # Separar nomes
        children = praca[praca.index(':') + 1:].split()
        children.sort()
        result = f"Praça {numero}: {' '.join(children)}" # Construir ordenada
        print(result)
# Entrada
nomePracas = int(input())  # Número de praças
lugarPracas = []
for _ in range(nomePracas):
    praca = input()
    lugarPracas.append(praca)
funcBubbleSort(lugarPracas)