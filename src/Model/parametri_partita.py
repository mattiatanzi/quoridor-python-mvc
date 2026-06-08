from datetime import timedelta

from src.Model.costanti_giocatore import CostantiGiocatore


class ErroreParametriPartita(Exception):
    pass

class ParametriPartita:

    __numero_giocatori: int
    __limite_tempo: timedelta
    __avvia_partita: bool


    # Costruttore
    def __init__(
        self,
        new_numero_giocatori: int = len(CostantiGiocatore._POSSIBILI_ID_GIOCATORE),
        new_limite_tempo = CostantiGiocatore._DEF_TIMER_PREDEFINITI[0],
        new_avvia_partita = True):
            self.set_limite_tempo(new_limite_tempo)
            self.set_avvia_partita(new_avvia_partita)
            self.set_numero_giocatori(new_avvia_partita)



    # Accesso Attributi Privati
    def set_numero_giocatori(self, new_numero_giocatori: int):
        if (new_numero_giocatori > 0):
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
