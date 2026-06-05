from src.Model.costanti_giocatore import CostantiGiocatore

class CostantiPartita:
    """Classe CostantiPartita.

        DESCRIZIONE
            Classe contenente tutte le costanti riguardanti la partita

        COSTANTI
            - COORDINATE_INIZIALI
                Contiene le coordinate iniziali.
                Ad ogni ID di giocatore viene associata la coordinata iniziale

    """

    _COORDINATE_INIZIALI = {
        CostantiGiocatore._POSSIBILI_ID_GIOCATORE[0]: "e1",
        CostantiGiocatore._POSSIBILI_ID_GIOCATORE[1]: "e9",
    }
