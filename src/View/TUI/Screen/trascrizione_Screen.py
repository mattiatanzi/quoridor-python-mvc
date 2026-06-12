from textual.app import ComposeResult
from textual.containers import Vertical
from textual.screen import ModalScreen
from textual.widgets import Button, Label

from src.View.TUI.Widget.trascrizione_Widget import TrascrizioneWidget


class TrascrizioneScreen(ModalScreen):
    """Popup oscurante che mostra la trascrizione della partita.

    DESCRIZIONE
        Visualizza la lista delle mosse della partita tramite widget
        dedicato e permette di chiudere il popup per tornare al gioco.

    METODI

        def __init__(self, trascrizione: str, **kwargs):
            DESCRIZIONE
                Inizializza il popup con la trascrizione da visualizzare.

        def compose(self) -> ComposeResult:
            DESCRIZIONE
                Costruisce il layout del popup con titolo, trascrizione
                e pulsante di chiusura.

        def on_button_pressed(self, event: Button.Pressed) -> None:
            DESCRIZIONE
                Gestisce la chiusura del popup quando viene premuto
                il pulsante "Chiudi".
    """

    def __init__(self, trascrizione: str, **kwargs):
        super().__init__(**kwargs)
        self._trascrizione = trascrizione

    def compose(self) -> ComposeResult:
        with Vertical(id="pannello-trascrizione"):
            yield Label("TRASCRIZIONE MOSSE", id="titolo-trascrizione")

            # 1. Usiamo il tuo Widget riutilizzabile!
            yield TrascrizioneWidget(self._trascrizione)

            # 2. Bottone per chiudere il popup e tornare a giocare
            yield Button(
                "Chiudi",
                id="btn-chiudi-trascrizione",
                variant="error",
                classes="btn-menu",
            )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "btn-chiudi-trascrizione":
            self.dismiss()
