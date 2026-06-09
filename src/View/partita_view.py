from abc import ABC, abstractmethod

from src.Model.partita import Partita
from src.View.giocatore_view import GiocatoreViewAstratta
from src.View.tavoliere_view import TavoliereviewAstratta


class PartitaViewAstratta(ABC):
    """Classe PartitaView.

    DESCRIZIONE
        Rappresenta la classe che gestisce operazioni di input / stampa per la
        Partita


    ATTRIButi    
        giocatoreView
            TIPO
                Privato, Tipo GiocatoreViewAstratta
            DESCRIZIONE
                View della classe Giocatore astratta

        tavoliereView
            TIPO
                Privato, Tipo TavoliereViewAstratta
            DESCRIZIONE
                View della classe Tavoliere astratta

    METODI

        ------ COSTRUTTORE ------

        def __init__(
            self, new_giocatore_view: GiocatoreView, new_tavoliere_view: TavoliereView
        ):
            DESCRIZIONE
                Costruttore di base.
                Data un modello GiocatoreView e un TavoliereView restituisce
                un PartitaView


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
    
    # Accesso Attributi Privati

    @abstractmethod
    def set_tavoliere_view(self, new_tavoliere_view: TavoliereviewAstratta):
        pass

    @abstractmethod
    def get_tavoliere_view(self):
        pass

    @abstractmethod
    def set_giocatore_view(self, new_giocatore_view: GiocatoreViewAstratta):
        pass

    @abstractmethod
    def get_giocatore_view(self):
        pass
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