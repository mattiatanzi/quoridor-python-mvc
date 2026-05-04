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

    def inizializzaNodi(self): # Inizializza i nodi
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
                    self.scacchiera[self.__COLONNE[j]+str(i)] = [self.__COLONNE[j]+str(i+1),self.__NO_ARCO]
                elif i == self.__PRIMA_RIGA:
                    self.scacchiera[self.__COLONNE[j]+str(i)] = [self.__NO_ARCO,self.__COLONNE[j]+str(i-1)]
                else: 
                    self.scacchiera[self.__COLONNE[j]+str(i)] = [self.__COLONNE[j]+str(i+1),self.__COLONNE[j]+str(i-1)]
                if j == self.__PRIMA_COLONNA:
                    self.scacchiera[self.__COLONNE[j]+str(i)].append(self.__NO_ARCO)
                    self.scacchiera[self.__COLONNE[j]+str(i)].append(self.__COLONNE[j+1]+str(i))
                elif j == self.__ULTIMA_COLONNA:
                    self.scacchiera[self.__COLONNE[j]+str(i)].append(self.__COLONNE[j-1]+str(i))
                    self.scacchiera[self.__COLONNE[j]+str(i)].append(self.__NO_ARCO)
                else:
                    self.scacchiera[self.__COLONNE[j]+str(i)].append(self.__COLONNE[j-1]+str(i))
                    self.scacchiera[self.__COLONNE[j]+str(i)].append(self.__COLONNE[j+1]+str(i))
                j+=1
            i-=1