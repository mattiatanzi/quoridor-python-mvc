from datetime import datetime

import copy
import time

from src.Controller.replay_controller import ErroreReplay, ReplayController
from src.Model.giocatore import ErrorePosizione
from src.Model.partita import ErroreFormattazione, ErrorePartita, Partita
from src.Model.tavoliere import ErroreTavoliere
from src.View.partita_view import PartitaViewAstratta
from src.View.CLI.replay_view_CLI import ReplayViewCLI 
from src.View.funzioni_utili_stampa import chiedi_input_utente



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
    __view: PartitaViewAstratta
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

    def __init__(self, model: Partita, view: PartitaViewAstratta):
        self.set_model(model)
        self.set_view(view)
        self.__snapshot_iniziale = copy.deepcopy(model)

    # Accesso Attributi Privati

    def get_model(self) -> Partita:
        return self.__model

    def set_model(self, model: Partita):
        self.__model = model

    def get_view(self) -> PartitaViewAstratta:
        return self.__view

    def set_view(self, view: PartitaViewAstratta):
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
        ids_giocatori = [g.get_id() for g in self.get_model().get_giocatori()]
        # Dice alla view (e quindi all'App) di montare lo schermo della partita
        self.get_view().avvia_interfaccia_partita(ids_giocatori)
        
        errore = ""
        continuare_partita = True
        continuare_gioco = True

        
        while continuare_partita and continuare_gioco:
            self.__view.stampa_partita(self.get_model())
            self.get_view().stampa_errore_partita(errore)
            id_giocatore_attivo = self.__model.get_id_giocatore_attivo()
            giocatore_attivo = self.get_giocatore(id_giocatore_attivo)

            # Inizio a cronometrare il giocatore
            if giocatore_attivo.is_attivo():
                if giocatore_attivo.possiede_limite_tempo():
                    tempo_inizio_turno = datetime.now()

                azione = self.__view.get_input()
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
                        "Uscita In Corso...\n"
                        "Sicuro di voler abbandonare la partita?\n"
                        "[si/no]"
                    )
                    risposta = ""

                    # Stampa Fin quando l'utente non decide
                    while risposta != "si" and risposta != "no":
                        risposta = chiedi_input_utente(messaggio_conferma)
                    else:
                        if risposta == "si":
                            continuare_partita = False

                # Uscire dal gioco
                elif azione_pulita in self.__COMANDI_USCITA_GIOCO:
                    messaggio_conferma = (
                        "Uscita In Corso...\nSicuro di voler uscire dal gioco? [si/no]"
                    )
                    risposta = ""

                    while risposta != "si" and risposta != "no":
                        risposta = chiedi_input_utente(messaggio_conferma)
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
                        if giocatore_attivo.possiede_limite_tempo():
                            tempo_fine_turno = datetime.now()
                            giocatore_attivo.riduci_tempo(
                                tempo_fine_turno - tempo_inizio_turno
                            )
                            if giocatore_attivo.ha_finito_tempo():
                                self.get_model().elimina_giocatore(
                                    giocatore_attivo.get_id()
                                )

                                id_vincitore = self.__model.verifica_vittoria()
                                if id_vincitore:
                                    # Impostiamo il motivo richiesto
                                    motivo_vincita = (
                                        f"Il giocatore {id_vincitore} "
                                        "è l'unico rimasto in partita"
                                    )
                                    # Mostriamo la schermata di vittoria comune
                                    self.__view.stampa_vittoria(
                                        id_vincitore, motivo_vincita
                                    )

                                    replay = ReplayController(
                                        trascrizione_replay_flat, partita_replay
                                    )

                                    stampa_replay = ReplayViewCLI()
                                    autoplay = {"autoplay": False}  # Modificato in
                                    # dizionario perché in python i booleani non sono
                                    # oggetti mutable, mentre i dizionari lo sono

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
                                            stato,
                                            descrizione,
                                            lista_tagliata,
                                            _auto["autoplay"],
                                        )

                                    replay.set_on_stato_cambiato(
                                        callback_aggiorna_schermo
                                    )

                                    if scelta_pulita in self.__COMANDI_REPLAY:
                                        ris = True
                                        # Prima stampa per mostrare l'inizio
                                        callback_aggiorna_schermo(
                                            replay.get_stato_corrente(),
                                            replay.get_descrizione_corrente(),
                                        )
                                        while ris:
                                            if errore != "":
                                                callback_aggiorna_schermo(
                                                    replay.get_stato_corrente(),
                                                    replay.get_descrizione_corrente(),
                                                )

                                            self.__view.stampa_errore_partita(errore)

                                            errore = ""
                                            scelta_replay = (
                                                self.get_view().chiedi_input_utente()
                                            )
                                            try:
                                                ris = replay.esegui_comando(
                                                    scelta_replay
                                                )

                                                n = replay.get_indice_corrente()
                                                if (
                                                    n == replay.get_totale_mosse()
                                                    and scelta_replay
                                                    in self.__COMANDI_AVANTI
                                                ):
                                                    errore = (
                                                        "Errore: Impossibile"
                                                        " andare avanti, mosse "
                                                        "terminate"
                                                    )
                                                if (
                                                    n == 0
                                                    and scelta_replay
                                                    in self.__COMANDI_INDIETRO
                                                ):
                                                    errore = (
                                                        "Errore: Impossibile "
                                                        "andare indietro, stai ancora "
                                                        "all'inizio del replay"
                                                    )
                                            except ErroreReplay as err_com:
                                                errore = err_com
                                    else:
                                        autoplay["autoplay"] = True
                                        callback_aggiorna_schermo(
                                            replay.get_stato_corrente(),
                                            replay.get_descrizione_corrente(),
                                        )
                                        time.sleep(1.5)
                                        while not replay.replay_fine():
                                            replay.avanza()
                                            time.sleep(1.5)

                                    scelta_pulita = ""
                                else:
                                    self.get_view().stampa_errore_partita(errore)
                                    scelta_pulita = (
                                        self.__view.get_input().lower().strip()
                                    )
                                    while scelta_pulita != "m":
                                        self.__view.stampa_vittoria(
                                            id_vincitore, motivo_vincita
                                        )
                                        scelta_pulita = (
                                            self.__view.get_input().lower().strip()
                                        )
                                    else:
                                        continuare_partita = False
                                        continue

                        # Prima di incrementare il turno salva la trascrizione
                        self.__model.aggiungi_mossa_trascrizione(azione_pulita)
                        self.__model.incrementa_turno()

                # Mossa
                elif len(azione_pulita) == self.__LUNGHEZZA_COMANDO_MOSSA:
                    if azione_pulita[0].isalpha() and azione_pulita[1].isdigit():
                        try:
                            self.__model.muovi_giocatore(
                                azione_pulita, giocatore_attivo
                            )
                        except ErrorePosizione as err_pos:
                            errore = f"Errore movimento: {err_pos}"
                        # Solo se non ci sono eccezioni si continua con il flusso
                        else:
                            if giocatore_attivo.possiede_limite_tempo():
                                tempo_fine_turno = datetime.now()
                                giocatore_attivo.riduci_tempo(
                                    tempo_fine_turno - tempo_inizio_turno
                                )
                                if giocatore_attivo.ha_finito_tempo():
                                    self.get_model().elimina_giocatore(
                                        giocatore_attivo.get_id()
                                    )

                                    id_vincitore = self.__model.verifica_vittoria()
                                    if id_vincitore:
                                        # Impostiamo il motivo richiesto
                                        motivo_vincita = (
                                            f"Il giocatore {id_vincitore} è l'unico"
                                            "rimasto in partita"
                                        )
                                        # Mostriamo la schermata di vittoria comune
                                        self.__view.stampa_vittoria(
                                            id_vincitore, motivo_vincita
                                        )
                                        # Richiedi input per tornare al menu
                                        scelta_pulita = (
                                            self.__view.get_input().lower().strip()
                                        )
                                        while scelta_pulita != "m":
                                            self.__view.stampa_vittoria(
                                                id_vincitore, motivo_vincita
                                            )
                                            scelta_pulita = (
                                                self.__view.get_input().lower().strip()
                                            )
                                        else:
                                            continuare_partita = False
                                            # Blocca Ciclo Turno Corrente
                                            continue

                            # Salva Trascrizione Prima delle logiche della mossa
                            self.__model.aggiungi_mossa_trascrizione(azione_pulita)
                            # Controllo vittoria
                            id_vincitore = self.__model.verifica_vittoria()

                            # Vittoria
                            if id_vincitore is not None:
                                # Stampa tabellone per mostrare la mossa vincente
                                self.__view.stampa_partita(self.__model)

                                # Stampa vittoria
                                motivo_vincita = (
                                    "Ha raggiunto con successo la linea di fondo"
                                    "avversaria!"
                                )

                                # Stampa vittoria e motivo
                                self.__view.stampa_vittoria(
                                    id_vincitore, motivo_vincita
                                )

                                # Richiedi input per tornare al menu o avviare replay/trascrizione
                                scelta_pulita = self.__view.get_input().lower().strip()

                                # Ciclo fin quando l'utente non decide di tornare al menù
                                while scelta_pulita != "m":
                                    errore = ""
                                    
                                    # --- GESTIONE REPLAY ---
                                    if (
                                        scelta_pulita in self.__COMANDI_REPLAY
                                        or scelta_pulita in self.__COMANDI_REPLAY_AUTOMATICO
                                    ):
                                        partita_replay = self.get_snapshot_iniziale()
                                        trascrizione_replay = self.__model.get_trascrizione()
                                        trascrizione_replay_flat = self.__trasforma_trascrizione(
                                            trascrizione_replay
                                        )

                                        replay = ReplayController(
                                            trascrizione_replay_flat, partita_replay
                                        )
                                        stampa_replay = ReplayViewCLI(self.__view.get_tavoliere_view(),self.__view) # da implementare con scelta TUI
                                        autoplay = {"autoplay": False}

                                        def callback_aggiorna_schermo(
                                            stato: Partita,
                                            descrizione: str,
                                            _rep=replay,
                                            _trasc=trascrizione_replay,
                                            _st_re=stampa_replay,
                                            _auto=autoplay,
                                        ):
                                            indice = _rep.get_indice_corrente()
                                            lista_tagliata = self.__ottieni_trascrizione_parziale(
                                                _trasc, indice
                                            )
                                            _st_re.stampa_replay(
                                                stato,
                                                descrizione,
                                                lista_tagliata,
                                                _auto["autoplay"],
                                            )

                                        replay.set_on_stato_cambiato(callback_aggiorna_schermo)

                                        if scelta_pulita in self.__COMANDI_REPLAY:
                                            ris = True
                                            callback_aggiorna_schermo(
                                                replay.get_stato_corrente(),
                                                replay.get_descrizione_corrente(),
                                            )
                                            while ris:
                                                if errore != "":
                                                    callback_aggiorna_schermo(
                                                        replay.get_stato_corrente(),
                                                        replay.get_descrizione_corrente(),
                                                    )
                                                    self.__view.stampa_errore_partita(errore)
                                                    errore = ""
                                                
                                                scelta_replay = self.get_view().chiedi_input_utente()
                                                try:
                                                    ris = replay.esegui_comando(scelta_replay)
                                                    n = replay.get_indice_corrente()
                                                    if n == replay.get_totale_mosse() and scelta_replay in self.__COMANDI_AVANTI:
                                                        errore = "Errore: Impossibile andare avanti, mosse terminate"
                                                    if n == 0 and scelta_replay in self.__COMANDI_INDIETRO:
                                                        errore = "Errore: Impossibile andare indietro, stai ancora all'inizio del replay"
                                                except ErroreReplay as err_com:
                                                    errore = err_com
                                        else:
                                            autoplay["autoplay"] = True
                                            callback_aggiorna_schermo(
                                                replay.get_stato_corrente(),
                                                replay.get_descrizione_corrente(),
                                            )
                                            time.sleep(1.5)
                                            while not replay.replay_fine():
                                                replay.avanza()
                                                time.sleep(1.5)
                                        
                                        # Alla fine del replay, svuotiamo la scelta per richiedere nuovamente input
                                        scelta_pulita = ""

                                    # --- GESTIONE TRASCRIZIONE ---
                                    elif scelta_pulita in self.__COMANDI_TRASCRIZIONE:
                                        self.__view.stampa_trascrizione(
                                            self.__model.get_trascrizione(),
                                            len(self.__model.get_giocatori()),
                                        )
                                        # Dopo aver stampato la trascrizione, svuotiamo per ristampare la vittoria
                                        scelta_pulita = ""

                                    # --- GESTIONE INPUT NON RICONOSCIUTI O RIPRISTINO SCHERMATA ---
                                    else:
                                        if scelta_pulita != "":
                                            self.__view.stampa_errore_partita("Comando non riconosciuto. Inserisci 'm' per il menù, 'r' per il replay o 'mosse' per la trascrizione.")
                                        
                                        # Ristampa la schermata di vittoria e aspetta un nuovo comando
                                        self.__view.stampa_vittoria(id_vincitore, motivo_vincita)
                                        scelta_pulita = self.__view.get_input().lower().strip()
                                        
                                else:
                                    # L'utente ha premuto "m"
                                    continuare_partita = False
                            else:
                                # Nessuna vittoria
                                self.__model.incrementa_turno()

                    else:
                        errore = (
                            "Formato errato: usa una lettera (a-i) e un numero (1-9)."
                        )

                    # Input sconosciuto
                else:
                    errore = "Comando non riconosciuto"
            else:
                self.get_model().incrementa_turno()
        return continuare_gioco
