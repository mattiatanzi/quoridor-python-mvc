from src.Model.giocatore import Giocatore
from src.Model.nodo import Nodo
from src.Model.partita import Partita
from src.Model.tavoliere import Tavoliere


class ErroreReplay(Exception):
    """Eccezione che gestisce errori durante il replay."""

    pass


class ReplayPartita:
    """Classe ReplayPartita.

    DESCRIZIONE:
        Gestisce il replay animato di una partita appena conclusa.
        Ricostruisce gli stati del gioco riseguendo le mosse della trascrizione a
        partire da uno stato iniziale pulito.

    ATTRIBUTI:

        ------ COSTANTI ------

        - P1
            TIPO
                Privato, Tipo str
            DESCRIZIONE
                ID del giocatore 1

        - P2
            TIPO
                Privato, Tipo str
            DESCRIZIONE
                ID del giocatore 2

        - POSIZIONE_P1
            TIPO
                Privato, Tipo Nodo
            DESCRIZIONE
                Posizione iniziale del giocatore 1

        - POSIZIONE_P2
            TIPO
                Privato, Tipo Nodo
            DESCRIZIONE
                Posizione iniziale del giocatore 2

        - MURI_INIZIALI
            TIPO
                Privato, Tipo int
            DESCRIZIONE
                Numero di muri inizlai per ogni giocatore

        ------ VARIABILI ------

        - mosse_flat
            TIPO
                Privato, Lista di tuple (str, str)
            DESCRIZIONE
                Lista piatta di (id_giocatore, mossa) estratta dalla
                trascrizione, nell'ordine in cui le mosse sono state
                eseguite durante la partita.
                Esempio:
                    [("P1", "e2"), ("P2", "e8"), ("P1", "e3h"), ...]

    METODI:
        ------ COSTRUTTORI ------

        - def __init__(self, trascrizione: list[str])
            DESCRIZIONE
                Costruttore di Base.
                Costruisce il replay della trascrizione della partita.

        ------ ACCESSO ATTRIBUTI ------

        - def get_indice_corrente(self) -> int:
            DESCRIZIONE
                Restituisce l'indice della mossa correntemente mostrata.

        - def get_totale_mosse(self) -> int:
            DESCRIZIONE
                Restituisce il numero totale di mosse della partita.

        ------ COSTRUZIONE STATI ------

        - crea_partita_iniziale(self) -> Partita
            DESCRIZIONE
                Crea una nuova partita nello stato iniziale

        ------ UTILITÀ ------

        - parse_trascrizione(self, trascrizione: list[str]) -> list[tuple[str, str]]
            DESRCIZIONE
                Converte la trascrizione in una lista piatta
                di (giocatore, mossa).

                La trascrizione ha il formato: ["1. e2 e8", "2. e3h d7v", ...]
                dove ogni elemento del turno può contenere 1 o 2 mosse
                (la seconda mossa potrebbe mancare nell'ultimo turno se P2
                non ha giocato prima della fine).

        - build_stati(self) -> list[Partita]
            DESCRIZIONE
                Costruisce la lista di tutti gli stati rieseguendo le mosse.

                Riesegue le mosse della trascrizione in ordine su una nuova partita
                pulita.

        -  get_mossa_corrente(self) -> tuple[str, str] | None
            DESCRIZIONE
                Restituisce la tupla (id_giocatore, mossa) dell'ultima mossa eseguita.
                Se si è allo stato iniziale restiuisce invece None.

        - get_numero_mossa_corrente(self) -> str
            DESCRIZIONE
                Restituisce una stringa descrittiva del passo corrente.
                Riconosce il caso speciale in cui non ci sono state mosse e lo avvisa.

                Esempio (formato): "Mossa N/TOT".

        ------ NAVIGAZIONE ------

        - get_stato_corrente(self) -> Partita
            DESCRIZIONE
                Restituisce lo stato della partita corrispondente all'indice corrente.

        - avanza(self) -> bool
            DESCRIZIONE
                Avanza al passo successivo del replay e restituisce un booleano in
                base alla buona riuscita dell'avanzamento.

        - torna_indietro(self) -> bool
            DESCRIZIONE
                Torna al passo precedente del replay e restituisce un booleano in
                base alla buona riuscita dell'indietreggiamento.

        - vai_a(self, indice: int):
            DESCRIZIONE
                Posizione il replay all'indice specificato, solleva ErroreReplay
                in caso l'indice sia fuori dai limiti.

        - replay_inizio(self) -> bool:
            DESCRIZIONE
                Restituisce true se il replay si trova nello stato iniziale.

        - replay_fine(self) -> bool:
            DESCRIZIONE
                Restituisce true se il replay si trova nello stato finale.
    """

    # Attributi
    __giocatori_setup: set[Giocatore]
    __id_giocatori_ordinati: list[str]
    

    # Metodi

    # ------ Costruttori ------ #
    def __init__(self, trascrizione: list[str], giocatori_iniziali: set[Giocatore]):
        # Ricava gli ID ordinati dei partecipanti
        self.__giocatori_setup = giocatori_iniziali
        self.__id_giocatori_ordinati = sorted([g.get_id() for g in giocatori_iniziali])
        self.__mosse_flat = self.__parse_trascrizione(trascrizione)
        self.__indice_corrente = 0
        self.__stati = self.__build_stati()

    # ------ Accesso attributi ------ #
    def get_indice_corrente(self) -> int:
        return self.__indice_corrente

    def get_totale_mosse(self) -> int:
        return len(self.__mosse_flat)

    # ------ Utilità ------ #
    def __parse_trascrizione(self, trascrizione: list[str]) -> list[tuple[str, str]]:
        mosse_flat: list[tuple[str, str]] = []
        for turno in trascrizione:
            # Rimuove il numero del turno e divide le mosse
            parti = turno.split(". ", 1)
            if len(parti) < 2:
                continue
            mosse_turno = parti[1].split()

            # P1 parte per primo
            giocatori_turno = self.__id_giocatori_ordinati
            for i, mossa in enumerate(mosse_turno):
                if i < len(giocatori_turno):
                    mosse_flat.append((giocatori_turno[i], mossa))

        return mosse_flat

    def __build_stati(self) -> list[Partita]:
        stati: list[Partita] = []

        # Stato 0: la partita iniziale
        partita = self.__crea_partita_iniziale()
        stati.append(partita)

        for _ in self.__mosse_flat:
            # Ricrea una partita pulita e riesegue le mosse fino a questo punto
            partita_step = self.__crea_partita_iniziale()
            n_mosse_da_eseguire = len(stati)  # indice della mossa corrente

            for i in range(n_mosse_da_eseguire):
                id_g, m = self.__mosse_flat[i]
                g = partita_step.get_giocatore(id_g)

                # Sincronizzazione del turno
                if partita_step.get_id_giocatore_attivo() != id_g:
                    partita_step.incrementa_turno()
                if len(m) == 3:  # Muro
                    partita_step.piazza_muro(m, g)
                    partita_step.rimuovi_un_muro_giocatore(id_g)
                else:  # Pedone
                    partita_step.muovi_giocatore(m, g)
                partita_step.incrementa_turno()

            stati.append(partita_step)

        return stati

    def get_mossa_corrente(self) -> tuple[str, str] | None:
        if self.replay_inizio():
            return None
        return self.__mosse_flat[self.__indice_corrente - 1]

    def get_numero_mossa_corrente(self) -> str:
        if self.replay_inizio():
            return "Non ci sono ancora state mosse!"
        return f"Mossa {self.__indice_corrente}/{len(self.__mosse_flat)}"

    # ------ Costruzione stati ------ #
    def __crea_partita_iniziale(self) -> Partita:
        # Assegnazioni per la creazione di una nuova partita
        tavoliere = Tavoliere()
        nuovi_giocatori = set()

        for g_setup in self.__giocatori_setup:
            nodo_iniziale = Nodo(g_setup.get_posizione().get_valore_id_nodo())
            
            giocatore_pulito = Giocatore(
                g_setup.get_id(),
                nodo_iniziale,
                g_setup.get_muri_disponibili()
            )
            nuovi_giocatori.add(giocatore_pulito)

        return Partita(tavoliere, nuovi_giocatori)

    # ------ Navigazione ------ #
    def get_stato_corrente(self) -> Partita:
        return self.__stati[self.__indice_corrente]

    def avanza(self) -> bool:
        if self.__indice_corrente < len(self.__mosse_flat):
            self.__indice_corrente += 1
            return True
        return False

    def torna_indietro(self) -> bool:
        if self.__indice_corrente > 0:
            self.__indice_corrente -= 1
            return True
        return False

    def vai_a(self, indice: int):
        if not (0 <= indice <= len(self.__mosse_flat)):
            raise ErroreReplay(
                f"Indice {indice} fuori dai limiti: [0, {len(self.__mosse_flat)}]"
            )
        self.__indice_corrente = indice

    def replay_inizio(self) -> bool:
        return self.__indice_corrente == 0

    def replay_fine(self) -> bool:
        return self.__indice_corrente == len(self.__mosse_flat)
