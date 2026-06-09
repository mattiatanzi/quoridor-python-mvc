from src.Controller.partita_controller import PartitaController
from src.Model.giocatore import Giocatore
from src.Model.nodo import Nodo
from src.Model.partita import Partita
from src.Model.tavoliere import Tavoliere
from src.View.giocatore_view_CLI import GiocatoreViewCLI
from src.View.partita_view_CLI import PartitaViewCLI
from src.View.quoridor_view_CLI import QuoridorViewCLI
from src.View.tavoliere_view_CLI import TavoliereViewCLI


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

    def __init__(self,toi: bool):
        if toi:
            self.__menu = QuoridorViewCLI()
        # aggiungere else per view in Gui
    def gioca(self):
        errore: str = ""
        continuare_gioco = True
        while continuare_gioco:
            self.__menu.menu_di_gioco()
            self.__menu.stampa_messaggio(errore)
            scelta: str = self.__menu.get_input_menu()

            errore = ""
            if scelta == "1":
                tavoliere = Tavoliere()

                giocatore1 = Giocatore(
                    self.__P1, self.__POSIZIONE_P1, self.__MURI_INIZIALI
                )
                giocatore2 = Giocatore(
                    self.__P2, self.__POSIZIONE_P2, self.__MURI_INIZIALI
                )
                giocatori = {giocatore1, giocatore2}

                view_giocatore = GiocatoreViewCLI() # Se GUI si crea GiocatoreViewGUI
                view_tavoliere = TavoliereViewCLI() # Se GUI si crea TavoliereViewGUI
                partita = PartitaController(
                    Partita(tavoliere, giocatori),
                    PartitaViewCLI(view_giocatore, view_tavoliere),# Se gui si cre aPartita View GuI
                )
                continuare_gioco = partita.gioca_partita()
            elif scelta == "0":
                self.__menu.stampa_messaggio("Uscita in corso, alla prossima!")
                return
            else:
                errore = "Errore nell'inserimento della scelta, riprova"
