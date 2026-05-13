from src.Model.tavoliere import Tavoliere
from src.View.tavoliere_view import TavoliereView


class TavoliereController:
    """Effettua controlli sul tavoliere su dati di input per evitare errori esecuzione.

    Attributi
    ---------
    nome: model
        Contiene la controparte di tavoliere presente in model
    nome: view
        Contiene la controparte di tavoliere presente in view
    """

    def __init__(self, model: Tavoliere, view: TavoliereView):
        self.model = model
        self.view = view
