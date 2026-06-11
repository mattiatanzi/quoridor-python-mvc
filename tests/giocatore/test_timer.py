
from datetime import timedelta

import pytest
from src.Model.costanti_giocatore import CostantiGiocatore
from src.Model.giocatore import Giocatore, TempoException


class TestGiocatoreRiduciTempo:
    """Classe TestGiocatoreRiduciTempo.

    DESCRIZIONE
        Suite di test funzionali per la funzione riduci_tempo()
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
            timedelta(0),
            timedelta(minutes = -1)
        ]

        # CE1
        giocatore_creato = Giocatore(new_tempo_iniziale = timedelta(minutes = 5))

        tempo_iniziale = giocatore_creato.get_tempo_residuo()
        tempo_da_ridurre = classi_equivalenza[0]

        assert giocatore_creato.riduci_tempo(tempo_da_ridurre) is True
        assert giocatore_creato.get_tempo_residuo() == tempo_iniziale - tempo_da_ridurre

        # CE2
        giocatore_creato = Giocatore(new_tempo_iniziale = timedelta(minutes = 5))

        tempo_iniziale = giocatore_creato.get_tempo_residuo()
        tempo_da_ridurre = classi_equivalenza[1]

        assert giocatore_creato.riduci_tempo(tempo_da_ridurre) is True
        assert giocatore_creato.get_tempo_residuo() == tempo_iniziale

        # CE3
        giocatore_creato = Giocatore(new_tempo_iniziale = timedelta(minutes = 5))

        tempo_da_ridurre = classi_equivalenza[2]
        with pytest.raises(TempoException):
            giocatore_creato.riduci_tempo(tempo_da_ridurre)

        # CP1
        giocatore_creato = Giocatore(new_tempo_iniziale = timedelta(minutes = 5))

        tempo_iniziale = giocatore_creato.get_tempo_residuo()
        tempo_da_ridurre = tempo_iniziale

        assert giocatore_creato.riduci_tempo(tempo_da_ridurre) is False
        assert giocatore_creato.get_tempo_residuo() == timedelta(0)

        # CP2
        giocatore_creato = Giocatore(new_tempo_iniziale = timedelta(minutes = 5))

        tempo_iniziale = giocatore_creato.get_tempo_residuo()
        tempo_da_ridurre = tempo_iniziale + timedelta(minutes = 1)

        assert giocatore_creato.riduci_tempo(tempo_da_ridurre) is False
        assert giocatore_creato.get_tempo_residuo() == timedelta(0)


    def test_giocatore_senza_limite_tempo(self):
        """Verifica riduci_tempo() in caso di Giocatore senza limite di tempo.

            Input di riduci_tempo():
                CE1, INPUT : tempo_da_ridurre > 0

        Oracolo:
            CE1 <=> Viene sollevata un'eccezione (il giocatore non ha limite di tempo)

        """
        # CE1
        giocatore_creato = Giocatore(new_tempo_iniziale = CostantiGiocatore.DEF_SENZA_LIMITE_TEMPO)


        tempo_da_ridurre = timedelta(seconds = 1)
        with pytest.raises(TempoException):
            giocatore_creato.riduci_tempo(tempo_da_ridurre)


    def test_giocatore_tempo_zero(self):
        """Verifica riduci_tempo() in caso di Giocatore con tempo limite zero.

        Classi di equivalenza
            Input di riduci_tempo():
                CE1, INPUT : tempo_da_ridurre > 0
                CE2, INPUT : tempo_da_ridurre = 0
                CE3, INPUT : tempo_da_ridurre < 0

        Oracolo:
            CE1 <=> Viene sollevata un'eccezione (tempo già scaduto)
            CE2 <=> Viene sollevata un'eccezione (tempo già scaduto)
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
        tempo_iniziale = timedelta(0)
        giocatore_creato = Giocatore(new_tempo_iniziale = tempo_iniziale)

        tempo_da_ridurre = timedelta(seconds=-1)
        with pytest.raises(TempoException):
            giocatore_creato.riduci_tempo(tempo_da_ridurre)

class TestGiocatorePossiedeLimiteTempo:
    """Classe TestGiocatorePossiedeLimiteTempo.

    DESCRIZIONE
        Suite di test funzionali per la funzione possiede_limite_tempo()
    """

    def test_giocatore_limite_tempo_regolare(self):
        """Verifica possiede_limite_tempo() in caso di Giocatore con tempo limite regolare.

        Condizioni particolari
            CP1: tempo_iniziale = 0


        Oracolo:
            Caso Generale => restituisce True
            CP1 => restitusce True (il timer è presente ed è finito)

        """
        # Caso Generale
        giocatore_creato = Giocatore(new_tempo_iniziale = timedelta(minutes = 5))
        assert giocatore_creato.possiede_limite_tempo() is True

        # CP1
        giocatore_creato = Giocatore(new_tempo_iniziale = timedelta(0))
        assert giocatore_creato.possiede_limite_tempo() is True


    def test_giocatore_senza_limite_tempo(self):
        """Verifica possiede_limite_tempo() in caso di Giocatore con tempo limite nullo.

        Oracolo:
            Caso Generale => restituisce False

        """
        giocatore_creato = Giocatore(new_tempo_iniziale = CostantiGiocatore.DEF_SENZA_LIMITE_TEMPO)

        assert giocatore_creato.possiede_limite_tempo() is False

class TestGiocatoreHaFinitoTempo:
    """Classe TestGiocatoreHaFinitoTempo.

    DESCRIZIONE
        Suite di test funzionali per la funzione ha_finito_tempo()
    """

    def test_giocatore_tempo_non_esaurito(self):
        """Verifica ha_finito_tempo() in caso di Giocatore con tempo limite non esaurito.

        Oracolo:
            Caso Generale => restituisce False


        """
        giocatore_creato = Giocatore(new_tempo_iniziale = CostantiGiocatore.DEF_TIMER_PREDEFINITI[0])

        assert giocatore_creato.ha_finito_tempo() is False


    def test_giocatore_tempo_esaurito(self):
        """Verifica ha_finito_tempo() in caso di Giocatore con tempo limite esaurito.

        Condizioni particolari
            CP1: Giocatore senza limite di tempo

        Oracolo:
            Caso Generale => restituisce True
            CP1 => restitusce False (non avere limite tempo vuol dire che non lo finirà mai)

        """
        # Caso Generale
        giocatore_creato = Giocatore(new_tempo_iniziale = timedelta(0))
        assert giocatore_creato.ha_finito_tempo() is True

        # CP1
        giocatore_creato = Giocatore(new_tempo_iniziale = CostantiGiocatore.DEF_SENZA_LIMITE_TEMPO)
        assert giocatore_creato.ha_finito_tempo() is False
