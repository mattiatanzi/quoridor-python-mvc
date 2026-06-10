# proj-stonebraker/src/View/TUI/Screen/modalita_partita_Screen.py

from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Button, Label
from textual.containers import Vertical, Horizontal

class ModalitaPartitaScreen(Screen):
    def __init__(self, coda_input, **kwargs):
        super().__init__(**kwargs)
        self.__coda_input = coda_input

    def compose(self) -> ComposeResult:
        with Horizontal(classes="layout-menu-aiuto"):
            with Vertical(id="menu-modalita-container"):
                yield Label("Selezionare Una Modalità Di Gioco", id="titolo-modalita")
                yield Button("1 - Partita con Timer", id="btn-timer")
                yield Button("2 - Partita senza Timer", id="btn-notimer")
                yield Button("h - Aiuto", id="btn-aiuto") # <-- Bottone Aiuto
                yield Button("0 - Torna Indietro", id="btn-indietro", variant="error")
            
            yield Label("", id="pannello-aiuto")

    def on_button_pressed(self, event: Button.Pressed):
        id_premuto = event.button.id
        if id_premuto == "btn-timer":
            self.__coda_input.put("1")
            self.app.pop_screen()
        elif id_premuto == "btn-notimer":
            self.__coda_input.put("2")
            self.app.pop_screen()
        elif id_premuto == "btn-aiuto":
            self.__coda_input.put("h")
            # NESSUN pop_screen() qui!
        elif id_premuto == "btn-indietro":
            self.__coda_input.put("0")
            self.app.pop_screen()