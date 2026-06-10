from src.View.giocatore_view import GiocatoreViewAstratta

class GiocatoreViewTUI(GiocatoreViewAstratta):
    """classe GiocatoreView.

    DESCRIZIONE
        Rappresenta la classe che gestisce operazioni di input / stampa per il Giocatore

    METODI

        ------ VISUALIZZAZIONE ATTRIBUTI ------

        def stampa_id_giocatore(self, id_giocatore):
            DESCRIZIONE
                Mostra dell'id giocatore

        def stampa_giocatore_attivo(self, id, muri_disponibili):
            DESCRIZIONE
                Mostra informazioni riguardanti il giocatore che ha il turno

        def stampa_info_giocatore(self, id, muri_disponibili):
            DESCRIZIONE
                Mostra informazioni generali riguardanti un giocatore

        ------ VISUALIZZZIONI ERRORI ------

        def stampa_errore_giocatore(self, messaggio):
            DESCRIZIONE
                Mostra il messaggio di errore in input relativo al giocatore

    """

    # Stampe Video

    def __init__(self,app_condivisa):
        self.__app_condivisa = app_condivisa
    def stampa_id_giocatore(self, id_giocatore):
        pass

    
    def stampa_giocatore_attivo(self, id, muri_disponibili):
        pass
    
    
    def stampa_info_giocatore(self, id, muri_disponibili):
        pass

    # Stampe Errori

    def stampa_errore_giocatore(self, messaggio):
        pass
