import queue
from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Header, Footer, Input, Label
from textual.containers import Horizontal, Vertical

from src.View.TUI.Widget.giocatore_view_Widget import GiocatoreViewWidget
from src.View.TUI.Widget.tavoliere_view_Widget import TavoliereViewWidget


class PartitaViewScreen(Screen):
    """Screen principale della partita.

    Compone in un layout orizzontale:
    - Pannello sinistro: info giocatori + campo input
    - Centro:           griglia tavoliere
    
    La coda viene passata dal costruttore, coerentemente
    con il pattern già usato in QuoridorViewApp.

    ATTRIBUTI
        _coda_input : queue.Queue
            Coda condivisa con il controller per ricevere i comandi

        _ids_giocatori : list[str]
            Lista degli id giocatori (es. ["P1","P2"]) necessaria
            per montare il numero corretto di GiocatoreWidget

    METODI
        compose()
            Costruisce il layout della screen

        on_button_pressed(event)
            Gestisce il click sulle caselle del tavoliere,
            traducendolo in un comando nella coda

        on_input_submitted(event)
            Gestisce l'invio del campo di testo,
            mettendo il testo nella coda e svuotando il campo

        aggiorna_label_errore(messaggio)
            Aggiorna il label errore nella screen
    """

    def __init__(self, coda_input: queue.Queue, ids_giocatori: list[str]):
        super().__init__()
        self._coda_input = coda_input
        self._ids_giocatori = ids_giocatori

    def compose(self) -> ComposeResult:
        yield Header()

        with Horizontal(id="partita-container"):

            # Pannello sinistro: giocatori + input
            with Vertical(id="pannello-laterale"):
                yield Label("— Giocatori —", id="label-titolo-giocatori")

                # Monta un GiocatoreWidget per ogni giocatore
                for id_g in self._ids_giocatori:
                    yield GiocatoreViewWidget(id_g)

                yield Label("", id="label-errore-partita", classes="label-errore")
                yield Label("Fai la tua mossa:", id="label-input-hint")
                yield Input(placeholder="es. e5 oppure e5h", id="input-mossa")

            # Centro: tavoliere
            yield TavoliereViewWidget()

        yield Footer()

    def on_button_pressed(self, event):
        """Click su una casella del tavoliere → manda la coordinata nella coda."""
        btn_id = event.button.id  # es. "btn_e5"
        if btn_id and btn_id.startswith("btn_"):
            coordinata = btn_id.replace("btn_", "")  # es. "e5"
            self._coda_input.put(coordinata)
            event.stop()  # non propaga al livello superiore

    def on_input_submitted(self, event):
        """Invio del campo testo → manda il comando nella coda e svuota il campo."""
        comando = event.value.strip().lower()
        self._coda_input.put(comando)
        self.query_one("#input-mossa", Input).value = ""

    def aggiorna_label_errore(self, messaggio: str):
        try:
            self.query_one("#label-errore-partita", Label).update(messaggio)
        except Exception:
            pass