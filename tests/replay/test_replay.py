import pytest
import copy

from src.Controller.replay_controller import ReplayController
from src.Model.giocatore import Giocatore
from src.Model.nodo import Nodo
from src.Model.partita import Partita
from src.Model.tavoliere import Tavoliere
from src.Model.replay_partita import ErroreReplay


@pytest.fixture
def dati_replay_standard():
    """Fixture che simula 2 turni di gioco e restituisce (snapshot_iniziale, trascrizione)."""
    tavoliere = Tavoliere()
    g1 = Giocatore("P1", new_posizione=Nodo("e1"))
    g2 = Giocatore("P2", new_posizione=Nodo("e9"))
    partita = Partita(tavoliere, {g1, g2})

    # 1. Salviamo lo snapshot iniziale
    snapshot_iniziale = copy.deepcopy(partita)

    # 2. Simuliamo il Turno 1
    partita.set_id_giocatore_attivo("P1")
    partita.muovi_giocatore("e2", partita.get_giocatore("P1"))
    partita.aggiungi_mossa_trascrizione("e2")
    partita.incrementa_turno()

    partita.set_id_giocatore_attivo("P2")
    partita.muovi_giocatore("e8", partita.get_giocatore("P2"))
    partita.aggiungi_mossa_trascrizione("e8")
    partita.incrementa_turno()

    trascrizione = partita.get_trascrizione()
    
    return snapshot_iniziale, trascrizione


class TestReplayInizializzazione:
    """Suite di test per la corretta generazione degli stati del Replay."""

    def test_compilazione_stati_standard(self, dati_replay_standard):
        """Verifica che il ReplayController generi gli stati corretti a partire dalla trascrizione.

        Classi di equivalenza:
            CE1: Trascrizione valida con mosse pedone regolari.

        Oracolo:
            CE1 => Il controller viene istanziato senza errori.
            CE1 => Il numero totale di mosse riconosciute deve essere 2.
            CE1 => Lo stato finale (indice massimo) deve avere i giocatori nelle posizioni finali.
        """
        snapshot, trascrizione = dati_replay_standard
        
        # Inizializziamo il Controller del Replay (che a sua volta istanzia ReplayPartita)
        replay_ctrl = ReplayController(trascrizione, snapshot)

        # Oracolo 1: Il sistema ha letto correttamente 2 mosse
        assert replay_ctrl.get_totale_mosse() == 2

        # Oracolo 2: Verifichiamo che all'ultimo stato i giocatori siano effettivamente mossi
        replay_ctrl.vai_a_fine()
        stato_finale = replay_ctrl.get_stato_corrente()
        
        assert stato_finale.get_giocatore("P1").get_posizione().get_valore_id_nodo() == "e2"
        assert stato_finale.get_giocatore("P2").get_posizione().get_valore_id_nodo() == "e8"
        
class TestReplayNavigazione:
    """Suite di test per la navigazione degli stati all'interno del Replay."""

    def test_navigazione_base(self, dati_replay_standard):
        """Verifica la corretta navigazione passo-passo (avanti e indietro).

        Classi di equivalenza:
            CE1: Comando avanza() in condizioni standard (ci sono mosse successive).
            CE2: Comando torna_indietro() in condizioni standard (ci sono mosse precedenti).

        Oracolo:
            CE1 => avanza() restituisce True e l'indice corrente incrementa di 1.
            CE2 => torna_indietro() restituisce True e l'indice corrente decrementa di 1.
        """
        snapshot, trascrizione = dati_replay_standard
        replay_ctrl = ReplayController(trascrizione, snapshot)

        # Assicuriamoci di essere all'inizio
        assert replay_ctrl.get_indice_corrente() == 0

        # CE1: Avanziamo di un passo
        esito_avanza = replay_ctrl.avanza()
        assert esito_avanza is True
        assert replay_ctrl.get_indice_corrente() == 1

        # CE2: Torniamo indietro di un passo
        esito_indietro = replay_ctrl.torna_indietro()
        assert esito_indietro is True
        assert replay_ctrl.get_indice_corrente() == 0

    def test_navigazione_limiti(self, dati_replay_standard):
        """Verifica la tenuta della navigazione quando si raggiungono gli estremi.

        Condizioni particolari:
            CP1: Tentativo di avanza() quando si è già all'ultima mossa.
            CP2: Tentativo di torna_indietro() quando si è allo Stato 0.

        Oracolo:
            CP1 => avanza() restituisce False, l'indice non supera il totale_mosse.
            CP2 => torna_indietro() restituisce False, l'indice resta a 0.
        """
        snapshot, trascrizione = dati_replay_standard
        replay_ctrl = ReplayController(trascrizione, snapshot)

        totale_mosse = replay_ctrl.get_totale_mosse()

        # CP1: Saltiamo alla fine e proviamo ad andare ancora avanti
        replay_ctrl.vai_a_fine()
        assert replay_ctrl.get_indice_corrente() == totale_mosse
        
        esito_avanza_fuori_limite = replay_ctrl.avanza()
        assert esito_avanza_fuori_limite is False
        assert replay_ctrl.get_indice_corrente() == totale_mosse  # L'indice non deve sforare

        # CP2: Saltiamo all'inizio e proviamo ad andare ancora indietro
        replay_ctrl.vai_a_inizio()
        assert replay_ctrl.get_indice_corrente() == 0
        
        esito_indietro_fuori_limite = replay_ctrl.torna_indietro()
        assert esito_indietro_fuori_limite is False
        assert replay_ctrl.get_indice_corrente() == 0  # L'indice non deve scendere in negativo