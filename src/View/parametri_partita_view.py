from src.Model.parametri_partita import ErroreParametriPartita
from src.View.costanti_quoridor_view import CostantiQuoridorView
from src.View.funzioni_utili_stampa import chiedi_input_utente, pulisci_schermo


class ParametriPartitaView:
    """Classe ParametriPartitaView.

    DESCRIZIONE
        Classe che gestisce stampa e input per ParametriPartita

    METODI

        def stampa_errore_parametri(self, errore: ErroreParametriPartita):
            DESCRIZIONE
                Stampa un errore riguardante i parametri della partita

        def get_input_modalita_partita(self, err: str = "") -> str:
            DESCRIZIONE
                Stampa interfaccia per chiedere la modalità di partita
                (con timer o senza timer)
                Restituisce una scelta.
                Eventualmente è possibile passare una stringa di errore da mostrare
                per aiutare l'utente a inserire il giusto input

        def get_input_limite_tempo(self, err: str = "") -> str:
            DESCRIZIONE
                Stampa interfaccia per chiedere quale limite di tempo usare in partita
                (2 limiti tempo di default + tempo personalizzato)
                Restituisce una scelta.
                Eventualmente è possibile passare una stringa di errore da mostrare
                per aiutare l'utente a inserire il giusto input.
                In caso di tempo personalizzato, l'utente deve inserire
                il tempo nel formato: "HH:MM:SS"


    """

    def stampa_errore_parametri(self, errore: ErroreParametriPartita):
        print(f"Errore Parametri:  {errore}")

    def get_input_modalita_partita(self, err: str = "") -> str:
        pulisci_schermo()

        messaggio = "Selezionare Una Modalità Di Gioco:\n"

        for (
            chiave,
            descrizione,
        ) in CostantiQuoridorView.POSSIBILI_SCELTE_MODALITA.items():
            messaggio = messaggio + f"\n{chiave}. {descrizione}\n"

        messaggio = messaggio + "\nDigitare `help` o `aiuto` per una breve guida"

        messaggio = messaggio + err

        return chiedi_input_utente(messaggio)

    def get_input_limite_tempo(self, err: str = "") -> str:
        pulisci_schermo()

        messaggio = "Selezionare Un Limite di Tempo:\n"

        for chiave, descrizione in CostantiQuoridorView.POSSIBILI_TIMER_DEFAULT.items():
            messaggio = messaggio + f"\n{chiave}. {descrizione}\n"

        messaggio = messaggio + CostantiQuoridorView.MESSAGGIO_ALTERNATIVO_SCELTA_TIMER

        messaggio = messaggio + "Digitare `help` o `aiuto` per una breve guida"

        messaggio = messaggio + err

        return chiedi_input_utente(messaggio)


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

    def stampa_aiuto_modalita_partita(self):
        pulisci_schermo()

        aiuto = f"""

        -- AIUTO SCELTA MODALITA --

        In questo menu potrai selezionare se giocare una partita con timer o senza.

        Per selezionare una partita con timer, premere:
            "{CostantiQuoridorView.SCELTA_PARTITA_CON_TIMER}"

        Altrimenti premere:
            "{CostantiQuoridorView.SCELTA_PARTITA_SENZA_TIMER}"

        Per tornare indietro, premere:
            "{CostantiQuoridorView.SCELTA_TORNA_INDIETRO}"

        """
        # Questa notazione fa una stampa di color blu
        print(f"\033[94m{aiuto}\033[0m")

    def stampa_aiuto_limite_tempo(self):
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
        digitarlo nel formato HH:MM:SS

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
