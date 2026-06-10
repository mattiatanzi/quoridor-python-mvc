from textual.app import ComposeResult
from textual.widget import Widget 
from textual.widgets import Button, Label
from textual.containers import Grid

class TavoliereViewWidget(Widget):
    def compose(self) -> ComposeResult:
        # Creiamo una griglia
        with Grid(id="griglia-tavoliere"):
            
            # Riga lettere in alto
            yield Label("") 
            for lettera in "abcdefghi":
                yield Label(lettera)
                
            # Righe del tabellone (da 9 a 1)
            for riga in range(9, 0, -1):
                yield Label(str(riga)) # Numero a sinistra
                
                for colonna in "abcdefghi":
                    # Il bottone giocabile! Gli diamo un ID come "btn_e1"
                    yield Button("", id=f"btn_{colonna}{riga}", classes="casella")