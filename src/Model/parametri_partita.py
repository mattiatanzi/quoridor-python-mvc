from datetime import timedelta

from src.Model.costanti_giocatore import CostantiGiocatore


class ErroreParametriPartita(Exception):
    """Eccezione che gestisce errori riguardanti i parametri."""

    pass


class ParametriPartita:
    """Classe ParametriPartita.

    DESCRIZIONE:
        Contiene informazioni relative ai parametri in corso.

    ATTRIBUTI:
        ------ VARIABILI ------

        - numero_giocatori
            TIPO
                Privato, Tipo int positivo
            DESCRIZIONE
                Il numero di giocatori scelto per la partita.
                Per adesso può essere solo 2 o 4

        - limite_tempo
            TIPO
                Privato, Tipo timedelta
            DESCRIZIONE
                Il limite di tempo scelto per la partita.
                None se non viene utilizzato un limite di tempo

        - id_giocatore_attivo
            TIPO
                Privato, Tipo str
            DESCRIZIONE
                L'id del giocatore che sta svolgendo il turno

        - avvia_partita
            TIPO
                Privato, Tipo bool
            DESCRIZIONE
                Indica se la partita può essere avviata o meno.
                Utile in caso dopo la creazione dei parametri non si volesse
                avviare la partita e tornare al menu iniziale, ricominciando
                la configurazione.

    METODI:

        ------ COSTRUTTORI ------

            def __init__(
                self,
                new_numero_giocatori: int = len(CostantiGiocatore._POSSIBILI_ID_GIOCATORE),
                new_limite_tempo = CostantiGiocatore._DEF_TIMER_PREDEFINITI[0],
                new_avvia_partita = True
            )
                DESCRIZIONE
                Costruttore di Base.
                Inizializza di default una partita con max numero giocatori,
                timer predefinito uno. Impostato per avviare la partita


        ------ ACCESSO ATTRIBUTI PRIVATI ------

        def set_numero_giocatori(self, new_numero_giocatori: int)
            DESCRIZIONE
                Modfica il numero di giocatori scelti.
                Lancia eccezione in caso il nuovo numero sia invalido.

        def get_numero_giocatori(self) -> Tavoliere:
            DESCRIZIONE
                Restituisce il numero di giocatori scelti.

        def set_limite_tempo(self, new_limite_tempo: timedelta)
            DESCRIZIONE
                Imposta il nuovo limite di tempo scelto per la partita

        def get_limite_tempo(self) -> timedelta:
            DESCRIZIONE
                Restituisce il limite di tempo scelto per la partita

        def set_avvia_partita(self, new_avvia_partita: bool):
            DESCRIZIONE
                Imposta il valore di avvia_partita nei parametri.

        def get_avvia_partita(self) -> bool:
            DESCRIZIONE
                Restituisce avvia_partita.
    """

    __numero_giocatori: int
    __limite_tempo: timedelta
    __avvia_partita: bool

    # Costruttore
    def __init__(
        self,
        new_numero_giocatori: int = len(CostantiGiocatore.POSSIBILI_ID_GIOCATORE),
        new_limite_tempo=CostantiGiocatore.DEF_TIMER_PREDEFINITI[0],
        new_avvia_partita=True,
    ):
        self.set_limite_tempo(new_limite_tempo)
        self.set_avvia_partita(new_avvia_partita)
        self.set_numero_giocatori(new_numero_giocatori)

    # Accesso Attributi Privati
    def set_numero_giocatori(self, new_numero_giocatori: int):
        if new_numero_giocatori > 0:
            self.__numero_giocatori = new_numero_giocatori
        else:
            raise ErroreParametriPartita

    def get_numero_giocatori(self):
        return self.__numero_giocatori

    def set_limite_tempo(self, new_limite_tempo: timedelta):
        self.__limite_tempo = new_limite_tempo

    def get_limite_tempo(self) -> timedelta:
        return self.__limite_tempo

    def set_avvia_partita(self, new_avvia_partita: bool):
        self.__avvia_partita = new_avvia_partita

    def get_avvia_partita(self) -> bool:
        return self.__avvia_partita
