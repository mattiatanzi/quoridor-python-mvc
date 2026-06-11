import pytest

from src.Model.costanti_partita import CostantiPartita
from src.Model.giocatore import Giocatore
from src.Model.nodo import Nodo
from src.Model.partita import ErroreFormattazione, Partita
from src.Model.tavoliere import Tavoliere


# Utilizziamo una fixture per preparare un'istanza "pulita" della partita
@pytest.fixture
def partita_iniziale_due_giocatori():
    """Fornisce una nuova istanza di Partita inizializzata correttamente."""
    tavoliere = Tavoliere()

    # Inizializziamo i giocatori in modo coerente sulle celle centrali delle righe base
    g1 = Giocatore("P1", new_posizione=Nodo("e1"))
    g2 = Giocatore("P2", new_posizione=Nodo("e9"))

    giocatori = {g1, g2}
    return Partita(tavoliere, giocatori)

class TestPartitaTrascrizione:
    """Suite di test funzionali per la trascrizione delle mosse in Partita."""

    def test_aggiungi_mossa_trascrizione_base(
        self, partita_iniziale_due_giocatori
    ):
        r"""Verifica che una mossa venga aggiunta correttamente allo storico.

        Classi di equivalenza:
            Input di aggiungi_mossa_trascrizione():
                CE1: Aggiunta prima mossa (P1) -> Inizio di un nuovo turno
                CE2: Aggiunta seconda mossa (P2) -> Completamento del turno corrente

        Oracolo:
            CE1 => Viene creata una nuova riga formattata con "1.\t{mossa}"
            CE2 => La mossa si accoda alla riga esistente separata da un tabulatore "\t"
        """
        # Assicuriamoci che tocchi al P1
        partita = partita_iniziale_due_giocatori
        
        # CE1: Mossa P1
        partita.set_id_giocatore_attivo(CostantiPartita.ID_PRIMO_GIOCATORE_ATTIVO)
        partita.aggiungi_mossa_trascrizione("e2")

        trascrizione = partita.get_trascrizione()
        assert len(trascrizione) == 1
        # Nota: L'implementazione attuale usa "\t" per separare le colonne
        assert trascrizione[0] == "1.\te2"

        # CE2: Mossa P2
        partita.set_id_giocatore_attivo("P2")
        partita.aggiungi_mossa_trascrizione("e3h")
        
        trascrizione_aggiornata = partita.get_trascrizione()
        assert len(trascrizione_aggiornata) == 1
        # La mossa del P2 si accoda sulla stessa riga, separata da "\t"
        assert trascrizione_aggiornata[0] == "1.\te2\te3h"

    def test_aggiungi_mossa_salto_turno(self):
        """Verifica la trascrizione quando un giocatore eliminato salta il turno.
        
        Classi di equivalenza:
            Input di aggiungi_mossa_trascrizione() in partita a 4 giocatori:
                CE1: P2 salta il turno, muove direttamente P3
                
        Oracolo:
            CE1 => Il sistema inserisce un segnaposto "---" nella colonna del
                   giocatore mancante.
        """
        # Setup rapido partita a 4 giocatori
        g1 = Giocatore("P1")
        g2 = Giocatore("P2")
        g3 = Giocatore("P3")
        g4 = Giocatore("P4")
        partita = Partita(Tavoliere(), {g1, g2, g3, g4})

        # Mossa P1
        partita.set_id_giocatore_attivo("P1")
        partita.aggiungi_mossa_trascrizione("e2")
        
        # P2 eliminato/salta, muove direttamente P3
        partita.set_id_giocatore_attivo("P3")
        partita.aggiungi_mossa_trascrizione("a6")

        trascrizione = partita.get_trascrizione()
        # L'oracolo prevede che il buco lasciato da P2 venga riempito da "---"
        assert trascrizione[0] == "1.\te2\t---\ta6"

class TestPartitaMeccanicheBase:
    """Suite di test funzionali per le meccaniche base di gioco della Partita."""

    def test_piazza_muro_formato_errato(self, partita_iniziale_due_giocatori):
        """Verifica input anomali sul piazzamento muro delegati alla classe Partita.

        Classi di equivalenza:
            Input di piazza_muro():
                CE1: Input di lunghezza errata (manca orientamento)
                CE2: Input con coordinate non valide per la scacchiera

        Oracolo:
            CE1 => Viene sollevata un'eccezione ErroreFormattazione
            CE2 => Viene sollevata un'eccezione ErroreFormattazione
        """
        partita = partita_iniziale_due_giocatori
        giocatore_attivo = partita.get_giocatore("P1")

        # CE1
        with pytest.raises(ErroreFormattazione):
            # Manca l'orientamento h/v (lunghezza 2 invece di 3)
            partita.piazza_muro("e5", giocatore_attivo)

        # CE2
        with pytest.raises(ErroreFormattazione):
            # Lettera fuori dalla scacchiera (es. z)
            partita.piazza_muro("z5h", giocatore_attivo)