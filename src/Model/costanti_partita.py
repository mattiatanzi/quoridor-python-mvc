from src.Model.costanti_giocatore import CostantiGiocatore

class CostantiPartita:
    """Classe CostantiPartita.

        DESCRIZIONE
            Classe contenente tutte le costanti riguardanti la partita

        COSTANTI
            - COORDINATE_INIZIALI
                Contiene le coordinate iniziali.
                Ad ogni ID di giocatore viene associata la coordinata iniziale

            - TOTALE_GIOCATORI
                TIPO
                    Privato, Tipo int
                DESCRIZIONE
                    Il numero massimo dei giocatori amessi in partita

            - ID_PRIMO_GIOCATORE_ATTIVO
                TIPO
                    Privato, Tipo str
                DESCRIZIONE
                    Indica l'id del primo giocatore attivo

            - PRIMA_COLONNA
                TIPO
                    Privato, Tipo str
                DESCRIZIONE
                    Indica la prima colonna del tavoliere

            - ULTIMA_COLONNA
                TIPO
                    Privato, Tipo str
                DESCRIZIONE
                    Indica l'ultima colonna del tavoliere

            - PRIMA_RIGA
                TIPO
                    Privato, Tipo str
                DESCRIZIONE
                    Indica la prima riga del tavoliere

            - ULTIMA_RIGA
                TIPO
                    Privato, Tipo str
                DESCRIZIONE
                    Indica l'ultima riga del tavoliere

            - ORIZZONTALE
                TIPO
                    Privato, Tipo str
                DESCRIZIONE
                    Indica il carattere presente quando si legge un muro orizzontale

            - VERTICALE
                TIPO
                    Privato, Tipo str
                DESCRIZIONE
                    Indica il carattere presente quando si legge un muro verticale

            - RIGHE_FINALI
                TIPO
                    Privato, Tipo Dizionario
                DESCRIZIONE
                    E' un dizionario che ha per chiavi gli id dei giocatori e per valore
                    la riga di arrivo
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
