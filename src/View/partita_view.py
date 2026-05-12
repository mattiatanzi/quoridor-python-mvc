from Model.partita import Partita
from View.giocatore_view import GiocatoreView
from View.tavoliere_view import TavoliereView


class PartitaView:
    """Classe PartitaView.

    DESCRIZIONE
        Rappresenta la classe che gestisce operazioni di input / stampa per la
        Partita

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
            Stampa a video la partita corrente, ossia tavoliere di gioco e info sui 
            giocatori
            
        def stampa_aiuto(self)
            DESCRIZIONE
            Stampa a video la guida riassuntiva dei comandi disponibili.


        ------ STAMPE ERRORI ------

        def stampa_errore_partita(self, messaggio):
            DESCRIZIONE
                Stampa il messaggio di errore in input relativo alla partita

        ------ INPUT UTENTE ------
        
        def get_input(self):
            DESCRIZIONE
                Scrive un messaggio e prende e restituisce quello che scrive l'utente
                in input

    """

    # Attributi
    __giocatoreView: GiocatoreView
    __tavoliereView: TavoliereView

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
        
    def stampa_aiuto(self):
        aiuto = """
        ╔══════════════════════════════════════════════════════════════╗
        ║             QUORIDOR: GUIDA AI COMANDI PRINCIPALI            ║
        ╠══════════════════════════════════════════════════════════════╣
        ║  SEI IN DIFFICOLTÀ?                                          ║
        ║   Ecco per te un elenco dei comandi principali:              ║
        ║                                                              ║
        ║  - MOSSA PEDONE:                                             ║
        ║     Inserisci le coordinate della casella di destinazione    ║
        ║     Formato: <colonna><riga>  (es. 'e2', 'e3')               ║
        ║                                                              ║
        ║  - PIAZZAMENTO MURO:                                         ║
        ║     Inserisci coordinate e orientamento (h=orizz, v=vert).   ║
        ║     Formato: <colonna><riga><h/v>  (es. 'e2h', 'a4v')        ║
        ║                                                              ║
        ║  - AIUTO:                                                    ║
        ║     Scrivi 'help' o 'aiuto' per rileggere questo             ║
        ║      menu in ogni turno.                                     ║
        ║                                                              ║
        ║  - USCIRE DAL GIOCO:                                         ║
        ║     Scrivi 'exit' o 'esci' per uscire dal gioco.             ║
        ║                                                              ║
        ║  -  ABBANDONARE LA PARTITA:                                  ║
        ║     Scrivi 'quit' o 'abbandona' per uscire dalla partita.    ║
        ║                                                              ║
        ╚══════════════════════════════════════════════════════════════╝
        """
        print(aiuto)
        

    # Stampe Errori

    def stampa_errore_partita(self, messaggio):
        print(messaggio)
    
    def get_input(self) -> str:
        return input("Fai la tua mossa: ")
