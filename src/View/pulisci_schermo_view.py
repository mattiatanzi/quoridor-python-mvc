import os


def pulisci_schermo():
    """Pulisce il terminale in modo incrociato su tutti i SO e Shell."""
    if os.name == 'posix':
        # Sistemi nativi Unix (Linux e macOS)
        os.system('clear')
    else:
        # Sistemi Windows (CMD, PowerShell, Git Bash)
        # Git Bash imposta variabili d'ambiente specifiche ('TERM' o 'MSYSTEM')
        if 'TERM' in os.environ or 'MSYSTEM' in os.environ:
            os.system('clear') # Siamo su Git Bash
        else:
            os.system('cls')   # Siamo su PowerShell o CMD