from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Button, Label
from textual.containers import Vertical, Horizontal
from src.View.costanti_quoridor_view import CostantiQuoridorView

class ModalitaPartitaScreen(Screen):
    def __init__(self, coda_input, **kwargs):
        super().__init__(**kwargs)
        self.__coda_input = coda_input

    def compose(self) -> ComposeResult:
        with Horizontal(classes="layout-menu-aiuto"):
            with Vertical(id="menu-modalita-container"):
                yield Label("Selezionare Una Modalità Di Gioco", id="titolo-modalita")
                yield Button(f"{CostantiQuoridorView.POSSIBILI_SCELTE_MODALITA.get(CostantiQuoridorView.SCELTA_PARTITA_CON_TIMER)}", id="btn-timer" , classes= "btn-menu")
                yield Button(f"{CostantiQuoridorView.POSSIBILI_SCELTE_MODALITA.get(CostantiQuoridorView.SCELTA_PARTITA_SENZA_TIMER)}", id="btn-notimer" , classes= "btn-menu")
                yield Button(f"{CostantiQuoridorView.MOSTRA_AIUTO}", id="btn-aiuto" , classes= "btn-menu") # <-- Bottone Aiuto
                yield Button(f"{CostantiQuoridorView.POSSIBILI_TIMER_DEFAULT.get(CostantiQuoridorView.SCELTA_TORNA_INDIETRO)}", id="btn-indietro", variant="error" , classes= "btn-menu")
            
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
                event.button.label = f"{CostantiQuoridorView.MOSTRA_AIUTO}"
            else:
                event.button.label = f"{CostantiQuoridorView.NASCONDI_AIUTO}"
                self.__coda_input.put("help")
            # NESSUN pop_screen() qui!
        elif id_premuto == "btn-indietro":
            self.__coda_input.put("0")
            self.app.pop_screen()