from src.Model import tempo
from src.Model.giocatore import Giocatore
from src.Model.parametri_partita import ErroreParametriPartita, ParametriPartita
from src.View.costanti_quoridor_view import CostantiQuoridorView
from src.View.parametri_partita_view import ParametriPartitaView


class ParametriPartitaController:
    __view: ParametriPartitaView
    __model: ParametriPartita

    # Costruttore
    def __init__(
        self,
        new_model: ParametriPartita = ParametriPartita(),
        new_view: ParametriPartitaView = ParametriPartitaView(),
    ):
        self.set_view(new_view)
        try:
            self.set_model(new_model)
        except ErroreParametriPartita as err:
            self.get_view().stampa_errore_parametri(err)

    # Accesso attributi Privati
    def set_view(self, new_view: ParametriPartitaView):
        self.__view = new_view

    def get_view(self) -> ParametriPartitaView:
        return self.__view

    def set_model(self, new_model: ParametriPartita):
        self.__model = new_model

    def get_model(self) -> ParametriPartita:
        return self.__model

    # Altri Metodi
    def ottieni_parametri_utente(self) -> ParametriPartita:
        tornaMenuIniziale = False

        while not tornaMenuIniziale:
            # Interfaccia 1: Chiedere se usare limite di tempo per partita
            sceltaInterfaccia = self.get_view().get_input_modalita_partita()

            while (
                sceltaInterfaccia
                not in CostantiQuoridorView._POSSIBILI_SCELTE_MODALITA
                and

            ):
                sceltaInterfaccia = self.get_view().get_input_modalita_partita()

            # TORNARE INDIETRO
            if sceltaInterfaccia != CostantiQuoridorView._SCELTA_TORNA_INDIETRO:
                # IF NOT TORNARE INDIETRO AND NO TIMER
                if (
                    sceltaInterfaccia
                    == CostantiQuoridorView._SCELTA_PARTITA_SENZA_TIMER
                ):
                    tempo_limite = None

                # IF NOT TORNARE INDIETRO AND TIMER
                elif (
                    sceltaInterfaccia
                    == CostantiQuoridorView._SCELTA_PARTITA_SENZA_TIMER
                ):
                    # Interfaccia 2: Avvalorare Limite di Tempo
                    sceltaInterfaccia = self.get_view().get_input_modalita_partita()

                    while (
                        sceltaInterfaccia
                        not in CostantiQuoridorView._POSSIBILI_TIMER_DEFAULT
                        and
                        tempo.stringa_to_tempo_limite(sceltaInterfaccia) == None
                    ):
                        sceltaInterfaccia = self.get_view().get_input_modalita_partita()

            else:
                tornaMenuIniziale = True
                avvia_partita = False

        return ParametriPartita(
            new_limite_tempo = tempo_limite,
            new_avvia_partita = avvia_partita
        )
