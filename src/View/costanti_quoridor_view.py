class CostantiQuoridorView:

    # Scelte di default nella stampa
    _SCELTA_TORNA_INDIETRO = "\n3. Torna Indietro\n"

    # Costanti riguardanti le modalità di Gioco (con o senza timer)
    __SCELTA_PARTITA_NO_TIMER = "\n1. Partita Senza Timer\n"
    __SCELTA_PARTITA_CON_TIMER = "\n2. Partita Con Timer\n"

    _POSSIBILI_SCELTE_MODALITA = [
        __SCELTA_PARTITA_NO_TIMER,
        __SCELTA_PARTITA_CON_TIMER
    ]


    # Costanti riguardanti la scelta del timer
    __SCELTA_TIMER_1 = "\n1. Partita Senza Timer\n"
    __SCELTA_TIMER_2 = "\n2. Partita Con Timer\n"

    __MESSAGGIO_ALTERNATIVO_SCELTA_TIMER = "\n(In alternativa, digitare il limite di tempo nel formato HH:MM:SS)\n"

    _POSSIBILI_TIMER_DEFAULT = [
        __SCELTA_TIMER_1,
        __SCELTA_TIMER_2
    ]
