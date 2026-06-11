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
                yield Button("- Partita con Timer", id="btn-timer")
                yield Button("- Partita senza Timer", id="btn-notimer")
                yield Button("- Mostra aiuto", id="btn-aiuto") # <-- Bottone Aiuto
                yield Button("- Torna Indietro", id="btn-indietro", variant="error")
            
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
            pannello = self.query_one("#pannello-aiuto", Label)
            if pannello.has_class("visibile"):
                pannello.remove_class("visibile")
                event.button.label = "- Mostra Aiuto"
            else:
                event.button.label = "- Nascondi Aiuto"
                self.__coda_input.put("help")
            # NESSUN pop_screen() qui!
        elif id_premuto == "btn-indietro":
            self.__coda_input.put("0")
            self.app.pop_screen()