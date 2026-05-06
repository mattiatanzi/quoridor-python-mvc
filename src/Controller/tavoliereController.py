from Model.tavoliere import Tavoliere
from View.tavoliereView import TavoliereView


class TavoliereController:
    """Effettua controlli sul tavoliere su i dati di input per evitare errori in esecuzione."""

    def __init__(self):
        self.model = Tavoliere()
        self.view  = TavoliereView()
        