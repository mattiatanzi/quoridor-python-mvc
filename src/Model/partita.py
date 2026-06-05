from src.Model.costanti_partita import CostantiPartita
from src.Model.giocatore import ErrorePosizione, Giocatore
from src.Model.nodo import Nodo
from src.Model.tavoliere import Tavoliere


class ErrorePartita(Exception):
    """Eccezione che gestisce errori durante la partita."""

    pass


class ErroreFormattazione(ErrorePartita):
    """Eccezione che gestisce tutti gli errori sulle formattazioni sbagliate."""

    pass


class Partita:
    """Classe Partita.

    DESCRIZIONE:
        Contiene informazioni relative alla partita in corso.

    ATTRIBUTI:
        ------ VARIABILI ------

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

        - id_giocatore_attivo
            TIPO
                Privato, Tipo str
            DESCRIZIONE
                L'id del giocatore che sta svolgendo il turno
        - trascrizione
            TIPO
                Privato, Lista di Stringhe
            DESCRIZIONE
                La lista che memorizza le mosse

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

        def set_giocatori(self, new_giocatori: set[Giocatore]):
            DESCRIZIONE
                Modifica l'insieme di giocatori della partita.

        def get_giocatori(self):
            DESCRIZIONE
                Restituisce l'insieme di giocatori della partita.

        def set_id_giocatore_attivo(self, id):
            DESCRIZIONE
                Sostituisce l'id del giocatore con il turno attivo.

        def get_id_giocatore_attivo(self):
            DESCRIZIONE
                Restituisce l'id del giocatore con il turno attivo.

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

        def elimina_giocatore(self, id):
            DESCRIZIONE
                Elimina il giocatore con id in input dalla partita

                ATTENZIONE
                    Eliminare un Giocatore != Rimuovere un Giocatore
                    Rimuovere un giocatore dalla partita vuol dire rimuoverlo
                    dal set di giocatori presenti. Eliminare il giocatore dalla
                    partita invece significa mantenerlo in partita, ma segnare con un
                    flag che non può più giocare i propri turni.
                    Per adesso l'eliminazione avviene soltanto nel momento in cui il
                    giocatore finisce il limite di tempo


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

        def incrementa_turno(self):
            DESCRIZIONE
                Passa il turno al giocatore successivo

        def piazza_muro(self,azione,giocatore):
            DESCRIZIONE
                Controlla se è possibile piazzare un muro e se piazzarlo verticale o
                orizzontale

        def muovi_giocatore(self, azione, giocatore_attivo)
            DESCRIZIONE
                Esegue il movimento del pedone.
                Controlla sul tavoliere se la mossa può essere fatta, poi aggiorna
                la posizione.

        def verifica_vittoria(self)
            DESCRIZIONE
                Controlla la posizione dei pedoni per decretare la fine della partita.
                Controlla anche che in partita ci sia almeno un giocatore, altrimenti
                l'ultimo giocatore è il vincitore.
                Restituisce l'ID del vincitore.

        def aggiungi_mossa_trascrizione(self, mossa: str)
            DESCRIZIONE
                Aggiunge una mossa alla trascrizione della partita.

        def get_trascrizione(self) -> list[str]:
            DESCRIZIONE
                Restituisce una copia della trascrizione partita. La trascrizione
                avviene nel seguente modo:
                    -Per ogni turno viene creato un elemento nella lista trascrizioni
                    - Ogni elemento della lista trascrizioni contiene le mosse svolte
                      da ogni giocatore in quel turno, ordinate per numero di giocatore

                Esempio: La seguente lista indica che ci sono 2 giocatori e sono stati
                svolti due turni, in cui P1 si è mosso in a2 e poi in a3,
                mentre P2 in b5 e poi b6. [1. a2 b5 , 2. a3 b6]
    """

    # Variabili
    __giocatori: set[Giocatore]
    __tavoliere: Tavoliere
    __id_giocatore_attivo: str
    __trascrizione: list[str]

    # Metodi

    # Costruttore

    def __init__(self, new_tavoliere: Tavoliere, new_giocatori: set[Giocatore]):
        self.set_tavoliere(new_tavoliere)
        self.set_giocatori(new_giocatori)
        self.set_id_giocatore_attivo(CostantiPartita._ID_PRIMO_GIOCATORE_ATTIVO)
        self.__trascrizione = []

    # Accesso Attributi Privati

    def set_tavoliere(self, new_tavoliere: Tavoliere):
        self.__tavoliere = new_tavoliere

    def get_tavoliere(self) -> Tavoliere:
        return self.__tavoliere

    def set_giocatori(self, new_giocatori: set[Giocatore]):
        self.__giocatori = new_giocatori

    def get_giocatori(self) -> set[Giocatore]:
        return self.__giocatori

    def set_id_giocatore_attivo(self, id):
        self.__id_giocatore_attivo = id

    def get_id_giocatore_attivo(self):
        return self.__id_giocatore_attivo

    def get_trascrizione(self) -> list[str]:
        return list(self.__trascrizione)

    # Modificatori / Osservatori

    # Aggiungere mossa nella trascrizione
    def aggiungi_mossa_trascrizione(self, mossa: str):
        if self.__id_giocatore_attivo == CostantiPartita._ID_PRIMO_GIOCATORE_ATTIVO:
            numero = len(self.__trascrizione) + 1
            self.__trascrizione.append(f"{numero}. {mossa}")
        else:
            self.__trascrizione[-1] += f" {mossa}"

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

        if numero_giocatori_partita < CostantiPartita._TOTALE_GIOCATORI:
            self.get_giocatori().add(new_giocatore)
        else:
            raise ErrorePartita(
                "Impossibile Aggiungere Giocatori (Numero giocatori: "
                f"{numero_giocatori_partita}/{CostantiPartita._TOTALE_GIOCATORI})"
            )

    def rimuovi_giocatore(self, id):
        numero_giocatori_partita = len(self.get_giocatori())

        if numero_giocatori_partita > 0:
            giocatore_selezionato = self.get_giocatore(id)
            self.get_giocatori().remove(giocatore_selezionato)
        else:
            raise ErrorePartita(
                f"Impossibile Rimuovere Giocatori (Numero giocatori: "
                f"{numero_giocatori_partita}/{CostantiPartita._TOTALE_GIOCATORI})"
            )

    def elimina_giocatore(self, id):
        giocatore_selezionato = self.get_giocatore(id)
        giocatore_selezionato.set_attivo(False)


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

    # Modificatori turno

    def incrementa_turno(self):
        id_giocatore_attivo = self.get_id_giocatore_attivo()

        numeroGiocatore = int(id_giocatore_attivo[1]) + 1

        if numeroGiocatore > CostantiPartita._TOTALE_GIOCATORI:
            numeroGiocatore = 1

        nuovo_id_giocatore_attivo = f"{id_giocatore_attivo[0]}{numeroGiocatore}"

        self.set_id_giocatore_attivo(nuovo_id_giocatore_attivo)

    def piazza_muro(self, azione: str, giocatore_attivo: Giocatore):
        if giocatore_attivo.get_muri_disponibili() == 0:
            raise ErrorePartita("Errore: Muri da piazzare terminati")

        if CostantiPartita._PRIMA_COLONNA <= azione[0] <= CostantiPartita._ULTIMA_COLONNA:
            if CostantiPartita._PRIMA_RIGA <= azione[1] <= CostantiPartita._ULTIMA_RIGA:
                if azione[2] == CostantiPartita._ORIZZONTALE:
                    self.__tavoliere.piazza_muro_orizzontale(azione)
                elif azione[2] == CostantiPartita._VERTICALE:
                    self.__tavoliere.piazza_muro_verticale(azione)
                else:
                    raise ErroreFormattazione(
                        "Errore: inserire dopo la posizione h/v per indicare muro "
                        + "verticale o orizzontale"
                    )
            else:
                raise ErroreFormattazione(
                    "Errore: inserire dopo la colonna un numero tra 1 e 9"
                )
        else:
            raise ErroreFormattazione(
                "Errore: inserire colonna corretta come primo carattere tra 'a' e 'i'"
            )

    def muovi_giocatore(self, azione: str, giocatore_attivo: Giocatore):
        if not (
            CostantiPartita._PRIMA_COLONNA <= azione[0] <= CostantiPartita._ULTIMA_COLONNA
            and CostantiPartita._PRIMA_RIGA <= azione[1] <= CostantiPartita._ULTIMA_RIGA
        ):
            raise ErrorePosizione(f"Coordinate fuori scacchiera: {azione}")

        nodo_partenza = giocatore_attivo.get_posizione()
        nodo_arrivo = Nodo(azione)

        # Riconoscere uno spostamento sulla medesima casella
        if nodo_partenza == nodo_arrivo:
            mess_err = f"Mossa non valida: Sei già sulla casella {azione}..."
            raise ErrorePosizione(mess_err)
        # Verifica dell'esistenza passaggio
        elif self.__tavoliere.mossa_permessa(nodo_partenza, nodo_arrivo):

            # Evitiamo che ci si possa spostare su una casella occupata
            for avversario in self.get_giocatori():

                # Esclusione del giocatore attivo dal controllo
                if avversario.get_id() == giocatore_attivo.get_id():
                    continue

                # Controllo sovrapposizione (il controllo avviene tra nodi)
                if avversario.get_posizione() == nodo_arrivo:
                    mess_err = f"Mossa non valida: {azione} è occupata dall'avversario"
                    raise ErrorePosizione(mess_err)
            # Il passaggio è libero
            self.set_posizione_giocatore(giocatore_attivo.get_id(), nodo_arrivo)
        else:
            # Il passaggio non è libero (o non è adiacente)
            raise ErrorePosizione(f"Mossa non valida: {azione} non è raggiungibile")

    # Osservatore condizione di vittoria

    def verifica_vittoria(self):

        giocatori_attivi = set()

        for giocatore in self.get_giocatori():

            if (giocatore.is_attivo()):

                giocatori_attivi.add(giocatore)

                id_giocatore = giocatore.get_id()

                # Estrazione carattere corrispondente alla riga
                pos_giocatore = giocatore.get_posizione().get_valore_id_nodo()
                riga = pos_giocatore[1]

                # Verifica raggiunta del traguardo
                if CostantiPartita._RIGHE_FINALI.get(id_giocatore) == riga:
                    return id_giocatore


        # Caso in cui sia rimasto un giocatore
        if len(giocatori_attivi) == 1:
            vincitore = giocatori_attivi.pop()
            return vincitore.get_id()

        # In caso non sia stato rilevato un vincitore
        return None
