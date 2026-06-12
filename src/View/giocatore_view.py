from abc import ABC, abstractmethod

class GiocatoreViewAstratta(ABC):
    """classe GiocatoreView.

    DESCRIZIONE
        Rappresenta la classe che gestisce operazioni di input / stampa per il Giocatore

    METODI

        ------ VISUALIZZAZIONE ATTRIBUTI ------

        def stampa_id_giocatore(self, id_giocatore):
            DESCRIZIONE
                Mostra dell'id giocatore

        def stampa_giocatore_attivo(
            self,
            id,
            muri_disponibili,
            tempo_formattato = None
        ):
            DESCRIZIONE
                Mostra informazioni riguardanti il giocatore che ha il turno

        def stampa_info_giocatore(self, id, muri_disponibili, tempo_formattato = None):
            DESCRIZIONE
                Mostra informazioni generali riguardanti un giocatore


        def stampa_giocatore_eliminato(
            self,
            id,
            muri_disponibili,
            tempo_formattato = None
        ):
            DESCRIZIONE
            Mostra informazioni generali riguardanti i giocatori.
            
        ------ VISUALIZZIONE ERRORI ------

        def stampa_errore_giocatore(self, messaggio):
            DESCRIZIONE
                Mostra il messaggio di errore in input relativo al giocatore

    """

    # Stampe Video

    @abstractmethod
    def stampa_id_giocatore(self, id_giocatore):
        pass

    @abstractmethod
    def stampa_giocatore_attivo(self, id, muri_disponibili):
        pass
    
    @abstractmethod
    def stampa_info_giocatore(self, id, muri_disponibili):
        pass

    @abstractmethod
    def stampa_giocatore_eliminato(self, id, muri_disponibili, tempo_formattato=None):
        pass
    # Stampe Errori
    @abstractmethod
    def stampa_errore_giocatore(self, messaggio):
        pass
