# Nó inicial
class ClassNo:
    def __init__(self, profileUsuary):
        self.profileUsuary = profileUsuary
        self.next = None
        self.prox = None

# Lista duplamente encadeada
class class_List:
    def __init__(self):
        self.start = None
        self.end = None
        self.size = 0

    # Verifica se a lista está vazia
    def nenhum(self):
        return self.size == 0
    
    # Adiciona no início da lista
    def add(self, profileUsuary):
        novo_no = ClassNo(profileUsuary)
        if self.nenhum():
            self.start = self.end = novo_no
        else:
            novo_no.next = self.start 
            self.start.prox = novo_no
            self.start = novo_no
        self.size += 1
        
    # Remove um nó da lista
    def remove(self, classNo):
        if classNo.prox:
            classNo.prox.next = classNo.next
        else:
            self.start = classNo.next
        if classNo.next:
            classNo.next.prox = classNo.prox
        else:
            self.end = classNo.prox
        self.size -= 1

    # Procura um perfil na lista
    def seach(self, profileUsuary):
        atual = self.start
        while atual:
            if atual.profileUsuary == profileUsuary:
                return atual
            atual = atual.next
        return None

    # Imprime a lista
    def print_Lista(self):
        atual = self.start
        while atual:
            print(atual.profileUsuary)
            atual = atual.next

# Função principal
def main():
    fun_profile = class_List()
    check = True
    while check:
        action = input().split()
        if action[1] in ["seguiu", "curtiu", "comentou"]:
            profileUsuary = action[-1]
            procurarUsuary = fun_profile.seach(profileUsuary)
            if procurarUsuary:
                fun_profile.remove(procurarUsuary)
            fun_profile.add(profileUsuary)
        elif action[1] == "deixou":
            profileUsuary = action[-1]
            procurarUsuary = fun_profile.seach(profileUsuary)
            if procurarUsuary:
                fun_profile.remove(procurarUsuary)
        elif action[1] == "fechou":
            check = False
    fun_profile.print_Lista()

if __name__ == "__main__":
    main()