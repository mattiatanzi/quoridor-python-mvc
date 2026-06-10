from abc import ABC, abstractmethod

from src.Model.partita import Partita
from src.View.giocatore_view import GiocatoreViewAstratta
from src.View.tavoliere_view import TavoliereviewAstratta


class PartitaViewAstratta(ABC):
    """Classe PartitaViewAstratta.

    DESCRIZIONE
        Rappresenta la classe che gestisce operazioni di input / stampa per la
        Partita

    MEDOTI

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


        ------ STAMPE ERRORI ------

        def stampa_errore_partita(self, messaggio):
            DESCRIZIONE
                Mostra il messaggio di errore in input relativo alla partita

        ------ INPUT UTENTE ------

        def chiedi_input_utente(self, indicazioniInput: str = "") -> str:
            DESCRIZIONE
                Mostra un interfaccia con un eventuale messaggio di indicazioni in cui
                viene chiesto all'utente di inserire un input. La funzione restituisce
                l'input inserito dall'utente

        def stampa_richiesta_input(self, indicazioni: str = ""):
            DESCRIZIONE
                Mostra un interfaccia con un eventuale messaggio di indicazioni in cui
                viene chiesto all'utente di inserire un input.

        def get_input(self):
            DESCRIZIONE
                Mostra un messaggio e prende e restituisce quello che scrive l'utente
                in input.

    """
    
    def __init__(self, new_giocatore_view: GiocatoreViewAstratta, new_tavoliere_view: TavoliereviewAstratta):
        self.set_giocatore_view(new_giocatore_view)
        self.set_tavoliere_view(new_tavoliere_view)
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
    def chiedi_input_utente(self, indicazioniInput: str = "") -> str:
        pass

    @abstractmethod
    def stampa_richiesta_input(self, indicazioni: str = ""):
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