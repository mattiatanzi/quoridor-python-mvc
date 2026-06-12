import builtins
import os
import queue
import threading

_gestore_input_personalizzato = None

# --- SISTEMA UNIFICATO DI INPUT ASINCRONO (Fix Doppio Invio) ---
_coda_input_globale = queue.Queue()
_thread_input_avviato = False

_input_originale = builtins.input


def _lettore_input_globale():
    while True:
        try:
            # Usa il vero input per prendere i dati dalla tastiera
            testo = _input_originale()
            _coda_input_globale.put(testo)
        except EOFError:
            break


def _avvia_lettore_se_necessario():
    """Avvia il thread solo la prima volta che serve un input."""
    global _thread_input_avviato
    if not _thread_input_avviato:
        _thread_input_avviato = True
        t = threading.Thread(target=_lettore_input_globale, daemon=True)
        t.start()


def inserisci_input_forzato(testo: str):
    """Permette al timer di inviare 'resa_per_tempo' aggirando la tastiera."""
    _coda_input_globale.put(testo)


# -----------------------------------------------------------------


def pulisci_schermo():
    """Pulisce il terminale in modo incrociato su tutti i SO e Shell."""
    if os.name == "posix":
        print("\033[2J\033[H", end="", flush=True)
    else:
        if "TERM" in os.environ or "MSYSTEM" in os.environ:
            print("\033[2J\033[H", end="", flush=True)
        else:
            os.system("cls")


def imposta_gestore_input(funzione_gestore):
    """Permette alla TUI di 'iniettare' la sua logica."""
    global _gestore_input_personalizzato
    _gestore_input_personalizzato = funzione_gestore


def chiedi_input_utente(indicazioniInput: str = "") -> str:
    """Restituisce input utente dalla coda globale (asincrono)."""
    
    if _gestore_input_personalizzato is not None:
        return _gestore_input_personalizzato(indicazioniInput)

    # Assicura che il lettore in background sia attivo
    _avvia_lettore_se_necessario()

    print(f"\n{indicazioniInput} ", end="\n\n")
    print("Input: ", end="", flush=True)

    # Si blocca in attesa che l'utente scriva o che scada il timer, in modo pulito!
    return _coda_input_globale.get()

builtins.input = lambda prompt="": chiedi_input_utente(prompt)
