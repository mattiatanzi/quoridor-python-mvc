from Model.tavoliere import Tavoliere
from View.tavoliereView import TavoliereView


class TavoliereController:
    def __init__(self):
        self.model = Tavoliere()
        self.view  = TavoliereView()
        