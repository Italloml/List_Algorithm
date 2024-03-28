def funcOrdenaDobra(lista, metodo, dobrar=False): #funão que dobra e ordena
    def funInsertSort(arr):
        for i in range(1, len(arr)):
            chave = arr[i]
            j = i - 1
            while j >= 0 and chave < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = chave
    def funcQuickSor(arr): #Função Quick Sort
        if len(arr) <= 1:
            return arr
        else:
            pivo = arr[0]
            les = [x for x in arr[1:] if x <= pivo]
            greater = [x for x in arr[1:] if x > pivo]
            return funcQuickSor(les) + [pivo] + funcQuickSor(greater)
    def funcMergeSort(arr): #função Merge Sort
        if len(arr) > 1:
            mid = len(arr) // 2
            esqHalf = arr[:mid]
            dirHalf = arr[mid:]
            funcMergeSort(esqHalf)
            funcMergeSort(dirHalf)
            i = j = k = 0
            while i < len(esqHalf) and j < len(dirHalf):
                if esqHalf[i] < dirHalf[j]:
                    arr[k] = esqHalf[i]
                    i += 1
                else:
                    arr[k] = dirHalf[j]
                    j += 1
                k += 1
            while i < len(esqHalf):
                arr[k] = esqHalf[i]
                i += 1
                k += 1
            while j < len(dirHalf):
                arr[k] = dirHalf[j]
                j += 1
                k += 1

    def funcShellSort(arr): #função Shell Sort
        n = len(arr)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                variTemp = arr[i]
                j = i
                while j >= gap and arr[j - gap] > variTemp:
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = variTemp
            gap //= 2
    def funSeletionSort(arr): #função Selection Sort
        for i in range(len(arr)):
            minIndi = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[minIndi]:
                    minIndi = j
            arr[i], arr[minIndi] = arr[minIndi], arr[i]
    if metodo == "Insertion Sort": # Escolher o método 
        funInsertSort(lista)
    elif metodo == "Quick Sort":
        lista = funcQuickSor(lista)
    elif metodo == "Merge Sort":
        funcMergeSort(lista)
    elif metodo == "Shell Sort":
        funcShellSort(lista)
    elif metodo == "Selection Sort":
        funSeletionSort(lista)
    else:
        print("Método de ordenação não reconhecido!")

    if dobrar: # Dobrar a lista
        lista = [x * 2 for x in lista]
    return lista
# Entrada
entrada_lista = input().split(", ")
entrada_metodo = input()
dobrado = input()
if dobrado == "dobre!":
  lista_presente = [(int(x) * 2) for x in entrada_lista] # Converter 
else:
  lista_presente = [int(x) for x in entrada_lista] 
resultado = funcOrdenaDobra(lista_presente, entrada_metodo, dobrado == "dobrado") # Chamar a função 
print(resultado)