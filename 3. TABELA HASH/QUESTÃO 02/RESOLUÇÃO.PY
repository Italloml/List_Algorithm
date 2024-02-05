class Node:
    def __init__(self, nome, tamanhoGrupo):
        self.nome = nome
        self.tamanhoGrupo = tamanhoGrupo
        self.next = None

    def __str__(self):
        return self.nome

class HashTable:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.table = [None] * tamanho

    def funçãoHash(self, chave):
        return chave % self.tamanho

    def inseri(self, chave, value):
        index = self.funçãoHash(chave)
        novoNo = Node(value, chave)
        if self.table[index] is None:
            self.table[index] = novoNo
        else:
            atual = self.table[index]
            while atual.next:
                atual = atual.next
            atual.next = novoNo

    def valor(self, chave): #função valor
        index = self.funçãoHash(chave)
        valores = []
        atual = self.table[index]
        while atual:
            if atual.tamanhoGrupo == chave:
                valores.append(atual)
            atual = atual.next
        return valores

def formar_grupos(entrada): #grupos
    hash_table = HashTable(100)

    for line in entrada:
        data = line.split()
        if len(data) == 2:
            name, group_size = data
            group_size = int(group_size)
            hash_table.inseri(group_size, name)
    result = []
    for size in range(1, 11):
        names = hash_table.valor(size)
        if names:
            names.sort(key=lambda x: x.nome)  # Ordenar os nomes dentro de cada grupo
            grupoAtual = []
            for node in names:
                grupoAtual.append(str(node))
                if len(grupoAtual) == size:
                    result.append(grupoAtual.copy())
                    grupoAtual.clear()
    return result
def entradaLinha(): #entrada
    entrada = []
    while True:
        try:
            entLinhas = input()
            if not entLinhas:
                break
            entrada.append(entLinhas)
        except EOFError:
            break
    return entrada
entrada = entradaLinha()
output = formar_grupos(entrada)
print(output) 


