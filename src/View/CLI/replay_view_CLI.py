import sys

from src.Model.partita import Partita
from src.View.CLI.tavoliere_view_CLI import TavoliereViewCLI
from src.View.funzioni_utili_stampa import pulisci_schermo
from src.View.replay_view import ReplayViewAstratta


class ReplayViewCLI(ReplayViewAstratta):
    """Classe view del replay.

    Attributi:
    -----------
    stampa_tavoliere : TavoliereView
        Contiene tutte le stampe per il tavoliere


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

    def __init__(self):
        self.__stampa_tavoliere = TavoliereViewCLI()

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

        self.__stampa_tavoliere.stampa_tavoliere(
            stato_corrente.get_tavoliere(), stato_corrente.get_giocatori()
        )

        print(f"\n\033[93m>>> {descrizione_mossa} <<<\033[0m")

        print("-" * 60)
        if not automatico:
            print("Comandi:")
            print(
                "- Per andare avanti: [Next] / [Avanti] / [N], vale anche premere invio senza scrivere niente"
            )
            print("- Per andare indietro: [Prev] / [Indietro] / [P] / [Back]")
            print("- Per tornare all'inizio del replay: [Start] / [Inizio] / [First]")
            print("- Per arrivare alla fine del replay: [End] / [Fine] / [Last]")
            print("- Per uscire: [Exit] / [Esci] / [Stop] / [Quit]")
        else:
            print("\n\n")
            print(" " * 10 + "[\033[92m Riproduzione Automatica in corso... \033[0m]")
            print("\n\n")
        print("Vengono mostrate per semplicità solo gli ultimi 15 turni")

        num_giocatori = len(stato_corrente.get_giocatori())
        # Chiamiamo il metodo interno della classe invece di sporcare PartitaView
        self.__disegna_storico_mosse_laterale(trascrizione_parziale, num_giocatori)

    def __disegna_storico_mosse_laterale(
        self, trascrizione: list[str], num_giocatori: int
    ):
        RIGA_IN = 5
        COLONNA_DESTRA = 55

        sys.stdout.write("\033[s")  # Memorizza il cursore in basso
        sys.stdout.write(
            f"\033[{RIGA_IN};{COLONNA_DESTRA}H\033[1m--- STORICO MOSSE ---\033[0m"
        )

        intestazione = ""
        for i in range(num_giocatori):
            intestazione += "P" + str(i + 1) + "\t"
        sys.stdout.write(
            f"\033[{RIGA_IN + 1};{COLONNA_DESTRA + 5}H\033[94m{intestazione}\033[0m"
        )

        MAX_MOSSE_VISIBILI = 15
        mosse_da_stampare = (
            trascrizione[-MAX_MOSSE_VISIBILI:]
            if len(trascrizione) > MAX_MOSSE_VISIBILI
            else trascrizione
        )

        for i, riga_turno in enumerate(mosse_da_stampare):
            riga_attuale = RIGA_IN + 2 + i

            # Splittiamo sulla sequenza ".\t" che separa il numero del turno dalle mosse
            parti = riga_turno.split(".\t", 1)
            if len(parti) >= 2:
                num_turno = parti[0] + "."  # es: "1."
                stringa_mosse = parti[1]  # es: "e2\te8\tb5" (già tabulata!)

                sys.stdout.write(
                    f"\033[{riga_attuale};{COLONNA_DESTRA}H\033[K{num_turno:<4} {stringa_mosse}\t"
                )
            else:
                sys.stdout.write(
                    f"\033[{riga_attuale};{COLONNA_DESTRA}H\033[K{riga_turno}\t"
                )

        sys.stdout.write("\033[u")  # Ripristina il cursore originale
        sys.stdout.flush()
