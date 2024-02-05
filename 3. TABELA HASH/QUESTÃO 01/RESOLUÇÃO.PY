class tabHash:
    def __init__(self):
        self.tamanho = 10 #tamanho referente ao numero de dias
        self.table = ['vago'] 
        self.calculation = self.table * self.tamanho 
        
    def carater(self, letras): #separa os carateres
        times = []
        for letra in letras:
            if times and letra not in times[-1]:
                times[-1].append(letra)
            else:
                times.append([letra])     
        return times
    
    def registro(self, times): #regitro dos nomes que ficam em posição da lista
        for time in times:
            timesOrd = (sum(ord(letra) for letra in time)) % 10
            while self.calculation[timesOrd] != 'vago':
                timesOrd = timesOrd + 1 
                timesOrd = timesOrd % 10
            self.calculation[timesOrd] = time
        return self.calculation
    
def main(): 
    chamaTable = tabHash()
    operationCaracter = input()
    times = chamaTable.carater(operationCaracter)
    resultado = chamaTable.registro(times)
    print(resultado)

#inicializando
if __name__ == "__main__":
    main()