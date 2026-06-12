from datetime import timedelta


class CostantiGiocatore:
    """Classe CostantiGiocatore.

    DESCRIZIONE
        Classe contenente tutte le costanti riguardanti il giocatore

    COSTANTI:
        - DEF_COORDINATE
            Coordinate di default, usate per esempio nel costruttore di Giocatore
            in caso non venisse specificata la posizione iniziale

        - DEF_ID_P1, DEF_ID_P2
            ID di default assegnati ai giocatori.
            Non sono accessibili all'esterno, sono contenuti in un'apposita lista
            accessibile all'esterno

        - POSSIBILI_ID_GIOCATORE
            Lista contenente tutti i possibili ID assegnabili ai giocatori.
            Per introdurre un nuovo possibile ID, bisogna creare una nuova costante
            contenente l'id e inserirla nella lista

        - DEF_MURI_DISPONIBILI
            Muri disponibili di default per ogni giocatore

        - DEF_TEMPO_MINIMO
            Tempo limite minimo per le partite con tempo limite

        - DEF_SENZA_LIMITE_TEMPO
            Valore di default, indica che il giocatore non ha un tempo limite.
            I giocatori parte di una partita possiedono questa costante come tempo
            a disposizione.

        - DEF_TIMER_PREDEFINITI
            Una lista di tempi di default.
            Viene presentata all'utente prima di cominciare la partita con limite
            di tempo, in modo tale da evitare di usare tempi personalizzati

    """

    # Costanti Posizione
    DEF_COORDINATE = "a1"

    # Costanti ID
    __DEF_ID_P1 = "P1"
    __DEF_ID_P2 = "P2"
    __DEF_ID_P3 = "P3"
    __DEF_ID_P4 = "P4"

    POSSIBILI_ID_GIOCATORE = [__DEF_ID_P1, __DEF_ID_P2, __DEF_ID_P3, __DEF_ID_P4]
    DEF_MURI_DISPONIBILI = 10

    # Costanti Limite Tempo
    DEF_TEMPO_MINIMO = timedelta(minutes=1)
    DEF_SENZA_LIMITE_TEMPO = timedelta.max
    DEF_TIMER_PREDEFINITI = [timedelta(minutes=3), timedelta(minutes=5)]
