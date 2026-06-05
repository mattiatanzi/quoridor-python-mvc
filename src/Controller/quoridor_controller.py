from datetime import timedelta

from src.Controller.partita_controller import PartitaController
from src.Model.costanti_giocatore import CostantiGiocatore
from src.Model.costanti_partita import CostantiPartita
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
        errore: str = ""
        continuare_gioco = True
        scelta: str

        # continuare_gioco = True <=> Non uscire dal gioco
        while continuare_gioco:

            # Chiedi all'utente se giocare o uscire dal gioco
            self.get_view().menu_di_gioco()
            scelta = self.get_view().get_input_menu()

            tornaIndietro = False

            # Scelta = 1 <=> Procedere con creazione Partita
            if scelta == "1":
                while not tornaIndietro:

                    tornaIndietro = False
                    # Chiedi all'utente se giocare con timer, senza, o tornare indietro
                    scelta_modalita_timer = self.get_view().get_input_modalita_partita()
                    while (scelta_modalita_timer != "1" and scelta_modalita_timer != "2" and scelta_modalita_timer != "3" ):
                        scelta_modalita_timer = self.get_view().get_input_modalita_partita()

                    if (scelta_modalita_timer == "3"):
                        tornaIndietro = True

                    # Se l'utente non vuole uscire dalla creazione partita
                    if not tornaIndietro:

                        limite_tempo_scelto = None

                        # Caso Utente Sceglie Timer
                        if scelta_modalita_timer == "1":
                            while (limite_tempo_scelto is None and not tornaIndietro):
                                scelta_limite_tempo = self.get_view().get_input_limite_tempo()
                                if (scelta_limite_tempo == "3"):
                                    tornaIndietro = True
                                else:
                                    if (scelta_limite_tempo == "1"  or scelta_limite_tempo == "2"):
                                        limite_tempo_scelto = CostantiGiocatore._DEF_TIMER_PREDEFINITI[int(scelta_limite_tempo) - 1]
                                    else:
                                        limite_tempo_scelto = self.__stringa_to_tempo_limite(scelta_limite_tempo)

                        else:
                            limite_tempo_scelto = CostantiGiocatore._DEF_SENZA_TIMER

                        if (not tornaIndietro):
                            tavoliere = Tavoliere()

                            giocatore1 = Giocatore(
                                self.__P1, self.__POSIZIONE_P1, self.__MURI_INIZIALI, limite_tempo_scelto
                            )
                            giocatore2 = Giocatore(
                                self.__P2, self.__POSIZIONE_P2, self.__MURI_INIZIALI, limite_tempo_scelto
                            )
                            giocatori = {giocatore1, giocatore2}

                            view_giocatore = GiocatoreView()
                            view_tavoliere = TavoliereView()
                            partita = PartitaController(
                                Partita(tavoliere, giocatori),
                                PartitaView(view_giocatore, view_tavoliere),
                            )

                            continuare_gioco = partita.gioca_partita()
                            tornaIndietro = True
                        else:
                            tornaIndietro = False

            # Scelta = 0 <=> Esci dal gioco
            elif scelta == "0":
                    self.__view.stampa_messaggio("Uscita in corso, alla prossima!")
                    continuare_gioco = False
            elif scelta in ("h", "help", "aiuto"):
                PartitaView(GiocatoreView(), TavoliereView()).stampa_aiuto()
                input("---- Premi INVIO per tornare al menu... ----")
            else:
                errore = "Errore nell'inserimento della scelta, riprova"
                self.get_view().stampa_messaggio(errore)
                errore = ""


    def __stringa_to_tempo_limite(self, stringa_tempo: str) -> timedelta:
        try:
            ore, minuti, secondi = map(int, stringa_tempo.split(":"))
            return timedelta(hours = ore, minutes = minuti, seconds = secondi)
        except ValueError:
            self.get_view().stampa_messaggio("Errore Formato Tempo")
            return None
