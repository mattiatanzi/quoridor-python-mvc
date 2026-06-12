from datetime import datetime

import copy
import time

from src.Controller.replay_controller import ErroreReplay, ReplayController
from src.Model.giocatore import ErrorePosizione
from src.Model.partita import ErroreFormattazione, ErrorePartita, Partita
from src.Model.tavoliere import ErroreTavoliere
from src.View.funzioni_utili_stampa import chiedi_input_utente
from src.View.partita_view import PartitaViewAstratta
from src.View.CLI.replay_view_CLI import ReplayViewCLI


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


    def __ottieni_trascrizione_parziale(
        self, trascrizione_completa: list[str], indice: int,num_giocatori: int
    ) -> list[str]:
        if indice == 0:
            return []
    
        risultato = []
        # Calcoliamo quanti round interi di mosse sono stati completati
        round_completi = indice // num_giocatori
        # Calcoliamo quante mosse sono state fatte nel round parziale corrente
        mosse_parziali = indice % num_giocatori

        # 1. Aggiunge tutti i round (stringhe) interamente completati
        for i in range(round_completi):
            risultato.append(trascrizione_completa[i])

        # 2. Se ci sono mosse fatte nel round corrente ma non completato
        if mosse_parziali > 0 and round_completi < len(trascrizione_completa):
            linea_corrente = trascrizione_completa[round_completi]
            parti = linea_corrente.split()
            
            # parti[0] è il numero del turno (es: "1."), parti[1:] sono le mosse.
            # Ricostruiamo la riga prendendo il numero turno + le mosse parziali.
            # Es: Se ho fatto 2 mosse su 4, prendo parti[0] (turno) + parti[1] + parti[2]
            nuova_linea = [parti[0]] + parti[1:mosse_parziali + 1]
            risultato.append(" ".join(nuova_linea))

        return risultato
    def gioca_partita(self) -> bool:
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
                    chiedi_input_utente("---- Premi INVIO per tornare alla partita... ----")
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
                        chiedi_input_utente("---- Premi INVIO per tornare alla partita... ----")

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
                                # Richiedi input per tornare al menu
                                scelta_pulita = (
                                    self.__view.get_input().lower().strip()
                                )
                                while scelta_pulita != "m":
                                    if (
                                        scelta_pulita in self.__COMANDI_REPLAY
                                        or scelta_pulita in self.__COMANDI_REPLAY_AUTOMATICO
                                    ):
                                        risultato_replay = self.gestisci_replay(scelta_pulita)
                                        if risultato_replay == "REPLAY_EXIT":
                                            # Forziamo il reset dell'input in modo che non riesegua il replay all'infinito
                                            scelta_pulita = ""
                                        else:
                                            errore = risultato_replay
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
                                    continuare_partita = False
                                    continue


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

                        # Prima di incrementare il turno salva la trascrizione
                        self.__model.aggiungi_mossa_trascrizione(azione_pulita)

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
                                    # Richiedi input per tornare al menu
                                    scelta_pulita = (
                                        self.__view.get_input().lower().strip()
                                    )
                                    while scelta_pulita != "m":
                                        if (
                                            scelta_pulita in self.__COMANDI_REPLAY
                                            or scelta_pulita in self.__COMANDI_REPLAY_AUTOMATICO
                                        ):
                                            risultato_replay = self.gestisci_replay(scelta_pulita)
                                            if risultato_replay == "REPLAY_EXIT":
                                                # Forziamo il reset dell'input in modo che non riesegua il replay all'infinito
                                                scelta_pulita = ""
                                            else:
                                                errore = risultato_replay
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
                                        continuare_partita = False
                                        continue


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

                            # Salva Trascrizione Prima delle logiche della mossa
                            self.__model.aggiungi_mossa_trascrizione(azione_pulita)

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
                                            f"Il giocatore {id_vincitore} è l'unico "
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
                                            errore = ""

                                            # --- GESTIONE REPLAY ---
                                            if (
                                                scelta_pulita in self.__COMANDI_REPLAY
                                                or scelta_pulita in self.__COMANDI_REPLAY_AUTOMATICO
                                            ):
                                                risultato_replay = self.gestisci_replay(scelta_pulita)
                                                if risultato_replay == "REPLAY_EXIT":
                                                    # Forziamo il reset dell'input in modo che non riesegua il replay all'infinito
                                                    scelta_pulita = ""
                                                else:
                                                    errore = risultato_replay

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


                            # Controllo vittoria
                            if continuare_partita:
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
                                            risultato_replay = self.gestisci_replay(scelta_pulita)
                                            if risultato_replay == "REPLAY_EXIT":
                                                # Forziamo il reset dell'input in modo che non riesegua il replay all'infinito
                                                scelta_pulita = ""
                                            else:
                                                errore = risultato_replay

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


    def gestisci_replay(self, modalita_replay):
        errore = ""
        partita_replay = self.get_snapshot_iniziale()
        trascrizione_replay = self.__model.get_trascrizione()

        replay = ReplayController(
            trascrizione_replay, partita_replay
        )
        
        stampa_replay = self.__view.crea_replay_view() 
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
            num_giocatori = len(stato.get_giocatori())
            lista_tagliata = self.__ottieni_trascrizione_parziale(
                _trasc, indice,num_giocatori=num_giocatori
            )
            _st_re.stampa_replay(
                stato,
                descrizione,
                lista_tagliata,
                _auto["autoplay"],
            )

        replay.set_on_stato_cambiato(callback_aggiorna_schermo)

        if modalita_replay in self.__COMANDI_REPLAY:
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

                scelta_replay = chiedi_input_utente()

                # Se l'utente preme invio a vuoto, consideriamolo come stringa vuota per andare avanti
                cmd_pulito = scelta_replay.strip().lower()

                try:
                    

                    n = replay.get_indice_corrente()
                    if n == replay.get_totale_mosse() and cmd_pulito in self.__COMANDI_AVANTI:
                        errore = "Errore: Impossibile andare avanti, mosse terminate"
                    if n == 0 and cmd_pulito in self.__COMANDI_INDIETRO:
                        errore = "Errore: Impossibile andare indietro, stai ancora all'inizio del replay"

                    ris = replay.esegui_comando(scelta_replay)

                    # SE IL COMANDO SEGNALA L'USCITA (False), INTERROMPIAMO IMMEDIATAMENTE IL CICLO
                    if not ris:
                        break
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

        # Alla fine del replay, restituiamo un flag speciale o puliamo l'errore
        # Ma soprattutto, dobbiamo dire al ciclo chiamante di resettare l'input!
        return "REPLAY_EXIT"
    

    