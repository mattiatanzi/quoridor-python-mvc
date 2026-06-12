from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual.screen import Screen
from textual.widgets import Button, Footer, Header, Label

from src.View.costanti_quoridor_view import CostantiQuoridorView


class QuoridorViewScreen(Screen):
    """Parte grafica che effettuata con Textual.

    Contiene soltanto quello che viene mostrato a video
    def compose(self) -> ComposeResult
        DESCRIZIONE
        Mostra a video i componenti

    def on_event_pressed(self,event: Button.Pressed)
        DESCRIZIONE
        Cattura il click del mouse e traduce il click in un comando da mandare
        all APP che gestira il collegamento con partita controller
    """

    def compose(self) -> ComposeResult:
        yield Header()

        # Sostituisci il blocco with Center(): con questo:
        with Horizontal(classes="layout-menu-aiuto"):
            with Vertical(id="menu-container"):
                yield Label(
                    "Benvenuto in Quoridor", id="menu-titolo", classes="btn-menu"
                )
                yield Button(
                    "- Avvia una nuova partita", id="btn-avviaPart", classes="btn-menu"
                )
                yield Button(
                    f"{CostantiQuoridorView.MOSTRA_AIUTO}",
                    id="btn-avviaHelp",
                    classes="btn-menu",
                )
                yield Button(
                    f"{CostantiQuoridorView.ESCI_GIOCO}",
                    id="btn-Esci",
                    variant="error",
                    classes="btn-menu",
                )

            # Pannello laterale per l'aiuto
            yield Label("", id="pannello-aiuto")
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed):
        id_premuto = event.button.id

        if id_premuto == "btn-avviaPart":
            comando = "1"
        elif id_premuto == "btn-avviaHelp":
            pannello = self.query_one("#pannello-aiuto", Label)
            if pannello.has_class("visibile"):
                # Se è visibile, lo nascondiamo e cambiamo il bottone
                pannello.remove_class("visibile")
                event.button.label = f"{CostantiQuoridorView.MOSTRA_AIUTO}"
                return  # <-- IMPORTANTISSIMO: usciamo senza inviare nulla alla coda!
            else:
                # Se è nascosto, cambiamo il bottone in Nascondi e inviamo "h" al controller
                event.button.label = f"{CostantiQuoridorView.NASCONDI_AIUTO}"
                comando = "h"
        elif id_premuto == "btn-Esci":
            comando = "0"

            self.set_timer(1.5, self.app.exit)  # Con questo comando indichiamo che
            # se premuto 0 aspetta 1,5 secondi poi chiude l'interfaccia grafica
            # altrimenti rimarrebbe attivo il thread dell'interfaccia grafica
        else:
            comando = ""

        self.app.invia_comando(
            comando
        )  # Screen eredita app quindi di base app funziona
