class Grafo:
    __COLONNE = ("a","b","c","d","e","f","g","h","i")

    __PRIMA_RIGA = 9
    __ULTIMA_RIGA = 1
    __PRIMA_COLONNA = 0
    __ULTIMA_COLONNA = 8
    __NO_ARCO = "0" 

    def __init__(self): # Inizializza il grafo
        self.tavoliere = dict.fromkeys(self.inizializzaNodi())
        self.inizializzaArchi()

    def inizializzaNodi(self) ->list[str]: # Inizializza i nodi
        chiavi = []
        i = self.__PRIMA_RIGA
        while i >=self.__ULTIMA_RIGA: # Imposta il valore della prima lettera del nome
            for j in self.__COLONNE: # Imposta il valore della seconda lettera del nome
                chiavi.append(j+str(i))
            i-=1
        return chiavi
    
    def inizializzaArchi(self): # Inizializzazione degli archi
        i = self.__PRIMA_RIGA
        while i>=self.__ULTIMA_RIGA:
            j = self.__PRIMA_COLONNA
            while j<=self.__ULTIMA_COLONNA:# Archi con ordine: Sopra, Sotto, Sinistra, Destra
                if i == self.__ULTIMA_RIGA:
                    self.tavoliere[self.__COLONNE[j]+str(i)] = [self.__COLONNE[j]+str(i+1),self.__NO_ARCO] # Aggiunta solo dell'arco adiacente sopra
                elif i == self.__PRIMA_RIGA:
                    self.tavoliere[self.__COLONNE[j]+str(i)] = [self.__NO_ARCO,self.__COLONNE[j]+str(i-1)] # Aggiunta solo dell'arco adiacente sotto
                else: 
                    self.tavoliere[self.__COLONNE[j]+str(i)] = [self.__COLONNE[j]+str(i+1),self.__COLONNE[j]+str(i-1)] # Aggiunta degli archi adiacenti sotto e sopra
                if j == self.__PRIMA_COLONNA:
                    self.tavoliere[self.__COLONNE[j]+str(i)].append(self.__NO_ARCO) # Aggiunta dell'arco adiacente sinistra
                    self.tavoliere[self.__COLONNE[j]+str(i)].append(self.__COLONNE[j+1]+str(i)) # Aggiunta dell'arco adiacente destra
                elif j == self.__ULTIMA_COLONNA:
                    self.tavoliere[self.__COLONNE[j]+str(i)].append(self.__COLONNE[j-1]+str(i))# Aggiunta dell'arco adiacente sinistra
                    self.tavoliere[self.__COLONNE[j]+str(i)].append(self.__NO_ARCO)# Aggiunta dell'arco adiacente destra
                else:
                    self.tavoliere[self.__COLONNE[j]+str(i)].append(self.__COLONNE[j-1]+str(i)) # Aggiunta dell'arco adiacente sinistra
                    self.tavoliere[self.__COLONNE[j]+str(i)].append(self.__COLONNE[j+1]+str(i))# Aggiunta dell'arco adiacente destra
                j+=1
            i-=1

    def esisteArco (self, nodo1: str, nodo2: str) ->bool: # Controlla se esiste un arco tra 2 nodi
        for i in self.tavoliere[nodo1]:
            if i == nodo2:
                return True
        return False


