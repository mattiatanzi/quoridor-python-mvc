from textual.app import ComposeResult
from textual.containers import Vertical
from textual.screen import ModalScreen
from textual.widgets import Button

from src.View.TUI.Widget.aiuto_Widget import AiutoWidget


class AiutoScreen(ModalScreen):
    """Schermata modale per mostrare i comandi di aiuto e bloccare il gioco."""

    # Permette di chiudere la finestra premendo il tasto Esc
    BINDINGS = [("escape", "chiudi", "Chiudi")]

    def __init__(self, testo_aiuto: str):
        super().__init__()
        self.testo_aiuto = testo_aiuto

    def compose(self) -> ComposeResult:
        # Usa la stessa classe CSS che probabilmente usi già per gli altri popup
        with Vertical(id="aiuto-modal-container"):
            yield AiutoWidget(self.testo_aiuto)
            yield Button("Chiudi", id="btn-chiudi-aiuto", variant="error")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "btn-chiudi-aiuto":
            self.dismiss()

    def action_chiudi(self) -> None:
        self.dismiss()
