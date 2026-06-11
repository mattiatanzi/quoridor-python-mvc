import os

_gestore_input_personalizzato = None

def pulisci_schermo():
    """Pulisce il terminale in modo incrociato su tutti i SO e Shell.

    Abbiamo notato che durante l'esecuzione sui terminali di Ubuntu e di Windows
    Powershell non viene pulito lo schermo come avviene negli altri terminali,
    ma tralasciamo questo problema in quanto di base Ubuntu e Powershell mantengono
    il buffer di scorrimento ma ogni qual volta si richiama la funzione la stampa
    riporta sempre all'ultima stampa emessa lasciando quindi come 'storico'
    i precedenti comandi e/o precedenti stampe a video
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




def imposta_gestore_input(funzione_gestore):
    """Permette alla TUI di 'iniettare' la sua logica (code e popup)."""
    global _gestore_input_personalizzato
    _gestore_input_personalizzato = funzione_gestore


def chiedi_input_utente(indicazioniInput: str = "") -> str:
    """Funzione Generica di richiesta input (Agisce da ponte)."""
    
    # Se la TUI ha attivato il suo gestore, devia la chiamata lì!
    if _gestore_input_personalizzato is not None:
        return _gestore_input_personalizzato(indicazioniInput)

    # ALTRIMENTI: Comportamento originale per la CLI
    __stampa_richiesta_input(indicazioniInput)
    return input()


def __stampa_richiesta_input(indicazioni: str = ""):
    print(f"\n{indicazioni}", end="\n\n")
    print("Input: ", end="")
