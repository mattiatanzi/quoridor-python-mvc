import pytest

from src.Model.costanti_partita import CostantiPartita
from src.Model.giocatore import Giocatore
from src.Model.nodo import Nodo
from src.Model.partita import Partita
from src.Model.tavoliere import Tavoliere
from src.Model.partita import ErroreFormattazione


# Utilizziamo una fixture per preparare un'istanza "pulita" della partita
@pytest.fixture
def partita_iniziale():
    """Fornisce una nuova istanza di Partita inizializzata correttamente."""
    tavoliere = Tavoliere()
    
    # Inizializziamo i giocatori in modo coerente sulle celle centrali delle righe base
    g1 = Giocatore("P1", new_posizione=Nodo("e1"))
    g2 = Giocatore("P2", new_posizione=Nodo("e9"))
    
    giocatori = {g1, g2}
    return Partita(tavoliere, giocatori)

# TEST 1: Classe di equivalenza VALIDA
def test_aggiungi_mossa_trascrizione_valida(partita_iniziale):
    """Verifica che una mossa venga aggiunta e formattata correttamente allo storico."""
    # Assicuriamoci che tocchi al P1
    partita_iniziale.set_id_giocatore_attivo(CostantiPartita.ID_PRIMO_GIOCATORE_ATTIVO)
    
    # Simulo l'inserimento di una mossa valida (es. pedone in e2)
    partita_iniziale.aggiungi_mossa_trascrizione("e2")
    trascrizione = partita_iniziale.get_trascrizione()
    
    assert len(trascrizione) == 1
    # Verifica del padding e del numero di turno applicato dal Model
    assert trascrizione[0] == "1. e2 "
    
    # Simulo una seconda mossa (P2 piazza muro orizzontale)
    partita_iniziale.set_id_giocatore_attivo("P2")
    partita_iniziale.aggiungi_mossa_trascrizione("e3h")
    trascrizione_aggiornata = partita_iniziale.get_trascrizione()
    
    assert len(trascrizione_aggiornata) == 1
    # La mossa del P2 si accoda sulla stessa riga, separata dallo spazio
    assert trascrizione_aggiornata[0] == "1. e2  e3h"
    
# TEST 2: Classe di equivalenza NON VALIDA (Formattazione errata su piazzamento muro)
def test_piazza_muro_formato_errato(partita_iniziale):
    """Verifica input anomali sul piazzmento muro."""
    giocatore_attivo = partita_iniziale.get_giocatore("P1")
    
    with pytest.raises(ErroreFormattazione):
        # Manca l'orientamento h/v
        partita_iniziale.piazza_muro("e5", giocatore_attivo)
        
    with pytest.raises(ErroreFormattazione):
        # Lettera fuori dalla scacchiera (es. z)
        partita_iniziale.piazza_muro("z5h", giocatore_attivo)
        
# TEST 3: Classe non valida (Valore nullo o vuoto)
def test_aggiungi_mossa_trascrizione_stringa_vuota(partita_iniziale):
    """Verifica che una stringa vuota blocchi l'esecuzione."""
    partita_iniziale.set_id_giocatore_attivo(CostantiPartita.ID_PRIMO_GIOCATORE_ATTIVO)
    
    with pytest.raises(ErroreFormattazione):
        partita_iniziale.aggiungi_mossa_trascrizione("")
        
    # Verifica fondamentale: nessuna riga di turno inutile creata
    assert len(partita_iniziale.get_trascrizione()) == 0