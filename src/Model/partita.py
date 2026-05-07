from Model.tavoliere import Tavoliere
from Model.giocatore import Giocatore

class Partita:
    """Classe Partita.

    Descrizione:
        Contiene informazioni relative alla partita in corso

    Attributi:

        - giocatori
            TIPO
                Privato, Tipo Set di Giocatori
            DESCRIZIONE
                L'insieme dei giocatori che partecipa alla partita corrente

        - tavoliere
            TIPO
                Privato, Tipo Tavoliere
            DESCRIZIONE
                Il tavoliere utilizzato nella partita in corso

    Metodi:

        ------ Costruttori ------

        def __init__(self, newTavoliere: Tavoliere, newGiocatori: set[Giocatore]):
            DESCRIZIONE
                Costruttore di Base.
                Dato un Tavoliere e un insieme di Giocatori restituisce una partita

        ------ Metodi Accesso Attributi Privati ------

        def setTavoliere(self, newTavoliere: Tavoliere):
            DESCRIZIONE
                Modfica il Tavolere della partita

        def getTavoliere(self) -> Tavoliere:
            DESCRIZIONE
                Restituisce il Tavoliere utilizzato in partita

        def setGiocatori(self, newGiocatori: set[Giocatore]):
            DESCRIZIONE
                Modifica l'insieme di giocatori della partita

        def getGiocatori(self):
            DESCRIZIONE
                Restituisce l'insieme di giocatori della partita

    """

    # Costanti
    __TOTALE_GIOCATORI = 2

    # Variabili
    __giocatori: set[Giocatore]
    __tavoliere: Tavoliere

    # Metodi

    # Costruttore

    def __init__(self, newTavoliere: Tavoliere, newGiocatori: set[Giocatore]):
        self.setTavoliere(newTavoliere)
        self.setGiocatori(newGiocatori)

    # Modificatori / Osservatori

    def setTavoliere(self, newTavoliere: Tavoliere):
        self.__tavoliere = newTavoliere

    def getTavoliere(self) -> Tavoliere:
        return self.__tavoliere

    def setGiocatori(self, newGiocatori: set[Giocatore]):
        self.__giocatori = newGiocatori

    def getGiocatori(self):
        return self.__giocatori
