from Model.tavoliere import Tavoliere
from View.tavoliereView import TavoliereView


class TavoliereController:
    """Effettua controlli sul tavoliere su i dati di input per evitare errori in esecuzione.
    
    Attributi
    ---------
    nome: model
        Contiene la controparte di tavoliere presente in model
    nome: view
        Contiene la controparte di tavoliere presente in view
    """

    def __init__(self,model,view):
        self.model = model
        self.view  = view
        