from textual.app import ComposeResult
from textual.widget import Widget
from textual.widgets import Label
from textual.containers import Vertical


class GiocatoreViewWidget(Widget):
    """Widget che mostra le informazioni di un singolo giocatore.
    
    Viene creato uno per ogni giocatore e montato nel pannello
    laterale della PartitaViewScreen.
    
    ID dei label interni:
        #label-stato-{id}  →  es. #label-stato-P1
        #label-muri-{id}   →  es. #label-muri-P1
        #label-tempo-{id}  →  es. #label-tempo-P1
    """

    def __init__(self, id_giocatore: str):
        # L'id del widget stesso diventa "giocatore-widget-P1" ecc.
        super().__init__(id=f"giocatore-widget-{id_giocatore}")
        self._id_giocatore = id_giocatore

    def compose(self) -> ComposeResult:
        with Vertical(classes="giocatore-box"):
            yield Label(self._id_giocatore,
                        id=f"label-stato-{self._id_giocatore}",
                        classes="giocatore-label-stato")
            yield Label("Muri: --",
                        id=f"label-muri-{self._id_giocatore}",
                        classes="giocatore-label-muri")
            yield Label("",
                        id=f"label-tempo-{self._id_giocatore}",
                        classes="giocatore-label-tempo")

    def aggiorna_attivo(self, muri_disponibili: int, tempo_formattato: str = None):
        """Evidenzia il giocatore come quello di turno."""
        self.query_one(f"#label-stato-{self._id_giocatore}", Label).update(
            f"► {self._id_giocatore} — TURNO"
        )
        self.query_one(f"#label-muri-{self._id_giocatore}", Label).update(
            f"Muri: {muri_disponibili}"
        )
        self.query_one(f"#label-tempo-{self._id_giocatore}", Label).update(
            f"⏱ {tempo_formattato}" if tempo_formattato else ""
        )
        self.add_class("giocatore-attivo")
        self.remove_class("giocatore-eliminato")

    def aggiorna_info(self, muri_disponibili: int, tempo_formattato: str = None):
        """Mostra il giocatore come in attesa."""
        self.query_one(f"#label-stato-{self._id_giocatore}", Label).update(
            self._id_giocatore
        )
        self.query_one(f"#label-muri-{self._id_giocatore}", Label).update(
            f"Muri: {muri_disponibili}"
        )
        self.query_one(f"#label-tempo-{self._id_giocatore}", Label).update(
            f"⏱ {tempo_formattato}" if tempo_formattato else ""
        )
        self.remove_class("giocatore-attivo")
        self.remove_class("giocatore-eliminato")

    def aggiorna_eliminato(self, muri_disponibili: int, tempo_formattato: str = None):
        """Mostra il giocatore come eliminato."""
        self.query_one(f"#label-stato-{self._id_giocatore}", Label).update(
            f"✖ {self._id_giocatore} — ELIMINATO"
        )
        self.query_one(f"#label-muri-{self._id_giocatore}", Label).update(
            f"Muri: {muri_disponibili}"
        )
        self.query_one(f"#label-tempo-{self._id_giocatore}", Label).update("")
        self.add_class("giocatore-eliminato")
        self.remove_class("giocatore-attivo")