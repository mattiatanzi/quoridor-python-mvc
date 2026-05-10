from Model.partita import Partita
from View.giocatore_view import GiocatoreView
from View.tavoliere_view import TavoliereView


class PartitaView:
    """Classe PartitaView.

    DESCRIZIONE
        Rappresenta la classe che gestisce operazioni di input / stampa per la
        Partita

    ATTRIBUTI

        ------ COSTANTI ------

        - LUNGHEZZA_DIVISORI
            TIPO
                Privato, Tipo int
            DESCRIZIONE
                La lunghezza dei divisori utilizzati in qualche interfaccia.
                Esempio
                    LUNGHEZZA_DIVISORI = 20
                    <=>
                    La stampa del divisore sarà 20 caratteri "=":

                    ====================

        ------ VARIABILI ------

        giocatoreView
            TIPO
                Privato, Tipo GiocatoreView
            DESCRIZIONE
                View della classe Giocatore, necessaria per eventuali
                stampe riguardanti il giocatore

        tavoliereView
            TIPO
                Privato, Tipo TavoliereView
            DESCRIZIONE
                View della classe Tavoliere, necessaria per eventuali
                stampe riguardanti il tavoliere

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

        def set_tavoliere_view(self, new_tavoliere_view: TavoliereView):
            DESCRIZIONE
                Modifica il TavoliereView contenuto in PartitaView

        def get_tavoliere_view(self):
            DESCRIZIONE
                Restituisce il TavoliereView contenuto in PartitaView

        def set_giocatore_view(self, new_giocatore_view: GiocatoreView):
            DESCRIZIONE
                Modifica il GiocatoreView contenuto in PartitaView

        def get_giocatore_view(self):
            DESCRIZIONE
                Restituisce il GiocatoreView contenuto in PartitaView


        ------ STAMPE VIDEO ------

        def stampa_partita(self, partita: Partita):
            DESCRIZIONE
                Stampa a video la partita corrente

        def stampa_vittoria(self, idVincitore):
            DESCRIZIONE
                Stampa a video l'interfaccia di vittoria


        ------ STAMPE ERRORI ------

        def stampa_errore_partita(self, messaggio):
            DESCRIZIONE
                Stampa il messaggio di errore in input relativo alla partita

    """

    # Attributi
    __giocatoreView: GiocatoreView
    __tavoliereView: TavoliereView

    # Costanti
    __LUNGHEZZA_DIVISORI = 40

    # Metodi

    # Costruttore

    def __init__(
        self, new_giocatore_view: GiocatoreView, new_tavoliere_view: TavoliereView
    ):
        self.set_giocatore_view(new_giocatore_view)
        self.set_tavoliere_view(new_tavoliere_view)

    # Accesso Attributi Privati

    def set_tavoliere_view(self, new_tavoliere_view: TavoliereView):
        self.__tavoliereView = new_tavoliere_view

    def get_tavoliere_view(self):
        return self.__tavoliereView

    def set_giocatore_view(self, new_giocatore_view: GiocatoreView):
        self.__giocatoreView = new_giocatore_view

    def get_giocatore_view(self):
        return self.__giocatoreView

    # Stampe Video

    def stampa_partita(self, partita: Partita):
        print("\n\n")
        giocatori = partita.get_giocatori()
        tavoliere = partita.get_tavoliere()
        for g in giocatori:
            id_selezionato = g.get_id()
            muri_rimanenti = partita.get_muri_disponibili_giocatore(id_selezionato)

            if id_selezionato == partita.get_id_giocatore_attivo():
                self.get_giocatore_view().stampa_giocatore_attivo(
                    id_selezionato, muri_rimanenti
                )
            else:
                self.get_giocatore_view().stampa_info_giocatore(
                    id_selezionato, muri_rimanenti
                )

        self.get_tavoliere_view().stampa_tavoliere(tavoliere, giocatori)


    def stampa_vittoria(self, idVincitore):

        # Stampa ==============================
        for i in range(0, self.__LUNGHEZZA_DIVISORI)
            print("=", end = "")

        # Stampa Scritta Vittoria Centrata

        # Messaggio da stampare
        messaggioVittoria = f"{idVincitore} HA VINTO"

        # Calcolo di caratteri vuoti per centrare la scritta
        numeroCaratteriVuoti = (int)((self.__LUNGHEZZA_DIVISORI - len(messaggioVittoria)) / 2)


        for i in range(0, numeroCaratteriVuoti):
            print(" ", end = "")

        print(messaggioVittoria, end = "")

        for i in range(0, numeroCaratteriVuoti):
            print(" ", end = "")

        # Stampa ==============================
        for i in range(0, self.__LUNGHEZZA_DIVISORI)
            print("=", end = "")

        # Stampa descrizione della vittoria
        print("\n\n")
        print(f"\tIl giocatore {idVincitore} ha raggiunto destinazione.")
        print("\n\n")

        # Stampa -------------------------------
        for i in range(0, self.__LUNGHEZZA_DIVISORI):
            print("-", end = "")

        # Stampa Opzioni per uscire
        print("")
        print("[M] Menu")
        print("")

        # Stampa ==============================
        for i in range(0, self.__LUNGHEZZA_DIVISORI):
            print("=", end = "")

    # Stampe Errori

    def stampa_errore_partita(self, messaggio):
        print(messaggio)
