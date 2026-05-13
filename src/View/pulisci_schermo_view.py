import os


def pulisci_schermo():
    """Pulisce il terminale in modo incrociato su tutti i SO e Shell."""
    if os.name == 'posix':
        # Sistemi nativi Unix (Linux e macOS)
        print("\033[2J\033[H", end="", flush=True)
    else:
        # Sistemi Windows (CMD, PowerShell, Git Bash)
        # Git Bash imposta variabili d'ambiente specifiche ('TERM' o 'MSYSTEM')
        if 'TERM' in os.environ or 'MSYSTEM' in os.environ:
            print("\033[2J\033[H", end="", flush=True) # Siamo su Git Bash
        else:
            os.system('cls')   # Siamo su PowerShell o CMD