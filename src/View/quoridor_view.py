from abc import ABC, abstractmethod
from src.View.TUI.App.App_textual import QuoridorViewApp

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

    @abstractmethod
    def is_tui(self) -> bool:
        pass

    @abstractmethod
    def get_app(self) -> QuoridorViewApp:
        return self.__app    

    @abstractmethod
    def get_coda_input(self):
        return self.__coda_input
