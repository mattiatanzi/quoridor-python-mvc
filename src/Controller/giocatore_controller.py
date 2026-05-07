from Model.giocatore import ErroreMuro, Giocatore, ErroreId
from View.giocatore_view import GiocatoreView


class GiocatoreController:
    """Classe GiocatoreController.

    DESCRIZIONE
        Rappresenta il controller del Giocatore

    ATTRIBUTI

        - model
            TIPO
                Privato, tipo Giocatore

            DESCRIZIONE
                Il modello del Giocatore

        - view
            TIPO
                Privato, tipo GiocatoreView

            DESCRIZIONE
                Responsabile della gestione di stampa e input del Giocatore

    METODI
        ------ COSTRUTTORI ------

        __init__(self, model: Giocatore, view: GiocatoreView):
            DESCRIZIONE
                Costruttore di base


        ------ ACCESSO ATTRIBUTI PRIVATI ------

        def get_model(self) -> Giocatore:
            DESCRIZIONE
                Restituisce il Model del Giocatore contenuto nel Controller

        def set_model(self, model: Giocatore):
            DESCRIZIONE
                Modifica il Model del Giocatore nel Controller

        def get_view(self) -> GiocatoreView:
            DESCRIZIONE
                Restituisce la classe responsabile del View del Giocatore contenuta nel
                Controller

        def set_view(self, view: GiocatoreView):
            DESCRIZIONE
                Modifica la classe responsabile del View del Giocatore nel Controller


        ------ OSSERVATORI / MODIFICATORI ------

        def set_giocatore_id(self, new_id: str):
            DESCRIZIONE
                Modifica l'id del giocatore, mostrando errore in caso il formato inserito sia errato

        def get_giocatore_id(self):
            DESCRIZIONE
                Restituisce l'id del giocatore

    """

    __model: Giocatore
    __view: GiocatoreView

    def __init__(self, model: Giocatore, view: GiocatoreView):
        self.set_model(model)
        self.set_view(view)

    def get_model(self) -> Giocatore:
        return self.__model

    def set_model(self, model: Giocatore):
        self.__model = model

    def get_view(self) -> GiocatoreView:
        return self.__view

    def set_view(self, view: GiocatoreView):
        self.__view = view

    def set_giocatore_id(self, new_id: str):
        try:
            self.get_model().set_id(new_id)
        except ErroreId as errore_id:
            self.get_view().stampa_errore_id(errore_id)

    def get_giocatore_id(self):
        return self.get_model().get_id()

    def set_giocatore_muri(self, new_muri_disponibili: int):
        try:
            self.get_model().set_muri_disponibili(new_muri_disponibili)
        except ErroreMuro as errore_muro:
            self.get_view().stampa_errore_muri(errore_muro)
