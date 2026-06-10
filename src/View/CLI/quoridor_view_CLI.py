from src.View.pulisci_schermo_view import pulisci_schermo
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
        return input("Seleziona un'opzione: ")

    def stampa_messaggio(self, messaggio: str):
        print(messaggio)
