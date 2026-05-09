from View.quoridorView import QuoridorView
from partitaController import PartitaController
from tavoliereController import TavoliereController
from Model.partita import Partita
from View.partitaView import PartitaView


class QuoridorController:
    """Classe contenente l'esecuzione principale.

    Attributi
    ---------
    nome: menu
        Oggetto di QuoridorView e permette di visualizzare il menu
        e di visualizzare se ci sono errori

    Metodi
    -------
    nome: gioca()
        Esegue il menu principale e gestisce le scelte dell'utente
    """

    def __init__(self):
        self.__menu = QuoridorView()

    def gioca(self):
        while True:
            scelta: str = self.__menu.menu_di_gioco()

            if scelta == "1":
                partita = PartitaController(Partita(), PartitaView())
                partita.gioca_partita()
            elif scelta == "0":
                self.__menu.stampa_messaggio("Uscita in corso, alla prossima!")
                return
            else:
                self.__menu.stampa_messaggio(
                    "Errore nell'inserimento della scelta, riprova"
                )
