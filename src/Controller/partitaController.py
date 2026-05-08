from Model.partita import Partita
from View.partitaView import PartitaView


class PartitaController:

    # Attributi

    __model: Partita
    __view: PartitaView

    # Metodi

    # Costruttore

    def __init__(self, model: Partita, view: PartitaView):
        self.set_model(model)
        self.set_view(view)

    # Accesso Attributi Privati

    def get_model(self) -> Partita:
        return self.__model

    def set_model(self, model: Partita):
        self.__model = model

    def get_view(self) -> PartitaView:
        return self.__view

    def set_view(self, view: PartitaView):
        self.__view = view
