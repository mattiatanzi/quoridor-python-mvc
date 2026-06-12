from abc import ABC, abstractmethod

from src.Model.parametri_partita import ErroreParametriPartita


class ParametriPartitaView(ABC):
    """Classe ParametriPartitaView.

    DESCRIZIONE
        Classe che gestisce stampa e input per ParametriPartita

    METODI

        def stampa_errore_parametri(self, errore: ErroreParametriPartita):
            DESCRIZIONE
                Stampa un errore riguardante i parametri della partita

        def get_input_modalita_partita(self, err: str = "") -> str:
            DESCRIZIONE


        def get_input_limite_tempo(self, err: str = "") -> str:
            DESCRIZIONE



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
