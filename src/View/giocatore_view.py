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

        def stampa_errore_giocatore(self):
            DESCRIZIONE
                Stampa un errore generico relativo a operazioni errate sulla classe Giocatore

        def stampa_errore_id(self, messaggio):
            DESCRIZIONE
                Stampa un errore su operazioni errate svolte sull'id di un Giocatore

    """

    def stampa_id_giocatore(self, id_giocatore):
        print(id_giocatore)

    def stampa_muri_rimanenti_giocatore(self, muri_disponibili):
        print(f"Muri Rimanenti: {muri_disponibili}")

    def stampa_errore_giocatore(self):
        print("Errore Giocatore: ")

    def stampa_errore_id(self, messaggio):
        self.stampa_errore_giocatore()
        print(f"Errore id: {messaggio}")

    def stampa_errore_muri(self, messaggio):
        self.stampa_errore_giocatore()
        print(f"Errore Muri: {messaggio}")
