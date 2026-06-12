# proj-stonebraker/src/View/TUI/Screen/imposta_timer_Screen.py

from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual.screen import Screen
from textual.widgets import Button, Input, Label

from src.View.costanti_quoridor_view import CostantiQuoridorView


class ImpostaTimerScreen(Screen):
    """Schermata di selezione del timer di gioco.

    DESCRIZIONE
        Permette all'utente di selezionare un limite di tempo predefinito
        oppure inserire un tempo personalizzato in formato HH:MM:SS.

    METODI

        def __init__(self, coda_input, **kwargs):
            DESCRIZIONE
                Inizializza la schermata e collega la coda degli input.

        def compose(self) -> ComposeResult:
            DESCRIZIONE
                Crea e visualizza l'interfaccia per la scelta del timer.

        def on_button_pressed(self, event: Button.Pressed):
            DESCRIZIONE
                Gestisce la selezione dei timer predefiniti, la richiesta
                di aiuto e il ritorno alla schermata precedente.

        def on_input_submitted(self, event: Input.Submitted):
            DESCRIZIONE
                Gestisce l'inserimento di un timer personalizzato da parte
                dell'utente.
    """

    def __init__(self, coda_input, **kwargs):
        super().__init__(**kwargs)
        self.__coda_input = coda_input

    def compose(self) -> ComposeResult:
        with Horizontal(classes="layout-menu-aiuto"):
            with Vertical(id="menu-timer-container"):
                yield Label("Selezionare Un Limite di Tempo", id="titolo-timer")
                yield Button(
                    f"- {CostantiQuoridorView.POSSIBILI_TIMER_DEFAULT.get(
                        CostantiQuoridorView.SCELTA_TIMER_DEFAULT_1
                    )}",
                    id="btn-3min",
                    classes="btn-menu",
                )
                yield Button(
                    f"- {CostantiQuoridorView.POSSIBILI_TIMER_DEFAULT.get(
                        CostantiQuoridorView.SCELTA_TIMER_DEFAULT_2
                    )}",
                    id="btn-5min",
                    classes="btn-menu",
                )
                yield Label(
                    f"{CostantiQuoridorView.MESSAGGIO_ALTERNATIVO_SCELTA_TIMER}"
                )
                yield Input(placeholder="HH:MM:SS", id="input-custom-timer")
                yield Button(
                    f"{CostantiQuoridorView.MOSTRA_AIUTO}",
                    id="btn-aiuto",
                    classes="btn-menu",
                )  # <-- Bottone Aiuto
                yield Button(
                    f"{CostantiQuoridorView.POSSIBILI_TIMER_DEFAULT.get(CostantiQuoridorView.SCELTA_TORNA_INDIETRO)}",
                    id="btn-indietro",
                    variant="error",
                    classes="btn-menu",
                )

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
            pannello = self.query_one("#pannello-aiuto", Label)
            if pannello.has_class("visibile"):
                pannello.remove_class("visibile")
                event.button.label = f"{CostantiQuoridorView.MOSTRA_AIUTO}"
            else:
                event.button.label = f"{CostantiQuoridorView.NASCONDI_AIUTO}"
                self.__coda_input.put("help")

        elif id_premuto == "btn-indietro":
            self.__coda_input.put("0")
            self.app.pop_screen()

    # Questo evento scatta quando l'utente preme "Invio" sul campo Input
    def on_input_submitted(self, event: Input.Submitted):
        if event.input.id == "input-custom-timer":
            # Inseriamo nella coda esattamente ciò che l'utente
            # ha scritto (es. "00:10:00")
            self.__coda_input.put(event.value)
            self.app.pop_screen()
