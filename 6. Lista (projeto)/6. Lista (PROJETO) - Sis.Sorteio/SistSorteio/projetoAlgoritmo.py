from random import sample
from tkinter import *

window = Tk()

class Application():
    def __init__(self):
        self.window = window
        self.Tela()
        self.createButton()
        self.createLabel()
        window.mainloop()
    
    def createButton(self):
        self.btn = Button(text="Sortear", background='#4F4F4F', command=self.btnSort)
        self.btn.place(relx=0.40, rely=0.4, relheight=0.1, relwidth=0.2)

    def Tela(self):
        self.window.title("SISTEMA DE SORTEIO")
        self.window.configure(background='#1e3743')
        self.window.geometry('720x620')
        self.window.resizable(True, True)
        self.window.maxsize(height=900, width=700)
        self.window.minsize(height=400, width=300)
    
    def createLabel(self):
        self.image = PhotoImage(file="SistSorteio\Assets\img.png")
        # Create a Label to display the image
        self.image_label = Label(self.window, image=self.image, bg='#1e3743')
        self.image_label.place(relx=0.25, rely=0.05)

        self.result_label = Label(self.window, text="", bg='#dfe3ee', font=('Helvetica', 12), highlightbackground='#759fab', highlightthickness=3)
        self.result_label.place(relx=0.1, rely=0.6, relheight=0.1, relwidth=0.8)
    
    def btnSort(self):
        options = list(range(1, 101))
        sorteados = sample(options, 5)
        self.result_label.configure(text=f"{sorteados}")
        graph = [[0] * 5 for _ in range(5)]  # Inicializando uma matriz 5x5 para o grafo
        for i in range(5): # Preenche a matriz com os pesos (números sorteados)
            for j in range(5):
                if i != j:  # Evitando auto-loops
                    graph[i][j] = abs(sorteados[i] - sorteados[j])
        self.prim_mst(graph) # Executando o algoritmo de Prim para encontrar a Árvore Geradora Mínima
    def prim_mst(self, graph):
        vertices = len(graph)
        key = [float('inf')] * vertices
        parent = [None] * vertices
        key[0] = 0
        mst_set = [False] * vertices
        parent[0] = -1
        for _ in range(vertices - 1):
            u = self.min_key(vertices, key, mst_set)
            mst_set[u] = True
            for v in range(vertices):
                if 0 < graph[u][v] < key[v] and not mst_set[v]:
                    key[v] = graph[u][v]
                    parent[v] = u
    def min_key(self, vertices, key, mst_set):
        min_val = float('inf')
        min_index = -1
        for v in range(vertices):
            if key[v] < min_val and not mst_set[v]:
                min_val = key[v]
                min_index = v
        return min_index
       
Application()
