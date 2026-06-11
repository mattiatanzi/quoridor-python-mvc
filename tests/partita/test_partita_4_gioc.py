import pytest

from src.Controller.partita_controller import PartitaController
from src.Model.costanti_giocatore import CostantiGiocatore
from src.Model.costanti_partita import CostantiPartita
from src.Model.giocatore import Giocatore
from src.Model.partita import ErrorePartita, Partita
from src.Model.tavoliere import Tavoliere


class TestPartitaAggiungiGiocatore:
    """Classe TestPartitaAggiungiGiocatore.

    DESCRIZIONE
        Suite di test funzionali per la funzione aggiungi_giocatore()
    """

    def test_partita_minore_4_giocatori(self):
        """Verifica aggiungi_giocatore() con partita con numero di giocatori adeguato.

        Classi di equivalenza

            Stato della partita:
                CE1 : numero_giocatori < MAX_GIOCATORI_AMMESSI

        Condizioni particolari

            Stato della partita:
                CP1: numero_giocatori = 0
                CP2: numero_giocatori = MAX_GIOCATORI_AMMESSI - 1

        Oracolo:
            CE1 => Giocatore aggiunto correttamente alla partita
            CP1 => Giocatore aggiunto correttamente alla partita
            CP2 => Giocatore aggiunto correttamente alla partita

        """
        classi_equivalenza = [
            int(CostantiPartita.GIOCATORI_TOTALI_2),
            0,
            int(CostantiPartita.MAX_GIOCATORI_AMMESSI) - 1
        ]

        # CE1
        giocatori_partita = set([
                Giocatore(
                    new_id_giocatore = CostantiGiocatore.POSSIBILI_ID_GIOCATORE[i]
                ) for i in range(0, classi_equivalenza[0])
            ]
        )
        partita_creata = Partita(Tavoliere(), giocatori_partita)
        id_nuovo_giocatore = CostantiGiocatore.POSSIBILI_ID_GIOCATORE[
            len(partita_creata.get_giocatori())
        ]
        nuovo_giocatore = Giocatore(
            new_id_giocatore = id_nuovo_giocatore
        )
        partita_creata.aggiungi_giocatore(nuovo_giocatore)
        assert len(partita_creata.get_giocatori()) == classi_equivalenza[0] + 1
        assert partita_creata.get_giocatore(id_nuovo_giocatore).get_id() == id_nuovo_giocatore


        # CP1
        giocatori_partita = set()
        partita_creata = Partita(Tavoliere(), giocatori_partita)
        id_nuovo_giocatore = CostantiGiocatore.POSSIBILI_ID_GIOCATORE[
            len(partita_creata.get_giocatori()) + 1
        ]
        nuovo_giocatore = Giocatore(
            new_id_giocatore = id_nuovo_giocatore
        )
        partita_creata.aggiungi_giocatore(nuovo_giocatore)
        assert len(partita_creata.get_giocatori()) == classi_equivalenza[1] + 1
        assert partita_creata.get_giocatore(id_nuovo_giocatore).get_id() == id_nuovo_giocatore

        # CP2
        giocatori_partita = set([
                Giocatore(
                    new_id_giocatore = CostantiGiocatore.POSSIBILI_ID_GIOCATORE[i]
                ) for i in range(0, classi_equivalenza[2]
                )
            ]
        )
        partita_creata = Partita(Tavoliere(), giocatori_partita)
        id_nuovo_giocatore = CostantiGiocatore.POSSIBILI_ID_GIOCATORE[
            int(CostantiPartita.MAX_GIOCATORI_AMMESSI) - 1
        ]
        nuovo_giocatore = Giocatore(
            new_id_giocatore = id_nuovo_giocatore
        )
        partita_creata.aggiungi_giocatore(nuovo_giocatore)
        assert len(partita_creata.get_giocatori()) == int(CostantiPartita.MAX_GIOCATORI_AMMESSI)
        assert partita_creata.get_giocatore(id_nuovo_giocatore).get_id() == id_nuovo_giocatore


    def test_partita_maggiore_4_giocatori(self):
        """Verifica aggiungi_giocatore() con partita con numero di giocatori >= 4.

        Classi di equivalenza

            Stato della partita:
                CE1 : numero_giocatori >= MAX_GIOCATORI_AMMESSI

        Oracolo:
            CE1 => Eccezione sollevata (numero max giocatori raggiunti)

        """
        giocatori_partita = set([
                Giocatore(
                    new_id_giocatore = CostantiGiocatore.POSSIBILI_ID_GIOCATORE[i]
                ) for i in range(0, int(CostantiPartita.MAX_GIOCATORI_AMMESSI))

            ]
        )
        partita_creata = Partita(Tavoliere(), giocatori_partita)
        id_nuovo_giocatore = CostantiGiocatore.POSSIBILI_ID_GIOCATORE[0]

        nuovo_giocatore = Giocatore(
            new_id_giocatore = id_nuovo_giocatore
        )

        with pytest.raises(ErrorePartita):
            partita_creata.aggiungi_giocatore(nuovo_giocatore)
        assert len(partita_creata.get_giocatori()) == int(CostantiPartita.MAX_GIOCATORI_AMMESSI)


class TestPartitaRimuoviGiocatore:
    """Classe TestPartitaRimuoviGiocatore.

    DESCRIZIONE
        Suite di test funzionali per la funzione rimuovi_giocatore()
    """

    def test_partita_maggiore_0_giocatori(self):
        """Verifica aggiungi_giocatore() con partita con numero di giocatori > 0.

        Classi di equivalenza

            Stato della partita:
                CE1 : numero_giocatori > 0

        Condizioni particolari

            Stato della partita:
                CP1: numero_giocatori = 1

        Oracolo:
            CE1 => Giocatore rimosso correttamente dalla partita
            CP2 => Giocatore rimosso correttamente dalla partita

        """
        classi_equivalenza = [
            int(CostantiPartita.GIOCATORI_TOTALI_4),
            1
        ]

        # CE1
        giocatori_partita = set([
                Giocatore(
                    new_id_giocatore = CostantiGiocatore.POSSIBILI_ID_GIOCATORE[i]
                ) for i in range(0, classi_equivalenza[0])
            ]
        )
        partita_creata = Partita(Tavoliere(), giocatori_partita)

        partita_creata.rimuovi_giocatore(partita_creata.get_giocatore(CostantiGiocatore.POSSIBILI_ID_GIOCATORE[0]).get_id())
        assert len(partita_creata.get_giocatori()) == classi_equivalenza[0] - 1


        # CP2
        giocatori_partita = set([
                Giocatore(
                    new_id_giocatore = CostantiGiocatore.POSSIBILI_ID_GIOCATORE[0]
                )
            ]
        )
        partita_creata = Partita(Tavoliere(), giocatori_partita)

        partita_creata.rimuovi_giocatore(partita_creata.get_giocatore(CostantiGiocatore.POSSIBILI_ID_GIOCATORE[0]).get_id())
        assert len(partita_creata.get_giocatori()) == classi_equivalenza[1] - 1



    def test_partita_minore_uguale_0_giocatori(self):
        """Verifica aggiungi_giocatore() con partita con numero di giocatori <= 0.

        Classi di equivalenza

            Stato della partita:
                CE1 : numero_giocatori = 0

        Oracolo:
            CE1 => Eccezione sollevata (nessun giocatore in partita raggiunti)

        """
        giocatori_partita = set()

        partita_creata = Partita(Tavoliere(), giocatori_partita)
        giocatore_da_rimuovere = Giocatore(
            new_id_giocatore = CostantiGiocatore.POSSIBILI_ID_GIOCATORE[0]
        )

        with pytest.raises(ErrorePartita):
            partita_creata.rimuovi_giocatore(partita_creata.get_giocatore(giocatore_da_rimuovere).get_id())
        assert len(partita_creata.get_giocatori()) == 0


class TestPartitaEliminaGiocatore:
    """Classe TestPartitaEliminaGiocatore.

    DESCRIZIONE
        Suite di test funzionali per la funzione elimina_giocatore()
    """

    def test_partita_elimina_giocatore_attivo(self):
        """Verifica elimina_giocatore() con partita con numero di giocatori > 0.

            In questo caso i giocatori sono tutti attivi

        Classi di equivalenza

            Stato della partita:
                CE1 : numero_giocatori > 0, tutti giocatori non eliminati

        Condizioni particolari

            Stato della partita:
                CP1: numero_giocatori = 1

        Oracolo:
            CE1 => Giocatore eliminato correttamente dalla partita
            CP2 => Giocatore eliminato correttamente dalla partita

        """
        classi_equivalenza = [
            int(CostantiPartita.GIOCATORI_TOTALI_4),
            1
        ]

        # CE1
        giocatori_partita = set([
                Giocatore(
                    new_id_giocatore = CostantiGiocatore.POSSIBILI_ID_GIOCATORE[i]
                ) for i in range(0, classi_equivalenza[0])
            ]
        )
        partita_creata = Partita(Tavoliere(), giocatori_partita)

        id_giocatore_da_eliminare = CostantiGiocatore.POSSIBILI_ID_GIOCATORE[0]

        partita_creata.elimina_giocatore(id_giocatore_da_eliminare)
        assert partita_creata.get_giocatore(id_giocatore_da_eliminare).is_attivo() is False


        # CP2
        giocatori_partita = set([
                Giocatore(
                    new_id_giocatore = CostantiGiocatore.POSSIBILI_ID_GIOCATORE[0]
                )
            ]
        )
        partita_creata = Partita(Tavoliere(), giocatori_partita)

        id_giocatore_da_eliminare = CostantiGiocatore.POSSIBILI_ID_GIOCATORE[0]

        partita_creata.elimina_giocatore(id_giocatore_da_eliminare)
        assert partita_creata.get_giocatore(id_giocatore_da_eliminare).is_attivo() is False


    def test_partita_elimina_giocatore_eliminato(self):
        """Verifica elimina_giocatore() con partita con numero di giocatori > 0.

            In questo caso il giocatore da eliminare è già stato eliminato

        Classi di equivalenza

            Stato della partita:
                CE1 : numero_giocatori > 0, solo un giocatore eliminato

        Condizioni particolari

            Stato della partita:
                CP2: numero_giocatori = 1

        Oracolo:
            CE1 => Raise errore (giocatore già eliminato dalla partita)
            CP2 => Raise errore (giocatore già eliminato dalla partita)

        """
        classi_equivalenza = [
            int(CostantiPartita.GIOCATORI_TOTALI_4),
            1
        ]

        # CE1
        giocatori_partita = set([
                Giocatore(
                    new_id_giocatore = CostantiGiocatore.POSSIBILI_ID_GIOCATORE[i]
                ) for i in range(0, classi_equivalenza[0])
            ]
        )
        partita_creata = Partita(Tavoliere(), giocatori_partita)

        id_giocatore_da_eliminare = CostantiGiocatore.POSSIBILI_ID_GIOCATORE[0]
        partita_creata.elimina_giocatore(id_giocatore_da_eliminare)

        with pytest.raises(ErrorePartita):
            partita_creata.elimina_giocatore(id_giocatore_da_eliminare)

        # Controllo che il giocatore non abbia subito cambiamenti nello stato
        assert partita_creata.get_giocatore(id_giocatore_da_eliminare).is_attivo() is False

        # CP2
        giocatori_partita = set([
                Giocatore(
                    new_id_giocatore = CostantiGiocatore.POSSIBILI_ID_GIOCATORE[0]
                )
            ]
        )
        partita_creata = Partita(Tavoliere(), giocatori_partita)

        id_giocatore_da_eliminare = CostantiGiocatore.POSSIBILI_ID_GIOCATORE[0]
        partita_creata.elimina_giocatore(id_giocatore_da_eliminare)

        with pytest.raises(ErrorePartita):
            partita_creata.elimina_giocatore(id_giocatore_da_eliminare)

        # Controllo che il giocatore non abbia subito cambiamenti nello stato
        assert partita_creata.get_giocatore(id_giocatore_da_eliminare).is_attivo() is False


    def test_partita_partita_senza_giocatori(self):
        """Verifica elimina_giocatore() con partita con numero di giocatori = 0.

        Classi di equivalenza

            Stato della partita:
                CE1 : numero_giocatori = 0, solo un giocatore eliminato

        Oracolo:
            CE1 => Raise errore (nessun giocatore in partita)
            CP2 => Raise errore (giocatore già eliminato dalla partita)

        """
        giocatori_partita = set()

        partita_creata = Partita(Tavoliere(), giocatori_partita)

        id_giocatore_da_eliminare = CostantiGiocatore.POSSIBILI_ID_GIOCATORE[0]

        with pytest.raises(ErrorePartita):
            partita_creata.elimina_giocatore(id_giocatore_da_eliminare)

        # Controllo che il giocatore non abbia subito cambiamenti nello stato
        assert len(partita_creata.get_giocatori()) == 0


class TestPartitaIncrementaTurno:
    """Classe TestPartitaIncrementaTurno.

    DESCRIZIONE
        Suite di test funzionali per la funzione incrementa_turno()
    """

    def test_partita_incrementa_turno_con_giocatori(self):
        """Verifica elimina_giocatore() con partita con numero di giocatori > 0.

        Classi di equivalenza

            Stato della partita:
                CE1 : numero_giocatori > 0, turno_corrente in formato corretto
                CE2 : numero_giocatori > 0, turno_corrente in formato errato

        Oracolo:
            CE1 => incrementa turno prendendo prossimo giocatore
            CE2 => asserisci turno al primo giocatore
        """
        classi_equivalenza = [
            CostantiGiocatore.POSSIBILI_ID_GIOCATORE[2],
            ""
        ]

        # CE1
        giocatori_partita = set([
                Giocatore(
                    new_id_giocatore = CostantiGiocatore.POSSIBILI_ID_GIOCATORE[i]
                ) for i in range(0, len(CostantiGiocatore.POSSIBILI_ID_GIOCATORE))
            ]
        )
        partita_creata = Partita(Tavoliere(), giocatori_partita)

        id_nuovo_giocatore_attivo = classi_equivalenza[0]
        partita_creata.set_id_giocatore_attivo(id_nuovo_giocatore_attivo)

        id_prossimo_giocatore_attivo = CostantiGiocatore.POSSIBILI_ID_GIOCATORE[3]
        partita_creata.incrementa_turno()
        assert partita_creata.get_id_giocatore_attivo() == id_prossimo_giocatore_attivo


        # CE2
        giocatori_partita = set([
                Giocatore(
                    new_id_giocatore = CostantiGiocatore.POSSIBILI_ID_GIOCATORE[i]
                ) for i in range(0, len(CostantiGiocatore.POSSIBILI_ID_GIOCATORE))
            ]
        )
        partita_creata = Partita(Tavoliere(), giocatori_partita)

        id_nuovo_giocatore_attivo = ""
        partita_creata.set_id_giocatore_attivo(id_nuovo_giocatore_attivo)

        partita_creata.incrementa_turno()
        assert partita_creata.get_id_giocatore_attivo() == CostantiPartita.ID_PRIMO_GIOCATORE_ATTIVO


    def test_partita_incrementa_turno_senza_giocatori(self):
        """Verifica elimina_giocatore() con partita con numero di giocatori = 0.

        Classi di equivalenza

            Stato della partita:
                CE1 : numero_giocatori = 0

        Oracolo:
            CE1 => Raise errore (non si può incrementare turno in partita senza giocatori)
        """
        # CE1
        giocatori_partita = set()
        partita_creata = Partita(Tavoliere(), giocatori_partita)

        with pytest.raises(ErrorePartita):
            partita_creata.incrementa_turno()
