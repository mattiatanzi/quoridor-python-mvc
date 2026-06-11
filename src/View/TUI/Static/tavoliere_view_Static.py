from textual.app import ComposeResult
from textual.widgets import Static, Button, Label
from textual.containers import Grid, Horizontal, Vertical

class TavoliereViewStatic(Static):
    """Il Widget puro che disegna il tabellone 17x17 e le coordinate esterne."""

    def __init__(self, coda_input, **kwargs):
        super().__init__(**kwargs)
        self._coda_input = coda_input

    def compose(self) -> ComposeResult:
        colonne = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
        
        with Vertical(id="contenitore-tavoliere-completo"):
            
            # --- 1. RIGA LETTERE (Spostata in alto) ---
            with Horizontal(id="riga-lettere"):
                for col in colonne:
                    yield Label(col, classes="label-lettera")
                    
            with Horizontal(id="fascia-centrale"):
                # --- 2. COLONNA NUMERI (a sinistra) ---
                with Vertical(id="colonna-numeri"):
                    for riga in range(9, 0, -1):
                        yield Label(str(riga), classes="label-numero")
                        
                # --- 3. LA GRIGLIA GIOCABILE ---
                with Grid(id="griglia-tavoliere"):
                    for riga in range(9, 0, -1):
                        
                        # RIGA DISPARI: Caselle e Muri Verticali
                        for c_idx, col in enumerate(colonne):
                            yield Button("", id=f"btn-{col}{riga}", classes="casella")
                            if c_idx < 8:
                                yield Button("", id=f"btn-{col}{riga}v", classes="muro-v")
                        
                        # RIGA PARI: Muri Orizzontali e Intersezioni
                        if riga > 1:
                            for c_idx, col in enumerate(colonne):
                                yield Button("", id=f"btn-{col}{riga}h", classes="muro-h")
                                if c_idx < 8:
                                    yield Static("", id=f"int-{col}{riga}", classes="intersezione")

    def on_button_pressed(self, event: Button.Pressed):
        """Cattura il click su QUALSIASI cosa (casella o lineetta) e lo invia al controller."""
        id_premuto = event.button.id
        if id_premuto and id_premuto.startswith("btn-"):
            mossa = id_premuto.replace("btn-", "")
            self._coda_input.put(mossa)