from src.View.costanti_quoridor_view import CostantiQuoridorView
from src.View.funzioni_utili_stampa import chiedi_input_utente, pulisci_schermo
from src.View.quoridor_view import QuoridorViewAstratta


class QuoridorViewCLI(QuoridorViewAstratta):
    """Stampa del menu di base.

    Metodi
    ------
    nome: menu_base:
        Permette di stampare la base del menu che è solo visiva

    nome: menu_di_gioco:
        Permette di stampare il menu di base e restituisce l'input che riceve
        dall'utente

    nome: stampa_messaggio:
        Permette di stampare un messaggio nella fase di menu
    """

    def __menu_base(self):
        pulisci_schermo()
        print("Benvenuto in Quoridor \n")
        print("1 - Avvia una nuova partita \n")
        print("0 - Esci dal gioco \n")

        print("h - Aiuto (Comandi di gioco) \n")

    def menu_di_gioco(self):
        self.__menu_base()

    def get_input_menu(self) -> str:
        return chiedi_input_utente("Seleziona un'opzione:")

    def stampa_messaggio(self, messaggio: str):
        print(messaggio)

    def get_input_modalita_partita(self) -> str:
        pulisci_schermo()

        messaggio = "Selezionare Una Modalità Di Gioco:\n"

        for (
            chiave,
            descrizione,
        ) in CostantiQuoridorView.POSSIBILI_SCELTE_MODALITA.items():
            messaggio = messaggio + f"\n{chiave}. {descrizione}\n"

    def get_input_limite_tempo(self) -> str:
        pulisci_schermo()

        messaggio = "Selezionare Un Limite di Tempo:"

        for chiave, descrizione in CostantiQuoridorView.POSSIBILI_TIMER_DEFAULT.items():
            messaggio = messaggio + f"\n{chiave}. {descrizione}\n"

        messaggio = messaggio + CostantiQuoridorView.MESSAGGIO_ALTERNATIVO_SCELTA_TIMER

        return chiedi_input_utente(messaggio)

    def is_tui(self) -> bool:
        return False

    def get_app(self):
        pass

    def get_coda_input(self):
        pass
