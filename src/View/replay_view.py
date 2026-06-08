from src.Model.partita import Partita
from src.View.giocatore_view import GiocatoreView
from src.View.partita_view import PartitaView
from src.View.tavoliere_view import TavoliereView


class ReplayView:
    """Classe view del replay.

    Attributi:
    -----------
    stampa_tavoliere : TavoliereView
        Contiene tutte le stampe per il tavoliere
    stampa_trascrizione : PartitaView
        Contiene tutte le stampe per la partita

    COSTANTI:
    RIGA_INIZIALE
        Indica la riga iniziale di stampa a destra dello schermo

    COLONNA_DESTRA
        Indica la colonna iniziale di stampa a destra dello schermo


    METODI:
    __init__(self):
        Inizializza gli attributi

    stampa_replay(self,stato_corrente: Partita,descrizione_mossa: str,
        trascrizione_parziale: list[str],automatico: bool = False)
        Stampa la partita con la sua trascrizione ogni volta che si sta guardando il
        replay e si esegue una mossa


    """

    __RIGA_INIZIALE = 3
    __COLONNA_DESTRA = 55

    def __init__(self):
        self.__stampa_tavoliere = TavoliereView()
        self.__stampa_trascrizione = PartitaView(
            self.__stampa_tavoliere, GiocatoreView()
        )

    def stampa_replay(
        self,
        stato_corrente: Partita,
        descrizione_mossa: str,
        trascrizione_parziale: list[str],
        automatico: bool = False,
    ):
        print("--- REPLAY ---")

        self.__stampa_tavoliere.stampa_tavoliere(
            stato_corrente.get_tavoliere(), stato_corrente.get_giocatori()
        )

        print(f"\n\033[93m>>> {descrizione_mossa} <<<\033[0m")

        print("-" * 60)
        if not automatico:
            print("Comandi:")
            print(
                "- Per andare avanti: [Next] / [Avanti] / [N], vale anche "
                "premere invio senza scrivere niente"
            )
            print("- Per andare indietro: [Prev] / [Indietro] / [P] / [Back]")
            print("- Per tornare all'inizio del replay: [Start] / [Inizio] / [First]")
            print("- Per arrivare alla fine del replay: [End] / [Fine] / [Last]")
            print("- Per uscire: [Exit] / [Esci] / [Stop] / [Quit]")
        else:
            print("\n\n")
            print(" " * 10 + "[\033[92m Riproduzione Automatica in corso... \033[0m]")
            print("\n\n")
        num_giocatori = len(stato_corrente.get_giocatori())
        self.__stampa_trascrizione.stampa_trascrizione(
            trascrizione_parziale, num_giocatori, True
        )
