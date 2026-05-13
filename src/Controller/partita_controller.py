from src.Model.giocatore import ErrorePosizione
from src.Model.partita import ErroreFormattazione, ErrorePartita, Partita
from src.Model.tavoliere import ErroreTavoliere
from src.View.partita_view import PartitaView


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

    COSTANTI:
        - LUNGHEZZA_COMANDO_MURO
            Si riferisce alla lunghezza di un comando relativo al piazzamento di un
            qualsiasi muro.

        - LUNGHEZZA_COMANDO_MOSSA
            Si riferisce alla lunghezza di un comando relativo ad un movimento
            del pedone.

        - COMANDI_ABBANDONA_PARTITA
            Tutti i comandi possibili per abbandonare la partita


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

        ------ MODIFICATORI / OSSERVATORI ------

        def get_giocatore(self, id):
            DESCRIZIONE
                Restituisce un giocatore dato un id

        def aggiungi_giocatore(self, new_giocatore):
            DESCRIZIONE
                Aggiunge il giocatore in input alla partita.
                IL giocatore non verrà aggiunto se è già in partita o se
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
    """

    # Attributi

    __model: Partita
    __view: PartitaView

    # Metodi

    # Costanti

    __LUNGHEZZA_COMANDO_MURO = 3
    __LUNGHEZZA_COMANDO_MOSSA = 2

    __COMANDI_ABBANDONA_PARTITA = {"quit", "abbandona"}
    __COMANDI_USCITA_GIOCO = {"exit", "esci"}

    # Costruttore

    def __init__(self, model: Partita, view: PartitaView):
        self.set_model(model)
        self.set_view(view)

    # Accesso Attributi Privati

    def get_model(self) -> Partita:
        return self.__model

    def set_model(self, model: Partita):
        self.__model = model

    def get_view(self) -> PartitaView:
        return self.__view

    def set_view(self, view: PartitaView):
        self.__view = view

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

    def gioca_partita(self) -> bool:
        errore = ""
        continuarePartita = True
        continuareGioco = True

        while continuarePartita and continuareGioco:
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

            # Uscire dalla partita
            elif azione_pulita in self.__COMANDI_ABBANDONA_PARTITA:
                # Messaggi per chiedere conferma
                messaggioConferma = (
                    "Uscita In Corso...\nSicuro di voler "
                    "abbandonare la partita? [si/no]"
                )
                risposta = ""

                # Stampa Fin quando l'utente non decide
                while risposta != "si" and risposta != "no":
                    risposta = self.get_view().chiedi_input_utente(messaggioConferma)
                else:
                    if risposta == "si":
                        continuarePartita = False

            # Uscire dal gioco
            elif azione in self.__COMANDI_USCITA_GIOCO:
                messaggioConferma = (
                    "Uscita In Corso...\nSicuro di voler uscire dal gioco? [si/no]"
                )
                risposta = ""

                while risposta != "si" and risposta != "no":
                    risposta = self.get_view().chiedi_input_utente(messaggioConferma)
                else:
                    if risposta == "si":
                        continuareGioco = False

            # Piazzamento muro
            elif len(azione_pulita) == self.__LUNGHEZZA_COMANDO_MURO:
                try:
                    self.__model.piazza_muro(azione_pulita, giocatore_attivo)
                    self.__model.rimuovi_un_muro_giocatore(id_giocatore_attivo)
                    self.__model.incrementa_turno()
                except ErroreFormattazione as err_from:
                    errore = err_from
                except ErroreTavoliere as err_tav:
                    errore = err_tav
                except ErrorePartita as err_part:
                    errore = err_part

            # Mossa
            elif len(azione_pulita) == self.__LUNGHEZZA_COMANDO_MOSSA:
                if azione_pulita[0].isalpha() and azione_pulita[1].isdigit():
                    try:
                        self.__model.muovi_giocatore(azione_pulita, giocatore_attivo)

                        # Controllo vittoria
                        vincitore = self.__model.verifica_vittoria()

                        # Vittoria
                        if vincitore is not None:
                            # Stampa tabellone per mostrare la mossa vincente
                            self.__view.stampa_partita(self.__model)

                            # Stampa vittoria
                            self.__view.stampa_vittoria(vincitore)

                            # Terminazione partita
                            break

                        # Nessuna vittoria
                        self.__model.incrementa_turno()

                    except ErrorePosizione as err_pos:
                        errore = f"Errore movimento: {err_pos}"
                else:
                    errore = "Formato errato: usa una lettera (a-i) e un numero (1-9)."

            # Input sconosciuto
            else:
                errore = "Comando non riconosciuto"

        return continuareGioco
