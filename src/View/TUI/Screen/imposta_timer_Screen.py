# proj-stonebraker/src/View/TUI/Screen/imposta_timer_Screen.py

from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Button, Label, Input
from textual.containers import Vertical, Center,Horizontal


class ImpostaTimerScreen(Screen):
    def __init__(self, coda_input, **kwargs):
        super().__init__(**kwargs)
        self.__coda_input = coda_input

    def compose(self) -> ComposeResult:
        with Horizontal(classes="layout-menu-aiuto"):
            with Vertical(id="menu-timer-container"):
                yield Label("Selezionare Un Limite di Tempo", id="titolo-timer")
                yield Button("1 - 3 Minuti", id="btn-3min")
                yield Button("2 - 5 Minuti", id="btn-5min")
                yield Label("\nOppure inserisci tempo: HH:MM:SS")
                yield Input(placeholder="HH:MM:SS", id="input-custom-timer")
                yield Button("h - Aiuto", id="btn-aiuto") # <-- Bottone Aiuto
                yield Button("0 - Torna Indietro", id="btn-indietro", variant="error")
            
            yield Label("", id="pannello-aiuto")
    def on_button_pressed(self, event: Button.Pressed):
        id_premuto = event.button.id
        
        if id_premuto == "btn-3min":
            self.__coda_input.put("1")
            self.app.pop_screen()
        elif id_premuto == "btn-5min":
            self.__coda_input.put("2")
            self.app.pop_screen()
        elif id_premuto == "btn-aiuto":
            self.__coda_input.put("h")

        elif id_premuto == "btn-indietro":
            self.__coda_input.put("0")
            self.app.pop_screen()

    # Questo evento scatta quando l'utente preme "Invio" sul campo Input
    def on_input_submitted(self, event: Input.Submitted):
        if event.input.id == "input-custom-timer":
            # Inseriamo nella coda esattamente ciò che l'utente ha scritto (es. "00:10:00")
            self.__coda_input.put(event.value)
            self.app.pop_screen()