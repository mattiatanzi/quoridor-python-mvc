# proj-stonebraker/src/View/TUI/parametri_partita_view_TUI.py

import queue
from src.View.parametri_partita_view import ParametriPartitaView
from src.View.TUI.Screen.modalita_partita_Screen import ModalitaPartitaScreen
from src.View.TUI.Screen.imposta_timer_Screen import ImpostaTimerScreen

class ParametriPartitaViewTUI(ParametriPartitaView):
    def __init__(self, app_condivisa, coda_input: queue.Queue):
        self.__app = app_condivisa
        self.__coda_input = coda_input

    def get_input_modalita_partita(self, err: str = "") -> str:
        # Se il controller rileva un errore, mostriamo un pop-up
        if err.strip():
            self.__app.call_from_thread(self.__app.notify, err.strip(), severity="error")

        def mostra_schermo():
            self.__app.push_screen(ModalitaPartitaScreen(self.__coda_input))
        
        self.__app.call_from_thread(mostra_schermo)
        
        # Blocca il thread del Controller finché l'utente non interagisce con lo schermo
        return self.__coda_input.get()

    def get_input_limite_tempo(self, err: str = "") -> str:
        if err.strip():
            self.__app.call_from_thread(self.__app.notify, err.strip(), severity="error")

        def mostra_schermo():
            self.__app.push_screen(ImpostaTimerScreen(self.__coda_input))

        self.__app.call_from_thread(mostra_schermo)
        return self.__coda_input.get()

    def stampa_errore_parametri(self, errore):
        self.__app.call_from_thread(self.__app.notify, str(errore), title="Errore", severity="error")

    # I menu di help nella TUI sono superflui perché i bottoni sono autoesplicativi.
    # Evitiamo crash implementando il metodo astratto e mostrando un pop-up se invocato.
    def stampa_aiuto_modalita_partita(self):
        messaggio = "Seleziona 'Partita con Timer' o 'Senza Timer' tramite i bottoni."
        self.__app.call_from_thread(self.__app.notify, messaggio, title="Aiuto")

    def stampa_aiuto_limite_tempo(self):
        messaggio = "Seleziona un tempo predefinito o inserisci un formato valido HH:MM:SS."
        self.__app.call_from_thread(self.__app.notify, messaggio, title="Aiuto")