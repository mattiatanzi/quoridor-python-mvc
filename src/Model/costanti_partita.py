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
                    Pubblico, Tipo int
                DESCRIZIONE
                    Il numero massimo dei giocatori amessi in partita

            - ID_PRIMO_GIOCATORE_ATTIVO
                TIPO
                    Pubblico, Tipo str
                DESCRIZIONE
                    Indica l'id del primo giocatore attivo

            - PRIMA_COLONNA
                TIPO
                    Pubblico, Tipo str
                DESCRIZIONE
                    Indica la prima colonna del tavoliere

            - ULTIMA_COLONNA
                TIPO
                    Pubblico, Tipo str
                DESCRIZIONE
                    Indica l'ultima colonna del tavoliere

            - PRIMA_RIGA
                TIPO
                    Pubblico, Tipo str
                DESCRIZIONE
                    Indica la prima riga del tavoliere

            - ULTIMA_RIGA
                TIPO
                    Pubblico, Tipo str
                DESCRIZIONE
                    Indica l'ultima riga del tavoliere

            - ORIZZONTALE
                TIPO
                    Pubblico, Tipo str
                DESCRIZIONE
                    Indica il carattere presente quando si legge un muro orizzontale

            - VERTICALE
                TIPO
                    Pubblico, Tipo str
                DESCRIZIONE
                    Indica il carattere presente quando si legge un muro verticale

            - RIGHE_FINALI
                TIPO
                    Pubblico, Tipo Dizionario
                DESCRIZIONE
                    E' un dizionario che ha per chiavi gli id dei giocatori e per valore
                    la riga di arrivo
    """

    # Costanti
    TOTALE_GIOCATORI = 2
    ID_PRIMO_GIOCATORE_ATTIVO = CostantiGiocatore.POSSIBILI_ID_GIOCATORE[0]

    PRIMA_COLONNA = "a"
    ULTIMA_COLONNA = "i"
    PRIMA_RIGA = "1"
    ULTIMA_RIGA = "9"
    ORIZZONTALE = "h"
    VERTICALE = "v"

    COORDINATE_INIZIALI = {
        CostantiGiocatore.POSSIBILI_ID_GIOCATORE[0]: "e1",
        CostantiGiocatore.POSSIBILI_ID_GIOCATORE[1]: "e9",
    }

    RIGHE_FINALI = {
        CostantiGiocatore.POSSIBILI_ID_GIOCATORE[0]: "9",
        CostantiGiocatore.POSSIBILI_ID_GIOCATORE[1]: "1"}
