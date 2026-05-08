from Model.tavoliere import Tavoliere
from Model.giocatore import Giocatore

class ErrorePartita(Exception):
    """Eccezione che gestisce errori durante la partita."""

    pass


class Partita:
    """Classe Partita.

    Descrizione:
        Contiene informazioni relative alla partita in corso

    Attributi:

        - giocatori
            TIPO
                Privato, Tipo Set di Giocatori
            DESCRIZIONE
                L'insieme dei giocatori che partecipa alla partita corrente

        - tavoliere
            TIPO
                Privato, Tipo Tavoliere
            DESCRIZIONE
                Il tavoliere utilizzato nella partita in corso

    Metodi:

        ------ Costruttori ------

        def __init__(self, newTavoliere: Tavoliere, newGiocatori: set[Giocatore]):
            DESCRIZIONE
                Costruttore di Base.
                Dato un Tavoliere e un insieme di Giocatori restituisce una partita

        ------ Metodi Accesso Attributi Privati ------

        def setTavoliere(self, newTavoliere: Tavoliere):
            DESCRIZIONE
                Modfica il Tavolere della partita

        def getTavoliere(self) -> Tavoliere:
            DESCRIZIONE
                Restituisce il Tavoliere utilizzato in partita

        def setGiocatori(self, newGiocatori: set[Giocatore]):
            DESCRIZIONE
                Modifica l'insieme di giocatori della partita

        def getGiocatori(self):
            DESCRIZIONE
                Restituisce l'insieme di giocatori della partita

        ------ Modificatori / Osservatori ------

        def getGiocatore(self, id):
            DESCRIZIONE
                Restituisce il giocatore in partita con l'id in input

        def setGiocatore(self, id, newGiocatore: Giocatore):
            DESCRIZIONE
                Sostitusce il giocatore in partita con l'id in input con il nuovo
                giocatore in input


        def aggiungiGiocatore(self, newGiocatore: Giocatore):
            DESCRIZIONE
                Aggiunge il giocatore in input alla partita.
                IL giocatore non verrà aggiunto se è già in partita o se fosse raggiunto
                il massimo numero di giocatori in partita

        def rimuoviGiocatore(self, id):
            DESCRIZIONE
                Rimuove il giocatore con l'id in input dalla partita (Se il giocatore
                risulta essere in partita)
    """

    # Costanti
    __TOTALE_GIOCATORI = 2

    # Variabili
    __giocatori: set[Giocatore]
    __tavoliere: Tavoliere

    # Metodi

    # Costruttore

    def __init__(self, newTavoliere: Tavoliere, newGiocatori: set[Giocatore]):
        self.setTavoliere(newTavoliere)
        self.setGiocatori(newGiocatori)

    # Accesso Attributi Privati

    def setTavoliere(self, newTavoliere: Tavoliere):
        self.__tavoliere = newTavoliere

    def getTavoliere(self) -> Tavoliere:
        return self.__tavoliere

    def setGiocatori(self, newGiocatori: set[Giocatore]):
        self.__giocatori = newGiocatori

    def getGiocatori(self):
        return self.__giocatori

    # Modificatori / Osservatori

    # Modificare / Restituire un Giocatore in Partita

    def getGiocatore(self, id):
        for g in self.getGiocatori():
            if g.get_id() == id:
                return g
        raise ErrorePartita("Giocatore non presente nella partita")

    def setGiocatore(self, id, newGiocatore: Giocatore):
        self.rimuoviGiocatore(id)
        self.aggiungiGiocatore(newGiocatore)

    # Aggiungere / Rimuovere Giocatore in partita

    def aggiungiGiocatore(self, newGiocatore: Giocatore):
        numeroGiocatoriPartita = len(self.getGiocatori())

        if (numeroGiocatoriPartita < self.__TOTALE_GIOCATORI):
            self.getGiocatori().add(newGiocatore)
        else:
            raise ErrorePartita(f"Impossibile Aggiungere Giocatori (Numero giocatori: {numeroGiocatoriPartita}/{self.__TOTALE_GIOCATORI}")

    def rimuoviGiocatore(self, id):
        numeroGiocatoriPartita = len(self.getGiocatori())

        if (numeroGiocatoriPartita > 0):
            giocatoreSelezionato = self.getGiocatore(id)
            self.getGiocatori().remove(giocatoreSelezionato)
        else:
            raise ErrorePartita(f"Impossibile Rimuovere Giocatori (Numero giocatori: {numeroGiocatoriPartita}/{self.__TOTALE_GIOCATORI}")

    # Cambiare Posizione di Giocatore in partita

    def getPosizioneGiocatore(self, id):
        g = self.getGiocatore(id)
        return g.get_posizione()

    def setPosizioneGiocatore(self, id, newPosizione):
        giocatoreSelezionato = self.getGiocatore(id)
        giocatoreSelezionato.set_posizione(newPosizione)

    # Cambiare muri disponibili di giocatore in partita

    def setMuriDisponibiliGiocatore(self, id, newMuriDisponibili):

        giocatoreSelezionato = self.getGiocatore(id)
        giocatoreSelezionato.set_muri_disponibili(newMuriDisponibili)

    def getMuriDisponibiliGiocatore(self, id):
        giocatoreSelezionato = self.getGiocatore(id)
        return giocatoreSelezionato.get_muri_disponibili()

    def rimuoviUnMuroGiocatore(self, id):
        self.setMuriDisponibiliGiocatore(id, self.getMuriDisponibiliGiocatore(id) - 1)
