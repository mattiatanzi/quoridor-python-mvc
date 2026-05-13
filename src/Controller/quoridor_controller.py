from Controller.partita_controller import PartitaController
from Model.giocatore import Giocatore
from Model.nodo import Nodo
from Model.partita import Partita
from Model.tavoliere import Tavoliere
from View.giocatore_view import GiocatoreView
from View.partita_view import PartitaView
from View.quoridor_view import QuoridorView
from View.tavoliere_view import TavoliereView


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

    __P1 = "P1"
    __P2 = "P2"

    __POSIZIONE_P1 = Nodo("e1")
    __POSIZIONE_P2 = Nodo("e9")

    __MURI_INIZIALI = 10

    def __init__(self):
        self.__menu = QuoridorView()

    def gioca(self):
        continuareGioco = True
        while continuareGioco:
            scelta: str = self.__menu.menu_di_gioco()

            if scelta == "1":
                tavoliere = Tavoliere()

                giocatore1 = Giocatore(
                    self.__P1, self.__POSIZIONE_P1, self.__MURI_INIZIALI
                )
                giocatore2 = Giocatore(
                    self.__P2, self.__POSIZIONE_P2, self.__MURI_INIZIALI
                )
                giocatori = {giocatore1, giocatore2}

                view_giocatore = GiocatoreView()
                view_tavoliere = TavoliereView()
                partita = PartitaController(
                    Partita(tavoliere, giocatori),
                    PartitaView(view_giocatore, view_tavoliere),
                )
                continuareGioco = partita.gioca_partita()
            elif scelta == "0":
                self.__menu.stampa_messaggio("Uscita in corso, alla prossima!")
                return
            else:
                self.__menu.stampa_messaggio(
                    "Errore nell'inserimento della scelta, riprova"
                )
