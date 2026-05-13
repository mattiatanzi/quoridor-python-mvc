from src.Model.grafo import Grafo
from src.Model.nodo import Nodo


class ErroreTavoliere(Exception):
    """"""

    pass


class Tavoliere:
    """Contiene il tavoliere di gioco.

    Attributi
    ---------
    nome: tavoliere
        Il tavoliere di gioco realizzato con un grafo

    Metodi:
    -------

    nome get_adiacente
        Restituisce l'adiacente presente ad un nodo specifico+

    nome piazza_muro
        Piazza l'effettivo muro tra 2 nodi

    nome piazza_muro_orizzontale
        Effettua dei controlli per poter piazzare il muro orizzontale e se va a buon
          fine richiama piazza_muro

    nome piazza_muro_verticale
        Effettua dei controlli per poter piazzare il muro verticale e se va a buon
        fine richiama piazza_muro
          
    nome esiste_arco
        Controlla se esiste un passaggio tra due caselle.
    """

    def __init__(self):
        self.__tavoliere = Grafo()
        self.__muri_piazzati = []

    def get_adiacente(self, nodo, posizione):
        return self.__tavoliere.get_adiacente(nodo, posizione)

    def __piazza_muro(self, primo_nodo: Nodo, secondo_nodo: Nodo):
        self.__tavoliere.rimuovi_arco(primo_nodo, secondo_nodo)

    def piazza_muro_orizzontale(self, azione: str):
        colonna_input = azione[0]
        riga_input = int(azione[1])

        # Se colonna è 'i' (ultima), la spostiamo a 'h' (coprirà h-i)
        col_sx = "h" if colonna_input == "i" else colonna_input
        # Se riga è '1' (ultima), la spostiamo a '2' (coprirà 2-1)
        riga_alt = 2 if riga_input == 1 else riga_input

        # Calcolo della colonna a destra e riga sotto
        col_dx = chr(ord(col_sx) + 1)
        riga_bas = riga_alt - 1

        # Definiamo l'azione "effettiva" piazzata (utile per i controlli futuri)
        azione_effettiva = f"{col_sx}{riga_alt}h"

        n_sx_alto = Nodo(f"{col_sx}{riga_alt}")
        n_sx_bass = Nodo(f"{col_sx}{riga_bas}")
        n_dx_alto = Nodo(f"{col_dx}{riga_alt}")
        n_dx_bass = Nodo(f"{col_dx}{riga_bas}")

        if not self.__tavoliere.esiste_arco(
            n_sx_alto, n_sx_bass
        ) or not self.__tavoliere.esiste_arco(n_dx_alto, n_dx_bass):
            raise ErroreTavoliere("Errore: Qui è già presente un muro orizzontale.")

        # Se piazzo 'e8h', il muro che mi impedisce l'incrocio è 'e8v'
        muro_verticale_critico = f"{col_sx}{riga_alt}v"
        if muro_verticale_critico in self.__muri_piazzati:
            raise ErroreTavoliere(
                "Errore: Non puoi incrociare a croce un muro verticale!"
            )

        self.__piazza_muro(n_sx_alto, n_sx_bass)
        self.__piazza_muro(n_dx_alto, n_dx_bass)
        self.__muri_piazzati.append(azione_effettiva)


    def piazza_muro_verticale(self, azione: str):
        colonna_input = azione[0]
        riga_input = int(azione[1])

        # Se riga è 1, la spostiamo a 2 (coprirà 2-1)
        riga_alt = 2 if riga_input == 1 else riga_input
        riga_bas = riga_alt - 1

        # Calcolo colonne coinvolte (sx e dx rispetto al muro)
        col_sx = "h" if colonna_input == "i" else colonna_input
        col_dx = chr(ord(col_sx) + 1)

        n_sx_alto = Nodo(f"{col_sx}{riga_alt}")
        n_dx_alto = Nodo(f"{col_dx}{riga_alt}")
        n_sx_bass = Nodo(f"{col_sx}{riga_bas}")
        n_dx_bass = Nodo(f"{col_dx}{riga_bas}")

        # Controllo muri verticali già presenti per evitare sovrapposizione
        if not self.__tavoliere.esiste_arco(
        n_sx_alto, n_dx_alto
        ) or not self.__tavoliere.esiste_arco(n_sx_bass, n_dx_bass):
            raise ErroreTavoliere("Errore: Qui è già presente un muro verticale.")

        # Controllo presenza di muri orizzontali che portino a un incrocio a croce
        muro_orizzontale_critico = f"{col_sx}{riga_alt}h"
        if muro_orizzontale_critico in self.__muri_piazzati:
            raise ErroreTavoliere("Errore: Non puoi incrociare a croce un muro orizzontale!")

        self.__piazza_muro(n_sx_alto, n_dx_alto)
        self.__piazza_muro(n_sx_bass, n_dx_bass)
        azione_effettiva = f"{col_sx}{riga_alt}v"
        self.__muri_piazzati.append(azione_effettiva)
        
    def mossa_permessa(self, nodo1: Nodo, nodo2: Nodo) -> bool:
        return self.__tavoliere.esiste_arco(nodo1, nodo2)
