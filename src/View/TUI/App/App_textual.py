import queue  # Aggiunto perché così non andiamo a rompere l'input richiesto in fase 

# di gioco, infatti vengono salvati in una coda i comandi eseguiti
from textual.app import App

from src.View.TUI.Screen.quoridor_view_Screen import QuoridorViewScreen
from src.View.TUI.Screen.partita_view_Screen import PartitaViewScreen

class QuoridorViewApp(App):
    """Gestisce cosa viene mostrato a video, ossia quale screen.

    DESCRIZIONE
        Gestisce la logica di visualizzazione della TUI e la gestione degli screen.

    METODI

        def __init__(self, coda_input: queue.Queue, **kwargs):
            DESCRIZIONE
                Inizializza l'app TUI e salva la coda degli input.

        def on_mount(self):
            DESCRIZIONE
                Imposta lo screen iniziale quando l'app viene avviata.

        def invia_comando(self, comando: str):
            DESCRIZIONE
                Inserisce un comando nella coda input per essere processato dal gioco.

        def mostra_schermo_partita(self, ids_giocatori: list[str]) -> None:
            DESCRIZIONE
                Mostra lo screen della partita.

        def torna_al_menu(self):
            DESCRIZIONE
                Chiude lo screen della partita tornando al menu.

        def get_coda_input(self):
            DESCRIZIONE
                Restituisce la coda degli input della TUI.
    """

    CSS_PATH = "stile_quoridor_view_TUI.tcss"

    def __init__(self, coda_input: queue.Queue, **kwargs):
        super().__init__(**kwargs)
        self.__coda_input = coda_input

    def on_mount(self):
        self.push_screen(QuoridorViewScreen())
    
    def invia_comando(self, comando: str):
        self.__coda_input.put(comando)

    def mostra_schermo_partita(self, ids_giocatori: list[str]) -> None:
        self.push_screen(PartitaViewScreen(self.__coda_input, ids_giocatori))
        
    def torna_al_menu(self):
        """Chiude lo schermo della partita rivelando nuovamente il menu."""
        self.pop_screen()

    def get_coda_input(self):
        return self.__coda_input