
from datetime import timedelta

import pytest
from src.Model.costanti_giocatore import CostantiGiocatore
from src.Model.giocatore import Giocatore, TempoException


class TestGiocatoreTimer:
    """Classe TestGiocatoreTimer.

    DESCRIZIONE
        Suite di test funzionali per le meccaniche del timer del Giocatore.
    """

    def test_giocatore_senza_limite_tempo(self):
        """Verifica comportamento del giocatore senza limite di tempo.

        Classi di equivalenza:
            CE2 (Giocatore Senza Limite tempo)

        """
        giocatore_creato = Giocatore(new_tempo_iniziale = CostantiGiocatore.DEF_SENZA_LIMITE_TEMPO)

        assert giocatore_creato.possiede_limite_tempo() is False
        assert giocatore_creato.ha_finito_tempo() is False

        with pytest.raises(TempoException) as err:
            giocatore_creato.riduci_tempo(timedelta(seconds=1))
