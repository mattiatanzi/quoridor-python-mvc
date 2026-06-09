from src.Model.tavoliere import Tavoliere
from src.View.tavoliere_view import TavoliereviewAstratta


class TavoliereController:
    """Effettua controlli sul tavoliere su dati di input per evitare errori esecuzione.

    Attributi
    ---------
    nome: model
        Contiene la controparte di tavoliere presente in model
    nome: view
        Contiene la controparte di tavoliere presente in view

    Metodi
    -------
    nome get_model
        Restituisce il model del tavoliere controller

    nome get_view
        Restituisce il view del tavoliere controller

    nome set_model
        Imposta il valore del model del tavoliere controller

    nome set_view
        Imposta il valore del view del tavoliere controller
    """

    def __init__(self, model: Tavoliere, view: TavoliereviewAstratta):
        self.__model = model
        self.__view = view

    def get_model(self) -> Tavoliere:
        return self.__model

    def get_view(self) -> TavoliereviewAstratta:
        return self.__view

    def set_model(self, model: Tavoliere):
        self.__model = model

    def set_view(self, view: TavoliereviewAstratta):
        self.__view = view
