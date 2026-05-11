from Model.partita import ErrorePartita, ErroreFormattazione, Partita
from View.partita_view import PartitaView
from Model.tavoliere import ErroreTavoliere


class PartitaController:
    """Classe PartitaController.

    DESCRIZIONE:
        Il controller della partita in corso.

    ATTRIBUTI:

        - model
            TIPO
                Privato, tipo Partita

            DESCRIZIONE
                Il modello della Partita

        - view
            TIPO
                Privato, tipo PartitaView

            DESCRIZIONE
                Responsabile della gestione di stampa e input della Partita

    METODI:

        ------ COSTRUTTORI ------

        def __init__(self, model: Partita, view: PartitaView):
            DESCRIZIONE
                Costruttore di Base.
                Data un modello Partita e un PartitaView restituisce
                un PartitaController

        ------ ACCESSO ATTRIBUTI PRIVATI ------

        def get_model(self) -> Partita:
            DESCRIZIONE
                Restituisce il Model di Partita contenuto nel Controller

        def set_model(self, model: Partita):
            DESCRIZIONE
                Modifica il Model di Partita nel Controller

        def get_view(self) -> PartitaView:
            DESCRIZIONE
                Restituisce la classe responsabile del View di Partita contenuta nel
                Controller

        def set_view(self, view: PartitaView):
            DESCRIZIONE
                Modifica la classe responsabile del View di Partita contenuta nel
                Controller

        ------ MODIFICATORI / OSSERVATORI ------

        def get_giocatore(self, id):
            DESCRIZIONE
                Restituisce un giocatore dato un id

        def aggiungi_giocatore(self, new_giocatore):
            DESCRIZIONE
                Aggiunge il giocatore in input alla partita.
                IL giocatore non verrà aggiunto se è già in partita o se
                fosse raggiunto.
                il massimo numero di giocatori in partita.

        def rimuovi_giocatore(self, id):
            DESCRIZIONE
                Rimuove il giocatore con l'id in input dalla partita (Se il giocatore
                risulta essere in partita).

        def gioca_partita(self):
            DESCRIZIONE
            Permette di avviare giocare una partita, stampa la partita in corso e prende
            i dati di input dall'utente e gestice il dato
    """

    # Attributi

    __model: Partita
    __view: PartitaView

    # Metodi
    __POSSIBILE_MURO = 3
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

    def gioca_partita(self):
        while True:
            azione: str = self.__view.stampa_partita(self.get_model())
            id_giocatore_attivo = self.__model.get_id_giocatore_attivo()
            if len(azione) == self.__POSSIBILE_MURO:
                try:
                    self.__model.piazza_muro(azione)
                    self.__model.rimuovi_un_muro_giocatore(id_giocatore_attivo)
                    self.__model.incrementa_turno()
                except ErroreFormattazione as err_from:
                    self.get_view().stampa_errore_partita(err_from)
                except ErroreTavoliere as err_tav:
                    self.get_view().stampa_errore_partita(err_tav)
