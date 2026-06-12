from abc import ABC, abstractmethod

from src.Model.giocatore import Giocatore
from src.Model.tavoliere import Tavoliere


class TavoliereviewAstratta(ABC):
    """Rappresenta l'insieme di operazioni per mostrare a video il tavoliere.

    METODI

    def stampa_tavoliere
        DESCRIZIONE
            Stampa il tavoliere di gioco con le informazioni dei giocatori e i muri
            posizionati in partita.
    """

    @abstractmethod
    def stampa_tavoliere(self, tavoliere: Tavoliere, giocatori: set[Giocatore]):
        pass
