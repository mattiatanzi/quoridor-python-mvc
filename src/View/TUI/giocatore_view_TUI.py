from src.View.giocatore_view import GiocatoreViewAstratta
from src.View.TUI.Widget.giocatore_view_Widget import GiocatoreViewWidget


class GiocatoreViewTUI(GiocatoreViewAstratta):
    """Implementazione TUI della view del giocatore.

    Non stampa nulla direttamente: aggiorna i GiocatoreWidget
    già montati nella screen corrente tramite call_from_thread.

    ATTRIBUTI
        _app : QuoridorViewApp
            Riferimento all'app Textual condivisa

    METODI
        stampa_giocatore_attivo(id, muri_disponibili, tempo_formattato)
            Evidenzia il widget del giocatore di turno

        stampa_info_giocatore(id, muri_disponibili, tempo_formattato)
            Aggiorna il widget del giocatore in attesa

        stampa_giocatore_eliminato(id, muri_disponibili, tempo_formattato)
            Segna il widget del giocatore come eliminato

        stampa_errore_giocatore(messaggio)
            Mostra una notifica di errore tramite l'app
    """

    def __init__(self, app_condivisa):
        self._app = app_condivisa

    def _get_widget(self, id_giocatore: str) -> GiocatoreViewWidget | None:
        """Recupera il GiocatoreWidget dalla screen corrente."""
        try:
            return self._app.screen.query_one(
                f"#giocatore-widget-{id_giocatore}", GiocatoreViewWidget
            )
        except Exception:
            return None

    def stampa_giocatore_attivo(self, id, muri_disponibili, tempo_formattato=None):
        def _aggiorna():
            widget = self._get_widget(id)
            if widget:
                widget.aggiorna_attivo(muri_disponibili, tempo_formattato)
        self._app.call_from_thread(_aggiorna)

    def stampa_info_giocatore(self, id, muri_disponibili, tempo_formattato=None):
        def _aggiorna():
            widget = self._get_widget(id)
            if widget:
                widget.aggiorna_info(muri_disponibili, tempo_formattato)
        self._app.call_from_thread(_aggiorna)

    def stampa_giocatore_eliminato(self, id, muri_disponibili, tempo_formattato=None):
        def _aggiorna():
            widget = self._get_widget(id)
            if widget:
                widget.aggiorna_eliminato(muri_disponibili, tempo_formattato)
        self._app.call_from_thread(_aggiorna)

    def stampa_id_giocatore(self, id_giocatore):
        pass  # Non necessario nella TUI, l'id è già nel widget

    def stampa_errore_giocatore(self, messaggio):
        self._app.call_from_thread(self._app.notify, messaggio, severity="error")

    
    def is_tui(self) -> bool:
        return True