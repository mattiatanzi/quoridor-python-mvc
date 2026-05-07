from Model.tavoliere import Tavoliere
from Model.giocatore import Giocatore

class Partita:

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
