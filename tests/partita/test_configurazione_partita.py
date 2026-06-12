from datetime import timedelta

from src.Model.costanti_giocatore import CostantiGiocatore
from src.Model.giocatore import Giocatore


class TestConfigurazionePartitaTimer:
    """Suite di test funzionali per la configurazione dei timer a inizio partita.

    Verifica che il sistema assegni i corretti limiti temporali a seconda del numero
    di giocatori (2 o 4) e della tipologia di partita scelta.
    """

    def test_partita_due_giocatori_con_timer(self):
        """Verifica la configurazione per una partita standard a 2 giocatori con tempo limite.

        Classi di equivalenza
            Input di Configurazione:
                CE1, NUM_GIOCATORI : n = 2
                CE2, TIMER         : tempo_iniziale > 0 (Standard)

        Oracolo:
            - Vengono istanziati esattamente 2 giocatori.
            - Entrambi i giocatori devono avere `possiede_limite_tempo() == True`.
            - Il tempo residuo iniziale deve corrispondere al profilo selezionato.
        """
        tempo_scelto = timedelta(minutes=5)

        # Simuliamo la creazione dei giocatori per la partita a 2
        g1 = Giocatore(new_id_giocatore="P1", new_tempo_iniziale=tempo_scelto)
        g2 = Giocatore(new_id_giocatore="P2", new_tempo_iniziale=tempo_scelto)
        lista_giocatori = [g1, g2]

        # Verifica dimensione della partita (CE1)
        assert len(lista_giocatori) == 2

        # Verifica Oracolo sui Timer (CE2)
        for g in lista_giocatori:
            assert g.possiede_limite_tempo() is True
            assert g.ha_finito_tempo() is False
            assert g.get_tempo_residuo() == tempo_scelto

    def test_partita_quattro_giocatori_con_timer(self):
        """Verifica la configurazione per una partita a 4 giocatori con tempo limite.

        Classi di equivalenza
            Input di Configurazione:
                CE1, NUM_GIOCATORI : n = 4
                CE2, TIMER         : tempo_iniziale > 0 (Standard)

        Oracolo:
            - Vengono istanziati esattamente 4 giocatori.
            - Tutti e 4 i giocatori hanno il limite di tempo attivo (`True`).
            - Tutti i timer sono sincronizzati sullo stesso valore iniziale.
        """
        tempo_scelto = timedelta(minutes=10)

        # Simuliamo la creazione dei giocatori per la partita a 4
        lista_giocatori = [
            Giocatore(new_id_giocatore="P1", new_tempo_iniziale=tempo_scelto),
            Giocatore(new_id_giocatore="P2", new_tempo_iniziale=tempo_scelto),
            Giocatore(new_id_giocatore="P3", new_tempo_iniziale=tempo_scelto),
            Giocatore(new_id_giocatore="P4", new_tempo_iniziale=tempo_scelto),
        ]

        # Verifica dimensione (CE1)
        assert len(lista_giocatori) == 4

        # Verifica Oracolo sui Timer (CE2)
        for g in lista_giocatori:
            assert g.possiede_limite_tempo() is True
            assert g.get_tempo_residuo() == tempo_scelto

    def test_partita_senza_limite_tempo(self):
        """Verifica la configurazione di partite (a 2 o 4 giocatori) in modalità senza fine.

        Classi di equivalenza
            Input di Configurazione:
                CE1, NUM_GIOCATORI : n = 2 oppure n = 4 (Invariante per questo scenario)
                CE2, TIMER         : tempo_iniziale = DEF_SENZA_LIMITE_TEMPO (Irregolare)

        Oracolo:
            - Tutti i giocatori creati devono avere `possiede_limite_tempo() == False`.
            - Nessun giocatore deve risultare con il tempo già scaduto a inizio partita.
        """
        # Testiamo il comportamento accoppiando sia il caso a 2 che a 4 giocatori
        partita_2_giocatori = [
            Giocatore(
                new_id_giocatore="P1",
                new_tempo_iniziale=CostantiGiocatore.DEF_SENZA_LIMITE_TEMPO,
            ),
            Giocatore(
                new_id_giocatore="P2",
                new_tempo_iniziale=CostantiGiocatore.DEF_SENZA_LIMITE_TEMPO,
            ),
        ]

        partita_4_giocatori = [
            Giocatore(
                new_id_giocatore="P1",
                new_tempo_iniziale=CostantiGiocatore.DEF_SENZA_LIMITE_TEMPO,
            ),
            Giocatore(
                new_id_giocatore="P2",
                new_tempo_iniziale=CostantiGiocatore.DEF_SENZA_LIMITE_TEMPO,
            ),
            Giocatore(
                new_id_giocatore="P3",
                new_tempo_iniziale=CostantiGiocatore.DEF_SENZA_LIMITE_TEMPO,
            ),
            Giocatore(
                new_id_giocatore="P4",
                new_tempo_iniziale=CostantiGiocatore.DEF_SENZA_LIMITE_TEMPO,
            ),
        ]

        # Oracolo Partita a 2 senza tempo
        for g in partita_2_giocatori:
            assert g.possiede_limite_tempo() is False
            assert g.ha_finito_tempo() is False

        # Oracolo Partita a 4 senza tempo
        for g in partita_4_giocatori:
            assert g.possiede_limite_tempo() is False
            assert g.ha_finito_tempo() is False
