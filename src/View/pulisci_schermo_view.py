import os


def pulisci_schermo():
    """Pulisce il terminale in modo incrociato su tutti i SO e Shell.

    Abbiamo notato che durante l'esecuzione sul terminale di Ubuntu non viene pulito lo
    schermo come avviene negli altri terminali, ma traliasciamo questo problema in
    quanto di base Ubunto mantiene il buffer di scorrimento ma ogni qual volta
    si richiama la funzione la stampa riporta sempre all'ultima stampa emessa lasciando
    quindi come 'storico' i precedenti comandi e/o precedenti stampe a video
    """
    if os.name == "posix":
        # Sistemi nativi Unix (Linux e macOS)
        print("\033[2J\033[H", end="", flush=True)
    else:
        # Sistemi Windows (CMD, PowerShell, Git Bash)
        # Git Bash imposta variabili d'ambiente specifiche ('TERM' o 'MSYSTEM')
        if "TERM" in os.environ or "MSYSTEM" in os.environ:
            print("\033[2J\033[H", end="", flush=True)  # Siamo su Git Bash
        else:
            os.system("cls")  # Siamo su PowerShell o CMD
