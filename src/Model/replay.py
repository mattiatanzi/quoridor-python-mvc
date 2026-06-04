from src.Model.nodo import Nodo

class ErroreReplay(Exception):
    """Eccezione che gestisce errori durante il replay."""
    
    pass

class ReplayPartita:
    """Classe ReplayPartita.
    
    DESCRIZIONE:
        Gestisce il replay animato di una partita appena conclusa.
        Ricostruisce gli stati del gioco riseguendo le mosse della trascrizione a partire
        da uno stato iniziale pulito.
        
    ATTRIBUTI:
    
        ------ COSTANTI ------
        
        - P1
            TIPO
                Privato, Tipo str
            DESCRIZIONE
                ID del giocatore 1
                
        - P2
            TIPO
                Privato, Tipo str
            DESCRIZIONE
                ID del giocatore 2
                
        - POSIZIONE_P1
            TIPO 
                Privato, Tipo Nodo
            DESCRIZIONE 
                Posizione iniziale del giocatore 1
                
        - POSIZIONE_P2
            TIPO 
                Privato, Tipo Nodo
            DESCRIZIONE 
                Posizione iniziale del giocatore 2
                
        - MURI_INIZIALI
            TIPO    
                Privato, Tipo int
            DESCRIZIONE
                Numero di muri inizlai per ogni giocatore

    """
    
    # Costanti
    __P1 = "P1"
    __P2 = "P2"
    __POSIZIONE_P1 = Nodo("e1")
    __POSIZIONE_P2 = Nodo("e9")
    __MURI_INIZIALI = 10