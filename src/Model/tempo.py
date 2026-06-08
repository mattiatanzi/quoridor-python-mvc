from datetime import timedelta


def stringa_to_tempo_limite(stringa_tempo: str) -> timedelta:
    try:
        ore, minuti, secondi = map(int, stringa_tempo.split(":"))
        return timedelta(hours = ore, minutes = minuti, seconds = secondi)
    except ValueError:
        print("Errore Formato Tempo")
        return None

def get_tempo_formattato(tempo: timedelta) -> str:
    # 1. Prendiamo i secondi totali rimasti (es. 305 secondi)
    secondi_totali = int(tempo.total_seconds())

    # 2. Calcoliamo matematicamente ore, minuti e secondi restanti
    ore = secondi_totali // 3600
    minuti = (secondi_totali % 3600) // 60
    secondi = secondi_totali % 60

    # 3. Scegliamo il formato di return corretto
    if ore > 0:
        return f"{ore:02d}:{minuti:02d}:{secondi:02d}"
    else:
        return f"{minuti:02d}:{secondi:02d}"
