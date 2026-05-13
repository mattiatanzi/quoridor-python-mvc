from src.Model.nodo import Nodo


class ErroreId(Exception):
    """Eccezione che gestisce tutti gli errori riguardanti id del giocatore."""

    pass


class ErroreMuro(Exception):
    """Eccezione che gestisce gli errori riguardanti il muro."""

    pass


class ErrorePosizione(Exception):
    """Eccezione che gestisce errori riguardanti la posizione."""

    pass


class Giocatore:
    """Classe Giocatore.

    DESCRIZIONE:
        Contiene informazioni relative al giocatore

    ATTRIBUTI:

        ------ COSTANTI ------

        - DEF_COORDINATE
            TIPO
                Privato, Tipo str
            DESCRIZIONE
                Coordinate di default con cui creare la posizione in caso
                non venisse specificata

        - DEF_ID
            TIPO
                Privato, Tipo str
            DESCRIZIONE
                id di default con cui creare un giocatore in caso
                non venisse specificato

        - DEF_MURI_DISPONIBILI
            TIPO
                Privato, Tipo int
            DESCRIZIONE
                Numero di muri disponibili all'inizio di ogni partita

        ------ VARIABILI ------

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


    METODI:

        ------ COSTRUTTORI ------

        def __init__(
            self,
            new_id_giocatore: str = __DEF_ID,
            new_posizione = None,
            new_muri_disponibili: int = __DEF_MURI_DISPONIBILI,
        ):
            DESCRIZIONE
                Costruttore di Base.
                Dato un ID, una posizione e un numero di muri disponibili,
                restituisce un giocatore.


        ------ ACCESSO METODI PRIVATI ------

        def get_id(self) -> str:
            DESCRIZIONE
                Restituisce l'ID del giocatore


        def set_id(self, new_id_giocatore: str):
            DESCRIZIONE
                Modifica l'ID del giocatore

        def get_posizione(self) -> Nodo:
            DESCRIZIONE
                Restituisce la posizione del giocatore

        def set_posizione(self, new_posizione: Nodo):
            DESCRIZIONE
                Modifica la posizione del giocatore

        def get_muri_disponibili(self):
            DESCRIZIONE
                Restituisce numero di muri piazzabili dal giocatore

        def set_muri_disponibili(self, new_muri_disponibili: int):
            DESCRIZIONE
                Modifica numero di muri a disposizione

    """

    # Attributi
    __idGiocatore: str
    __posizioneCorrente: Nodo
    __muriDisponibili: int

    # Costanti
    __DEF_COORDINATE = "a1"
    __DEF_ID = "P1"
    __DEF_MURI_DISPONIBILI = 10

    # Metodi

    # Costruttore

    def __init__(
        self,
        new_id_giocatore: str = __DEF_ID,
        new_posizione=None,
        new_muri_disponibili: int = __DEF_MURI_DISPONIBILI,
    ):
        self.set_id(new_id_giocatore)

        # Caso in cui Posizione non viene specificata
        if new_posizione is None:
            self.set_posizione(Nodo(self.__DEF_COORDINATE))
        else:
            self.set_posizione(new_posizione)

        self.set_muri_disponibili(new_muri_disponibili)

    # Modificatori / Osservatori

    def get_id(self) -> str:
        return self.__idGiocatore

    def set_id(self, new_id_giocatore: str):
        # Caso in cui l'id è una stringa troppo lunga
        if len(new_id_giocatore) != 2:
            raise ErroreId("L'id deve avere lunghezza pari a 2")

        # id deve cominciare con la lettera P
        if new_id_giocatore[0] != "P":
            raise ErroreId("L'id deve avere come primo carattere 'P'")

        # id deve terminare con 1 o 2 (Giocatore 1 o 2)
        if new_id_giocatore[1] != "2" and new_id_giocatore[1] != "1":
            raise ErroreId(
                "L'id deve avere come secondo carattere '1' o '2', "
                "in base al numero del giocatore"
            )

        # Se l'id rispetta i criteri può essere inserito nel giocatore
        self.__idGiocatore = new_id_giocatore

    def get_posizione(self) -> Nodo:
        return self.__posizioneCorrente

    def set_posizione(self, new_posizione: Nodo):
        coordinate = new_posizione.get_valore_id_nodo()

        if "a" <= coordinate[0] <= "i":
            if "1" <= coordinate[1] <= "9":
                self.__posizioneCorrente = new_posizione
            else:
                raise ErrorePosizione(
                    "Il valore della riga deve essere compreso tra 1 e 9."
                    f"Valore Inserito: {coordinate[1]}"
                )
        else:
            raise ErrorePosizione(
                "Il valore della colonna deve essere compreso tra a e i."
                f"Valore Inserito: {coordinate[0]}"
            )

    def get_muri_disponibili(self) -> int:
        return self.__muriDisponibili

    def set_muri_disponibili(self, new_muri_disponibili: int):
        # Un giocatore può avere solo tra 0 e 10 muri
        if not (0 <= new_muri_disponibili <= 10):
            raise ErroreMuro("Il numero di muri deve essere compreso tra 0 e 10")

        # Se i muri sono compresi tra 0 e 10 posso assegnarli al giocatore
        self.__muriDisponibili = new_muri_disponibili
