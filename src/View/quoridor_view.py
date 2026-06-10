from abc import ABC, abstractmethod


class QuoridorViewAstratta(ABC):
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
    
    @abstractmethod
    def menu_di_gioco(self):
        pass

    @abstractmethod
    def get_input_menu(self) -> str:
        pass

    @abstractmethod
    def stampa_messaggio(self,messaggio: str):
        pass
