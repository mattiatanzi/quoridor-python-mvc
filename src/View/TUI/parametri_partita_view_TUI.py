import queue

from textual.widgets import Label

from src.View.parametri_partita_view import ParametriPartitaView
from src.View.TUI.Screen.imposta_timer_Screen import ImpostaTimerScreen
from src.View.TUI.Screen.modalita_partita_Screen import ModalitaPartitaScreen
from src.View.TUI.Screen.numero_giocatori_Screen import NumeroGiocatoriScreen


class ParametriPartitaViewTUI(ParametriPartitaView):
    """Implementazione TUI della gestione dei parametri di partita.

    DESCRIZIONE
        Gestisce l'interazione tra il controller e l'interfaccia TUI per la
        selezione dei parametri di gioco (modalità partita, numero giocatori,
        limite di tempo). Utilizza una coda condivisa per sincronizzare input
        asincroni provenienti dall'interfaccia Textual.

    ATTRIBUTI
        __app
            Riferimento all'applicazione Textual condivisa.

        __coda_input : queue.Queue
            Coda condivisa per la comunicazione tra UI e controller.

    METODI

        def get_input_modalita_partita(self, err: str = "") -> str:
            DESCRIZIONE
                Mostra lo schermo per la selezione della modalità di partita
                e attende l'input dell'utente.

        def get_input_limite_tempo(self, err: str = "") -> str:
            DESCRIZIONE
                Mostra lo schermo per la selezione del limite di tempo
                e attende l'input dell'utente.

        def get_input_numero_giocatori(self) -> str:
            DESCRIZIONE
                Mostra lo schermo per la selezione del numero di giocatori
                e attende l'input dell'utente.

        def stampa_aiuto_modalita_partita(self):
            DESCRIZIONE
                Mostra la guida relativa alla modalità di partita.

        def stampa_aiuto_limite_tempo(self):
            DESCRIZIONE
                Mostra la guida relativa al limite di tempo.

        def stampa_aiuto_numero_giocatori(self):
            DESCRIZIONE
                Mostra la guida relativa al numero di giocatori.

        def stampa_errore_parametri(self, errore):
            DESCRIZIONE
                Mostra un messaggio di errore relativo ai parametri della partita.
    """
    
    def __init__(self, app_condivisa, coda_input: queue.Queue):
        self.__app = app_condivisa
        self.__coda_input = coda_input

    def get_input_modalita_partita(self, err: str = "") -> str:
        if err.strip():
            self.__app.call_from_thread(
                self.__app.notify, err.strip(), severity="error"
            )

        def mostra_schermo():
            # Mostra lo schermo SOLO se non ci siamo già sopra!
            if not isinstance(self.__app.screen, ModalitaPartitaScreen):
                self.__app.push_screen(ModalitaPartitaScreen(self.__coda_input))

        self.__app.call_from_thread(mostra_schermo)
        return self.__coda_input.get()

    def get_input_limite_tempo(self, err: str = "") -> str:
        if err.strip():
            self.__app.call_from_thread(
                self.__app.notify, err.strip(), severity="error"
            )

        def mostra_schermo():
            # Mostra lo schermo SOLO se non ci siamo già sopra!
            if not isinstance(self.__app.screen, ImpostaTimerScreen):
                self.__app.push_screen(ImpostaTimerScreen(self.__coda_input))

        self.__app.call_from_thread(mostra_schermo)
        return self.__coda_input.get()

    def get_input_numero_giocatori(self) -> str:
        """Mostra il menu per la scelta 2 o 4 giocatori e attende l'input."""

        # Spinge lo schermo nella UI dal thread del controller
        def _mostra_schermo_giocatori():
            self.__app.push_screen(NumeroGiocatoriScreen(self.__coda_input))

        self.__app.call_from_thread(_mostra_schermo_giocatori)

        # Attende che l'utente prema un bottone sullo schermo ("2", "4", "0" o "help")
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
        messaggio = "=== GUIDA MODALITÀ ===\n\n - Con Timer: avrai un limite di tempo\n    per effettuare la mossa.\n - Senza Timer: puoi riflettere\n    senza alcun limite.\n - Torna al menu principale."
        self._mostra_aiuto_laterale(messaggio)

    def stampa_aiuto_limite_tempo(self):
        messaggio = "=== GUIDA TIMER ===\n\n- Scegli 3 o 5 minuti premendo i tasti.\n- Oppure scrivi manualmente il tempo nel\n  campo di testo (es. 00:10:00 per 10 min)\n  e premi INVIO sulla tastiera.\n- Premi Torna indietro per tornare indietro."
        self._mostra_aiuto_laterale(messaggio)

    def stampa_errore_parametri(self, errore):
        self._mostra_aiuto_laterale(errore)

    def stampa_aiuto_numero_giocatori(self):
        messaggio = "=== GUIDA GIOCATORI ===\n\n- 2 Giocatori: Partita 1 vs 1.\n  Ogni giocatore ha 10 muri.\n- 4 Giocatori: Tutti contro Tutti.\n  Ogni giocatore ha 5 muri.\n- Torna al menu principale."
        self._mostra_aiuto_laterale(messaggio)
