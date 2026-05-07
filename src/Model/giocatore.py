from Model.nodo import Nodo


class ErroreId(Exception):
    """Eccezione che gestisce tutti gli errori riguardanti id del giocatore.

    Descrizione:
        Gestisce i casi in cui viene passato un id errato

    """

    pass

class ErroreMuro(Exception):
    """Eccezione che gestisce gli errori riguardanti il muro.

    Descrizione:
        Gestisce i casi in cui il formato del muro è errato

    """

    pass


class Giocatore:
    """Classe Giocatore.

    Descrizione:
        Contiene informazioni relative al giocatore

    Attributi:

        - idGiocatore
            TIPO
                Privato, Tipo Stringa
            DESCRIZIONE
                l'ID del giocatore, necessario a determinarne la posizione sul
                tavoliere (oltre a eventualmente distinguerlo dagli altri giocatori).
                Indicata nel formato 'Pn', dove n appartiene a {1,2}.

                Esempi:
                    P1 (Giocatore 1)
                    P2 (Giocatore 2)

        - posizioneCorrente
            TIPO
                Privato, Tipo nodo
            DESCRIZIONE
                La posizione del giocatore rispetto al tavoliere nella partita in corso.
                La notazione utilizzata è la stessa di quella utilizzata
                per il tavoliere.
                Per informazioni sulla notazione usata per le posizioni consultare
                la documentazione sul tavoliere di gioco.

        - muriDisponibili
            TIPO
                Privato, Tipo int
            DESCRIZIONE
                Numero di muri piazzabili dal giocatore
                Ad inizio partita il giocatore ha a disposizione 10 muri.
                Se un giocatore termina i muri a disposizioni, non potrà più piazzarne.


    Metodi:

        ------ COSTRUTTORI ------

        def __init__(self, newIdGiocatore: str, newPosizione: str = __DEF_POSIZIONE):
            DESCRIZIONE
                Costruttore di Base.
                Dato un ID e una posizione restituisce un giocatore.


        ------ ACCESSO METODI PRIVATI ------

        def get_id(self) -> str:
            DESCRIZIONE
                Restituisce l'ID del giocatore


        def set_id(self, newIdGiocatore: str):
            DESCRIZIONE
                Modifica l'ID del giocatore

        def get_posizione(self) -> Nodo:
            DESCRIZIONE
                Restituisce la posizione del giocatore

        def set_posizione(self, newPosizione: Nodo):
            DESCRIZIONE
                Modifica la posizione del giocatore

        def get_muri_disponibili(self):
            DESCRIZIONE
                Restituisce numero di muri piazzabili dal giocatore

        def set_muri_disponibili(self, newNumeroMuri: int):
            DESCRIZIONE
                Modifica numero di muri a disposizione

    """

    # Variabili
    __idGiocatore: str
    __posizioneCorrente: Nodo
    __muriDisponibili: int

    # Costanti
    __DEF_POSIZIONE         = Nodo("a1")
    __DEF_ID                = "P1"
    __DEF_MURI_DISPONIBILI  = 10

    # Metodi

    # Costruttore

    def __init__(self, newIdGiocatore: str = __DEF_ID, newPosizione: Nodo = __DEF_POSIZIONE, newMuriDisponibili: int = __DEF_MURI_DISPONIBILI):

        self.set_id(newIdGiocatore)
        # Se non specifico il valore della posizione, assegno una copia del nodo posizione di default
        # # Altrimenti assegno la posizione specificata
        if (newPosizione is self.__DEF_POSIZIONE):
            self.set_posizione(Nodo("a1"))
        else:
            self.set_posizione(newPosizione)

        self.set_muri_disponibili(newMuriDisponibili)

    # Modificatori / Osservatori

    def get_id(self) -> str:
        return self.__idGiocatore

    def set_id(self, newIdGiocatore: str):

        # Caso in cui l'id è una stringa troppo lunga
        if len(newIdGiocatore) != 2:
            raise ErroreId("L'id deve avere lunghezza pari a 2")

        # id deve cominciare con la lettera P
        if newIdGiocatore[0] != 'P':
            raise ErroreId("L'id deve avere come primo carattere 'P'")

        # id deve terminare con 1 o 2 (Giocatore 1 o 2)
        if newIdGiocatore[1] != '2' and newIdGiocatore[1] != '1':
            raise ErroreId("L'id deve avere come secondo carattere '1' o '2', in base al numero del giocatore")

        # Se l'id rispetta i criteri può essere inserito nel giocatore
        self.__idGiocatore = newIdGiocatore

    def get_posizione(self) -> Nodo:
        return self.__posizioneCorrente

    def set_posizione(self, newPosizione: Nodo):
        self.__posizioneCorrente = newPosizione

    def get_muri_disponibili(self) -> int:
        return self.__muriDisponibili

    def set_muri_disponibili(self, newNumeroMuri: int):

        # Un giocatore può avere solo tra 0 e 10 muri
        if not(0 <= newNumeroMuri <= 10):
            raise ErroreMuro("Il numero di muri deve essere compreso tra 0 e 10")

        # Se i muri sono compresi tra 0 e 10 posso assegnarli al giocatore
        self.__muriDisponibili = newNumeroMuri
