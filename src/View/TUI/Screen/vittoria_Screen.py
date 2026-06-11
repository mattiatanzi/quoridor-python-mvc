from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Button, Label, Header,Footer
from textual.containers import Vertical,Horizontal
from src.View.TUI.Screen.quoridor_view_Screen import QuoridorViewScreen

class VittoriaScreen(Screen):
    def __init__(self, id_giocatore,motivo: str,app, **kwargs):
        super().__init__(**kwargs)
        self._id_giocatore = id_giocatore
        self._motivo = motivo
        self._app = app

    def compose(self) -> ComposeResult:
        yield Header()

        with Horizontal(classes="layout-menu-aiuto"):
            with Vertical(id="menu-vittoria-container"):
                yield Label("PARTITA TERMINATA", id="titolo-vittoria")
                yield Label(f"{self._id_giocatore}, {self._motivo}",id="motivo-vittoria") # Qui mostriamo il motivo!
                yield Button("Torna al Menu", id="btn-menu", variant="primary")
                yield Button("Vedi Trascrizione", id="btn-trascrizione", variant="default")
                yield Button("Vedi Replay (manuale)", id="btn-replay-m", variant="warning")
                yield Button("Vedi Replay (automatico)", id="btn-replay-a", variant="warning")


            yield Label("",id="pannello-aiuto")
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed):
        id_premuto = event.button.id
        
        comando  =""
        if id_premuto == "btn-menu":
            # SWITCH_SCREEN: svuota lo stack e torna al menu principale
            comando  = "m"
            self.app.switch_screen(QuoridorViewScreen())
            
        elif id_premuto == "btn-trascrizione":
            comando = "trascrizione"
            self.app.notify("Trascrizione in apertura...", title="Info")
            # Qui potresti chiamare la logica per aprire il file
            
        elif id_premuto == "btn-replay-m":
            comando = "r"
            self.app.notify("Replay caricamento...", title="Info")
        
        elif id_premuto == "brn-replay-a":
            comando = "ra"
            self.app.notify("Replay caricamento...", title="Info")

        self._app.invia_comando(comando) # Screen eredita app quindi di base app funziona
