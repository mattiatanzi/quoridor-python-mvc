from src.Model.costanti_tavoliere import Costanti
from src.Model.nodo import Nodo


class Grafo:
    """Struttura dati utilizzata per il tavoliere.

    Attributi
    ----------
    nome : grafo
        Grafo non orientato strutturato come se fosse una matrice
    Costanti:
    ---------
    nome: COSTANTI
        Classe che contiene tutte le costanti presenti
    Metodi
    -------
    inizializza_nodi(self) ->list[Nodo]:
        Inizializza tutti i nodi del grafo

    inizializza_archi(self):
        Imposta gli archi del grafo

    esiste_arco (self, nodo1: Nodo, nodo2: Nodo) ->bool:
        Controlla se esiste un arco tra i due nodi passati

    rimuovi_arco(self,nodo1: Nodo,nodo2: Nodo):
        Rimuove l'arco presente tra due nodi

    get_adiacente(slef, nodo: Nodo, posizione: str):
        Restituisce il nodo adiacente data una posizione

    """

    __COSTANTI = Costanti()

    def __init__(self):  # Inizializza il grafo
        self.__grafo = dict.fromkeys(self.__inizializza_nodi())
        self.__inizializza_archi()

    def __inizializza_nodi(self) -> set[Nodo]:  # Inizializza i nodi
        chiavi: set[Nodo] = set()
        i = self.__COSTANTI.PRIMA_RIGA
        while (
            i >= self.__COSTANTI.ULTIMA_RIGA
        ):  # Imposta il valore della prima lettera del nome
            for j in (
                self.__COSTANTI.COLONNE
            ):  # Imposta il valore della seconda lettera del nome
                nodo_attuale = Nodo(j + str(i))
                chiavi.add(nodo_attuale)
            i -= 1
        return chiavi

    def __inizializza_archi(self):  # Inizializzazione degli archi
        i = self.__COSTANTI.PRIMA_RIGA
        while i >= self.__COSTANTI.ULTIMA_RIGA:
            j = self.__COSTANTI.PRIMA_COLONNA
            while (
                j <= self.__COSTANTI.ULTIMA_COLONNA
            ):  # Archi con ordine: Sopra, Sotto, Sinistra, Destra
                nodo_attuale = Nodo(self.__COSTANTI.COLONNE[j] + str(i))
                self.__grafo[nodo_attuale] = [self.__COSTANTI.NO_ARCO] * 4
                if i == self.__COSTANTI.ULTIMA_RIGA:
                    nodo_adiacente_sopra = Nodo(self.__COSTANTI.COLONNE[j] + str(i + 1))
                    self.__grafo[nodo_attuale][self.__COSTANTI.ARCO_ADIACENTE_SOPRA] = (
                        nodo_adiacente_sopra  # Aggiunta solo dell'arco adiacente sopra
                    )
                elif i == self.__COSTANTI.PRIMA_RIGA:
                    nodo_adiacente_sotto = Nodo(self.__COSTANTI.COLONNE[j] + str(i - 1))
                    self.__grafo[nodo_attuale][self.__COSTANTI.ARCO_ADIACENTE_SOTTO] = (
                        nodo_adiacente_sotto  # Aggiunta solo dell'arco adiacente sotto
                    )
                else:
                    # Aggiunta degli archi adiacenti sotto e sopra
                    nodo_adiacente_sopra = Nodo(self.__COSTANTI.COLONNE[j] + str(i + 1))
                    nodo_adiacente_sotto = Nodo(self.__COSTANTI.COLONNE[j] + str(i - 1))
                    self.__grafo[nodo_attuale][self.__COSTANTI.ARCO_ADIACENTE_SOPRA] = (
                        nodo_adiacente_sopra
                    )
                    self.__grafo[nodo_attuale][self.__COSTANTI.ARCO_ADIACENTE_SOTTO] = (
                        nodo_adiacente_sotto
                    )
                if j == self.__COSTANTI.PRIMA_COLONNA:
                    nodo_adiacente_destra = Nodo(
                        self.__COSTANTI.COLONNE[j + 1] + str(i)
                    )
                    self.__grafo[nodo_attuale][
                        self.__COSTANTI.ARCO_ADIACENTE_DESTRA
                    ] = nodo_adiacente_destra  # Aggiunta dell'arco adiacente destra
                elif j == self.__COSTANTI.ULTIMA_COLONNA:
                    nodo_adiacente_sinistra = Nodo(
                        self.__COSTANTI.COLONNE[j - 1] + str(i)
                    )
                    self.__grafo[nodo_attuale][
                        self.__COSTANTI.ARCO_ADIACENTE_SINISTRA
                    ] = nodo_adiacente_sinistra  # Aggiunta dell'arco adiacente sinistra
                else:
                    nodo_adiacente_sinistra = Nodo(
                        self.__COSTANTI.COLONNE[j - 1] + str(i)
                    )
                    nodo_adiacente_destra = Nodo(
                        self.__COSTANTI.COLONNE[j + 1] + str(i)
                    )
                    self.__grafo[nodo_attuale][
                        self.__COSTANTI.ARCO_ADIACENTE_SINISTRA
                    ] = nodo_adiacente_sinistra  # Aggiunta dell'arco adiacente destra

                    self.__grafo[nodo_attuale][
                        self.__COSTANTI.ARCO_ADIACENTE_DESTRA
                    ] = nodo_adiacente_destra  # Aggiunta dell'arco adiacente destra

                j += 1
            i -= 1

    def esiste_arco(
        self, nodo1: Nodo, nodo2: Nodo
    ) -> bool:  # Controlla se esiste un arco tra 2 nodi
        if nodo2 == self.__COSTANTI.NO_ARCO:
            return False
        return any(i == nodo2 for i in self.__grafo[nodo1])

    def rimuovi_arco(self, nodo1: Nodo, nodo2: Nodo):
        for i in range(
            0, self.__COSTANTI.NUMERO_ADIACENTI
        ):  # Controlla per tutti gli adiacenti del nodo1
            if self.__grafo[nodo1][i] == nodo2:  # Se trovato elminia l'arco
                self.__grafo[nodo1][i] = self.__COSTANTI.NO_ARCO
                if (
                    i == self.__COSTANTI.ARCO_ADIACENTE_SOPRA
                ):  # Se precedentemente è stato eliminato un arco verso l'alto allora
                    # sicuramente per nodo2 ci sarà un arco verso il basso
                    self.__grafo[nodo2][i + 1] = self.__COSTANTI.NO_ARCO
                elif i == self.__COSTANTI.ARCO_ADIACENTE_SOTTO:
                    self.__grafo[nodo2][i - 1] = self.__COSTANTI.NO_ARCO
                elif i == self.__COSTANTI.ARCO_ADIACENTE_SINISTRA:
                    self.__grafo[nodo2][i + 1] = self.__COSTANTI.NO_ARCO
                else:
                    self.__grafo[nodo2][i - 1] = self.__COSTANTI.NO_ARCO
                return

    def get_adiacente(self, nodo: Nodo, posizione: str):
        return self.__grafo[nodo][posizione]
