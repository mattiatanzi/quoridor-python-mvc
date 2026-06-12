from textual.css.query import NoMatches
from textual.widgets import Label

from src.Model.partita import Partita
from src.View.replay_view import ReplayViewAstratta
from src.View.TUI.giocatore_view_TUI import GiocatoreViewTUI
from src.View.TUI.Screen.replay_Screen import ReplayScreen
from src.View.TUI.tavoliere_view_TUI import TavoliereViewTUI


class ReplayViewTUI(ReplayViewAstratta):
    """Implementazione TUI della view del replay.

    DESCRIZIONE
        Gestisce la visualizzazione del replay della partita
        aggiornando tavoliere, descrizione delle mosse e trascrizione
        tramite la UI Textual.

    ATTRIBUTI
        _app : QuoridorViewApp
            Riferimento all'app Textual condivisa

        _tavoliere_view : TavoliereViewTUI
            View del tavoliere utilizzata per aggiornare lo stato grafico

        _giocatore_view : GiocatoreViewTUI
            View dei giocatori utilizzata per aggiornamenti grafici indiretti

    METODI

        def __init__(self, app_condivisa):
            DESCRIZIONE
                Inizializza le view TUI necessarie al replay.

        def stampa_replay(
            self,
            stato_corrente: Partita,
            descrizione_mossa: str,
            trascrizione_parziale: list[str],
            automatico: bool = False
        ):
            DESCRIZIONE
                Aggiorna lo stato del replay mostrando il tavoliere,
                la mossa corrente e la trascrizione progressiva.
    """

    def __init__(self, app_condivisa):
        self._app = app_condivisa
        self._tavoliere_view = TavoliereViewTUI(self._app)
        self._giocatore_view = GiocatoreViewTUI(self._app)

    def stampa_replay(
        self,
        stato_corrente: Partita,
        descrizione_mossa: str,
        trascrizione_parziale: list[str],
        automatico: bool = False,
    ):
        self._tavoliere_view.stampa_tavoliere(
            stato_corrente.get_tavoliere(), stato_corrente.get_giocatori()
        )

        def _aggiorna():
            try:
                if not isinstance(self._app.screen, ReplayScreen):
                    self._app.push_screen(ReplayScreen(self._app.get_coda_input()))
                    self._app.set_timer(0.05, _aggiorna)
                    return

                schermo = self._app.screen

                # Aggiorna testi
                schermo.query_one("#replay-descrizione-mossa", Label).update(
                    descrizione_mossa
                )
                testo_trasc = (
                    "\n".join(trascrizione_parziale)
                    if trascrizione_parziale
                    else "Inizio partita"
                )
                schermo.query_one("#trascrizione-testo", Label).update(testo_trasc)

                if automatico:
                    schermo.query_one("#btn-inizio").display = False
                    schermo.query_one("#btn-indietro").display = False
                    schermo.query_one("#btn-avanti").display = False
                    schermo.query_one("#btn-fine").display = False
                    schermo.query_one("#btn-esci-replay").display = False

                self._tavoliere_view.stampa_tavoliere(
                    stato_corrente.get_tavoliere(), stato_corrente.get_giocatori()
                )
            except NoMatches:
                self._app.set_timer(0.05, _aggiorna)

        # Invia l'ordine al thread principale
        # Essendo chiamato DOPO il tabellone, i giocatori verranno sempre disegnati
        self._app.call_from_thread(_aggiorna)
