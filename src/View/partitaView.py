from Model.partita import Partita
from View.giocatore import GiocatoreView
from View.tavoliereView import TavoliereView


class PartitaView:


    # Attributi
    __giocatoreView: GiocatoreView
    __tavoliereView: TavoliereView


    # Metodi

    # Costruttore

    def __init__(self, newGiocatoreView: GiocatoreView, newTavoliereView: TavoliereView):
        self.setGiocatoreView(newGiocatoreView)
        self.setTavoliereView(newTavoliereView)

    # Accesso Attributi Privati

    def setTavoliereView(self, newTavoliereView: TavoliereView):
        self.__tavoliereView = newTavoliereView

    def setGiocatoreView(self, newGiocatoreView: GiocatoreView):
        self.__giocatoreView = newGiocatoreView

    def getTavoliereView(self):
        return self.__tavoliereView

    def getGiocatoreView(self):
        return self.__giocatoreView

    # Stampe Video

    def stampa_partita(self, partita: Partita):
        giocatori = partita.getGiocatori()

        for g in giocatori:
            idSelezionato = g.get_id()
            muriRimanenti = partita.getMuriDisponibiliGiocatore(idSelezionato)
            self.getGiocatoreView().stampa_muri_rimanenti_giocatore(idSelezionato, muriRimanenti)

        self.getTavoliereView().stampa_tavoliere()

    # Stampe Errori

    def stampa_errore_partita(self, messaggio):
        print(messaggio)
