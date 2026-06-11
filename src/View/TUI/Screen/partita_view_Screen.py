import queue
from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Header, Footer, Input, Label, Button
from textual.containers import Horizontal, Vertical


from src.View.TUI.Widget.giocatore_view_Widget import GiocatoreViewWidget
from src.View.TUI.Static.tavoliere_view_Static import TavoliereViewStatic


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
            
            # --- SINISTRA: Pannello Giocatori ---
            with Vertical(id="pannello-giocatori"):
                yield Label("— GIOCATORI —", id="label-titolo-giocatori")
                
                for id_g in self._ids_giocatori:
                    yield GiocatoreViewWidget(id_g)

                yield Label("", id="label-errore-partita", classes="label-errore")
                yield Label("Oppure scrivi mossa:", id="label-input-hint")
                # Lasciamo l'input testuale per sicurezza o per comodità
                yield Input(placeholder="es. e5 / e5h", id="input-mossa")

            # --- DESTRA: Area di Gioco e Bottoni ---
            with Vertical(id="area-gioco"):
                # Il nuovo tavoliere super interattivo!
                yield TavoliereViewStatic(self._coda_input)
                
                # I pulsanti in basso a destra
                with Horizontal(id="azioni-partita"):
                    yield Button("Mostra Aiuto", id="btn-aiuto", variant="primary")
                    yield Button("Resa / Abbandona", id="btn-abbandona", variant="warning")
                    yield Button("Esci dal Gioco", id="btn-esci-partita", variant="error")
            yield Label("", id="pannello-aiuto")
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed):
        """Gestisce tutti i tasti del menu inferiore della partita."""
        id_premuto = event.button.id
        
        if id_premuto == "btn-abbandona":
            self._coda_input.put("resa")
            
        elif id_premuto == "btn-esci-partita":
            self._coda_input.put("0")
            
        elif id_premuto == "btn-aiuto":
            # GESTIONE TOGGLE AIUTO
            pannello = self.query_one("#pannello-aiuto", Label)
            
            if pannello.has_class("visibile"):
                # Se è già aperto, nascondiamolo noi
                pannello.remove_class("visibile")
                event.button.label = "Mostra Aiuto"
            else:
                # Se è chiuso, inviamo 'h' al controller.
                # Il controller valuterà 'h' e chiamerà 'stampa_aiuto' passandoci il testo corretto!
                self._coda_input.put("help")

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