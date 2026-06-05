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

    # Costanti
    _TOTALE_GIOCATORI = 2
    _ID_PRIMO_GIOCATORE_ATTIVO = CostantiGiocatore._POSSIBILI_ID_GIOCATORE[0]

    _PRIMA_COLONNA = "a"
    _ULTIMA_COLONNA = "i"
    _PRIMA_RIGA = "1"
    _ULTIMA_RIGA = "9"
    _ORIZZONTALE = "h"
    _VERTICALE = "v"

    _COORDINATE_INIZIALI = {
        CostantiGiocatore._POSSIBILI_ID_GIOCATORE[0]: "e1",
        CostantiGiocatore._POSSIBILI_ID_GIOCATORE[1]: "e9",
    }

    _RIGHE_FINALI = {
        CostantiGiocatore._POSSIBILI_ID_GIOCATORE[0]: "9",
        CostantiGiocatore._POSSIBILI_ID_GIOCATORE[1]: "1"}
