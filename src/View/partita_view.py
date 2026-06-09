import sys

from src.Model.partita import Partita
from src.View.giocatore_view import GiocatoreView
from src.View.pulisci_schermo_view import pulisci_schermo
from src.View.tavoliere_view import TavoliereView


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
            Stampa a video la partita corrente, ossia tavoliere di gioco e info sui
            giocatori

        def stampa_aiuto(self)
            DESCRIZIONE
            Stampa a video la guida riassuntiva dei comandi disponibili.

        def stampa_vittoria(self, idVincitore):
            DESCRIZIONE
                Stampa a video l'interfaccia di vittoria

        def stampa_trascrizione(self,trascrizione : list[str], num_giocatori: int):
            DESCRIZIONE
                Stampa a video la trascrizione della partita in corso

        ------ STAMPE ERRORI ------

        def stampa_errore_partita(self, messaggio):
            DESCRIZIONE
                Stampa il messaggio di errore in input relativo alla partita

        ------ INPUT UTENTE ------

        def chiedi_input_utente(self, indicazioniInput: str = "") -> str:
            DESCRIZIONE
                Stampa un interfaccia con un eventuale messaggio di indicazioni in cui
                viene chiesto all'utente di inserire un input. La funzione restituisce
                l'input inserito dall'utente

        def stampa_richiesta_input(self, indicazioni: str = ""):
            DESCRIZIONE
                Stampa un interfaccia con un eventuale messaggio di indicazioni in cui
                viene chiesto all'utente di inserire un input.

        def get_input(self):
            DESCRIZIONE
                Scrive un messaggio e prende e restituisce quello che scrive l'utente
                in input.

    """

    # Attributi
    __giocatoreView: GiocatoreView
    __tavoliereView: TavoliereView

    # Costanti
    __LUNGHEZZA_DIVISORI = 70

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
        pulisci_schermo()
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

        print("")
        self.get_tavoliere_view().stampa_tavoliere(tavoliere, giocatori)

        print("\nSuggerimento -- Digitare 'help' per visualizzare i comandi\n")

    def chiedi_input_utente(self, indicazioniInput: str = "") -> str:
        # Stampa interfaccia Input
        self.stampa_richiesta_input(indicazioniInput)

        # Richiedi input
        return input()

    def stampa_richiesta_input(self, indicazioni: str = ""):
        print(indicazioni, end="\n\n")
        print("Input: ", end="")

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
        ║   [!] REGOLA DI PIAZZAMENTO:                                 ║
        ║        La coordinata indica la casella di ancoraggio.        ║
        ║        • Muro 'h': Si inserisce nel bordo in BASSO della     ║
        ║          casella e si estende per 2 spazi verso DESTRA.      ║
        ║        • Muro 'v': Si inserisce nel bordo a DESTRA della     ║
        ║          casella e si estende per 2 spazi verso il BASSO.    ║
        ║                                                              ║
        ║   -   TRASCRIZIONE E REPLAY:                                 ║
        ║     • 'trascrizione' o 'mosse': Mostra l'elenco delle mosse  ║
        ║     • 'replay': Avvia il replay a fine partita               ║
        ║                                                              ║
        ║             [COMANDI DI NAVIGAZIONE REPLAY]                  ║
        ║     • Avanti:   'avanti', 'next', 'n' o premi [INVIO]        ║
        ║     • Indietro: 'indietro', 'prev', 'p', 'back'              ║
        ║     • Inizio:   'inizio', 'start', 'first'                   ║
        ║     • Fine:     'fine', 'end', 'last'                        ║
        ║     • Esci:     'esci', 'exit', 'quit', 'stop'               ║
        ║                                                              ║
        ║                                                              ║
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
        ║  - TRASCRIZIONE DELLE MOSSE:                                 ║
        ║    Scrivi 'trascrizione' o 'trascrizione mosse' o            ║
        ║    'mosse' per visualizzare la trascrizione delle mosse      ║
        ╚══════════════════════════════════════════════════════════════╝
        """

        # Questa notazione fa una stampa di color blu
        print(f"\033[94m{aiuto}\033[0m")

    def stampa_vittoria(self, idVincitore):
        # Stampa ==============================
        for _ in range(0, self.__LUNGHEZZA_DIVISORI):
            print("=", end="")

        # Stampa Scritta Vittoria Centrata

        # Messaggio da stampare
        messaggioVittoria = f"{idVincitore} HA VINTO"

        # Calcolo di caratteri vuoti per centrare la scritta
        numeroCaratteriVuoti = (int)(
            (self.__LUNGHEZZA_DIVISORI - len(messaggioVittoria)) / 2
        )

        # Stampa effettiva
        print("\n")
        for _ in range(0, numeroCaratteriVuoti):
            print(" ", end="")

        print(messaggioVittoria, end="")
        print("\n")

        # Stampa ==============================
        for _ in range(0, self.__LUNGHEZZA_DIVISORI):
            print("=", end="")

        # Stampa descrizione della vittoria
        print("\n\n")
        print(f"\tIl giocatore {idVincitore} ha raggiunto destinazione.", end="")
        print("\n\n")

        # Stampa -------------------------------
        for _ in range(0, self.__LUNGHEZZA_DIVISORI):
            print("-", end="")

        # Stampa Opzioni per uscire
        print("\n")
        print("[M] Menu")
        print(
            "[Trascrizione],[Trascrizione mosse],[Mosse] Trascrizione delle mosse",
        )
        print("[replay], [r] Replay manuale")
        print("[replay automatico],[ra] Replay automatico", end="")
        print("\n")

        # Stampa ==============================
        for _ in range(0, self.__LUNGHEZZA_DIVISORI):
            print("=", end="")
        print("\n")

    # Stampe Errori

    def stampa_errore_partita(self, messaggio):
        print(messaggio)

    def get_input(self) -> str:
        return self.chiedi_input_utente("Fai la tua mossa: ")

    def stampa_trascrizione(
        self, trascrizione: list[str], num_giocatori: int, replay: bool = False
    ):
        if not replay:
            stampa = "   "
            for j in range(0, num_giocatori):
                stampa += "P" + str(j + 1) + "  "
            stampa += "\n\n"
            i = len(trascrizione)
            while i > 0:
                stampa += trascrizione[i - 1] + "\n"
                i -= 1
            print(stampa)
        else:
            RIGA_IN = 3
            COLONNA_DESTRA = 55

            sys.stdout.write("\033[s")  # memorizza la posizione del cursore in basso
            sys.stdout.write(
                f"\033[{RIGA_IN};{COLONNA_DESTRA}H\033[1m--- STORICO MOSSE ---\033[0m"
            )  # Sposta a destra e scrive STORICO MOSSE
            intestazione = ""
            for i in range(num_giocatori):
                intestazione += "P" + str(i + 1) + "   "
            sys.stdout.write(
                f"\033[{RIGA_IN + 1};{COLONNA_DESTRA + 3}H\033[94m{intestazione}\033[0m"
            )  # Sposta a destra e scrive l'intestazione ossia P1,P2 ...

            for i, mossa in enumerate(trascrizione):
                riga_attuale = RIGA_IN + 2 + i
                sys.stdout.write(f"\033[{riga_attuale};{COLONNA_DESTRA}H\033[K{mossa}")

            sys.stdout.write("\033[u")
            sys.stdout.flush()
