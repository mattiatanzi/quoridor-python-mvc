from abc import ABC, abstractmethod

from src.Model.partita import Partita
from src.View.giocatore_view import GiocatoreViewAstratta
from src.View.tavoliere_view import TavoliereviewAstratta


class PartitaViewAstratta(ABC):
    """Classe PartitaViewAstratta.

    DESCRIZIONE
        Rappresenta la classe che gestisce operazioni di input / stampa per la
        Partita

    METODI

        ------ ACCESSO ATTRIBUTI PRIVATI ------

        def set_tavoliere_view(self, new_tavoliere_view: TavoliereViewAstratta):
            DESCRIZIONE
                Modifica il tavoliereView contenuto in PartitaView

        def get_tavoliere_view(self) -> TavoliereViewAstratta:
            DESCRIZIONE
                Restituisce il tavoliereView contenuto in PartitaView

        def set_giocatore_view(self, new_giocatore_view: GiocatoreViewAstratta):
            DESCRIZIONE
                Modifica il GiocatoreView contenuto in PartitaView

        def get_giocatore_view(self):
            DESCRIZIONE
                Restituisce il GiocatoreView contenuto in PartitaView


        ------ STAMPE VIDEO ------

        def stampa_partita(self, partita: Partita):
            DESCRIZIONE
                Mostra la partita corrente, ossia tavoliere di gioco e info sui
            giocatori

        def stampa_aiuto(self)
            DESCRIZIONE
                Mostra la guida riassuntiva dei comandi disponibili.

        def stampa_vittoria(self, idVincitore):
            DESCRIZIONE
                Mostra l'interfaccia di vittoria

        def stampa_trascrizione(self,trascrizione : list[str], num_giocatori: int):
            DESCRIZIONE
                Stampa a video la trascrizione della partita in corso

        ------ STAMPE ERRORI ------

        def stampa_errore_partita(self, messaggio):
            DESCRIZIONE
                Mostra il messaggio di errore in input relativo alla partita

        ------ INPUT UTENTE ------

        def get_input(self):
            DESCRIZIONE
                Mostra un messaggio e prende e restituisce quello che scrive l'utente
                in input.

    """
    
    def __init__(
        self,
        new_giocatore_view: GiocatoreViewAstratta = None,
        new_tavoliere_view: TavoliereviewAstratta = None,
        ):
        self.set_giocatore_view(
            new_giocatore_view if new_giocatore_view is not None else GiocatoreViewAstratta()
        )
        self.set_tavoliere_view(
            new_tavoliere_view if new_tavoliere_view is not None else TavoliereviewAstratta()
        )
    # Accesso Attributi Privati

    def set_tavoliere_view(self, new_tavoliere_view: TavoliereviewAstratta):
        self.__tavoliereView = new_tavoliere_view

    def get_tavoliere_view(self):
        return self.__tavoliereView

    def set_giocatore_view(self, new_giocatore_view: GiocatoreViewAstratta):
        self.__giocatoreView = new_giocatore_view

    def get_giocatore_view(self):
        return self.__giocatoreView

    # Stampe Video

    @abstractmethod
    def stampa_partita(self, partita: Partita):
        pass

    @abstractmethod
    def stampa_aiuto(self):
        pass

    @abstractmethod
    def stampa_vittoria(self, idVincitore):
        pass
    
    # Stampe Errori
    @abstractmethod
    def stampa_errore_partita(self, messaggio):
        pass

    @abstractmethod
    def get_input(self) -> str:
        pass

    @abstractmethod
    def avvia_interfaccia_partita(self, ids_giocatori: list[str]) -> None:
        """Prepara la vista per mostrare la partita (cambia schermo in TUI, niente in CLI)."""
        pass

    @abstractmethod
    def torna_al_menu(self):
        pass

    @abstractmethod
    def crea_replay_view(self):
        """Genera e restituisce la View dedicata al Replay (CLI o TUI)."""
        pass