def quicksort(varNum): #função QuickSort
    if len(varNum) <= 1:
        return varNum
    pir = varNum[len(varNum) // 2]
    esq = [x for x in varNum if x < pir]
    EspMeio = [x for x in varNum if x == pir]
    dir = [x for x in varNum if x > pir]
    return quicksort(esq) + EspMeio + quicksort(dir)
# entrada
idades = input()
idades = list(map(int, idades.split()))

idade1 = idades[0]
idades = quicksort(idades)
idade2 = idades[-1]
print(f"Atenção, Grinch está indo atrás do cidadão de {idade2} anos, e logo após isso ele vai atrás do cidadão de {idade1} anos.")