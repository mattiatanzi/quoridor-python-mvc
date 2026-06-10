from textual.widgets import Button

from src.Model.costanti_tavoliere import Costanti
from src.Model.giocatore import Giocatore
from src.Model.nodo import Nodo
from src.Model.tavoliere import Tavoliere
from src.View.tavoliere_view import TavoliereviewAstratta


class TavoliereViewTUI(TavoliereviewAstratta):
    """Gestisce la stampa a schermo dei muri e dei giocatori."""
    
    __COSTANTI = Costanti()

    def __init__(self, app_condivisa):
        self.__app = app_condivisa

    def stampa_tavoliere(self, tavoliere: Tavoliere, giocatori: set[Giocatore]):
        """Aggiorna la grafica di Textual leggendo Grafo e Giocatori."""
        
        def aggiorna_grafica():
            schermo = self.__app.screen
            
            # ==========================================
            # FASE 1: PULIZIA GENERALE
            # ==========================================
            for btn in schermo.query(".casella"):
                # Rimuoviamo muri e colori dei giocatori
                btn.remove_class("muro-sotto", "muro-destra", "giocatore-1", "giocatore-2","giocatore-3","giocatore-4")
                # Svuotiamo il testo del bottone
                btn.label = "" 

            # ==========================================
            # FASE 2: DISEGNO DEI MURI (Lettura Grafo)
            # ==========================================
            i = self.__COSTANTI.PRIMA_RIGA 
            while i >= self.__COSTANTI.ULTIMA_RIGA:
                j = self.__COSTANTI.PRIMA_COLONNA
                while j <= self.__COSTANTI.ULTIMA_COLONNA:
                    col_lettera = self.__COSTANTI.COLONNE[j]
                    chiave_attuale = Nodo(f"{col_lettera}{i}")
                    
                    try:
                        btn = schermo.query_one(f"#btn_{col_lettera}{i}", Button)

                        # Muro Orizzontale (Sotto)
                        if i > self.__COSTANTI.ULTIMA_RIGA:
                            if tavoliere.get_adiacente(chiave_attuale, self.__COSTANTI.ARCO_ADIACENTE_SOTTO) == self.__COSTANTI.NO_ARCO:
                                btn.add_class("muro-sotto")

                        # Muro Verticale (Destra)
                        if j < self.__COSTANTI.ULTIMA_COLONNA:
                            if tavoliere.get_adiacente(chiave_attuale, self.__COSTANTI.ARCO_ADIACENTE_DESTRA) == self.__COSTANTI.NO_ARCO:
                                btn.add_class("muro-destra")
                    except Exception:
                        pass 
                    
                    j += 1
                i -= 1

            # ==========================================
            # FASE 3: PIAZZAMENTO GIOCATORI 
            # ==========================================
            # Usiamo enumerate per dare un indice (1 o 2) utile per il colore CSS
            for indice, g in enumerate(giocatori, start=1):
                # Otteniamo direttamente la stringa "e1" o "e9"
                coordinata = g.get_posizione().get_valore_id_nodo() 
                nome_giocatore = g.get_id() # "P1" o "P2"
                
                try:
                    # Andiamo a colpo sicuro sul bottone corretto!
                    btn_giocatore = schermo.query_one(f"#btn_{coordinata}", Button)
                    
                    # Scriviamo "P1" sul bottone
                    btn_giocatore.label = nome_giocatore
                    
                    # Aggiungiamo la classe CSS per colorarlo
                    btn_giocatore.add_class(f"giocatore-{indice}")
                except Exception:
                    pass

        # Eseguiamo in sicurezza
        self.__app.call_from_thread(aggiorna_grafica)