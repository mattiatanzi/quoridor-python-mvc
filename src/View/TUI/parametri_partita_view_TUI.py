# proj-stonebraker/src/View/TUI/parametri_partita_view_TUI.py

import queue
from src.View.parametri_partita_view import ParametriPartitaView
from src.View.TUI.Screen.modalita_partita_Screen import ModalitaPartitaScreen
from src.View.TUI.Screen.imposta_timer_Screen import ImpostaTimerScreen
from textual.widgets import Label

class ParametriPartitaViewTUI(ParametriPartitaView):
    def __init__(self, app_condivisa, coda_input: queue.Queue):
        self.__app = app_condivisa
        self.__coda_input = coda_input

    def get_input_modalita_partita(self, err: str = "") -> str:
        if err.strip():
            self.__app.call_from_thread(self.__app.notify, err.strip(), severity="error")

        def mostra_schermo():
            # Mostra lo schermo SOLO se non ci siamo già sopra!
            if not isinstance(self.__app.screen, ModalitaPartitaScreen):
                self.__app.push_screen(ModalitaPartitaScreen(self.__coda_input))
        
        self.__app.call_from_thread(mostra_schermo)
        return self.__coda_input.get()

    def get_input_limite_tempo(self, err: str = "") -> str:
        if err.strip():
            self.__app.call_from_thread(self.__app.notify, err.strip(), severity="error")

        def mostra_schermo():
            # Mostra lo schermo SOLO se non ci siamo già sopra!
            if not isinstance(self.__app.screen, ImpostaTimerScreen):
                self.__app.push_screen(ImpostaTimerScreen(self.__coda_input))

        self.__app.call_from_thread(mostra_schermo)
        return self.__coda_input.get()

    # Nuova funzione privata per iniettare il testo
    def _mostra_aiuto_laterale(self, messaggio):
        def aggiorna_aiuto():
            try:
                pannello = self.__app.screen.query_one("#pannello-aiuto", Label)
                pannello.update(messaggio)
                pannello.add_class("visibile")
            except Exception:
                self.__app.notify(messaggio, title="Aiuto")
        self.__app.call_from_thread(aggiorna_aiuto)

    def stampa_aiuto_modalita_partita(self):
        messaggio = "=== GUIDA MODALITÀ ===\n\n1 - Con Timer: avrai un limite di tempo\n    per effettuare la mossa.\n2 - Senza Timer: puoi riflettere\n    senza alcun limite.\n0 - Torna al menu principale."
        self._mostra_aiuto_laterale(messaggio)

    def stampa_aiuto_limite_tempo(self):
        messaggio = "=== GUIDA TIMER ===\n\n- Scegli 3 o 5 minuti premendo i tasti.\n- Oppure scrivi manualmente il tempo nel\n  campo di testo (es. 00:10:00 per 10 min)\n  e premi INVIO sulla tastiera.\n- Premi 0 per tornare indietro."
        self._mostra_aiuto_laterale(messaggio)

    def stampa_errore_parametri(self, errore):
        self._mostra_aiuto_laterale(errore)