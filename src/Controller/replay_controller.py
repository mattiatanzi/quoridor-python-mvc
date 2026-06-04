from src.Model.replay_partita import ErroreReplay, ReplayPartita
from src.Model.partita import Partita

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
        
        ------ COSTANTI ------
        
        - COMANDO_AVANTI
            Set di stirnghe riconosciute per avanzare di un passo
        
        - COMANDO_INDIETRO
            Set di stringhe riconosciute per tornare indietro di un passo
            
        - COMANDO_FINE
            Set di stringhe per saltare all'ultimo stato
        
        - COMANDO_INIZIO
            Set di stringhe per tornare allo stato iniziale
            
        - COMANDO_ESCI
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
        
        