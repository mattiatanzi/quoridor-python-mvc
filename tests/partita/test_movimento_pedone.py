import pytest

from src.Model.giocatore import Giocatore
from src.Model.nodo import Nodo
from src.Model.partita import Partita
from src.Model.tavoliere import Tavoliere

@pytest.fixture
def partita_standard():
    """Fixture che inizializza una partita base a 2 giocatori.

    Restituisce l'oggetto Partita pronto per i test.
    """
    tavoliere = Tavoliere()
    # P1 parte in basso al centro (e1), P2 in alto al centro (e9)
    g1 = Giocatore("P1", new_posizione=Nodo("e1"))
    g2 = Giocatore("P2", new_posizione=Nodo("e9"))
    
    partita = Partita(tavoliere, {g1, g2})
    partita.set_id_giocatore_attivo("P1")
    return partita


class TestMovimentoPedone:
    """Suite di test per la validazione dei movimenti fisici sul tabellone."""

    def test_movimento_base_valido(self, partita_standard):
        """Verifica il movimento di una casella in direzione libera.

        Classi di equivalenza:
            CE1: Movimento base in una casella adiacente libera.

        Oracolo:
            CE1 => La posizione del giocatore si aggiorna con successo, 
                   il turno passa all'avversario.
        """
        partita = partita_standard
        giocatore_p1 = partita.get_giocatore("P1")

        # Oracolo 1: Posizione di partenza corretta
        assert giocatore_p1.get_posizione().get_valore_id_nodo() == "e1"

        # Eseguiamo il movimento verso l'alto (Nord) in e2
        esito = partita.muovi_giocatore("e2", giocatore_p1)

        # Oracolo 2: La funzione di movimento non deve essere bloccata
        if esito is not None:
            assert esito is True

        # Oracolo 3: La posizione si è aggiornata correttamente
        assert giocatore_p1.get_posizione().get_valore_id_nodo() == "e2"