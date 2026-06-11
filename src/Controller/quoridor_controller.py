from src.Controller.parametri_partita_controller import ParametriPartitaController
from src.Controller.partita_controller import PartitaController
from src.Model.costanti_giocatore import CostantiGiocatore
from src.Model.costanti_partita import CostantiPartita
from src.Model.giocatore import Giocatore
from src.Model.nodo import Nodo
from src.Model.partita import Partita
from src.Model.tavoliere import Tavoliere
from src.View.quoridor_view import QuoridorViewAstratta
from src.View.partita_view import PartitaViewAstratta
from src.View.TUI.parametri_partita_view_TUI import ParametriPartitaViewTUI
from src.View.funzioni_utili_stampa import chiedi_input_utente



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
            Permette all'utente di settare i parametri per una partita e giocare.


    def __stringa_to_tempo_limite(self, stringa_tempo: str) -> timedelta:
        DESCRIZIONE
            Riceve in input un tempo sotto forma di stringa e lo converte nel corretto
            formato timedelta.
            In caso di errore di conversione lancia un'eccezione

            La stringa, per essere in formato corretto, deve essere nel formato
            HH:MM:SS
            Come indicato nel file delle costanti del Quoridor View


    """

    __view: QuoridorViewAstratta

    def __init__(self, quoridor_view: QuoridorViewAstratta, partita_view : PartitaViewAstratta):
        self.__menu = quoridor_view
        self.__partita_view = partita_view

        # aggiungere else per view in Gui
    def gioca(self):
        errore: str = ""
        continuare_gioco = True

        # Menu Principale
        while continuare_gioco:
            self.__menu.menu_di_gioco()
            self.__menu.stampa_messaggio(errore)
            scelta = self.__menu.get_input_menu()

            # Scelta = GIOCA
            if scelta == "1":
                if self.__menu.is_tui():
                    app = self.__menu.get_app()
                    coda = self.__menu.get_coda_input()
                    parametri_ctrl = ParametriPartitaController(
                        new_view=ParametriPartitaViewTUI(app, coda)
                    )
                else:
                    parametri_ctrl = ParametriPartitaController()
                parametri = parametri_ctrl.ottieni_parametri_utente()

                if parametri.get_avvia_partita():
                    tavoliere = Tavoliere()
                    giocatori = set()
                    ids_giocatori = []
                    for i in range(0, parametri.get_numero_giocatori()):
                        id_assegnato = CostantiGiocatore.POSSIBILI_ID_GIOCATORE[i]
                        ids_giocatori.append(id_assegnato)
                        giocatore = Giocatore(
                            new_id_giocatore=id_assegnato,
                            new_posizione=Nodo(
                                CostantiPartita.COORDINATE_INIZIALI[id_assegnato]
                            ),
                            new_tempo_iniziale=parametri.get_limite_tempo(),
                            new_muri_disponibili=CostantiPartita.MURI_DISPONIBILI.get(str(parametri.get_numero_giocatori()))
                        )
                        giocatori.add(giocatore)
                    self.__partita_view.avvia_interfaccia_partita(ids_giocatori)
                    partita = PartitaController(
                    Partita(tavoliere, giocatori),
                    self.__partita_view
                    )
                    continuare_gioco = partita.gioca_partita()
                if not continuare_gioco:
                    self.__partita_view.torna_al_menu()
            elif scelta == "0":
                self.__menu.stampa_messaggio("Uscita in corso, alla prossima!")
                continuare_gioco = False
            elif scelta in ("h", "help", "aiuto"):
                testo_aiuto = "=== GUIDA COMANDI ===\n\n1 - Avvia una nuova partita\n0 - Esci dal gioco"
                self.__menu.stampa_messaggio(testo_aiuto)
                chiedi_input_utente("-------- Premi INVIO per andare avanti ---------")
                
            else:
                errore = "Errore nell'inserimento della scelta, riprova\n"
