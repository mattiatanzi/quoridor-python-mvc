from src.View.costanti_quoridor_view import CostantiQuoridorView
from src.View.funzioni_utili_stampa import chiedi_input_utente, pulisci_schermo


class QuoridorView:
    """Stampa del menu di base.

    Metodi
    ------
    def __menu_base(self):
        Permette di stampare la base del menu che è solo visiva

    def menu_di_gioco(self):
        Permette di stampare il menu di base e restituisce l'input che riceve
        dall'utente

    def stampa_messaggio(self, messaggio: str):
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
        return input("Seleziona un'opzione: ")

    def stampa_messaggio(self, messaggio: str):
        print(messaggio)
