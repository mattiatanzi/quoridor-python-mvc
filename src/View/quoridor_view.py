from abc import ABC, abstractmethod
from src.View.TUI.App.App_textual import QuoridorViewApp

class QuoridorViewAstratta(ABC):
    """Classe QuoridorViewAstratta.

    DESCRIZIONE
        Interfaccia per la gestione della visualizzazione del menu principale
        e dell'interazione con l'utente.

    METODI

        menu_di_gioco()
            DESCRIZIONE
                Mostra il menu principale.

        get_input_menu() -> str
            DESCRIZIONE
                Richiede una scelta dall'utente nel menu principale.

        stampa_messaggio(messaggio: str)
            DESCRIZIONE
                Mostra un messaggio all'utente.

        is_tui() -> bool
            DESCRIZIONE
                Indica se la view utilizza una interfaccia TUI.

        get_app()
            DESCRIZIONE
                Restituisce l'applicazione TUI associata alla view.

        get_coda_input()
            DESCRIZIONE
                Restituisce la coda degli input utilizzata dalla view.
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
