from textual.app import ComposeResult
from textual.widgets import Button, Label, Header, Footer
from textual.screen import Screen
from textual.containers import Vertical, Center


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

        with Center():
            with Vertical(id = "menu-container"):
                yield Label("Benvenuto in Quoridor", id = "menu-titolo")

                yield Button("1 - Avvia una nuova partita", id = "btn-avviaPart")
                yield Button("h - Aiuto (Comandi di gioco)", id = "btn-avviaHelp")
                yield Button("0 - Esci dal gioco", id="btn-Esci", variant="error")

            yield Footer()

    def on_button_pressed(self, event: Button.Pressed):
        id_premuto = event.button.id

        if id_premuto == "btn-avviaPart":
            comando = "1"
        elif id_premuto == "btn-avviaHelp":
            comando = "2"
        elif id_premuto == "btn-Esci":
            comando = "0"
        else:
            comando = ""
        
        self.app.invia_comando(comando) # Screen eredita app quindi di base app funziona

    
