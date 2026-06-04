from datetime import timedelta

class CostantiGiocatore:
    _DEF_COORDINATE = "a1"
    _DEF_ID = "P1"
    _DEF_MURI_DISPONIBILI = 10

    # Costanti Limite Tempo
    _DEF_TEMPO_MINIMO = timedelta(minutes=1)
    _DEF_SENZA_TIMER = timedelta.max
    _DEF_TIMER_PREDEFINITI = [timedelta(minutes = 3), timedelta(minutes = 5)]
