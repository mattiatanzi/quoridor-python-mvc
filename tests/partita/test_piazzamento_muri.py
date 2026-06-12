import pytest

from src.Model.giocatore import Giocatore
from src.Model.nodo import Nodo
from src.Model.partita import ErrorePartita, Partita
from src.Model.tavoliere import ErroreTavoliere, Tavoliere


@pytest.fixture
def partita_standard():
    """Fixture che inizializza una partita base a 2 giocatori per i muri."""
    tavoliere = Tavoliere()
    g1 = Giocatore("P1", new_posizione=Nodo("e1"))
    g2 = Giocatore("P2", new_posizione=Nodo("e9"))

    partita = Partita(tavoliere, {g1, g2})
    partita.set_id_giocatore_attivo("P1")
    return partita


class TestPiazzamentoMuri:
    """Suite di test per la validazione del piazzamento dei muri."""

    def test_piazzamento_valido(self, partita_standard):
        """Verifica che un muro venga piazzato correttamente in una zona libera.

        Classi di equivalenza:
            CE1: Piazzamento valido.

        Oracolo:
            CE1 => Nessuna eccezione sollevata (il Tavoliere accetta il muro).
        """
        partita = partita_standard
        giocatore_p1 = partita.get_giocatore("P1")

        # Piazziamo un muro orizzontale valido (e3h)
        partita.piazza_muro("e3h", giocatore_p1)

        # Se il codice arriva qui senza lanciare eccezioni
        # significa che il piazzamento base è stato accettato dal Model.
        assert True

    def test_piazzamento_muri_esauriti(self, partita_standard):
        """Verifica il blocco della mossa se il giocatore non ha più muri.

        Classi di equivalenza:
            CE2: Piazzamento con muri esauriti.

        Oracolo:
            CE2 => Eccezione ErrorePartita sollevata.
        """
        partita = partita_standard
        giocatore_p1 = partita.get_giocatore("P1")

        # Portiamo a 0 i muri del giocatore usando il setter apposito
        partita.set_muri_disponibili_giocatore("P1", 0)

        # Proviamo a piazzare un muro, ci aspettiamo un ErrorePartita
        with pytest.raises(ErrorePartita):
            partita.piazza_muro("e3h", giocatore_p1)

    def test_sovrapposizione_muro(self, partita_standard):
        """Verifica che non si possano sovrapporre fisicamente due muri.

        Classi di equivalenza:
            CE3: Sovrapposizione parziale o totale.

        Oracolo:
            CE3 => Eccezione sollevata dal sistema.
        """
        partita = partita_standard
        giocatore_p1 = partita.get_giocatore("P1")
        giocatore_p2 = partita.get_giocatore("P2")

        # P1 piazza legittimamente il muro orizzontale in e3h
        partita.piazza_muro("e3h", giocatore_p1)

        # P2 prova a piazzare un muro verticale che si incrocia esattamente al centro
        with pytest.raises(ErroreTavoliere):
            partita.piazza_muro("e3v", giocatore_p2)
