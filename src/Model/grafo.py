class Grafo:
    """Struttura dati utilizzata per il tavoliere

    Attributi
    ----------
    name : grafo
        Grafo non orientato strutturato come se fosse una matrice
        Costanti
        ----------
        name : COLONNE
            Lista con elementi costanti contenente elementi da "a" ad "i" in ordine
        name: PRIMA_RIGA
            Indica la prima riga del grafo
        name: ULTIMA_RIGA
            Indica l'ultima riga del grafo
        name: PRIMA_COLONNA
            Indica la prima colonna del grafo
        name: ULTIMA_COLONNA
            Indica l'ultima colonan del grafo
        name: NO_ARCO
            Indica l'elemento che rappresenta che non c'è un arco tra due nodi
        name: ARCO_ADIACENTE_SOPRA
            Indica la posizione nella lista degli adiacenti dell'arco che ha il nodo verso sopra
        name: ARCO_ADIACENTE_SOTTO
            Indica la posizione nella lista degli adiacenti dell'arco che ha il nodo verso sotto
        name: ARCO_ADIACENTE_SINISTRA
            Indica la posizione nella lista degli adiacenti dell'arco che ha il nodo verso sinistra
        name: ARCO_ADIACENTE_DESTRA
            Indica la posizione nella lista degli adiacenti dell'arco che ha il nodo verso destra
        name: NUMERO_ADIACENTI
            Indica il numero degli adiacenti presenti
    Metodi
    -------
    inizializzaNodi(self) ->list[str]:
        Inizializza tutti i nodi del grafo

    inizializzaArchi(self):
        Imposta gli archi del grafo

    esisteArco (self, nodo1: str, nodo2: str) ->bool:
        Controlla se esiste un arco tra i due nodi passati

    rimuoviArco(self,nodo1: str,nodo2: str):
        Rimuove l'arco presente tra due nodi

    """

    __COLONNE = ("a", "b", "c", "d", "e", "f", "g", "h", "i")

    __PRIMA_RIGA = 9
    __ULTIMA_RIGA = 1
    __PRIMA_COLONNA = 0
    __ULTIMA_COLONNA = 8
    __NO_ARCO = "0"

    __ARCO_ADIACENTE_SOPRA = 0
    __ARCO_ADIACENTE_SOTTO = 1
    __ARCO_ADIACENTE_SINISTRA = 2
    __ARCO_ADIACENTE_DESTRA = 3

    __NUMERO_ADIACENTI = 4

    def __init__(self):  # Inizializza il grafo
        self.__grafo = dict.fromkeys(self.__inizializzaNodi())
        self.__inizializzaArchi()

    def __inizializza_nodi(self) -> list[str]:  # Inizializza i nodi
        chiavi = []
        i = self.__PRIMA_RIGA
        while i >= self.__ULTIMA_RIGA:  # Imposta il valore della prima lettera del nome
            for j in self.__COLONNE:  # Imposta il valore della seconda lettera del nome
                chiavi.append(j + str(i))
            i -= 1
        return chiavi

    def __inizializza_archi(self):  # Inizializzazione degli archi
        i = self.__PRIMA_RIGA
        while i >= self.__ULTIMA_RIGA:
            j = self.__PRIMA_COLONNA
            while (
                j <= self.__ULTIMA_COLONNA
            ):  # Archi con ordine: Sopra, Sotto, Sinistra, Destra
                if i == self.__ULTIMA_RIGA:
                    self.__grafo[self.__COLONNE[j] + str(i)] = [
                        self.__COLONNE[j] + str(i + 1),
                        self.__NO_ARCO,
                    ]  # Aggiunta solo dell'arco adiacente sopra
                elif i == self.__PRIMA_RIGA:
                    self.__grafo[self.__COLONNE[j] + str(i)] = [
                        self.__NO_ARCO,
                        self.__COLONNE[j] + str(i - 1),
                    ]  # Aggiunta solo dell'arco adiacente sotto
                else:
                    self.__grafo[self.__COLONNE[j] + str(i)] = [
                        self.__COLONNE[j] + str(i + 1),
                        self.__COLONNE[j] + str(i - 1),
                    ]  # Aggiunta degli archi adiacenti sotto e sopra
                if j == self.__PRIMA_COLONNA:
                    self.__grafo[self.__COLONNE[j] + str(i)].append(
                        self.__NO_ARCO
                    )  # Aggiunta dell'arco adiacente sinistra
                    self.__grafo[self.__COLONNE[j] + str(i)].append(
                        self.__COLONNE[j + 1] + str(i)
                    )  # Aggiunta dell'arco adiacente destra
                elif j == self.__ULTIMA_COLONNA:
                    self.__grafo[self.__COLONNE[j] + str(i)].append(
                        self.__COLONNE[j - 1] + str(i)
                    )  # Aggiunta dell'arco adiacente sinistra
                    self.__grafo[self.__COLONNE[j] + str(i)].append(
                        self.__NO_ARCO
                    )  # Aggiunta dell'arco adiacente destra
                else:
                    self.__grafo[self.__COLONNE[j] + str(i)].append(
                        self.__COLONNE[j - 1] + str(i)
                    )  # Aggiunta dell'arco adiacente sinistra
                    self.__grafo[self.__COLONNE[j] + str(i)].append(
                        self.__COLONNE[j + 1] + str(i)
                    )  # Aggiunta dell'arco adiacente destra
                j += 1
            i -= 1

    def esiste_arco(
        self, nodo1: str, nodo2: str
    ) -> bool:  # Controlla se esiste un arco tra 2 nodi
        return any(i == nodo2 for i in self.__grafo[nodo1])

    def rimuovi_arco(self, nodo1: str, nodo2: str):
        for i in range(
            0, self.__NUMERO_ADIACENTI
        ):  # Controlla per tutti gli adiacenti del nodo1
            if self.__grafo[nodo1][i] == nodo2:  # Se trovato elminia l'arco
                self.__grafo[nodo1][i] = self.__NO_ARCO
                if (
                    i == self.__ARCO_ADIACENTE_SOPRA
                ):  # Se precedentemente è stato eliminato un arco verso l'alto allora sicuramente per nodo2 ci sarà un arco verso il basso
                    self.__grafo[nodo2][i + 1] = self.__NO_ARCO
                elif i == self.__ARCO_ADIACENTE_SOTTO:
                    self.__grafo[nodo2][i - 1] = self.__NO_ARCO
                elif i == self.__ARCO_ADIACENTE_SINISTRA:
                    self.__grafo[nodo2][i + 1] = self.__NO_ARCO
                else:
                    self.__grafo[nodo2][i - 1] = self.__NO_ARCO
                return
