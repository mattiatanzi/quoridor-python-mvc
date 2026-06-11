from textual.app import ComposeResult
from textual.widget import Widget
from textual.widgets import Label
from textual.containers import Vertical


class GiocatoreViewWidget(Widget):
    """Widget che mostra le informazioni di un singolo giocatore."""

    def __init__(self, id_giocatore: str):
        super().__init__(id=f"giocatore-widget-{id_giocatore}")
        self._id_giocatore = id_giocatore
        
        # ==============================================================
        # OTTIMIZZAZIONE O(1): Creazione in RAM!
        # Creiamo i widget in memoria e li salviamo. Niente più query_one lenti!
        # Così possiamo aggiornarli anche prima che vengano disegnati a schermo.
        # ==============================================================
        self._lbl_stato = Label(self._id_giocatore, 
                                id=f"label-stato-{self._id_giocatore}", 
                                classes="giocatore-label-stato")
        
        self._lbl_muri = Label("Muri: --", 
                               id=f"label-muri-{self._id_giocatore}", 
                               classes="giocatore-label-muri")
        
        self._lbl_tempo = Label("", 
                                id=f"label-tempo-{self._id_giocatore}", 
                                classes="giocatore-label-tempo")

    def compose(self) -> ComposeResult:
        # Inseriamo nel layout i widget che abbiamo già creato in RAM
        with Vertical(classes="giocatore-box"):
            yield self._lbl_stato
            yield self._lbl_muri
            yield self._lbl_tempo

    def aggiorna_attivo(self, muri_disponibili: int, tempo_formattato: str = None):
        """Evidenzia il giocatore come quello di turno."""
        # Aggiornamento diretto in memoria (0 latenza, 0 crash)
        self._lbl_stato.update(f"► {self._id_giocatore} — TURNO")
        self._lbl_muri.update(f"Muri: {muri_disponibili}")
        self._lbl_tempo.update(f"⏱ {tempo_formattato}" if tempo_formattato else "")
        self.add_class("giocatore-attivo")
        self.remove_class("giocatore-eliminato")

    def aggiorna_info(self, muri_disponibili: int, tempo_formattato: str = None):
        """Mostra il giocatore come in attesa."""
        self._lbl_stato.update(self._id_giocatore)
        self._lbl_muri.update(f"Muri: {muri_disponibili}")
        self._lbl_tempo.update(f"⏱ {tempo_formattato}" if tempo_formattato else "")
        self.remove_class("giocatore-attivo")
        self.remove_class("giocatore-eliminato")

    def aggiorna_eliminato(self, muri_disponibili: int, tempo_formattato: str = None):
        """Mostra il giocatore come eliminato."""
        self._lbl_stato.update(f"✖ {self._id_giocatore} — ELIMINATO")
        self._lbl_muri.update(f"Muri: {muri_disponibili}")
        self._lbl_tempo.update("")
        self.add_class("giocatore-eliminato")
        self.remove_class("giocatore-attivo")