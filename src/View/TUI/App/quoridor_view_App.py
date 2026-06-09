import queue  # Aggiunto perché così non andiamo a rompere l'input richiesto in fase 

# di gioco, infatti vengono salvati in una coda i comandi eseguiti
from textual.app import App

from src.View.TUI.Screen.quoridor_view_Screen import QuoridorViewScreen


class QuoridorViewApp(App):
    """Gestice cosa viene mostrato a video, ossia quale screen.

    def __init__(self, coda_input: queue.Queue, **kwargs):
        DESCRIZIONE

    def on_mount(self):
        DESCRIZIONE
        Dice quale schermo deve essere mostrato appena creato un oggetto di tipo
        QuoridorViewApp

    def invia_comando(self, comando: str):
        DESCRIZIONE
        Memorizza il comando premuto nella TUI in modo tale da poterlo
        utilizzare successivamente per poter procedere nel gioco, questo ci permette di
        non andare a modificare tutti i metodi già precedentemente creati
    """

    CSS_PATH = "CSS/stile_quoridor_view_TUI.tcss"

    def __init__(self, coda_input: queue.Queue, **kwargs):
        super().__init__(**kwargs)
        self.__coda_input = coda_input

    def on_mount(self):
        self.push_screen(QuoridorViewScreen())
    
    def invia_comando(self, comando: str):
        self.__coda_input.put(comando)

