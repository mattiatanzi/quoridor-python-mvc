from src.Model.partita import Partita
from src.View.funzioni_utili_stampa import pulisci_schermo
from src.View.replay_view import ReplayViewAstratta


class ReplayViewCLI(ReplayViewAstratta):
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
        replay e si esegue una mossa. E' stato deciso per l'interfaccia CLI che 
        per evitare che la stampa della trascrizione vada troppo sotto è stato
        scelto di adottare un numero massimo di turni visibili durante
        il replay che è: gli ultimi 15 turni presenti


    """

    def __init__(self, stampa_tavoliere, stampa_trascrizione):
        super().__init__(stampa_tavoliere, stampa_trascrizione)

    def stampa_replay(
        self,
        stato_corrente: Partita,
        descrizione_mossa: str,
        trascrizione_parziale: list[str],
        automatico: bool = False,
    ):
        pulisci_schermo()
        print("\n\n")
        print("--- REPLAY ---")

        self._ReplayViewAstratta__stampa_tavoliere.stampa_tavoliere(# Messo ReplayViewAstratta perché se no altrimenti dava errore
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
        print ("Vengono mostrate per semplicità solo gli ultimi 15 turni")
        num_giocatori = len(stato_corrente.get_giocatori())
        self._ReplayViewAstratta__stampa_trascrizione.stampa_trascrizione(
            trascrizione_parziale, num_giocatori, True
        )
