from abc import ABC, abstractmethod


class QuoridorViewAstratta(ABC):
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
    
    @abstractmethod
    def menu_di_gioco(self):
        pass

    @abstractmethod
    def get_input_menu(self) -> str:
        pass

    @abstractmethod
    def stampa_messaggio(self,messaggio: str):
        pass
