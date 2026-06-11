from src.Model.parametri_partita import ErroreParametriPartita
from src.View.costanti_quoridor_view import CostantiQuoridorView
from abc import ABC, abstractmethod


class ParametriPartitaView(ABC):
    """Classe ParametriPartitaView.

    DESCRIZIONE
        Classe che gestisce stampa e input per ParametriPartita

    METODI

        def stampa_errore_parametri(self, errore: ErroreParametriPartita):
            DESCRIZIONE
                Stampa un errore riguardante i parametri della partita

        def get_input_modalita_partita(self, err: str = "") -> str:
            DESCRIZIONE
                

        def get_input_limite_tempo(self, err: str = "") -> str:
            DESCRIZIONE
               


    """

    @abstractmethod
    def stampa_errore_parametri(self, errore: ErroreParametriPartita):
        pass

    @abstractmethod
    def get_input_modalita_partita(self, err: str = "") -> str:
        pass

    @abstractmethod
    def get_input_limite_tempo(self, err: str = "") -> str:
        pass


<<<<<<< HEAD
    @abstractmethod
=======

    def get_input_numero_giocatori(self, err: str = "") -> str:
        pulisci_schermo()

        menu = "Selezionare Numero di Giocatori:\n"

        for (
            chiave,
            descrizione,
        ) in CostantiQuoridorView.POSSIBILI_NUMERO_GIOCATORI.items():
            menu = menu + f"\n{chiave}. {descrizione}\n"

        menu = menu + "Digitare `help` o `aiuto` per una breve guida"

        menu = menu + err

        return chiedi_input_utente(menu)

>>>>>>> 6d9a636516865b3a03b90713dd0743eff8592fb4
    def stampa_aiuto_modalita_partita(self):
        pass

    @abstractmethod
    def stampa_aiuto_limite_tempo(self):
<<<<<<< HEAD
        pass
=======
        pulisci_schermo()

        aiuto = f"""

        -- AIUTO SCELTA LIMITE TEMPO --

        In questo menu potrai selezionare quale limite di tempo usare nella
        partita.

        Per selezionare una partita limite di tempo: {
            CostantiQuoridorView.POSSIBILI_TIMER_DEFAULT[
                CostantiQuoridorView.SCELTA_TIMER_DEFAULT_1
            ]
        }, digitare:
            "{CostantiQuoridorView.SCELTA_TIMER_DEFAULT_1}"

        Altrimenti, se si vuole usare un limite di tempo {
            CostantiQuoridorView.POSSIBILI_TIMER_DEFAULT[
                CostantiQuoridorView.SCELTA_TIMER_DEFAULT_1
            ]
        }, digitare:
            "{CostantiQuoridorView.SCELTA_TIMER_DEFAULT_2}"

        Infine, per usare un limite di tempo personalizzato,
        digitarlo nel formato HH:MM:SS\n

        Per tornare indietro, digitare:
            "{CostantiQuoridorView.SCELTA_TORNA_INDIETRO}"
        """
        # Questa notazione fa una stampa di color blu
        print(f"\033[94m{aiuto}\033[0m")


    def stampa_aiuto_numero_giocatori(self):
        pulisci_schermo()

        aiuto = f"""

        -- AIUTO SCELTA NUMERO GIOCATORI --

        In questo menu potrai selezionare quanti giocatori introdurre in
        partita.

        Per selezionare 2 Giocatori, digitare:
            "{CostantiQuoridorView.SCELTA_2_GIOCATORI}"

        Altrimenti, se si vuole giocare con 4 Giocatori, digitare:
            "{CostantiQuoridorView.SCELTA_4_GIOCATORI}"

        Per tornare indietro, digitare:
            "{CostantiQuoridorView.SCELTA_TORNA_INDIETRO}"

        """
        # Questa notazione fa una stampa di color blu
        print(f"\033[94m{aiuto}\033[0m")
>>>>>>> 6d9a636516865b3a03b90713dd0743eff8592fb4
