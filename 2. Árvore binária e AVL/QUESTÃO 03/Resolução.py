# No da arvore
class no:
    def __init__(self, value, level):
        self.value = value
        self.level = level
        self.left = None
        self.right = None
# arvore
class Tree:
    def __init__(self):
        self.root = None
    # Adiciona
    def add(self, value):
        self.root = self._add(self.root, value, current_level=0)
    def _add(self, new_node, current_node, current_level):
        if new_node is None:
            return no(current_node, current_level)
        if current_node < new_node.value:
            new_node.left = self._add(new_node.left, current_node, current_level + 1)
        elif current_node > new_node.value:
            new_node.right = self._add(new_node.right, current_node, current_level + 1)
        return new_node
    # em ordem
    def funcOrd(self, inic):
        brek = []
        if inic:
            brek += self.funcOrd(inic.left)
            brek.append(inic.value)
            brek += self.funcOrd(inic.right)
        return brek
    # Encontre o no
    def encontNo(self, valor, inic):
        if inic is None:
            return -1
        elif inic.value == valor:
            return inic.level
        if valor < inic.value:
            return self.encontNo(valor, inic.left)
        else:
            return self.encontNo(valor, inic.right)

# função principal com tratamento de erro 
def main():
    tree = Tree()
    try:
        while True:
            operation = input().split()
            if operation[0] == "ADD":
                tree.add(int(operation[1]))
                print(tree.encontNo(int(operation[1]), tree.root))
            elif operation[0] == "SCH":
                rec = tree.encontNo(int(operation[1]), tree.root)
                print(rec)
                if rec >= 0:
                    lst = tree.funcOrd(tree.root)
                    lst.remove(int(operation[1]))
                    lst.insert(0, int(operation[1]))
                    tree = Tree()
                    for i in lst:
                        tree.add(i)
    except:
        pass
# chamando a função main
if __name__ == "__main__":
    main()