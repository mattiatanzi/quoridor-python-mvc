from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual.screen import Screen
from textual.widgets import Button, Label

from src.View.costanti_quoridor_view import CostantiQuoridorView


class NumeroGiocatoriScreen(Screen):
    """Schermata di selezione del numero di giocatori.

    DESCRIZIONE

        Permette all'utente di selezionare il numero di giocatori per la partita,
        oltre a fornire opzioni di aiuto e ritorno al menu precedente.

    METODI

        def __init__(self, coda_input, **kwargs):
            DESCRIZIONE
                Inizializza la schermata e collega la coda degli input.

        def compose(self) -> ComposeResult:
            DESCRIZIONE
                Crea e visualizza l'interfaccia per la scelta del numero di giocatori.

        def on_button_pressed(self, event: Button.Pressed):
            DESCRIZIONE
                Gestisce la selezione del numero di giocatori, la richiesta di aiuto
                e il ritorno alla schermata precedente.
    """

    def __init__(self, coda_input, **kwargs):
        super().__init__(**kwargs)
        self.__coda_input = coda_input

    def compose(self) -> ComposeResult:
        with Horizontal(classes="layout-menu-aiuto"):
            with Vertical(id="menu-giocatori-container"):
                yield Label("Selezionare Il Numero Di Giocatori", id="titolo-giocatori")
                yield Button(
                    f"{CostantiQuoridorView.POSSIBILI_NUMERO_GIOCATORI.get(CostantiQuoridorView.SCELTA_2_GIOCATORI)}",
                    id="btn-2-giocatori",
                    classes="btn-menu",
                )
                yield Button(
                    f"{CostantiQuoridorView.POSSIBILI_NUMERO_GIOCATORI.get(CostantiQuoridorView.SCELTA_4_GIOCATORI)}",
                    id="btn-4-giocatori",
                    classes="btn-menu",
                )
                yield Button(
                    f"{CostantiQuoridorView.MOSTRA_AIUTO}",
                    id="btn-aiuto",
                    classes="btn-menu",
                )
                yield Button(
                    f"{CostantiQuoridorView.POSSIBILI_TIMER_DEFAULT.get(CostantiQuoridorView.SCELTA_TORNA_INDIETRO)}",
                    id="btn-indietro",
                    variant="error",
                    classes="btn-menu",
                )

            # Pannello per l'help a scomparsa
            yield Label("", id="pannello-aiuto")

    def on_button_pressed(self, event: Button.Pressed):
        id_premuto = event.button.id

        if id_premuto == "btn-2-giocatori":
            self.__coda_input.put("1")
            self.app.pop_screen()

        elif id_premuto == "btn-4-giocatori":
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
