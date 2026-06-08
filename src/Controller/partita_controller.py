import copy
import time

from src.Controller.replay_controller import ErroreReplay, ReplayController
from src.Model.giocatore import ErrorePosizione
from src.Model.partita import ErroreFormattazione, ErrorePartita, Partita
from src.Model.tavoliere import ErroreTavoliere
from src.View.partita_view import PartitaView
from src.View.replay_view import ReplayView


class PartitaController:
    """Classe PartitaController.

    DESCRIZIONE:
        Il controller della partita in corso.

    ATTRIBUTI:

        - model
            TIPO
                Privato, tipo Partita

            DESCRIZIONE
                Il modello della Partita

        - view
            TIPO
                Privato, tipo PartitaView

            DESCRIZIONE
                Responsabile della gestione di stampa e input della Partita

        - snapshot_iniziale
            TIPO
                Privato, tipo Partita
            DESCRIZIONE
                Una copia dello stato iniziale del gioco

    COSTANTI:
        - LUNGHEZZA_COMANDO_MURO
            Si riferisce alla lunghezza di un comando relativo al piazzamento di un
            qualsiasi muro.

        - LUNGHEZZA_COMANDO_MOSSA
            Si riferisce alla lunghezza di un comando relativo ad un movimento
            del pedone.

        - COMANDI_ABBANDONA_PARTITA
            Tutti i comandi possibili per abbandonare la partita

        - COMANDI_USCITA_GIOCO
            Tutti i comandi possibili per uscire dal gioco

        - COMANDI_TRASCRIZIONE
            Tutti i comandi possibili per visualizzare la trascrizione delle mosse

    METODI:

        ------ COSTRUTTORI ------

        def __init__(self, model: Partita, view: PartitaView):
            DESCRIZIONE
                Costruttore di Base.
                Data un modello Partita e un PartitaView restituisce
                un PartitaController

        ------ ACCESSO ATTRIBUTI PRIVATI ------

        def get_model(self) -> Partita:
            DESCRIZIONE
                Restituisce il Model di Partita contenuto nel Controller

        def set_model(self, model: Partita):
            DESCRIZIONE
                Modifica il Model di Partita nel Controller

        def get_view(self) -> PartitaView:
            DESCRIZIONE
                Restituisce la classe responsabile del View di Partita contenuta nel
                Controller

        def set_view(self, view: PartitaView):
            DESCRIZIONE
                Modifica la classe responsabile del View di Partita contenuta nel
                Controller
        def get_snapshot_iniziale(self) -> Partita:
            DESCRIZIONE
                Restituisce la copia dello stato della partita

        ------ MODIFICATORI / OSSERVATORI ------

        def get_giocatore(self, id):
            DESCRIZIONE
                Restituisce un giocatore dato un id

        def aggiungi_giocatore(self, new_giocatore):
            DESCRIZIONE
                Aggiunge il giocatore in input alla partita.
                Il giocatore non verrà aggiunto se è già in partita o se
                fosse raggiunto.
                il massimo numero di giocatori in partita.

        def rimuovi_giocatore(self, id):
            DESCRIZIONE
                Rimuove il giocatore con l'id in input dalla partita (Se il giocatore
                risulta essere in partita).

        def gioca_partita(self):
            DESCRIZIONE
                Permette di avviare giocare una partita, stampa la partita in corso e
                prende i dati di input dall'utente e gestice il dato (muovere il
                giocatore, posizionare un muro, tornare al menu, abbandonare il gioco)

        def __trasforma_trascrizione(self, trascrizione:list[str])->list[tuple[str,str]]
            DESCRIZIONE
                Permette di trasformare la trascrizione in una lista di tuple in modo
                tale da stampare correttamente la mossa attualmente eseguita nel replay

        def __ottieni_trascrizione_parziale(self,trascrizione_completa:list[str],
            indice: int)-> list[str]:
            DESCRIZIONE
                Permette di trasformare la trascrizione in una lista in modo
                tale da stampare correttamente la trascrizione pre il replay
    """

    # Attributi

    __model: Partita
    __view: PartitaView
    __snapshot_iniziale: Partita

    # Metodi

    # Costanti

    __LUNGHEZZA_COMANDO_MURO = 3
    __LUNGHEZZA_COMANDO_MOSSA = 2

    __COMANDI_ABBANDONA_PARTITA = {"quit", "abbandona"}
    __COMANDI_USCITA_GIOCO = {"exit", "esci"}
    __COMANDI_TRASCRIZIONE = {"trascrizione", "trascrizione mosse", "mosse"}
    __COMANDI_REPLAY = {"replay", "r"}
    __COMANDI_REPLAY_AUTOMATICO = {"replay automatico", "ra"}

    __COMANDI_AVANTI = {"next", "avanti", "n", ""}
    __COMANDI_INDIETRO = {"prev", "indietro", "p", "back"}
    # Costruttore

    def __init__(self, model: Partita, view: PartitaView):
        self.set_model(model)
        self.set_view(view)
        self.__snapshot_iniziale = copy.deepcopy(model)

    # Accesso Attributi Privati

    def get_model(self) -> Partita:
        return self.__model

    def set_model(self, model: Partita):
        self.__model = model

    def get_view(self) -> PartitaView:
        return self.__view

    def set_view(self, view: PartitaView):
        self.__view = view

    def get_snapshot_iniziale(self) -> Partita:
        return self.__snapshot_iniziale

    # Modificatori / Osservatori

    def get_giocatore(self, id):
        try:
            return self.get_model().get_giocatore(id)
        except ErrorePartita as errPart:
            messaggio = f"Errore Giocatore in Partita. {errPart}"
            self.get_view().stampa_errore_partita(messaggio)

    def aggiungi_giocatore(self, new_giocatore):
        try:
            self.get_model().aggiungi_giocatore(new_giocatore)
        except ErrorePartita as errPart:
            messaggio = f"Errore Numero Giocatori in Partita. {errPart}"
            self.get_view().stampa_errore_partita(messaggio)

    def rimuovi_giocatore(self, id):
        try:
            self.get_model().rimuovi_giocatore(id)
        except ErrorePartita as errPart:
            messaggio = f"Errore Numero Giocatori in Partita. {errPart}"
            self.get_view().stampa_errore_partita(messaggio)

    def __trasforma_trascrizione(
        self, trascrizione: list[str]
    ) -> list[tuple[str, str]]:
        mosse_flat: list[tuple[str, str]] = []

        for turno in trascrizione:
            # Rimuove il numero del turno (es. da "1. e2 e8" a "e2 e8")
            giocatori = sorted([g.get_id() for g in self.__model.get_giocatori()])
            parti = turno.split(". ", 1)
            if len(parti) < 2:
                continue
            mosse_turno = parti[1].split()

            # Assegna ogni mossa al rispettivo giocatore in base all'ordine
            for i, mossa in enumerate(mosse_turno):
                if i < len(giocatori):
                    id_giocatore = giocatori[i]
                    mosse_flat.append((id_giocatore, mossa))

        return mosse_flat

    def __ottieni_trascrizione_parziale(
        self, trascrizione_completa: list[str], indice: int
    ) -> list[str]:
        if indice == 0:
            return []
        risultato = []
        turni_completi = indice // 2

        # Aggiunge tutti i turni completati
        for i in range(turni_completi):
            risultato.append(trascrizione_completa[i])

        # Se il turno è a metà (ha mosso solo P1), spezza l'ultima stringa
        if indice % 2 != 0:
            parti = trascrizione_completa[turni_completi].split()
            # Ricostruisce la riga con solo la mossa del giocatore 1 (es. "1. e2")
            risultato.append(f"{parti[0]} {parti[1]}")

        return risultato

    def gioca_partita(self) -> bool:
        errore = ""
        continuare_partita = True
        continuare_gioco = True

        while continuare_partita and continuare_gioco:
            self.__view.stampa_partita(self.get_model())
            self.get_view().stampa_errore_partita(errore)
            azione = self.__view.get_input()
            id_giocatore_attivo = self.__model.get_id_giocatore_attivo()
            giocatore_attivo = self.get_giocatore(id_giocatore_attivo)

            errore = ""

            # Pulizia input utente
            azione_pulita = azione.strip().lower()

            # Aiuto
            if azione_pulita in ["help", "aiuto"]:
                self.__view.stampa_aiuto()
                input("---- Premi INVIO per tornare alla partita... ----")
                # La richiesta di aiuto non incrementa il turno
                continue

            elif azione_pulita in self.__COMANDI_TRASCRIZIONE:
                if not self.__model.get_trascrizione():
                    errore = "Errore: Trascrizione vuota"
                else:
                    self.__view.stampa_trascrizione(
                        self.__model.get_trascrizione(),
                        len(self.__model.get_giocatori()),
                    )
                    input("---- Premi INVIO per tornare alla partita... ----")

            # Uscire dalla partita
            elif azione_pulita in self.__COMANDI_ABBANDONA_PARTITA:
                # Messaggi per chiedere conferma
                messaggio_conferma = (
                    "Uscita In Corso...\nSicuro di voler "
                    "abbandonare la partita? [si/no]"
                )
                risposta = ""

                # Stampa Fin quando l'utente non decide
                while risposta != "si" and risposta != "no":
                    risposta = self.get_view().chiedi_input_utente(messaggio_conferma)
                else:
                    if risposta == "si":
                        continuare_partita = False

            # Uscire dal gioco
            elif azione in self.__COMANDI_USCITA_GIOCO:
                messaggio_conferma = (
                    "Uscita In Corso...\nSicuro di voler uscire dal gioco? [si/no]"
                )
                risposta = ""

                while risposta != "si" and risposta != "no":
                    risposta = self.get_view().chiedi_input_utente(messaggio_conferma)
                else:
                    if risposta == "si":
                        continuare_gioco = False

            # Piazzamento muro
            elif len(azione_pulita) == self.__LUNGHEZZA_COMANDO_MURO:
                try:
                    self.__model.piazza_muro(azione_pulita, giocatore_attivo)
                    self.__model.rimuovi_un_muro_giocatore(id_giocatore_attivo)
                except ErroreFormattazione as err_from:
                    errore = err_from
                except ErroreTavoliere as err_tav:
                    errore = err_tav
                except ErrorePartita as err_part:
                    errore = err_part
                # Solo se non ci sono eccezioni si continua con il flusso
                else:
                    # Prima di incrementare il turno salva la trascrizione
                    self.__model.aggiungi_mossa_trascrizione(azione_pulita)
                    self.__model.incrementa_turno()

            # Mossa
            elif len(azione_pulita) == self.__LUNGHEZZA_COMANDO_MOSSA:
                if azione_pulita[0].isalpha() and azione_pulita[1].isdigit():
                    try:
                        self.__model.muovi_giocatore(azione_pulita, giocatore_attivo)
                    except ErrorePosizione as err_pos:
                        errore = f"Errore movimento: {err_pos}"
                    # Solo se non ci sono eccezioni si continua con il flusso
                    else:
                        # Prima di eseguire le logiche della mossa salva la trascrizione
                        self.__model.aggiungi_mossa_trascrizione(azione_pulita)
                        # Controllo vittoria
                        vincitore = self.__model.verifica_vittoria()

                        # Vittoria
                        if vincitore is not None:
                            # Stampa tabellone per mostrare la mossa vincente
                            self.__view.stampa_partita(self.__model)

                            # Stampa vittoria
                            self.__view.stampa_vittoria(vincitore)

                            # Richiedi input per tornare al menu
                            scelta_pulita = (
                                self.get_view().chiedi_input_utente().lower().strip()
                            )

                            # Stampa fin quando utente non decide di tornare al menù
                            while (
                                scelta_pulita != "m"
                                or scelta_pulita in self.__COMANDI_TRASCRIZIONE
                            ):
                                errore = ""
                                self.get_view().stampa_vittoria(vincitore)
                                if scelta_pulita in self.__COMANDI_TRASCRIZIONE:
                                    self.__view.stampa_trascrizione(
                                        self.__model.get_trascrizione(),
                                        len(self.__model.get_giocatori()),
                                    )
                                if (
                                    scelta_pulita in self.__COMANDI_REPLAY
                                    or scelta_pulita in self.__COMANDI_REPLAY_AUTOMATICO
                                ):
                                    partita_replay = self.get_snapshot_iniziale()

                                    trascrizione_replay = (
                                        self.__model.get_trascrizione()
                                    )

                                    trascrizione_replay_flat = (
                                        self.__trasforma_trascrizione(
                                            trascrizione_replay
                                        )
                                    )

                                    replay = ReplayController(
                                        trascrizione_replay_flat, partita_replay
                                    )

                                    stampa_replay = ReplayView()
                                    autoplay = False

                                    def callback_aggiorna_schermo(
                                        stato: Partita,
                                        descrizione: str,
                                        _rep=replay,
                                        _trasc=trascrizione_replay,
                                        _st_re=stampa_replay,
                                        _auto=autoplay,
                                    ):
                                        # 1.Chiede al replay a che numero di mossa siamo
                                        indice = _rep.get_indice_corrente()

                                        # 2. Usa la tua funzione per tagliare la lista
                                        lista_tagliata = (
                                            self.__ottieni_trascrizione_parziale(
                                                _trasc, indice
                                            )
                                        )

                                        # 3. Manda alla View lo stato, la stringa in
                                        # basso, e la lista di destra!
                                        _st_re.stampa_replay(
                                            stato, descrizione, lista_tagliata, _auto
                                        )

                                    replay.set_on_stato_cambiato(
                                        callback_aggiorna_schermo
                                    )

                                    # Prima stampa per mostrare l'inizio
                                    callback_aggiorna_schermo(
                                        replay.get_stato_corrente(),
                                        replay.get_descrizione_corrente(),
                                    )
                                    if scelta_pulita in self.__COMANDI_REPLAY:
                                        ris = True

                                        while ris:
                                            scelta_replay = (
                                                self.get_view().chiedi_input_utente()
                                            )
                                            n = replay.get_indice_corrente()
                                            if (
                                                n == replay.get_totale_mosse()
                                                and ris == self.__COMANDI_AVANTI
                                            ):
                                                errore = (
                                                    "Errore: Impossibile"
                                                    " andare avanti, mosse terminate"
                                                )
                                            if (
                                                n == 0
                                                and ris == self.__COMANDI_INDIETRO
                                            ):
                                                errore = (
                                                    "Errore: Impossibile "
                                                    "andare indietro, stai ancora "
                                                    "all'inizio del replay"
                                                )
                                        try:
                                            ris = replay.esegui_comando(scelta_replay)
                                        except ErroreReplay as err_com:
                                            errore = err_com
                                    else:
                                        autoplay = True
                                        while not replay.replay_fine():
                                            replay.avanza()
                                            time.sleep(1.5)

                                    scelta_pulita = ""
                                else:
                                    self.get_view().stampa_errore_partita(errore)
                                    scelta_pulita = (
                                        self.get_view()
                                        .chiedi_input_utente()
                                        .lower()
                                        .strip()
                                    )

                            else:
                                continuare_partita = False

                        # Nessuna vittoria
                        self.__model.incrementa_turno()

                else:
                    errore = "Formato errato: usa una lettera (a-i) e un numero (1-9)."

            # Input sconosciuto
            else:
                errore = "Comando non riconosciuto"

        return continuare_gioco
