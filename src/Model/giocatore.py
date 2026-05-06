from Model.nodo import Nodo


class ErroreId(Exception):
    """Eccezione che gestisce tutti gli errori riguardanti id del giocatore.

    Descrizione:
        Gestisce i casi in cui viene passato un id errato

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


    Metodi:

        ------ Costruttori ------

        - __init__(self, newIdGiocatore: str, newPosizione: str = __DEF_POSIZIONE):
            DESCRIZIONE
                Costruttore di Base.
                Dato un ID e una posizione restituisce un giocatore.

        ------ Metodi Accesso Attributi Privati ------

        - get_id(self) -> str:
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

    """

    # Variabili
    __idGiocatore: str
    __posizioneCorrente: Nodo

    # Costanti
    __DEF_POSIZIONE = Nodo("a1")
    __DEF_ID        = "P1"

    # Metodi

    # Costruttore

    def __init__(self, newIdGiocatore: str = __DEF_ID, newPosizione: Nodo = __DEF_POSIZIONE):
        self.set_id(newIdGiocatore)
        self.set_posizione(newPosizione)

    # Modificatori / Osservatori

    def get_id(self) -> str:
        return self.__idGiocatore

    def set_id(self, newIdGiocatore: str):

        if len(newIdGiocatore) != 2:
            raise ErroreId("L'id deve avere lunghezza pari a 2")

        if newIdGiocatore[0] != 'P':
            raise ErroreId("L'id deve avere come primo carattere 'P'")

        if newIdGiocatore[1] != '2' and newIdGiocatore[1] != '1':
            raise ErroreId("L'id deve avere come secondo carattere '1' o '2', in base al numero del giocatore")

        self.__idGiocatore = newIdGiocatore

    def get_posizione(self) -> Nodo:
        return self.__posizioneCorrente

    def set_posizione(self, newPosizione: Nodo):
        self.__posizioneCorrente = newPosizione
