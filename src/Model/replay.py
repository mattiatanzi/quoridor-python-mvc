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
                
        ------ VARIABILI ------
 
        - mosse_flat
            TIPO
                Privato, Lista di tuple (str, str)
            DESCRIZIONE
                Lista piatta di (id_giocatore, mossa) estratta dalla
                trascrizione, nell'ordine in cui le mosse sono state
                eseguite durante la partita.
                Esempio:
                    [("P1", "e2"), ("P2", "e8"), ("P1", "e3h"), ...]
                    
    METODI:

        ------ UTILITÀ ------
        
    - parse_trascrizione(self, trascrizione: list[str]) -> list[tuple[str, str]]
        DESRCIZIONE
            Converte la trascrizione in una lista piatta 
            di (giocatore, mossa).
    
            La trascrizione ha il formato: ["1. e2 e8", "2. e3h d7v", ...]
            dove ogni elemento del turno può contenere 1 o 2 mosse
            (la seconda mossa potrebbe mancare nell'ultimo turno se P2
            non ha giocato prima della fine).
 
    """
    
    # Costanti
    __P1 = "P1"
    __P2 = "P2"
    __POSIZIONE_P1 = Nodo("e1")
    __POSIZIONE_P2 = Nodo("e9")
    __MURI_INIZIALI = 10
    
    # Metodi
    def __parse_trascrizione(self, trascrizione: list[str]) -> list[tuple[str, str]]:
        
        mosse_flat: list[tuple[str, str]] = []
        for turno in trascrizione:
            # Rimuove il numero del turno e divide le mosse
            parti = turno.split(". ", 1)
            if len(parti) < 2:
                continue
            mosse_turno = parti[1].split()
            
            # P1 parte per primo
            giocatori_turno = [self.__P1, self.__P2]
            for i, mossa in enumerate(mosse_turno):
                if i < len(giocatori_turno):
                    mosse_flat.append((giocatori_turno[i], mossa))
                    
        return mosse_flat