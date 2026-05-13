from src.Model.giocatore import ErroreId, ErroreMuro, ErrorePosizione, Giocatore
from src.View.giocatore_view import GiocatoreView


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
                Responsabile della gestione di stampa e input del Giocatore.

    METODI
        ------ COSTRUTTORI ------

        def __init__(self, model: Giocatore, view: GiocatoreView):
            DESCRIZIONE
                Costruttore di base


        ------ ACCESSO ATTRIBUTI PRIVATI ------

        def get_model(self) -> Giocatore:
            DESCRIZIONE
                Restituisce il Model del Giocatore contenuto nel Controller.

        def set_model(self, model: Giocatore):
            DESCRIZIONE
                Modifica il Model del Giocatore nel Controller

        def get_view(self) -> GiocatoreView:
            DESCRIZIONE
                Restituisce la classe responsabile del View del Giocatore contenuta nel
                Controller.

        def set_view(self, view: GiocatoreView):
            DESCRIZIONE
                Modifica la classe responsabile del View del Giocatore nel Controller.


        ------ OSSERVATORI / MODIFICATORI ------

        def set_giocatore_id(self, new_id: str):
            DESCRIZIONE
                Modifica l'id del giocatore,
                mostrando errore in caso il formato inserito sia errato.

        def get_giocatore_id(self):
            DESCRIZIONE
                Restituisce l'id del giocatore.

        def set_giocatore_muri(self, new_muri_disponibili: int):
            DESCRIZIONE
                Modifica il numero di muri rimanenti per il giocatore,
                mostrando un errore in caso il numero sia errato.

        def get_giocatore_muri(self):
            DESCRIZIONE
                Restituisce numero di muri rimanenti al giocatore.

        def set_giocatore_posizione(self, new_posizione):
            DESCRIZIONE
                Modifica posizione del giocatore, mostrando un errore
                in caso essa sia errata.

    """

    # Attributi
    #
    __model: Giocatore
    __view: GiocatoreView

    # Costruttori

    def __init__(self, model: Giocatore, view: GiocatoreView):
        self.set_model(model)
        self.set_view(view)

    # Accesso Attributi Privati

    def set_model(self, model: Giocatore):
        self.__model = model

    def get_model(self) -> Giocatore:
        return self.__model

    def set_view(self, view: GiocatoreView):
        self.__view = view

    def get_view(self) -> GiocatoreView:
        return self.__view

    # Modificatori / Osservatori

    def set_giocatore_id(self, new_id: str):
        try:
            self.get_model().set_id(new_id)
        except ErroreId as errore_id:
            messaggio = f"Errore ID Giocatore. {errore_id}"
            self.get_view().stampa_errore_giocatore(messaggio)

    def get_giocatore_id(self):
        return self.get_model().get_id()

    def set_giocatore_muri(self, new_muri_disponibili: int):
        try:
            self.get_model().set_muri_disponibili(new_muri_disponibili)
        except ErroreMuro as errore_muro:
            messaggio = f"Errore Muro in Giocatore. {errore_muro}"
            self.get_view().stampa_errore_giocatore(messaggio)

    def get_giocatore_muri(self):
        return self.get_model().get_muri_disponibili()

    def set_giocatore_posizione(self, new_posizione):
        try:
            self.get_model().set_posizione(new_posizione)
        except ErrorePosizione as errore_posizione:
            messaggio = f"Errore Posizione in Giocatore. {errore_posizione}"
            self.get_view().stampa_errore_giocatore(messaggio)
