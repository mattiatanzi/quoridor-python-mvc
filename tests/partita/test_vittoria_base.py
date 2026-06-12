import pytest

from src.Model.giocatore import Giocatore
from src.Model.nodo import Nodo
from src.Model.partita import Partita
from src.Model.tavoliere import Tavoliere


@pytest.fixture
def partita_standard():
    """Fixture che inizializza una partita base a 2 giocatori."""
    tavoliere = Tavoliere()
    g1 = Giocatore("P1", new_posizione=Nodo("e1"))
    g2 = Giocatore("P2", new_posizione=Nodo("e9"))

    partita = Partita(tavoliere, {g1, g2})
    partita.set_id_giocatore_attivo("P1")
    return partita


class TestVittoriaBase:
    """Suite di test per le condizioni di vittoria del gioco."""

    def test_vittoria_raggiungimento_traguardo(self, partita_standard):
        """Verifica che P1 vinca arrivando sulla riga di fondo avversaria (riga 9).

        Classi di equivalenza:
            CE1: P1 entra in una casella della riga 9.

        Oracolo:
            CE1 => verifica_vittoria() restituisce l'ID 'P1'.
        """
        partita = partita_standard
        giocatore_p1 = partita.get_giocatore("P1")

        # Verifica preliminare: all'inizio nessuno ha vinto
        assert partita.verifica_vittoria() is None

        # Teletrasportiamo P1 a un passo dalla vittoria
        partita.set_posizione_giocatore("P1", Nodo("d8"))
        assert partita.verifica_vittoria() is None

        # Facciamo compiere a P1 il passo finale legittimo verso la riga 9
        partita.muovi_giocatore("d9", giocatore_p1)

        # Oracolo: Il sistema deve riconoscere P1 come vincitore assoluto
        assert partita.verifica_vittoria() == "P1"

    def test_nessuna_vittoria_se_arretra(self, partita_standard):
        """Verifica che un giocatore non vinca tornando sulla sua linea di partenza.

        Classi di equivalenza:
            CP1: P1 arretra ed entra in una casella della sua linea base.
        Oracolo:
            CP1 => verifica_vittoria() restituisce None.
        """
        partita = partita_standard
        giocatore_p1 = partita.get_giocatore("P1")

        # Mettiamo P1 vicino alla sua linea di partenza
        partita.set_posizione_giocatore("P1", Nodo("e2"))

        # Facciamo indietreggiare P1 verso la riga 1
        partita.muovi_giocatore("e1", giocatore_p1)

        # Oracolo: Non deve scattare assolutamente nessuna vittoria
        assert partita.verifica_vittoria() is None
