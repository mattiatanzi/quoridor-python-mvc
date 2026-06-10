from datetime import timedelta

from src.Model.costanti_giocatore import CostantiGiocatore
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


class TempoException(Exception):
    """Eccezione che gestisce errori riguardanti il tempo di gioco."""

    pass


class Giocatore:
    """Classe Giocatore.

    DESCRIZIONE:
        Contiene informazioni relative al giocatore

    ATTRIBUTI:

        ------ ATTRIBUTI ------

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

        - tempoResiduo
            TIPO
                Privato, Tipo timedelta
            DESCRIZIONE
                Contiene il tempo rimasto al giocatore.
                In caso il giocatore faccia parte di una partita senza limiti di tempo,
                questo campo conterrà la costante DEF_SENZA_LIMITE_TEMPO, come indicato
                nel file costanti_giocatore.py

        - attivo
            TIPO
                Privato, Tipo bool
            DESCRIZIONE
                Indica se il giocatore è stato eliminato dalla partita.
                In una partita, se attivo = False (<=> giocatore eliminato),
                non verrà stampato il suo pedone ma soltanto i muri che esso
                ha posizionato. Per adesso il giocatore può essere eliminato soltanto
                nel caso in cui, durante una partita con limite di tempo e il tempo
                a sua disposizione fosse stato esaurito.

    METODI:

        ------ COSTRUTTORI ------

        def __init__(
            self,
            new_id_giocatore: str = __DEF_ID,
            new_posizione = None,
            new_muri_disponibili: int = __DEF_MURI_DISPONIBILI,
            new_tempo_iniziale: timedelta = __DEF_TEMPO_INIZIALE
        ):
            DESCRIZIONE
                Costruttore di Base.
                Dato un ID, una posizione, un numero di muri disponibili e un tempo
                iniziale, restituisce un giocatore.


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

        def get_tempo_residuo(self) -> timedelta:
            DESCRIZIONE
                Restituisce il tempo residuo del giocatore come oggetto timedelta

        def set_tempo_residuo(self, tempo: timedelta):
            DESCRIZIONE
                Imposta il tempo residuo nel giocatore.

        def is_attivo(self) -> bool:
            DESCRIZIONE
                Restituisce True se il giocatore è attivo, False altrimenti.
                Il significato di giocatore attivo è già stato discusso nella sezione
                attributi.

        def set_attivo(self, new_stato: bool):
            DESCRIZIONE
                Modifica il campo attivo del giocatore.
                Il significato di giocatore attivo è già stato discusso nella sezione
                attributi.


        ------ MODIFICATORI / OSSERVATORI ------

        def riduci_tempo(
            self,
            tempo_trascorso: timedelta  = timedelta(seconds = 1)
        ) -> bool:
            DESCRIZIONE
                Sottrae il tempo in input al giocatore (se il giocatore ha un limite di
                tempo).

        def possiede_limite_tempo(self) -> bool:
            DESCRIZIONE
                Restituisce True se il Giocatore ha un limite di tempo,
                False se altrimenti non ha limite (fa parte di una partita senza
                limite di tempo)

        def ha_finito_tempo(self) -> bool:
            DESCRIZIONE
                Restituisce True se il Giocatore ha terminato il proprio tempo,
                False se ha ancora tempo a disposizione oppure se non ha limiti di tempo

    """

    # Attributi
    __idGiocatore: str
    __posizioneCorrente: Nodo
    __muriDisponibili: int
    __tempoResiduo: timedelta
    __attivo: bool

    # Metodi

    # Costruttore

    def __init__(
        self,
        new_id_giocatore: str = CostantiGiocatore.POSSIBILI_ID_GIOCATORE[0],
        new_posizione=None,
        new_muri_disponibili: int = CostantiGiocatore.DEF_MURI_DISPONIBILI,
        new_tempo_iniziale: timedelta = CostantiGiocatore.DEF_SENZA_LIMITE_TEMPO,
    ):
        self.set_id(new_id_giocatore)

        # Caso in cui Posizione non viene specificata
        if new_posizione is None:
            self.set_posizione(Nodo(CostantiGiocatore.DEF_COORDINATE))
        else:
            self.set_posizione(new_posizione)

        self.set_muri_disponibili(new_muri_disponibili)

        self.set_tempo_residuo(new_tempo_iniziale)

        self.set_attivo(True)

    # Accesso Attributi Privati

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

    def get_tempo_residuo(self) -> timedelta:
        return self.__tempoResiduo

    def set_tempo_residuo(self, tempo: timedelta):
        self.__tempoResiduo = tempo

    def is_attivo(self) -> bool:
        return self.__attivo

    def set_attivo(self, new_stato: bool):
        self.__attivo = new_stato

    # Modificatori / Osservatori

    def riduci_tempo(self, tempo_trascorso: timedelta = timedelta(seconds=1)) -> bool:
        if self.possiede_limite_tempo():
            if tempo_trascorso.seconds < 0:
                raise TempoException(
                    "I secondi passati devono essere un numero positivo"
                )

            if self.ha_finito_tempo():
                raise TempoException(
                    f"Il tempo del giocatore {self.get_id()} è già scaduto"
                )

            if self.get_tempo_residuo() <= tempo_trascorso:
                self.set_tempo_residuo(timedelta(seconds=0))
                return False  # Tempo finito
            else:
                self.set_tempo_residuo(self.get_tempo_residuo() - tempo_trascorso)
                return True  # C'è ancora tempo
        else:
            raise TempoException(
                f"Impossibile Ridurre il tempo, il Giocatore {self.get_id()}"
                "non ha limiti di tempo"
            )

    def possiede_limite_tempo(self) -> bool:
        return self.__tempoResiduo != CostantiGiocatore.DEF_SENZA_LIMITE_TEMPO

    def ha_finito_tempo(self) -> bool:
        tempo_disponibile = False

        if self.possiede_limite_tempo():
            tempo_disponibile = self.get_tempo_residuo() == timedelta()

        return tempo_disponibile
