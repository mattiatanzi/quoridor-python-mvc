from abc import ABC, abstractmethod

from src.Model.partita import Partita
from src.View.partita_view import PartitaViewAstratta
from src.View.tavoliere_view import TavoliereviewAstratta


class ReplayViewAstratta(ABC):
    """Classe ReplayViewAstratta.

    DESCRIZIONE
        Interfaccia che gestisce la visualizzazione del replay della partita.

    METODI

        def stampa_replay(
            stato_corrente: Partita,
            descrizione_mossa: str,
            trascrizione_parziale: list[str],
            automatico: bool = False
        )
            DESCRIZIONE
                Mostra lo stato del replay della partita e la relativa trascrizione
                delle mosse.
    """

    def __init__(
        self,
        stampa_tavoliere: TavoliereviewAstratta,
        stampa_trascrizione: PartitaViewAstratta,
    ):
        self.__stampa_tavoliere = stampa_tavoliere
        self.__stampa_trascrizione = stampa_trascrizione

    @abstractmethod
    def stampa_replay(
        self,
        stato_corrente: Partita,
        descrizione_mossa: str,
        trascrizione_parziale: list[str],
        automatico: bool = False,
    ):
        pass
