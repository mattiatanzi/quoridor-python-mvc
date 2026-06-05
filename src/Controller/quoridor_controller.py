from datetime import timedelta

from src.Controller.partita_controller import PartitaController
from src.Model.costanti_giocatore import CostantiGiocatore
from src.Model.costanti_partita import CostantiPartita
from src.View.costanti_quoridor_view import CostantiQuoridorView
from src.Model.giocatore import Giocatore
from src.Model.nodo import Nodo
from src.Model.partita import Partita
from src.Model.tavoliere import Tavoliere
from src.View.giocatore_view import GiocatoreView
from src.View.partita_view import PartitaView
from src.View.quoridor_view import QuoridorView
from src.View.tavoliere_view import TavoliereView


class QuoridorController:
    """Classe contenente l'esecuzione principale.

    Attributi
    ---------
    nome: menu
        Oggetto di QuoridorView e permette di visualizzare il menu
        e di visualizzare se ci sono errori

    Costanti
    --------
    nome: P1
        Contiene il nome visualizzato del giocatore 1

    nome: P2
        Contiene il nome visualizzato del giocatore 2

    nome: POSIZIONE_P1
        Contiene la posizione iniziale di P1

    nome: POSIZIONE_P2
        Contiene la posizione iniziale di P2

    nome: MURI_INIZIALI
        Contiene i muri iniziali dei giocatori


    Metodi
    -------
    nome: gioca()
        Esegue il menu principale e gestisce le scelte dell'utente
    """

    def __init__(self):
        self.set_view(QuoridorView())


    def get_view(self):
        return self.__view

    def set_view(self, new_view: QuoridorView):
        self.__view = new_view


    def gioca(self):
        continuare_gioco = True

        # Menu Principale
        while continuare_gioco:

            self.get_view().menu_di_gioco()
            scelta = self.get_view().get_input_menu()

            # Scelta = GIOCA
            if scelta == "1":

                scelta_modalita_timer = self.get_view().get_input_modalita_partita()

                # Scelta = TORNA INDIETRO
                if scelta_modalita_timer != CostantiQuoridorView._SCELTA_TORNA_INDIETRO:

                    limite_tempo_scelto = None
                    torna_indietro_da_timer = False

                    # Scelta = PARTITA CON TIMER
                    if scelta_modalita_timer == CostantiQuoridorView._SCELTA_PARTITA_CON_TIMER:

                        stringa_limite_tempo = self.get_view().get_input_limite_tempo()

                        # Scelta = TORNA INDIETRO
                        if stringa_limite_tempo == CostantiQuoridorView._SCELTA_TORNA_INDIETRO:
                            torna_indietro_da_timer = True

                        # Scelta = TIMER PREDEFINITO
                        elif stringa_limite_tempo in CostantiQuoridorView._POSSIBILI_TIMER_DEFAULT.keys():
                            limite_tempo_scelto = CostantiGiocatore._DEF_TIMER_PREDEFINITI[int(stringa_limite_tempo) - 1]
                        # Scelta = TIMER PERSONALIZZATO
                        else:
                            limite_tempo_scelto = self.__stringa_to_tempo_limite(stringa_limite_tempo)
                    # Scelta = PARTITA SENZA TIMER
                    else:
                        limite_tempo_scelto = CostantiGiocatore._DEF_SENZA_LIMITE_TEMPO

                    if not torna_indietro_da_timer and limite_tempo_scelto is not None:
                        # Inizializzazione Tavoliere e Giocatori
                        tavoliere = Tavoliere()
                        giocatori = set()
                        for i in range(0, 2):
                            id_assegnato = CostantiGiocatore._POSSIBILI_ID_GIOCATORE[i]
                            giocatore = Giocatore(
                                new_id_giocatore=id_assegnato,
                                new_posizione=Nodo(CostantiPartita._COORDINATE_INIZIALI[id_assegnato]),
                                new_tempo_iniziale=limite_tempo_scelto
                            )
                            giocatori.add(giocatore)

                        partita = PartitaController(
                            Partita(tavoliere, giocatori),
                            PartitaView(),
                        )
                        continuare_gioco = partita.gioca_partita()


            # Scelta = 0 <=> Esci dal gioco
            elif scelta == "0":
                    self.__view.stampa_messaggio("Uscita in corso, alla prossima!")
                    continuare_gioco = False
            elif scelta in ("h", "help", "aiuto"):
                PartitaView().stampa_aiuto()
                input("---- Premi INVIO per tornare al menu... ----")
            else:
                self.get_view().stampa_messaggio(
                    "Errore nell'inserimento della scelta, riprova"
                )



    def __stringa_to_tempo_limite(self, stringa_tempo: str) -> timedelta:
        try:
            ore, minuti, secondi = map(int, stringa_tempo.split(":"))
            return timedelta(hours = ore, minutes = minuti, seconds = secondi)
        except ValueError:
            self.get_view().stampa_messaggio("Errore Formato Tempo")
            return None
