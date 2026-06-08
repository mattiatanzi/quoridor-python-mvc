from src.Model.parametri_partita import ErroreParametriPartita
from src.View.costanti_quoridor_view import CostantiQuoridorView
from src.View.funzioni_utili_stampa import chiedi_input_utente, pulisci_schermo


class ParametriPartitaView:

    def stampa_errore_parametri(self, errore: ErroreParametriPartita):
        print(f"Errore Parametri:  + {errore}")


    def get_input_modalita_partita(self, err: str = "") -> str:

        pulisci_schermo()

        messaggio = "Selezionare Una Modalità Di Gioco:\n"

        for chiave, descrizione in CostantiQuoridorView._POSSIBILI_SCELTE_MODALITA.items():
            messaggio = messaggio + f"\n{chiave}. {descrizione}\n"

        messaggio = messaggio + err

        return chiedi_input_utente(messaggio)



    def get_input_limite_tempo(self, err: str = "") -> str:

        pulisci_schermo()

        messaggio = "Selezionare Un Limite di Tempo:\n"

        for chiave, descrizione in CostantiQuoridorView._POSSIBILI_TIMER_DEFAULT.items():
            messaggio = messaggio + f"\n{chiave}. {descrizione}\n"

        messaggio = messaggio + CostantiQuoridorView._MESSAGGIO_ALTERNATIVO_SCELTA_TIMER

        messaggio = messaggio + err

        return chiedi_input_utente(messaggio)
