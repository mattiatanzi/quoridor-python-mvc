class GiocatoreView:
    """classe GiocatoreView.

    DESCRIZIONE
        Rappresenta la classe che gestisce operazioni di input / stampa per il Giocatore

    METODI

        ------ STAMPE ATTRIBUTI ------

        def stampa_id_giocatore(self, id_giocatore):
            DESCRIZIONE
                Stampa dell'id giocatore

        def stampa_giocatore_attivo(self, id, muri_disponibili):
            DESCRIZIONE
                Stampa informazioni riguardanti il giocatore che ha il turno

        def stampa_info_giocatore(self, id, muri_disponibili):
            DESCRIZIONE
                Stampa informazioni generali riguardanti un giocatore

        ------ STAMPE ERRORI ------

        def stampa_errore_giocatore(self, messaggio):
            DESCRIZIONE
                Stampa il messaggio di errore in input relativo al giocatore

    """

    # Stampe Video

    def stampa_id_giocatore(self, id_giocatore):
        print(id_giocatore)

    def stampa_giocatore_attivo(self, id, muri_disponibili, tempo_formattato = None):
        print(f"Turno {id}, Muri Disponibili: {muri_disponibili}")

    def stampa_info_giocatore(self, id, muri_disponibili, tempo_formattato = None):
        print(f"Giocatore {id}, Muri Disponibili: {muri_disponibili}")

    
    # Stampe Errori

    def stampa_errore_giocatore(self, messaggio):
        print(messaggio)
