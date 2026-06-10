from threading import Event
import time

from src.Model.partita import Partita
from src.Model.tempo import get_tempo_formattato
from src.View.giocatore_view import GiocatoreViewAstratta
from src.View.partita_view import PartitaViewAstratta
from src.View.tavoliere_view import TavoliereviewAstratta
from src.View.TUI.Screen.partita_view_Screen import PartitaViewScreen
from textual.widgets import Label


class PartitaViewTUI(PartitaViewAstratta):
    """Implementazione TUI della view della partita.

    Non stampa nulla direttamente: aggiorna i widget
    già montati nella PartitaViewScreen tramite call_from_thread.

    ATTRIBUTI
        _app : QuoridorViewApp
            Riferimento all'app Textual condivisa
    """

    def __init__(
        self,
        new_giocatore_view: GiocatoreViewAstratta,
        new_tavoliere_view: TavoliereviewAstratta,
        app_condivisa,
    ):
        super().__init__(new_giocatore_view, new_tavoliere_view)
        self._app = app_condivisa

    # ------ Stampe Video ------ #

    def stampa_partita(self, partita: Partita):
        giocatori = partita.get_giocatori()
        tavoliere = partita.get_tavoliere()

        for g in giocatori:
            id_sel = g.get_id()
            muri = partita.get_muri_disponibili_giocatore(id_sel)
            tempo_fmt = (
                get_tempo_formattato(g.get_tempo_residuo())
                if g.possiede_limite_tempo()
                else None
            )

            if g.is_attivo():
                if id_sel == partita.get_id_giocatore_attivo():
                    self.get_giocatore_view().stampa_giocatore_attivo(
                        id_sel, muri, tempo_fmt
                    )
                else:
                    self.get_giocatore_view().stampa_info_giocatore(
                        id_sel, muri, tempo_fmt
                    )
            else:
                self.get_giocatore_view().stampa_giocatore_eliminato(
                    id_sel, muri, tempo_fmt
                )

        # Il tavoliere aggiorna i widget già montati nella screen
        self.get_tavoliere_view().stampa_tavoliere(tavoliere, giocatori)

    def stampa_errore_partita(self, messaggio):
        def _aggiorna():
            try:
                self._app.screen.aggiorna_label_errore(str(messaggio))
            except Exception:
                pass
        self._app.call_from_thread(_aggiorna)

    def stampa_aiuto(self):
        messaggio = """
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
        def aggiorna_aiuto():
            try:
                # Cerca il pannello sullo schermo attuale
                pannello = self.__app.screen.query_one("#pannello-aiuto", Label)
                pannello.update(messaggio)
                pannello.add_class("visibile") # Lo fa comparire
            except Exception:
                self.__app.notify(messaggio) # Sicurezza se il widget non esiste
        self.__app.call_from_thread(aggiorna_aiuto)

    def stampa_vittoria(self, id_vincitore, motivo_vittoria: str):
        testo = f"🏆 {id_vincitore} HA VINTO — {motivo_vittoria}"
        self._app.call_from_thread(
            self._app.notify, testo, severity="information", timeout=10
        )

    def stampa_trascrizione(
        self, trascrizione: list[str], num_giocatori: int, replay: bool = False
    ):
        # Nella TUI la trascrizione sarà nel pannello laterale della
        # ReplayViewScreen; durante la partita usiamo una notifica
        if not replay:
            testo = "\n".join(reversed(trascrizione[-15:]))
            self._app.call_from_thread(self._app.notify, testo, timeout=10)

    def chiedi_input_utente(self, indicazioniInput: str = "") -> str:
        # Il controller chiama questo metodo per leggere dalla coda,
        # che viene popolata da on_input_submitted nella screen
        return self._app.get_coda_input().get()

    def get_input(self) -> str:
        return self.chiedi_input_utente()

    def stampa_richiesta_input(self, indicazioni: str = ""):
        # Aggiorna il label hint sopra il campo input
        def _aggiorna():
            try:
                self._app.screen.query_one(
                    "#label-input-hint"
                ).update(indicazioni or "Fai la tua mossa:")
            except Exception:
                pass
        self._app.call_from_thread(_aggiorna)

    def avvia_interfaccia_partita(self, ids_giocatori: list[str]) -> None:
        """Chiede all'app Textual di mostrare la schermata di partita e attende che sia pronta."""
        evento = Event()
        
        def _cambia_schermo():
            self._app.mostra_schermo_partita(ids_giocatori)
            evento.set()

        # Esegue il push_screen nel thread principale (sicuro per Textual)
        self._app.call_from_thread(_cambia_schermo)
        
        # Blocca il Controller finché Textual non ha completato l'operazione
        evento.wait()
        
        # Una piccola pausa (100 millisecondi) per dare tempo a Textual 
        # di costruire materialmente i widget nel DOM prima della stampa successiva
        time.sleep(0.1)

    def torna_al_menu(self):
        """Rimuove lo schermo della partita e torna al menu."""
        # Anche le operazioni di chiusura (pop_screen) devono passare dal thread principale
        self._app.call_from_thread(self._app.torna_al_menu)