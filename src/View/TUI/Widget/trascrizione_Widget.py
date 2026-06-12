from textual.app import ComposeResult
from textual.containers import VerticalScroll
from textual.widget import Widget
from textual.widgets import Label


class TrascrizioneWidget(Widget):
    """Widget riutilizzabile che mostra l'elenco delle mosse scorrevole."""

    def __init__(self, trascrizione: str, **kwargs):
        super().__init__(**kwargs)
        self._trascrizione = trascrizione

    def compose(self) -> ComposeResult:
        with VerticalScroll(id="trascrizione-scroll"):
            # Se la stringa è vuota, mostriamo un testo di cortesia
            testo = (
                self._trascrizione
                if self._trascrizione.strip()
                else "Nessuna mossa effettuata finora."
            )
            yield Label(testo, id="trascrizione-testo")
