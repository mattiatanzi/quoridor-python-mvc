from Model.partita import ErrorePartita, Partita
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

    # Modificatori / Osservatori

    def get_giocatore(self, id):
        try:
            return self.get_model().get_giocatore(id)
        except ErrorePartita as errPart:
            messaggio = f"Errore Giocatore in Partita. {errPart}"
            self.get_view().stampa_errore_partita(messaggio)

    def aggiungi_giocatore(self, new_giocatore):
        try:
            self.get_model().aggiungi_giocatore(new_giocatore)
        except ErrorePartita as errPart:
            messaggio = f"Errore Numero Giocatori in Partita. {errPart}"
            self.get_view().stampa_errore_partita(messaggio)

    def rimuovi_giocatore(self, id):
        try:
            self.get_model().rimuovi_giocatore(id)
        except ErrorePartita as errPart:
            messaggio = f"Errore Numero Giocatori in Partita. {errPart}"
            self.get_view().stampa_errore_partita(messaggio)
