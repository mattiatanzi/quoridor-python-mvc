from threading import Event
import time

from src.Model.partita import Partita
from src.Model.tempo import get_tempo_formattato
from src.View.giocatore_view import GiocatoreViewAstratta
from src.View.partita_view import PartitaViewAstratta
from src.View.tavoliere_view import TavoliereviewAstratta
from textual.widgets import Label,Button
from src.View.funzioni_utili_stampa import imposta_gestore_input 
from src.View.TUI.Screen.conferma_Screen import ConfermaScreen
from src.View.TUI.Screen.vittoria_Screen import VittoriaScreen


class PartitaViewTUI(PartitaViewAstratta):
    """Implementazione TUI della view della partita.

    Non stampa nulla direttamente: aggiorna i widget
    già montati nella PartitaViewScreen tramite call_from_thread.

    ATTRIBUTI
        _app : QuoridorViewApp
            Riferimento all'app Textual condivisa
    """

    def __init__(
        self,
        new_giocatore_view: GiocatoreViewAstratta,
        new_tavoliere_view: TavoliereviewAstratta,
        app_condivisa,
    ):
        super().__init__(new_giocatore_view, new_tavoliere_view)
        self._app = app_condivisa
        imposta_gestore_input(self._gestore_input_tui)

    # ------ Stampe Video ------ #

    def stampa_partita(self, partita: Partita):
        giocatori = partita.get_giocatori()
        tavoliere = partita.get_tavoliere()

        for g in giocatori:
            id_sel = g.get_id()
            muri = partita.get_muri_disponibili_giocatore(id_sel)
            tempo_fmt = (
                get_tempo_formattato(g.get_tempo_residuo())
                if g.possiede_limite_tempo()
                else None
            )

            if g.is_attivo():
                if id_sel == partita.get_id_giocatore_attivo():
                    self.get_giocatore_view().stampa_giocatore_attivo(
                        id_sel, muri, tempo_fmt
                    )
                else:
                    self.get_giocatore_view().stampa_info_giocatore(
                        id_sel, muri, tempo_fmt
                    )
            else:
                self.get_giocatore_view().stampa_giocatore_eliminato(
                    id_sel, muri, tempo_fmt
                )

        # Il tavoliere aggiorna i widget già montati nella screen
        self.get_tavoliere_view().stampa_tavoliere(tavoliere, giocatori)

    def stampa_errore_partita(self, messaggio):
        # Se il controller passa una stringa vuota (nessun errore), non fare nulla
        if not messaggio or str(messaggio).strip() == "":
            return

        def _aggiorna():
            # Mostra una notifica rossa in basso a destra
            self._app.notify(
                str(messaggio), 
                title="Mossa Non Valida", 
                severity="error", 
                timeout=4  # Scompare da sola dopo 4 secondi
            )

        self._app.call_from_thread(_aggiorna)
    def stampa_aiuto(self):
        messaggio = """
QUORIDOR: COMANDI PRINCIPALI
        
• Muovi pedone: 
<colonna><riga> (es. 'e2')

• Piazza muro:  
<colonna><riga><h/v> (es. 'e2h')
  (h = in basso a dx | v = a destra in basso)
        
• Mostra aiuto: 'help' o 'aiuto'
• Elenco mosse: 'trascrizione' o 'mosse'
• Abbandona:    'quit' o 'abbandona'
• Esci:         'exit' o 'esci'
        
        """
        def _aggiorna_aiuto():
            try:
                # 1. Cerca il pannello, inserisce la stringa del Controller e lo apre
                pannello = self._app.screen.query_one("#pannello-aiuto", Label)
                pannello.update(messaggio)
                pannello.add_class("visibile")
                
                # 2. Sincronizza il testo del bottone
                try:
                    btn = self._app.screen.query_one("#btn-aiuto", Button)
                    btn.label = "Nascondi Aiuto"
                except Exception:
                    pass
                    
            except Exception:
                # Se la grafica dovesse avere problemi, usa le notifiche come fallback
                self._app.notify(messaggio)
                
        self._app.call_from_thread(_aggiorna_aiuto)

    def stampa_vittoria(self, id_vincitore, motivo_vittoria: str):
        def _mostra_vittoria():
            # Mostra lo schermo SOLO se non ci siamo già sopra!
            if not isinstance(self._app.screen, VittoriaScreen):
                self._app.push_screen(VittoriaScreen(id_vincitore,motivo_vittoria,self._app))    
        self._app.call_from_thread(_mostra_vittoria)

    def stampa_trascrizione(
        self, trascrizione: list[str], num_giocatori: int, replay: bool = False
    ):
        # Nella TUI la trascrizione sarà nel pannello laterale della
        # ReplayViewScreen; durante la partita usiamo una notifica
        if not replay:
            testo = "\n".join(reversed(trascrizione[-15:]))
            self._app.call_from_thread(self._app.notify, testo, timeout=10)

    def chiedi_input_utente(self, indicazioniInput: str = "") -> str:
        # Il controller chiama questo metodo per leggere dalla coda,
        # che viene popolata da on_input_submitted nella screen
        return self._app.get_coda_input().get()

    def get_input(self) -> str:
        return self.chiedi_input_utente()

    def stampa_richiesta_input(self, indicazioni: str = ""):
        # Aggiorna il label hint sopra il campo input
        def _aggiorna():
            try:
                self._app.screen.query_one(
                    "#label-input-hint"
                ).update(indicazioni or "Fai la tua mossa:")
            except Exception:
                pass
        self._app.call_from_thread(_aggiorna)

    def avvia_interfaccia_partita(self, ids_giocatori: list[str]) -> None:
        """Chiede all'app Textual di mostrare la schermata di partita e attende che sia pronta."""
        self._app.log("[RADAR-SCHERMO] A. Richiesto avvio schermo partita")
        evento = Event()
        
        def _cambia_schermo():
            self._app.log("[RADAR-SCHERMO] B. Chiamata mostra_schermo_partita in corso...")
            try:
                self._app.mostra_schermo_partita(ids_giocatori)
                self._app.log("[RADAR-SCHERMO] C. Schermo caricato senza errori grafici!")
            except Exception as e:
                self._app.log(f"[ERRORE SCHERMO] {e}")
            finally:
                # FONDAMENTALE: Sblocca il controller a prescindere!
                self._app.log("[RADAR-SCHERMO] D. Sblocco l'evento del controller")
                evento.set() 
                
        self._app.call_from_thread(_cambia_schermo)
        self._app.log("[RADAR-SCHERMO] E. Il controller è in pausa e aspetta l'evento...")
        evento.wait()
        self._app.log("[RADAR-SCHERMO] F. Evento sbloccato! Il controller riparte!")
        time.sleep(0.1)

    def torna_al_menu(self):
        """Rimuove lo schermo della partita e torna al menu."""
        # Anche le operazioni di chiusura (pop_screen) devono passare dal thread principale
        self._app.call_from_thread(self._app.torna_al_menu)


    def _gestore_input_tui(self, messaggio: str) -> str:
        """Intercetta le richieste del Controller e le adatta alla TUI."""
        testo_lower = messaggio.lower()
        coda = self._app.get_coda_input()
        
        # CASO 1: Domande di conferma con [si/no] apre il popup grafico bloccante
        if "[si/no]" in testo_lower:
            def _mostra_popup():
                self._app.push_screen(ConfermaScreen(messaggio, coda))
                
            self._app.call_from_thread(_mostra_popup)
            risposta = coda.get()
            if risposta == "si_uscita":
                self._app.notify("Chiusura gioco in corso...", title="Uscita", severity="information")
                time.sleep(1.5)
                self._app.exit()
                return "si"
            
            return "si" if risposta == "si" else "no"
            
        # CASO 2: Richieste di "Premi INVIO per continuare..." (Help, Trascrizione)
        elif "invio" in testo_lower:
            # Nella TUI questi elementi sono a scomparsa, non blocchiamo il gioco!
            # Sblocca il controller istantaneamente.
            return ""
            
        # CASO 3: Qualsiasi altra richiesta normale di gioco
        else:
            return coda.get()