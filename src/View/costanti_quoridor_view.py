class CostantiQuoridorView:
    """Classe CostantiQuoridorView.

    DESCRIZIONE
        Classe contenente le costanti di QuoridorView
        Per rappresentare al meglio le interfacce, è stato adottato un sistema
        di dizionari.

        Ciascun Dizionario messo a disposizione dalla classe contiene delle coppie
        costruite in questo modo:
            Chiave
                Input digitabile dall'utente, solitamente un carattere
            Valore
                Una breve descrizione del comando che verrà stampata nell'interfaccia

        Se un'interfaccia stampa un dizionario contenente la coppia TORNA_INDIETRO,
        sarà necessario organizzare l'interfaccia in modo tale che da essa sia
        possibile tornare al menu precedente

    COSTANTI:
        - SCELTA_TORNA_INDIETRO
            DESCRIZIONE
                Stringa che corrisponde alla scelta dell'utente per tornare indietro

        - TORNA_INDIETRO
            DESCRIZIONE
                Coppia Chiave, Valore contenente:
                    Chiave = SCELTA_TORNA_INDIETRO
                    Valore = Stringa descrizione del comando per tornare indietro

        - SCELTA_PARTITA_CON_TIMER
            DESCRIZIONE
                Stringa che corrisponde alla scelta dell'utente per selezionare
                partita con timer

        - SCELTA_PARTITA_SENZA_TIMER
            DESCRIZIONE
                Stringa che corrisponde alla scelta dell'utente per selezionare
                partita senza timer

        - POSSIBILI_SCELTE_MODALITA
            DESCRIZIONE
                Dizionario riguardante la scelta della modalità di partita
                (con o senza timer).

        - MESSAGGIO_ALTERNATIVO_SCELTA_TIMER
            DESCRIZIONE
                Messaggio da stampare a video per aiutare l'utente a digitare timer
                personalizzato.
                Non rientra nel dizionario poiché non è selezionabile dall'utente.
                In questo caso per poter usare un timer personalizzato, l'utente deve
                direttamente digitarlo nel corretto formato

        - SCELTA_TIMER_DEFAULT_1
            DESCRIZIONE
                Stringa che corrisponde alla scelta dell'utente per selezionare
                il primo limite di tempo di default

        - SCELTA_TIMER_DEFAULT_2
            DESCRIZIONE
                Stringa che corrisponde alla scelta dell'utente per selezionare
                il secondo limite di tempo di default

        - POSSIBILI_TIMER_DEFAULT
            DESCRIZIONE
                Dizionario riguardante la scelta del limite di tempo (Tempo breve,
                medio, ...)

    """

    # Scelte di default nella stampa
    SCELTA_TORNA_INDIETRO = "0"

    # Costanti per pulsanti
    MOSTRA_AIUTO = "- Mostra aiuto"
    NASCONDI_AIUTO = "- Nascondi aiuto"
    MOSTRA_MOSSE = "Mostra Mosse"
    ABBANDONA = "Resa / Abbandona"
    ESCI_GIOCO = "Esci dal Gioco"
    SI_CONFERMA = "Sì, Conferma"
    NO_ANNULLA = "No, Annulla"

    __TORNA_INDIETRO = {f"{SCELTA_TORNA_INDIETRO}": "Torna Indietro"}

    # Costanti riguardanti le modalità di Gioco TIMER / SENZA TIMER

    SCELTA_PARTITA_CON_TIMER = "1"
    SCELTA_PARTITA_SENZA_TIMER = "2"

    POSSIBILI_SCELTE_MODALITA = {
        SCELTA_PARTITA_CON_TIMER: "Partita con Timer",
        SCELTA_PARTITA_SENZA_TIMER: "Partita senza Timer",
        **__TORNA_INDIETRO,
    }

    # Costanti riguardanti i possibili valori di timer selezionabili

    MESSAGGIO_ALTERNATIVO_SCELTA_TIMER = (
        "\n(In alternativa, digitare il limite di tempo nel formato HH:MM:SS)\n\n"
    )

    SCELTA_TIMER_DEFAULT_1 = "1"
    SCELTA_TIMER_DEFAULT_2 = "2"

    POSSIBILI_TIMER_DEFAULT = {
        SCELTA_TIMER_DEFAULT_1: "Tempo Breve (3 Minuti)",
        SCELTA_TIMER_DEFAULT_2: "Tempo Medio (5 Minuti)",
        **__TORNA_INDIETRO,
    }

    # Costanti riguardanti possibili numeri di giocatori selezionabili

    SCELTA_2_GIOCATORI = "1"
    SCELTA_4_GIOCATORI = "2"

    POSSIBILI_NUMERO_GIOCATORI = {
        SCELTA_2_GIOCATORI: "Partita con 2 Giocatori",
        SCELTA_4_GIOCATORI: "Partita con 4 Giocatori",
        **__TORNA_INDIETRO,
    }
