from datetime import timedelta

from src.Controller.parametri_partita_controller import ParametriPartitaController
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
    nome: view
        Oggetto di QuoridorView e permette di visualizzare il menu
        e di visualizzare se ci sono errori

    Metodi

    ------ ACCESSO ATTRIBUTI PRIVATI ------

    def get_view(self) -> QuoridorView:
        DESCRIZIONE
            Restituisce il View di Quoridor contenuto nel Controller

    def set_view(self, new_view: QuoridorView):
        DESCRIZIONE
            Modifica il View di Quoridor nel Controller

    ------ MODIFICATORI / OSSERVATORI ------

    def gioca():
        DESCRIZIONE
            Permette all'utente di scegliere in che modo giocare, mostrando a video
            diversi menu e successivamente crea una partita con i parametri scelti.
            È possibile viaggiare tra i menù con comandi mostrari a video.
            Per ogni menù è possibile tornare indietro (tranne per menù principale).

        Menù implementati:
            1. Menu Principale
            2. Menu Modalità Partita (Con / Senza Tempo)
                2a. Menu Scelta Tempo (Tempo breve, tempo medio, ...)

    def __stringa_to_tempo_limite(self, stringa_tempo: str) -> timedelta:
        DESCRIZIONE
            Riceve in input un tempo sotto forma di stringa e lo converte nel corretto
            formato timedelta.
            In caso di errore di conversione lancia un'eccezione

            La stringa, per essere in formato corretto, deve essere nel formato
            HH:MM:SS
            Come indicato nel file delle costanti del Quoridor View


    """

    __view: QuoridorView

    def __init__(self):
        self.set_view(QuoridorView())


    def get_view(self):
        return self.__view

    def set_view(self, new_view: QuoridorView):
        self.__view = new_view


    def gioca(self):
        errore: str = ""
        continuare_gioco = True

        # Menu Principale
        while continuare_gioco:

            self.get_view().menu_di_gioco()
            self.get_view().stampa_messaggio(errore)
            scelta = self.get_view().get_input_menu()

            # Scelta = GIOCA
            if scelta == "1":


                parametri = ParametriPartitaController().ottieni_parametri_utente()

                if (parametri.get_avvia_partita()):


                    tavoliere = Tavoliere()
                    giocatori = set()
                    for i in range(0, parametri.get_numero_giocatori()):
                        id_assegnato = CostantiGiocatore._POSSIBILI_ID_GIOCATORE[i]
                        giocatore = Giocatore(
                            new_id_giocatore=id_assegnato,
                            new_posizione=Nodo(CostantiPartita._COORDINATE_INIZIALI[id_assegnato]),
                            new_tempo_iniziale=parametri.get_limite_tempo()
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
                errore = "Errore nell'inserimento della scelta, riprova\n"
