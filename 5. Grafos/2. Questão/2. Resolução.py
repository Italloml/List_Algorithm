def buscador(u, visited, grafic): #realiza busca
    visited[u] = True
    caount = 1
    for v in grafic[u]:
        if not visited[v]:
            caount += buscador(v, visited, grafic)
    return caount
def contUsuary(n, m, conection): #Recebe números de usuário
    grafic = [[] for _ in range(n + 1)]
    for u, v in conection:
        grafic[u].append(v)
        grafic[v].append(u)

    resultado = [0] * (n + 1)
    visited = [False] * (n + 1)
    for i in range(1, n + 1):
        visited = [False] * (n + 1)
        resultado[i] = buscador(i, visited, grafic)
    return resultado[1:]
n, m = map(int, input().split()) #entrada
conection = [list(map(int, input().split())) for _ in range(m)]
resultado = contUsuary(n, m, conection) #chamada de impressão
print(*resultado)