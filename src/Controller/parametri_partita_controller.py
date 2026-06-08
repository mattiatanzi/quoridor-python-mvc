from src.Model.parametri_partita import ErroreParametriPartita, ParametriPartita
from src.View.parametri_partita_view import ParametriPartitaView


class ParametriPartitaController:

    __view: ParametriPartitaView
    __model: ParametriPartita

    # Costruttore
    def __init__(
        self,
        new_model: ParametriPartita = ParametriPartita(),
        new_view: ParametriPartitaView = ParametriPartitaView()
    ):
        self.set_view(new_view)
        try:
            self.set_model(new_model)
        except ErroreParametriPartita as err:
            self.get_view().stampa_errore_parametri(err)

    # Accesso attributi Privati
    def set_view(self, new_view: ParametriPartitaView):
        self.__view = new_view

    def get_view(self) -> ParametriPartitaView:
        return self.__view

    def set_model(self, new_model: ParametriPartita):
        self.__model = new_model

    def get_model(self) -> ParametriPartita:
        return self.__model
