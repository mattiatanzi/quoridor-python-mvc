from textual.app import ComposeResult
from textual.screen import ModalScreen
from textual.widgets import Button, Label
from textual.containers import Vertical, Horizontal

class ConfermaScreen(ModalScreen):
    """Un popup oscurante che obbliga l'utente a scegliere SI o NO."""
    
    def __init__(self, messaggio: str, coda_input, **kwargs):
        super().__init__(**kwargs)
        # Rimuove il fastidioso "[si/no]" dal testo per renderlo più bello
        self._messaggio = messaggio.replace("[si/no]", "").strip()
        self._coda_input = coda_input

    def compose(self) -> ComposeResult:
        with Vertical(id="pannello-crash"): # Ricicliamo lo stile scuro del crash
            yield Label(self._messaggio, id="titolo-crash")
            
            with Horizontal(id="azioni-partita"):
                # Mettiamo i due bottoni
                yield Button("NO, Annulla", id="btn-no", variant="primary")
                yield Button("SÌ, Conferma", id="btn-si", variant="error")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        # Mette in coda la risposta finta come se l'utente l'avesse scritta da tastiera!
        if event.button.id == "btn-si":
            self._coda_input.put("si_uscita")
        else:
            self._coda_input.put("no")
            
        self.app.pop_screen()