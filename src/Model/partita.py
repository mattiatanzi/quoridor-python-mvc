from Model.giocatore import Giocatore
from Model.tavoliere import Tavoliere


class ErrorePartita(Exception):
    """Eccezione che gestisce errori durante la partita."""

    pass


class Partita:
    """Classe Partita.

    DESCRIZIONE:
        Contiene informazioni relative alla partita in corso.

    ATTRIBUTI:

        ------ COSTANTI ------

        - TOTALE_GIOCATORI
            TIPO
                Privato, Tipo int
            DESCRIZIONE
                Il numero massimo dei giocatori amessi in partita

        - giocatori
            TIPO
                Privato, Tipo Set di Giocatori
            DESCRIZIONE
                L'insieme dei giocatori che partecipa alla partita corrente.

        - tavoliere
            TIPO
                Privato, Tipo Tavoliere
            DESCRIZIONE
                Il tavoliere utilizzato nella partita in corso.

    METODI:

        ------ COSTRUTTORI ------

        def __init__(self, new_tavoliere: Tavoliere, new_giocatori: set[Giocatore]):
            DESCRIZIONE
                Costruttore di Base.
                Dato un Tavoliere e un insieme di Giocatori restituisce una partita.

        ------ ACCESSO ATTRIBUTI PRIVATI ------

        def set_tavoliere(self, new_tavoliere: Tavoliere):
            DESCRIZIONE
                Modfica il Tavolere della partita.

        def get_tavoliere(self) -> Tavoliere:
            DESCRIZIONE
                Restituisce il Tavoliere utilizzato in partita.

        def setGiocatori(self, new_giocatori: set[Giocatore]):
            DESCRIZIONE
                Modifica l'insieme di giocatori della partita.

        def getGiocatori(self):
            DESCRIZIONE
                Restituisce l'insieme di giocatori della partita.

        ------ MODIFICATORI / OSSERVATORI ------

        def set_giocatore(self, id, new_giocatore: Giocatore):
            DESCRIZIONE
                Sostitusce il giocatore in partita con l'id in input con il nuovo
                giocatore in input.

        def get_giocatore(self, id):
            DESCRIZIONE
                Restituisce il giocatore in partita con l'id in input


        def aggiungi_giocatore(self, new_giocatore: Giocatore):
            DESCRIZIONE
                Aggiunge il giocatore in input alla partita.
                IL giocatore non verrà aggiunto se è già in partita o se
                fosse raggiunto.
                il massimo numero di giocatori in partita.

        def rimuovi_giocatore(self, id):
            DESCRIZIONE
                Rimuove il giocatore con l'id in input dalla partita (Se il giocatore
                risulta essere in partita).


        def set_posizione_giocatore(self, id, new_posizione):
            DESCRIZIONE
                Modifica la posizione del giocatore con id in input sostituendola con
                una nuova posizione in input.

        def get_posizione_giocatore(self, id):
            DESCRIZIONE
                Restituisce la posizione del giocatore con id in input.


        def set_muri_disponibili_giocatore(self, id, new_muri_disponibili):
            DESCRIZIONE
                Sostituisce il numero di muri a disposizione del giocatore con id in
                input con un nuovo numero di muri disponibili in input.

        def get_muri_disponibili_giocatore(self, id):
            DESCRIZIONE
                Restituisce numero di muri a disposizione del giocatore con id in
                input.

        def rimuovi_un_muro_giocatore(self, id):
            DESCRIZIONE
                Decrementa di un valore pari a uno il numero di muri a disposizione del
                giocatore.

    """

    # Costanti
    __TOTALE_GIOCATORI = 2

    # Variabili
    __giocatori: set[Giocatore]
    __tavoliere: Tavoliere

    # Metodi

    # Costruttore

    def __init__(self, new_tavoliere: Tavoliere, new_giocatori: set[Giocatore]):
        self.set_tavoliere(new_tavoliere)
        self.set_giocatori(new_giocatori)

    # Accesso Attributi Privati

    def set_tavoliere(self, new_tavoliere: Tavoliere):
        self.__tavoliere = new_tavoliere

    def get_tavoliere(self) -> Tavoliere:
        return self.__tavoliere

    def set_giocatori(self, new_giocatori: set[Giocatore]):
        self.__giocatori = new_giocatori

    def get_giocatori(self):
        return self.__giocatori

    # Modificatori / Osservatori

    # Modificare / Restituire un Giocatore in Partita

    def get_giocatore(self, id):
        for g in self.get_giocatori():
            if g.get_id() == id:
                return g
        raise ErrorePartita("Giocatore non presente nella partita")

    def set_giocatore(self, id, new_giocatore: Giocatore):
        self.rimuovi_giocatore(id)
        self.aggiungi_giocatore(new_giocatore)

    # Aggiungere / Rimuovere Giocatore in partita

    def aggiungi_giocatore(self, new_giocatore: Giocatore):
        numero_giocatori_partita = len(self.get_giocatori())

        if numero_giocatori_partita < self.__TOTALE_GIOCATORI:
            self.get_giocatori().add(new_giocatore)
        else:
            raise ErrorePartita(
                "Impossibile Aggiungere Giocatori (Numero giocatori: "
                f"{numero_giocatori_partita}/{self.__TOTALE_GIOCATORI})"
            )

    def rimuovi_giocatore(self, id):
        numero_giocatori_partita = len(self.get_giocatori())

        if numero_giocatori_partita > 0:
            giocatore_selezionato = self.get_giocatore(id)
            self.get_giocatori().remove(giocatore_selezionato)
        else:
            raise ErrorePartita(
                f"Impossibile Rimuovere Giocatori (Numero giocatori: "
                f"{numero_giocatori_partita}/{self.__TOTALE_GIOCATORI})"
            )

    # Cambiare Posizione di Giocatore in partita

    def get_posizione_giocatore(self, id):
        g = self.get_giocatore(id)
        return g.get_posizione()

    def set_posizione_giocatore(self, id, new_posizione):
        giocatore_selezionato = self.get_giocatore(id)
        giocatore_selezionato.set_posizione(new_posizione)

    # Cambiare muri disponibili di giocatore in partita

    def set_muri_disponibili_giocatore(self, id, new_muri_disponibili):
        giocatore_selezionato = self.get_giocatore(id)
        giocatore_selezionato.set_muri_disponibili(new_muri_disponibili)

    def get_muri_disponibili_giocatore(self, id):
        giocatore_selezionato = self.get_giocatore(id)
        return giocatore_selezionato.get_muri_disponibili()

    def rimuovi_un_muro_giocatore(self, id):
        self.set_muri_disponibili_giocatore(
            id, self.get_muri_disponibili_giocatore(id) - 1
        )
