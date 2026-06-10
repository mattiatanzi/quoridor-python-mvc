from datetime import timedelta


def stringa_to_tempo_limite(stringa_tempo: str) -> timedelta:
    """Funzione di conversione tempo: stringa -> timedelta.

    DESCRIZIONE
        Converte una stringa nel formato "HH:MM:SS" in un oggetto timedelta

    """
    try:
        ore, minuti, secondi = map(int, stringa_tempo.split(":"))
        return timedelta(hours=ore, minutes=minuti, seconds=secondi)
    except ValueError:
        print("Errore Formato Tempo")
        return None


def get_tempo_formattato(tempo: timedelta) -> str:
    """Funzione di conversione tempo: timedelta -> stringa.

    DESCRIZIONE
        Converte un oggetto timedelta in una stringa in formato "HH:MM:SS

    """
    # 1. Prendiamo i secondi totali rimasti (es. 305 secondi)
    secondi_totali = int(tempo.total_seconds())

    # 2. Calcoliamo matematicamente ore, minuti e secondi restanti
    ore = secondi_totali // 3600
    minuti = (secondi_totali % 3600) // 60
    secondi = secondi_totali % 60

    # 3. Scegliamo il formato di return corretto
    return f"{ore:02d}:{minuti:02d}:{secondi:02d}"
