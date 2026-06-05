from src.Model.partita import Partita
from src.Model.replay_partita import ErroreReplay, ReplayPartita


class ReplayController:
    """Classe ReplayController.
    
    DESCRIZIONE
        Controller per il replay animato di una partita appena conclusa
        
        Gestisce tutta la logica di navigazione del replay, separando 
        logica e presentazione.
        
        La View viene chiamata tramite callback cosi il controllo rimane
        indipendente dell'implementazione grafica (CLI o TUI)
    
    ATTRIBUTI
        
        ------ VARIABILI ------
        
        - model 
            TIPO
                Privato, tipo ReplayPartita
            DESCRIZIONE
                Il modello del replay
        
        - on_stato_cambiato
            TIPO
                Callable[[Partita, str], None] | None
            DESCRIZIONE
                Callback opzionale chiamata ogni volta che lo stato del replay cambia.
                Riceve lo stato corrente della partita e una stringa descrittiva della
                mossa corrente. Viene lasciata a None finchè non viene impostata
                dalla View.
        
        ------ COSTANTI ------
        
        - COMANDI_AVANTI
            Set di stirnghe riconosciute per avanzare di un passo
        
        - COMANDI_INDIETRO
            Set di stringhe riconosciute per tornare indietro di un passo
            
        - COMANDI_FINE
            Set di stringhe per saltare all'ultimo stato
        
        - COMANDI_INIZIO
            Set di stringhe per tornare allo stato iniziale
            
        - COMANDI_ESCI
            Set di stringhe per uscire dal replay
            
    METODI
    
        ------ COSTRUTTORE ------
        
        - __init__(self, trascrizione: list[str]):
            DESCRIZIONE
                Costruttore di Base.
                Data la trascrizione di una partita crea il ReplayController.
                
        ------ ACCESSO ATTRIBUTI ------
        
        - set_on_stato_cambiato(self, callback)
            DESCRIZIONE
                Imposta il callback chiamato ad ogni scabmio di stato.
                Il callback deve accettare (partita: Partita, descrizione: str)
                
        - get_model(self) -> ReplayPartita
            DESCRIZIONE
                Restituisce il model del replay.
                
        ------ NAVIGAZIONE ------
        
        - avanza(self) -> bool:
            DESCRIZIONE
                Avanza al passo successivo. Chiama il callback se impostato.
                Restituisce True se l'avanzamento è avvenuto.
 
        - torna_indietro(self) -> bool:
            DESCRIZIONE
                Torna al passo precedente. Chiama il callback se impostato.
                Restituisce True se il ritorno è avvenuto.
 
        - vai_a_inizio(self):
            DESCRIZIONE
                Posiziona il replay allo stato iniziale.
 
        - vai_a_fine(self):
            DESCRIZIONE
                Posiziona il replay all'ultimo stato.
 
        - vai_a(self, indice: int) -> bool:
            DESCRIZIONE
                Posiziona il replay all'indice specificato.
                Restituisce True se l'operazione ha avuto successo,
                False altrimenti (indice non valido).
 
        - get_stato_corrente(self) -> Partita:
            DESCRIZIONE
                Restituisce lo stato corrente della partita.
 
        - get_descrizione_corrente(self) -> str:
            DESCRIZIONE
                Restituisce una stringa descrittiva del passo corrente.
                
                Formato: "Mossa N/TOT - <id_giocatore>: <mossa>" (passi > 0)
 
        - replay_inizio(self) -> bool:
            DESCRIZIONE
                True se il replay è allo stato iniziale.
 
        - replay_fine(self) -> bool:
            DESCRIZIONE
                True se il replay è all'ultimo stato.
 
        - get_totale_mosse(self) -> int:
            DESCRIZIONE
                Restituisce il numero totale di mosse nel replay.
        
        ------ ESECUZIONE COMANDI TESTUALI ------
        
        - replay_ha_mosse(self) -> bool
            DESCRIZIONE
                Restituisce true se la partita ha avuto almeno una mossa.
        
        - esegui_comando(self, comando: str) -> bool
            DESCRIZIONE
                Interpreta ed esegue un comando testuale del replay.
                
                I comandi si riferiscono alle diverse costanti e fanno riferimento a:
                - andare avanti
                - andare indietro
                - uscire
                - andare al primo stato
                - andare all'ultimo stato
                
        ------ PRIVATI ------
        
        - notifica_cambio_stato(self)
            DESCRIZIONE
                Chiama il callback on_stato_cambiato se impostato.
        
    """
    
    # Costanti comandi testuali (CLI)
    COMANDI_AVANTI = {"next", "avanti", "n", ""}
    COMANDI_INDIETRO = {"prev", "indietro", "p", "back"}
    COMANDI_FINE = {"end", "fine", "last"}
    COMANDI_INIZIO = {"start", "inizio", "first"}
    COMANDI_ESCI = {"exit", "esci", "stop", "quit"}
    
    # Metodi
    
    # ------ Costruttori ------ #
    def __init__(self, trascrizione: list[str]):
        self.__model = ReplayPartita(trascrizione)
        self.__on_stato_cambiato = None
        
    # ------ Accesso Attributi ------- #
    def set_on_stato_cambiato(self, callback):
        self.__on_stato_cambiato = callback
        
    def get_model(self) -> ReplayPartita:
        return self.__model
    
    # ------ Navigazione ------ #
    def avanza(self) -> bool:
        avanzato = self.__model.avanza()
        if avanzato:
            self.__notifica_cambio_stato()
        return avanzato
    
    def torna_indietro(self) -> bool: 
        tornato = self.__model.torna_indietro()
        if tornato:
            self.__notifica_cambio_stato()
        return tornato
    
    def vai_a_inizio(self):
        self.__model.vai_a(0)
        self.__notifica_cambio_stato()
        
    def vai_a_fine(self):
        self.__model.vai_a(self.__model.get_totale_mosse())
        self.__notifica_cambio_stato()
        
    def vai_a(self, indice: int) -> bool:
        try:
            self.__model.vai_a(indice)
            self.__notifica_cambio_stato()
            return True
        except ErroreReplay:
            return False
    
    def get_stato_corrente(self) -> Partita:
        return self.__model.get_stato_corrente()

    def get_descrizione_corrente(self) -> str:
        mossa_info = self.__model.get_mossa_corrente()
        numero = self.__model.get_numero_mossa_corrente()
        
        if mossa_info is None:
            return numero
        
        id_giocatore, mossa = mossa_info
        return f"{numero} - {id_giocatore}: {mossa}"
    
    def replay_inizio(self) -> bool:
        return self.__model.replay_inizio()
    
    def replay_fine(self) -> bool:
        return self.__model.replay_fine()
    
    def get_totale_mosse(self) -> int:
        return self.__model.get_totale_mosse()
    
    # ------ Esecuzione comandi testuali ------ #
    def replay_ha_mosse(self) -> bool:
        return self.__model.get_totale_mosse() > 0
    
    def esegui_comando(self, comando: str) -> bool:
        cmd = comando.strip().lower()
        
        if cmd in self.COMANDI_ESCI:
            return False
        elif cmd in self.COMANDI_AVANTI:
            self.avanza()
        elif cmd in self.COMANDI_INDIETRO:
            self.torna_indietro()
        elif cmd in self.COMANDI_FINE:
            self.vai_a_fine()
        elif cmd in self.COMANDI_INIZIO:
            self.vai_a_inizio()
        else: 
            raise ErroreReplay("Comando non riconosciuto")
            # Eventuale metodo view (?)
        
        return True
         
    # ------ Privati ------ #
    def __notifica_cambio_stato(self):
        if self.__on_stato_cambiato is not None:
            self.__on_stato_cambiato(
                self.get_stato_corrente(), 
                self.get_descrizione_corrente()
                )
    
    