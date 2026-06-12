import threading
import queue
import sys

from src.Model.partita import Partita
from src.Model.tempo import get_tempo_formattato
from src.View.funzioni_utili_stampa import chiedi_input_utente, pulisci_schermo
from src.View.giocatore_view import GiocatoreViewAstratta
from src.View.tavoliere_view import TavoliereviewAstratta
from src.View.partita_view import PartitaViewAstratta
from src.View.CLI.replay_view_CLI import ReplayViewCLI
from src.View.funzioni_utili_stampa import inserisci_input_forzato


class PartitaViewCLI(PartitaViewAstratta):
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

        def get_input(self):
            DESCRIZIONE
                Scrive un messaggio e prende e restituisce quello che scrive l'utente
                in input.

    """

    # Attributi
    __giocatoreView: GiocatoreViewAstratta
    __tavoliereView: TavoliereviewAstratta

    # Costanti
    __LUNGHEZZA_DIVISORI = 70


    # Metodi

    # Costruttore

    def __init__(
        self,
        new_giocatore_view: GiocatoreViewAstratta = None,
        new_tavoliere_view: TavoliereviewAstratta = None,
    ):
        self.__giocatoreView = new_giocatore_view
        self.__tavoliereView = new_tavoliere_view


    # Accesso Attributi Privati

    def set_tavoliere_view(self, new_tavoliere_view: TavoliereviewAstratta):
        self.__tavoliereView = new_tavoliere_view

    def get_tavoliere_view(self):
        return self.__tavoliereView

    def set_giocatore_view(self, new_giocatore_view: GiocatoreViewAstratta):
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

            if g.possiede_limite_tempo():
                stringa_tempo_rimanente = get_tempo_formattato(g.get_tempo_residuo())
            else:
                stringa_tempo_rimanente = None

            if g.is_attivo():
                if id_selezionato == partita.get_id_giocatore_attivo():
                    self.get_giocatore_view().stampa_giocatore_attivo(
                        id_selezionato, muri_rimanenti, stringa_tempo_rimanente
                    )
                else:
                    self.get_giocatore_view().stampa_info_giocatore(
                        id_selezionato, muri_rimanenti, stringa_tempo_rimanente
                    )
            else:
                self.get_giocatore_view().stampa_giocatore_eliminato(
                    id_selezionato, muri_rimanenti, stringa_tempo_rimanente
                )

        print("")
        self.get_tavoliere_view().stampa_tavoliere(tavoliere, giocatori)

        print("\nSuggerimento -- Digitare 'help' per visualizzare i comandi\n")

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

    def stampa_vittoria(self, idVincitore, motivo_vittoria: str):
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

        # Stampa descrizione della vittoria specifica
        print("\n\n")
        print(f"{motivo_vittoria:^{self.__LUNGHEZZA_DIVISORI}}")
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
        # Si appoggia semplicemente al nuovo sistema globale infallibile
        return chiedi_input_utente()

    def forza_input(self, testo: str):
        # Questo metodo verrà chiamato dal Controller quando scade il timer
        inserisci_input_forzato(testo)

    def stampa_trascrizione(
        self, trascrizione: list[str], num_giocatori: int
    ):
        stampa = "   "
        for j in range(0, num_giocatori):
            stampa += "P" + str(j + 1) + "  "
        stampa += "\n\n"
        i = len(trascrizione)
        while i > 0:
            stampa += trascrizione[i - 1] + "\n"
            i -= 1
        print(stampa)
       

    def avvia_interfaccia_partita(self, ids_giocatori: list[str]) -> None:
        pass   # nella CLI non serve cambiare schermo

    def torna_al_menu(self):
        pass

    def crea_replay_view(self):

        return ReplayViewCLI()
    
    def aggiorna_orologio_live(self, id_giocatore, tempo_formattato):
        RIGA_FISSA = 2     
        COLONNA_FISSA = 70
        
        # LA MAGIA ANSI ASSOLUTA:
        # \033[s              -> Salva la posizione attuale (in basso su "Input: ")
        # \033[{R};{C}H       -> Vola istantaneamente alla riga e colonna fisse
        # \033[K              -> Pulisce la riga da eventuali testi precedenti
        # \033[u              -> Torna istantaneamente in basso all'input
        
        testo = f" ⏱️ {id_giocatore} il tempo scorre: {tempo_formattato}"
        comando = f"\033[s\033[{RIGA_FISSA};{COLONNA_FISSA}H\033[K{testo}\033[u"
        
        sys.stdout.write(comando)
        sys.stdout.flush()

    def mostra_messaggio_timeout(self, id_giocatore: str):
        """Pulisce la riga sporcata dall'utente e annuncia l'eliminazione."""
        # \r\033[K = Torna all'inizio della riga in cui si stava scrivendo e cancellala
        sys.stdout.write(f"\r\033[K⏳ TEMPO SCADUTO! Il giocatore {id_giocatore} è eliminato.\n")
        sys.stdout.flush()