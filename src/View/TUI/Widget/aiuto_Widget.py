from textual.widgets import Static
from textual.app import ComposeResult

class AiutoWidget(Static):
    """Widget riutilizzabile che contiene e formatta il testo dell'aiuto."""
    
    def __init__(self, testo_aiuto: str, **kwargs):
        super().__init__(**kwargs)
        self._testo = testo_aiuto

    def compose(self) -> ComposeResult:
        yield Static(self._testo, id="testo-regole-aiuto")