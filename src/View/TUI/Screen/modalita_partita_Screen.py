# proj-stonebraker/src/View/TUI/Screen/modalita_partita_Screen.py

from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Button, Label
from textual.containers import Vertical, Center

class ModalitaPartitaScreen(Screen):
    def __init__(self, coda_input, **kwargs):
        super().__init__(**kwargs)
        self.__coda_input = coda_input

    def compose(self) -> ComposeResult:
        with Center():
            with Vertical(id="menu-modalita-container"):
                yield Label("Selezionare Una Modalità Di Gioco", id="titolo-modalita")
                # I valori "1", "2" e "0" sono i valori che il Controller si aspetta
                yield Button("1 - Partita con Timer", id="btn-timer")
                yield Button("2 - Partita senza Timer", id="btn-notimer")
                yield Button("0 - Torna Indietro", id="btn-indietro", variant="error")

    def on_button_pressed(self, event: Button.Pressed):
        id_premuto = event.button.id

        if id_premuto == "btn-timer":
            self.__coda_input.put("1")
        elif id_premuto == "btn-notimer":
            self.__coda_input.put("2")
        elif id_premuto == "btn-indietro":
            self.__coda_input.put("0")
        
        # Una volta fatta la scelta, togliamo questo schermo
        self.app.pop_screen()