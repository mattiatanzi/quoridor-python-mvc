class CostantiQuoridorView:

    # Scelte di default nella stampa
    _SCELTA_TORNA_INDIETRO = "0"

    __TORNA_INDIETRO = {f"{_SCELTA_TORNA_INDIETRO}": "Torna Indietro"}

    # Costanti riguardanti le modalità di Gioco TIMER / SENZA TIMER

    _SCELTA_PARTITA_CON_TIMER = "1"
    _SCELTA_PARTITA_SENZA_TIMER = "2"

    _POSSIBILI_SCELTE_MODALITA = {
        _SCELTA_PARTITA_CON_TIMER : "Partita con Timer",
        _SCELTA_PARTITA_SENZA_TIMER : "Partita senza Timer",
        **__TORNA_INDIETRO
    }
    # Costanti riguardanti i possibili valori di timer selezionabili

    _MESSAGGIO_ALTERNATIVO_SCELTA_TIMER = "\n(In alternativa, digitare il limite di tempo nel formato HH:MM:SS)\n"

    _SCELTA_TIMER_DEFAULT_1 = "1"
    _SCELTA_TIMER_DEFAULT_2 = "2"

    _POSSIBILI_TIMER_DEFAULT = {
        _SCELTA_TIMER_DEFAULT_1 : "Tempo Breve (3 Minuti)",
        _SCELTA_TIMER_DEFAULT_2 : "Tempo Medio (5 Minuti)",
        **__TORNA_INDIETRO
    }
