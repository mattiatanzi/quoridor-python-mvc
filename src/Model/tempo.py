import threading
import time
from datetime import timedelta

class Tempo:
    def __init__(self, durata_iniziale: timedelta):
        self._tempo_residuo = durata_iniziale
        self._attivo = False
        self._in_pausa = False
        self._thread = None
        
        self._on_tick = None
        self._on_timeout = None

    def imposta_callbacks(self, on_tick, on_timeout):
        """Imposta le funzioni da richiamare per l'aggiornamento grafico e la sconfitta."""
        self._on_tick = on_tick
        self._on_timeout = on_timeout

    def avvia(self):
        if not self._attivo and self._tempo_residuo.total_seconds() > 0:
            self._attivo = True
            self._in_pausa = False
            self._thread = threading.Thread(target=self._loop_timer, daemon=True)
            self._thread.start()

    def metti_in_pausa(self):
        self._in_pausa = True

    def riprendi(self):
        self._in_pausa = False

    def ferma(self):
        self._attivo = False
        if self._thread:
            self._thread.join(timeout=0.1)

    def _loop_timer(self):
        while self._attivo:
            time.sleep(1)
            
            if not self._in_pausa:
                sec_rimasti = self._tempo_residuo.total_seconds() - 1
                
                if sec_rimasti <= 0:
                    self._tempo_residuo = timedelta(seconds=0)
                    self._attivo = False
                    if self._on_timeout:
                        self._on_timeout()
                    break
                else:
                    self._tempo_residuo = timedelta(seconds=sec_rimasti)
                    if self._on_tick:
                        self._on_tick(self._tempo_residuo)

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