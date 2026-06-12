from abc import ABC, abstractmethod

from src.Model.parametri_partita import ErroreParametriPartita


class ParametriPartitaView(ABC):
    """Classe ParametriPartitaView.

    DESCRIZIONE
        Classe che gestisce stampa e input per ParametriPartita

    METODI

        def stampa_errore_parametri(self, errore: ErroreParametriPartita)
            DESCRIZIONE
                Stampa un errore riguardante i parametri della partita

        def get_input_modalita_partita(self, err: str = "") -> str
            DESCRIZIONE
                Richiede all'utente la modalità di gioco (con o senza timer)

        def get_input_limite_tempo(self, err: str = "") -> str
            DESCRIZIONE
                Richiede all'utente il limite di tempo da impostare per la partita

        def get_input_numero_giocatori(self, err: str = "") -> str
            DESCRIZIONE
                Richiede all'utente il numero di giocatori per la partita

        def stampa_aiuto_modalita_partita(self)
            DESCRIZIONE
                Mostra una guida per la scelta della modalità di gioco

        def stampa_aiuto_limite_tempo(self)
            DESCRIZIONE
                Mostra una guida per la scelta del limite di tempo

        def stampa_aiuto_numero_giocatori(self)
            DESCRIZIONE
                Mostra una guida per la scelta del numero di giocatori

    """

    @abstractmethod
    def stampa_errore_parametri(self, errore: ErroreParametriPartita):
        pass

    @abstractmethod
    def get_input_modalita_partita(self, err: str = "") -> str:
        pass

    @abstractmethod
    def get_input_limite_tempo(self, err: str = "") -> str:
        pass

    @abstractmethod
    def get_input_numero_giocatori(self, err: str = "") -> str:
        pass

    @abstractmethod
    def stampa_aiuto_modalita_partita(self):
        pass

    @abstractmethod
    def stampa_aiuto_limite_tempo(self):
        pass

    @abstractmethod
    def stampa_aiuto_numero_giocatori(self):
        pass
