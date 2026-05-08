class GiocatoreView:
    """classe GiocatoreView.

    DESCRIZIONE
        Rappresenta la classe che gestisce operazioni di input / stampa per il Giocatore

    METODI

        ------ STAMPE ATTRIBUTI ------

        def stampa_id_giocatore(self, id_giocatore):
            DESCRIZIONE
                Stampa dell'id giocatore


        ------ STAMPE ERRORI ------

        def stampa_errore_giocatore(self, messaggio):
            DESCRIZIONE
                Stampa il messaggio di errore in input relativo al giocatore

    """

    def stampa_id_giocatore(self, id_giocatore):
        print(id_giocatore)

    def stampa_muri_rimanenti_giocatore(self, id, muri_disponibili):
        print(f"Giocatore: {id}, Muri Rimanenti: {muri_disponibili}")

    def stampa_errore_giocatore(self, messaggio):
        print(messaggio)
