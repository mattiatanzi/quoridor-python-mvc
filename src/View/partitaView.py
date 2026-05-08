from Model.partita import Partita
from View.giocatore import GiocatoreView
from View.tavoliereView import TavoliereView


class PartitaView:


    # Attributi
    __giocatoreView: GiocatoreView
    __tavoliereView: TavoliereView


    # Metodi

    # Costruttore

    def __init__(self, new_giocatore_view: GiocatoreView, new_tavoliere_view: TavoliereView):
        self.set_giocatore_view(new_giocatore_view)
        self.set_tavoliere_view(new_tavoliere_view)

    # Accesso Attributi Privati

    def set_tavoliere_view(self, new_tavoliere_view: TavoliereView):
        self.__tavoliereView = new_tavoliere_view

    def get_tavoliere_view(self):
        return self.__tavoliereView


    def set_giocatore_view(self, new_giocatore_view: GiocatoreView):
        self.__giocatoreView = new_giocatore_view

    def get_giocatore_view(self):
        return self.__giocatoreView

    # Stampe Video

    def stampa_partita(self, partita: Partita):
        giocatori = partita.get_giocatori()

        for g in giocatori:
            id_selezionato = g.get_id()
            muri_rimanenti = partita.get_muri_disponibili_giocatore(id_selezionato)
            self.get_giocatore_view().stampa_muri_rimanenti_giocatore(id_selezionato, muri_rimanenti)

        self.get_tavoliere_view().stampa_tavoliere()

    # Stampe Errori

    def stampa_errore_partita(self, messaggio):
        print(messaggio)
