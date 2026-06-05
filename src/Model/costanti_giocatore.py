from datetime import timedelta

class CostantiGiocatore:

    # Costanti Posizione
    _DEF_COORDINATE = "a1"

    # Costanti ID
    __DEF_ID_P1 = "P1"
    __DEF_ID_P2 = "P2"

    _POSSIBILI_ID_GIOCATORE = [
        __DEF_ID_P1,
        __DEF_ID_P2,
    ]
    _DEF_MURI_DISPONIBILI = 10

    # Costanti Limite Tempo
    _DEF_TEMPO_MINIMO = timedelta(minutes=1)
    _DEF_SENZA_LIMITE_TEMPO = timedelta.max
    _DEF_TIMER_PREDEFINITI = [timedelta(minutes = 3), timedelta(minutes = 5)]
