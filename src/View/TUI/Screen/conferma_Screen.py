from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual.screen import ModalScreen
from textual.widgets import Button, Label

from src.View.costanti_quoridor_view import CostantiQuoridorView


class ConfermaScreen(ModalScreen):
    """Popup di conferma per azioni critiche.

    DESCRIZIONE
        Mostra una finestra modale che richiede una conferma esplicita
        da parte dell'utente tramite scelta SI/NO.

    METODI

        def __init__(self, messaggio: str, coda_input, **kwargs):
            DESCRIZIONE
                Inizializza la schermata di conferma e prepara il messaggio
                da visualizzare all'utente.

        def compose(self) -> ComposeResult:
            DESCRIZIONE
                Crea e visualizza l'interfaccia grafica del popup di conferma.

        def on_button_pressed(self, event: Button.Pressed) -> None:
            DESCRIZIONE
                Gestisce la risposta dell'utente e inserisce il comando
                nella coda input, chiudendo la schermata.
    """

    def __init__(self, messaggio: str, coda_input, **kwargs):
        super().__init__(**kwargs)
        # Rimuove il fastidioso "[si/no]" dal testo per renderlo più bello
        self._messaggio = messaggio.replace("[si/no]", "").strip()
        self._coda_input = coda_input

    def compose(self) -> ComposeResult:
        with Vertical(id="pannello-crash"):  # Ricicliamo lo stile scuro del crash
            yield Label(self._messaggio, id="titolo-crash")

            with Horizontal(id="azioni-partita"):
                # Mettiamo i due bottoni
                yield Button(
                    f"{CostantiQuoridorView.NO_ANNULLA}",
                    id="btn-no",
                    variant="primary",
                    classes="btn-menu",
                )
                yield Button(
                    f"{CostantiQuoridorView.SI_CONFERMA}",
                    id="btn-si",
                    variant="error",
                    classes="btn-menu",
                )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        # Mette in coda la risposta finta come se l'utente l'avesse scritta da tastiera!
        if event.button.id == "btn-si":
            testo_domanda = self._messaggio.lower()

            # Se la domanda parla di uscire dal gioco/partita
            if "uscir" in testo_domanda or "esci" in testo_domanda:
                self._coda_input.put("si_uscita")
            else:
                # Per tutti gli altri casi (es. "Vuoi davvero abbandonare la partita?")
                self._coda_input.put("si")
        else:
            self._coda_input.put("no")

        self.app.pop_screen()
