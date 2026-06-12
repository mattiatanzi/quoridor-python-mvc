from src.Model import tempo as funz_tempo
from src.Model.costanti_giocatore import CostantiGiocatore
from src.Model.costanti_partita import CostantiPartita
from src.Model.parametri_partita import ErroreParametriPartita, ParametriPartita
from src.View.costanti_quoridor_view import CostantiQuoridorView
from src.View.funzioni_utili_stampa import chiedi_input_utente
from src.View.parametri_partita_view import ParametriPartitaView


class ParametriPartitaController:
    """Classe ParametriPartitaController.

    DESCRIZIONE
        Classe che gestisce i parametri della partita.
        Utile per la stampa dei menu che richiedono l'interazione dell'utente per
        settare la partita (numero di giocatori, limite di tempo, ecc...)

    ATTRIBUTI:

        - model
            TIPO
                Privato, tipo ParametriPartita

            DESCRIZIONE
                Il modello di ParametriPartita

        - view
            TIPO
                Privato, tipo ParametriPartitaView

            DESCRIZIONE
                La view di ParametriPartita

    METODI:

        ------ COSTRUTTORI ------

        def __init__(self, model: Partita, view: PartitaView):
            DESCRIZIONE
                Costruttore di Base.
                Data un modello ParametriPartita e un ParametriPartitaView restituisce
                un ParametriPartitaController

        ------ ACCESSO ATTRIBUTI PRIVATI ------

        def get_model(self) -> ParametriPartita:
            DESCRIZIONE
                Restituisce il Model di ParametriPartitaController

        def set_model(self, model: ParametriPartita):
            DESCRIZIONE
                Sostituisce il Model di ParametriPartitaController

        def get_view(self) -> ParametriPartitaView:
            DESCRIZIONE
                Restituisce il View di ParametriPartitaController

        def set_view(self, view: PartitaView):
            DESCRIZIONE
                Sostituisce il View di ParametriPartitaController

        ------ MODIFICATORI / OSSERVATORI ------

        def ottieni_parametri_utente(self) -> ParametriPartita:
            DESCRIZIONE
                Interagisce con l'utente per creare una classe contenente
                tutti i parametri della partita. Per adesso chiede al giocatore se
                vuole una partita con limite di tempo (o meno), e successivamente quanto
                impostare di limite tempo



    """

    __view: ParametriPartitaView
    __model: ParametriPartita

    # Costruttore
    def __init__(
        self,
        new_model: ParametriPartita = None,
        new_view: ParametriPartitaView = None,
    ):
        self.__view = new_view
        try:
            self.set_model(new_model if new_model is not None else ParametriPartita())
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
        avvia_partita = True
        tempo_limite = None
        numero_giocatori = int(CostantiPartita.GIOCATORI_TOTALI_2)
        messaggio_errore = "\nInput Non Valido"

        while not tornaMenuIniziale:

            tornaIndietro = False
            # Interfaccia 1: Chiedere se usare limite di tempo per partita
            scelta_interfaccia = self.get_view().get_input_modalita_partita()

            while (
                scelta_interfaccia not in CostantiQuoridorView.POSSIBILI_SCELTE_MODALITA
            ):
                if scelta_interfaccia in ["help", "aiuto"]:
                    scelta_interfaccia = ""
                    self.get_view().stampa_aiuto_modalita_partita()
                    chiedi_input_utente("---- Premi INVIO per tornare alla partita... ----")
                    scelta_interfaccia = self.get_view().get_input_modalita_partita()
                else:
                    scelta_interfaccia = self.get_view().get_input_modalita_partita(
                        messaggio_errore
                    )

            # TORNARE INDIETRO
            if scelta_interfaccia != CostantiQuoridorView.SCELTA_TORNA_INDIETRO:
                # IF NOT TORNARE INDIETRO AND NO TIMER
                if (
                    scelta_interfaccia
                    == CostantiQuoridorView.SCELTA_PARTITA_SENZA_TIMER
                ):
                    tempo_limite = CostantiGiocatore.DEF_SENZA_LIMITE_TEMPO

                # IF NOT TORNARE INDIETRO AND TIMER
                elif scelta_interfaccia == CostantiQuoridorView.SCELTA_PARTITA_CON_TIMER:
                    # Interfaccia 2: Avvalorare Limite di Tempo
                    scelta_interfaccia = self.get_view().get_input_limite_tempo()

                    while (
                        scelta_interfaccia
                        not in CostantiQuoridorView.POSSIBILI_TIMER_DEFAULT
                        and funz_tempo.stringa_to_tempo_limite(scelta_interfaccia)
                        is None
                    ):
                        if scelta_interfaccia in ["help", "aiuto"]:
                            scelta_interfaccia = ""
                            self.get_view().stampa_aiuto_limite_tempo()
                            chiedi_input_utente("---- Premi INVIO per tornare alla partita... ----")
                            scelta_interfaccia = (
                                self.get_view().get_input_limite_tempo()
                            )
                        else:
                            scelta_interfaccia = self.get_view().get_input_limite_tempo(
                                messaggio_errore
                            )

                    if scelta_interfaccia != CostantiQuoridorView.SCELTA_TORNA_INDIETRO:
                        if (
                            scelta_interfaccia
                            in CostantiQuoridorView.POSSIBILI_TIMER_DEFAULT
                        ):
                            tempo_limite = CostantiGiocatore.DEF_TIMER_PREDEFINITI[
                                int(scelta_interfaccia) - 1
                            ]
                        else:
                            tempo_limite = funz_tempo.stringa_to_tempo_limite(
                                scelta_interfaccia
                            )

                        tornaMenuIniziale = True
                    else:
                        tornaIndietro = True

                if not tornaIndietro:
                    scelta_interfaccia = self.get_view().get_input_numero_giocatori()

                    while (
                        scelta_interfaccia not in CostantiQuoridorView.POSSIBILI_NUMERO_GIOCATORI
                    ):
                        if scelta_interfaccia in ["help", "aiuto"]:
                            scelta_interfaccia = ""
                            self.get_view().stampa_aiuto_numero_giocatori()
                            chiedi_input_utente("---- Premi INVIO per tornare alla partita... ----")
                            scelta_interfaccia = self.get_view().get_input_numero_giocatori()
                        else:
                            scelta_interfaccia = self.get_view().get_input_numero_giocatori(
                                messaggio_errore
                            )

                    if scelta_interfaccia != CostantiQuoridorView.SCELTA_TORNA_INDIETRO:
                        if (scelta_interfaccia == CostantiQuoridorView.SCELTA_2_GIOCATORI):
                            numero_giocatori = int(CostantiPartita.GIOCATORI_TOTALI_2)
                        elif (scelta_interfaccia == CostantiQuoridorView.SCELTA_4_GIOCATORI):
                            numero_giocatori = int(CostantiPartita.GIOCATORI_TOTALI_4)

                    else:
                        avvia_partita = False

                    tornaMenuIniziale = True

            else:
                tornaMenuIniziale = True
                avvia_partita = False




        return ParametriPartita(
            new_numero_giocatori = numero_giocatori,
            new_limite_tempo = tempo_limite,
            new_avvia_partita=avvia_partita,
        )