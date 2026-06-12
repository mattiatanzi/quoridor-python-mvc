import queue # Aggiunto perché così non andiamo a rompere l'input richiesto in fase 
# di gioco, infatti vengono salvati in una coda i comandi eseguiti
from src.View.quoridor_view import QuoridorViewAstratta
from src.View.TUI.App.App_textual import QuoridorViewApp
from textual.widgets import Label

class QuoridorViewTUI(QuoridorViewAstratta):
    """Classe TUI che gestisce l'interfaccia Textual.

    DESCRIZIONE
        Gestisce l'intera interfaccia TUI del gioco Quoridor,
        utilizzando una coda per comunicare con il controller
        e una App Textual per la gestione degli schermi.

    METODI

        def __init__(self):
            DESCRIZIONE
                Crea la coda degli input e inizializza la Textual App.

        def menu_di_gioco(self):
            DESCRIZIONE
                Non utilizzato nella TUI perché il menu è sempre
                gestito dagli Screen.

        def get_input_menu(self) -> str:
            DESCRIZIONE
                Restituisce un input dalla coda, bloccando il controller
                fino a interazione dell'utente.

        def stampa_messaggio(self, messaggio: str):
            DESCRIZIONE
                Mostra un messaggio nella UI tramite pannello laterale
                o notifica di fallback.

        def avvia_gui(self):
            DESCRIZIONE
                Avvia il motore grafico Textual.

        def get_app(self) -> QuoridorViewApp:
            DESCRIZIONE
                Restituisce l'istanza dell'app Textual.

        def get_coda_input(self):
            DESCRIZIONE
                Restituisce la coda condivisa tra UI e controller.

        def is_tui(self) -> bool:
            DESCRIZIONE
                Indica che questa implementazione è TUI.
    """
    
    def __init__(self):
        self.__coda_input = queue.Queue()
        self.__app = QuoridorViewApp(coda_input=self.__coda_input)
    
    def menu_di_gioco(self):
        pass 

    def get_input_menu(self):
        return self.__coda_input.get()
    
    def stampa_messaggio(self, messaggio):
        if messaggio.strip():
            def aggiorna_aiuto():
                try:
                    # Cerca il pannello a destra e ci inietta il testo dell'aiuto
                    pannello = self.__app.screen.query_one("#pannello-aiuto", Label)
                    pannello.update(messaggio)
                    pannello.add_class("visibile") # Lo fa apparire
                except Exception:
                    self.__app.notify(messaggio) # Fail-safe se il widget non si trova
            
            self.__app.call_from_thread(aggiorna_aiuto)

    def avvia_gui(self):
        self.__app.run()

    def get_app(self) -> QuoridorViewApp:
        return self.__app    

    def get_coda_input(self):
        return self.__coda_input

    
    def is_tui(self) -> bool:
        return True