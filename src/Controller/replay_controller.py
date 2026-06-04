class ReplayController:
    """Classe ReplayController.
    
    DESCRIZIONE
        Controller per il replay animato di una partita appena conclusa
        
        Gestisce tutta la logica di navigazione del replay, separando 
        logica e presentazione.
        
        La View viene chiamata tramite callback cosi il controllo rimane
        indipendente dell'implementazione grafica (CLI o TUI)
        
        
        
        
        
        
    """
    
    # Costanti comandi testuali (CLI)
    COMANDI_AVANTI = {"next", "avanti", "n", ""}
    COMANDI_INDIETRO = {"prev", "indietro", "p", "back"}
    COMANDI_FINE = {"end", "fine", "last"}
    COMANDI_INIZIO = {"start", "inizio", "first"}
    COMANDI_ESCI = {"exit", "esci", "stop", "quit"}
        
        