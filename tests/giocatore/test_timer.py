
from datetime import timedelta
from time import time

import pytest
from src.Model import giocatore
from src.Model.costanti_giocatore import CostantiGiocatore
from src.Model.giocatore import Giocatore, TempoException


class TestGiocatoreRiduciTempo:
    """Classe TestGiocatoreTimer.

    DESCRIZIONE
        Suite di test funzionali per le meccaniche del timer del Giocatore.
    """

    def test_giocatore_limite_tempo_regolare(self):
        """Verifica riduci_tempo() in caso di Giocatore con tempo limite regolare.

        Classi di equivalenza

            Input di riduci_tempo():
                CE1, INPUT : tempo_da_ridurre > 0
                CE2, INPUT : tempo_da_ridurre = 0
                CE3, INPUT : tempo_da_ridurre < 0

        Condizioni particolari
            CP1: tempo_da_ridurre = tempo_residuo
            CP2: tempo_da_ridurre > tempo_residuo

        Oracolo:
            CE1 => Il tempo viene ridotto regolarmente
            CE2 => Il tempo del giocatore rimane invariato
            CE3 => Viene sollevata un'eccezione (tempo in input irregolare)
            CP1 => Il tempo viene azzerato
            CP2 => Il tempo viene azzerato


        """
        classi_equivalenza = [
            timedelta(minutes = 1),
            timedelta(seconds = 0),
            timedelta(seconds = -1)
        ]

        # CE1
        giocatore_creato = Giocatore(new_tempo_iniziale = timedelta(minutes = 5))

        tempo_iniziale = giocatore_creato.get_tempo_residuo()
        tempo_da_ridurre = classi_equivalenza[0]
        giocatore_creato.riduci_tempo(tempo_da_ridurre)
        assert giocatore_creato.get_tempo_residuo() == tempo_iniziale - tempo_da_ridurre

        # CE2
        giocatore_creato = Giocatore(new_tempo_iniziale = timedelta(minutes = 5))

        tempo_da_ridurre = classi_equivalenza[1]
        giocatore_creato.riduci_tempo(tempo_da_ridurre)
        assert giocatore_creato.get_tempo_residuo() == tempo_iniziale

        # CE3
        giocatore_creato = Giocatore(new_tempo_iniziale = timedelta(minutes = 5))

        tempo_da_ridurre = classi_equivalenza[2]
        with pytest.raises(TempoException):
            giocatore_creato.riduci_tempo(tempo_da_ridurre)

        # CP1
        giocatore_creato = Giocatore(new_tempo_iniziale = timedelta(minutes = 5))

        tempo_da_ridurre = tempo_iniziale
        giocatore_creato.riduci_tempo(tempo_da_ridurre)
        assert giocatore_creato.get_tempo_residuo() == timedelta(0)

        # CP2
        giocatore_creato = Giocatore(new_tempo_iniziale = timedelta(minutes = 5))

        tempo_da_ridurre = tempo_iniziale + timedelta(minutes = 1)
        giocatore_creato.riduci_tempo(tempo_da_ridurre)
        assert giocatore_creato.get_tempo_residuo() == timedelta(0)


    def test_giocatore_senza_limite_tempo(self):
        """Verifica riduci_tempo() in caso di Giocatore con tempo limite irregolare.

            Input di riduci_tempo():
                CE1, INPUT : tempo > 0

        Oracolo:
            CE1 <=> Viene sollevata un'eccezione (il giocatore non ha limite di tempo)

        """
        # CE1
        giocatore_creato = Giocatore(new_tempo_iniziale = CostantiGiocatore.DEF_SENZA_LIMITE_TEMPO)


        tempo_da_ridurre = timedelta(seconds = 1)
        with pytest.raises(TempoException):
            giocatore_creato.riduci_tempo(tempo_da_ridurre)


    def test_giocatore_tempo_zero(self):
        """Verifica riduci_tempo() in caso di Giocatore con tempo limite regolare.

        Classi di equivalenza
            Input di riduci_tempo():
                CE1, INPUT : tempo > 0
                CE2, INPUT : tempo = 0
                CE3, INPUT : tempo < 0

        Oracolo:
            CE1 <=> Il tempo del giocatore rimane invariato
            CE2 <=> Il tempo del giocatore rimane invariato
            CE3 <=> Viene sollevata un'eccezione (tempo in input irregolare)

        """
        # CE1
        tempo_iniziale = timedelta(0)
        giocatore_creato = Giocatore(new_tempo_iniziale = tempo_iniziale)

        tempo_da_ridurre = timedelta(seconds = 1)
        with pytest.raises(TempoException):
            giocatore_creato.riduci_tempo(tempo_da_ridurre)

        # CE2
        tempo_iniziale = timedelta(0)
        giocatore_creato = Giocatore(new_tempo_iniziale = tempo_iniziale)

        tempo_da_ridurre = timedelta(0)
        with pytest.raises(TempoException):
            giocatore_creato.riduci_tempo(tempo_da_ridurre)

        # CE3
        with pytest.raises(TempoException):
            giocatore_creato.riduci_tempo(timedelta(seconds = -1))
