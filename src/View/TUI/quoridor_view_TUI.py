import queue # Aggiunto perché così non andiamo a rompere l'input richiesto in fase 
# di gioco, infatti vengono salvati in una coda i comandi eseguiti
from src.View.quoridor_view import QuoridorViewAstratta
from src.View.TUI.App.App_textual import QuoridorViewApp

class QuoridorViewTUI(QuoridorViewAstratta):
    """Classe TUI che gestisce l'interfaccia TUI.
    
    def __init__(self):
        DESCRIZIONE
        Crea una coda e crea un App per la gestione dell'interfaccia 
        Textual
    
    def menu_di_gioco(self):
        DESCRIZIONE
        Non serve in quanto il menu è sempre visibile quindi non necessita 
        di ristampa

    def get_input_menu(self) -> str:
        DESCRIZIONE
        Si mette in attesa sulla coda, così quando il controller richiamerà questa 
        funzione e si sta usando un interfaccia Textual il controller si blocca
        qui finché non viene premuto un pulsante
    
    def stampa_messaggio(self, messaggio: str):
        DESCRIZIONE
        Fa comparire un pop-up su Textual. Si usa un metodo call_from_thred
        perché l'interfaccia girerà su un thread diverso da quello principale

    def avvia_gui(self):
        DESCRIZIONE
        Fa partire il motore grafico
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
            self.__app.call_from_thread(self.__app.notify, messaggio)
    
    def avvia_gui(self):
        self.__app.run()

    def get_app(self) -> QuoridorViewApp:
        return self.__app    

    def get_coda_input(self):
        return self.__coda_input

    
    def is_tui(self) -> bool:
        return True