import pytest

from src.Model.costanti_giocatore import CostantiGiocatore
from src.Model.costanti_partita import CostantiPartita
from src.Model.giocatore import Giocatore
from src.Model.partita import ErrorePartita, Partita
from src.Model.tavoliere import Tavoliere


class TestPartitaAggiungiGiocatore:
    """Classe TestGiocatoreRiduciTempo.

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
                ) for i in range(0, classi_equivalenza[0]
                )
            ]
        )
        partita_creata = Partita(Tavoliere(), giocatori_partita)
        id_nuovo_giocatore = CostantiGiocatore.POSSIBILI_ID_GIOCATORE[
            len(partita_creata.get_giocatori()) + 1
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
