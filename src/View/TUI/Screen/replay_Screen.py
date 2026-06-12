import queue

from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical, VerticalScroll
from textual.screen import Screen
from textual.widgets import Button, Label

from src.View.TUI.Static.tavoliere_view_Static import TavoliereViewStatic
from src.View.TUI.Widget.trascrizione_Widget import TrascrizioneWidget


class ReplayScreen(Screen):
    def __init__(self, coda_input, **kwargs):
        super().__init__(**kwargs)
        self._coda_input = coda_input

    def compose(self) -> ComposeResult:
        with Horizontal(id="replay-layout"):
            # SINISTRA: Tavoliere e Descrizione Mossa
            with VerticalScroll(id="replay-sinistra"):
                yield Label("MODALITÀ REPLAY", id="replay-titolo")
                yield Label("", id="replay-descrizione-mossa")
                coda_finta = queue.Queue()  # Usiamo una coda fittizia per evitare di prendere input inutili durante la visione del replay
                yield TavoliereViewStatic(coda_finta, is_replay=True)

            # DESTRA: Trascrizione
            with Vertical(id="replay-destra"):
                yield Label("TRASCRIZIONE", classes="titolo-pannello")
                yield TrascrizioneWidget("")

        # IN BASSO: Bottoni di navigazione
        with Horizontal(id="replay-nav-buttons"):
            yield Button(
                "I<< Inizio", id="btn-inizio", variant="primary", classes="btn-menu"
            )
            yield Button(
                "< Indietro", id="btn-indietro", variant="primary", classes="btn-menu"
            )
            yield Button(
                "Avanti >", id="btn-avanti", variant="primary", classes="btn-menu"
            )
            yield Button(
                "Fine >>I", id="btn-fine", variant="primary", classes="btn-menu"
            )
            yield Button(
                "Esci", id="btn-esci-replay", variant="error", classes="btn-menu"
            )

    def on_button_pressed(self, event: Button.Pressed):
        """Invia i comandi esatti che il ReplayController si aspetta!"""
        id_premuto = event.button.id

        if id_premuto == "btn-inizio":
            self._coda_input.put("inizio")
        elif id_premuto == "btn-indietro":
            self._coda_input.put("p")
        elif id_premuto == "btn-avanti":
            self._coda_input.put("n")
        elif id_premuto == "btn-fine":
            self._coda_input.put("fine")
        elif id_premuto == "btn-esci-replay":
            self._coda_input.put("esci")
