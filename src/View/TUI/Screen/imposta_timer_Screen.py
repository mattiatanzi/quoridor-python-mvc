# proj-stonebraker/src/View/TUI/Screen/imposta_timer_Screen.py

from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Button, Label, Input
from textual.containers import Vertical, Center

class ImpostaTimerScreen(Screen):
    def __init__(self, coda_input, **kwargs):
        super().__init__(**kwargs)
        self.__coda_input = coda_input

    def compose(self) -> ComposeResult:
        with Center():
            with Vertical(id="menu-timer-container"):
                yield Label("Selezionare Un Limite di Tempo", id="titolo-timer")
                
                yield Button(" 3 Minuti", id="btn-3min")
                yield Button(" 5 Minuti", id="btn-5min")
                
                yield Label("\nOppure inserisci tempo personalizzato:")
                # Il widget Input permette all'utente di digitare liberamente
                yield Input(placeholder="Formato: HH:MM:SS", id="input-custom-timer")
                
                yield Button("0 - Torna Indietro", id="btn-indietro", variant="error")

    def on_button_pressed(self, event: Button.Pressed):
        id_premuto = event.button.id

        if id_premuto == "btn-3min":
            self.__coda_input.put("1")
            self.app.pop_screen()
        elif id_premuto == "btn-5min":
            self.__coda_input.put("2")
            self.app.pop_screen()
        elif id_premuto == "btn-indietro":
            self.__coda_input.put("0")
            self.app.pop_screen()

    # Questo evento scatta quando l'utente preme "Invio" sul campo Input
    def on_input_submitted(self, event: Input.Submitted):
        if event.input.id == "input-custom-timer":
            # Inseriamo nella coda esattamente ciò che l'utente ha scritto (es. "00:10:00")
            self.__coda_input.put(event.value)
            self.app.pop_screen()