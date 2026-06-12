from textual.app import ComposeResult
from textual.containers import Vertical
from textual.screen import ModalScreen  # <-- Cambiato: Ora è un popup sovrapposto!
from textual.widgets import Button, Label

from src.View.TUI.Screen.quoridor_view_Screen import QuoridorViewScreen


class VittoriaModalScreen(ModalScreen):
    """Schermata modale di vittoria.

    DESCRIZIONE
        Mostra la schermata di vittoria al termine della partita,
        permettendo all'utente di visualizzare opzioni come replay,
        trascrizione o ritorno al menu principale.

    METODI

        def __init__(self, id_giocatore, motivo: str, app, **kwargs):
            DESCRIZIONE
                Inizializza la schermata di vittoria con informazioni
                sul giocatore vincitore e motivo della vittoria.

        def compose(self) -> ComposeResult:
            DESCRIZIONE
                Crea e dispone gli elementi grafici della schermata modale.

        def on_button_pressed(self, event: Button.Pressed):
            DESCRIZIONE
                Gestisce la pressione dei pulsanti e invia i comandi
                appropriati al controller o modifica la UI.
    """

    def __init__(self, id_giocatore, motivo: str, app, **kwargs):
        super().__init__(**kwargs)
        self._id_giocatore = id_giocatore
        self._motivo = motivo
        self._app = app

    def compose(self) -> ComposeResult:
        # 1. BOTTONE FLOTTANTE (Nascosto di default)
        # Questo apparirà in alto solo quando nascondiamo il menu principale
        yield Button(
            "⬅ Menu",
            id="btn-ripristina-vittoria",
            variant="primary",
            classes="nascosto",
        )

        # 2. MENU VITTORIA CENTRALE
        with Vertical(id="menu-vittoria-container"):
            yield Label("🏆 PARTITA TERMINATA 🏆", id="titolo-vittoria")
            yield Label(f"{self._id_giocatore}\n{self._motivo}", id="motivo-vittoria")

            # NUOVO PULSANTE
            yield Button(
                "👀 Mostra Mossa Vincente", id="btn-guarda-tavoliere", variant="success"
            )

            yield Button("Torna al Menu", id="btn-menu", variant="primary")
            yield Button("Vedi Trascrizione", id="btn-trascrizione", variant="default")
            yield Button("Vedi Replay (manuale)", id="btn-replay-m", variant="warning")
            yield Button(
                "Vedi Replay (automatico)", id="btn-replay-a", variant="warning"
            )

    def on_button_pressed(self, event: Button.Pressed):
        id_premuto = event.button.id

        # ==========================================
        # LOGICA GRAFICA (NON SBLOCCA IL CONTROLLER)
        # ==========================================
        if id_premuto == "btn-guarda-tavoliere":
            # Nascondiamo il menu e mostriamo il bottoncino in alto
            self.query_one("#menu-vittoria-container").add_class("nascosto")
            self.query_one("#btn-ripristina-vittoria").remove_class("nascosto")
            self.app.notify(
                "Stai guardando il tabellone finale. Clicca il pulsante in alto per "
                "tornare al menu.",
                timeout=4,
            )
            return  # Interrompe la funzione qui!

        elif id_premuto == "btn-ripristina-vittoria":
            # Ripristiniamo il menu nascondendo il bottoncino
            self.query_one("#btn-ripristina-vittoria").add_class("nascosto")
            self.query_one("#menu-vittoria-container").remove_class("nascosto")
            return  # Interrompe la funzione qui!

        # ==========================================
        # LOGICA DI GIOCO (MANDA COMANDI AL CONTROLLER)
        # ==========================================
        comando = ""
        if id_premuto == "btn-menu":
            comando = "m"
            self.app.switch_screen(QuoridorViewScreen())

        elif id_premuto == "btn-trascrizione":
            comando = "trascrizione"
            self.app.notify("Trascrizione in apertura...", title="Info")

        elif id_premuto == "btn-replay-m":
            comando = "r"
            self.app.notify("Caricamento Replay manuale...", title="Info")

        elif id_premuto == "btn-replay-a":  # Corretto piccolo refuso (era brn)
            comando = "ra"
            self.app.notify("Caricamento Replay automatico...", title="Info")

        if comando:
            # Usiamo sempre la coda per sicurezza
            self._app.get_coda_input().put(comando)
