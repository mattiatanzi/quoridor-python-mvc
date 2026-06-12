from textual.app import ComposeResult
from textual.widget import Widget
from textual.widgets import Label
from textual.containers import VerticalScroll

class TrascrizioneWidget(Widget):
    """Widget riutilizzabile che mostra l'elenco delle mosse scorrevole.

    DESCRIZIONE
        Rappresenta un widget grafico utilizzato per visualizzare la trascrizione
        delle mosse della partita. Il contenuto viene mostrato in un'area scrollabile
        e può essere utilizzato sia durante la partita che nel replay.

    ATTRIBUTI
        _trascrizione : str
            Stringa contenente la trascrizione delle mosse della partita.
            Se vuota, viene mostrato un messaggio di default.

    METODI

        def __init__(self, trascrizione: str, **kwargs):
            DESCRIZIONE
                Inizializza il widget con la trascrizione fornita.

        def compose(self) -> ComposeResult:
            DESCRIZIONE
                Costruisce il layout del widget e gestisce la visualizzazione
                della trascrizione in un contenitore scrollabile.
    """
    
    def __init__(self, trascrizione: str, **kwargs):
        super().__init__(**kwargs)
        self._trascrizione = trascrizione

    def compose(self) -> ComposeResult:
        with VerticalScroll(id="trascrizione-scroll"):
            # Se la stringa è vuota, mostriamo un testo di cortesia
            testo = self._trascrizione if self._trascrizione.strip() else "Nessuna mossa effettuata finora."
            yield Label(testo, id="trascrizione-testo")