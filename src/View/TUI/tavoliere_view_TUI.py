import traceback

from textual.widgets import Button

from src.Model.costanti_tavoliere import Costanti
from src.Model.giocatore import Giocatore
from src.Model.nodo import Nodo
from src.Model.tavoliere import Tavoliere
from src.View.tavoliere_view import TavoliereviewAstratta


class TavoliereViewTUI(TavoliereviewAstratta):
    """Adattatore TUI del tavoliere di gioco.

    DESCRIZIONE
        Traduce lo stato del Tavoliere (modello) in aggiornamenti
        grafici della UI Textual, gestendo muri, intersezioni e
        posizione dei giocatori.

    ATTRIBUTI
        __app : QuoridorViewApp
            Riferimento all'app Textual condivisa

        __cache_nodi : dict | None
            Cache dei widget del tavoliere per ottimizzare gli aggiornamenti

        _schermo_cache : Screen | None
            Riferimento alla schermata corrente per invalidare la cache

    METODI

        def __init__(self, app_condivisa):
            DESCRIZIONE
                Inizializza la view TUI del tavoliere.

        def stampa_tavoliere(self, tavoliere: Tavoliere, giocatori: set[Giocatore]):
            DESCRIZIONE
                Aggiorna la rappresentazione grafica del tavoliere
                sincronizzandolo con lo stato del modello.
    """

    __COSTANTI = Costanti()

    def __init__(self, app_condivisa, coda_input=None):
        self.__app = app_condivisa
        self.__cache_nodi = None  # Il segreto per la velocità assoluta
        self._schermo_cache = None

    def stampa_tavoliere(self, tavoliere: Tavoliere, giocatori: set[Giocatore]):
        def _aggiorna_grafica():
            try:
                schermo = self.__app.screen

                # --- 1. CREAZIONE CACHE (Avviene solo al turno 1) ---
                if self.__cache_nodi is None or self._schermo_cache != schermo:
                    try:
                        griglia = schermo.query_one("#griglia-tavoliere")
                        self.__cache_nodi = {n.id: n for n in griglia.children if n.id}
                        self._schermo_cache = schermo
                    except Exception:
                        # Se la griglia non ha finito di caricare, aspetta il prossimo
                        # giro
                        return

                nodi = self.__cache_nodi

                # --- 2. PULIZIA DEL TABELLONE ---
                for widget in nodi.values():
                    widget.remove_class(
                        "muro-piazzato",
                        "giocatore-1",
                        "giocatore-2",
                        "giocatore-3",
                        "giocatore-4",
                    )
                    # Se è una casella (ha l'ID corto tipo 'btn-e5') puliamo il testo
                    if (
                        isinstance(widget, Button)
                        and len(widget.id) <= 6
                        and not widget.id.endswith(("h", "v"))
                    ):
                        widget.label = ""

                # --- 3. DISEGNO DEI MURI ORIZZONTALI (SOTTO) ---
                for riga in range(2, 10):
                    for col in self.__COSTANTI.COLONNE:
                        chiave = Nodo(f"{col}{riga}")
                        if (
                            tavoliere.get_adiacente(
                                chiave, self.__COSTANTI.ARCO_ADIACENTE_SOTTO
                            )
                            == self.__COSTANTI.NO_ARCO
                        ):
                            id_muro = f"btn-{col}{riga}h"
                            if id_muro in nodi:
                                nodi[id_muro].add_class("muro-piazzato")

                # --- 4. DISEGNO DEI MURI VERTICALI (DESTRA) ---
                for riga in range(1, 10):
                    for c_idx in range(8):  # Fino alla 'h'
                        col = self.__COSTANTI.COLONNE[c_idx]
                        chiave = Nodo(f"{col}{riga}")
                        if (
                            tavoliere.get_adiacente(
                                chiave, self.__COSTANTI.ARCO_ADIACENTE_DESTRA
                            )
                            == self.__COSTANTI.NO_ARCO
                        ):
                            id_muro = f"btn-{col}{riga}v"
                            if id_muro in nodi:
                                nodi[id_muro].add_class("muro-piazzato")

                # --- 5. DISEGNO DELLE INTERSEZIONI ---
                for riga in range(2, 10):
                    for c_idx in range(8):
                        c_sx = self.__COSTANTI.COLONNE[c_idx]
                        c_dx = self.__COSTANTI.COLONNE[c_idx + 1]

                        h1 = (
                            tavoliere.get_adiacente(
                                Nodo(f"{c_sx}{riga}"),
                                self.__COSTANTI.ARCO_ADIACENTE_SOTTO,
                            )
                            == self.__COSTANTI.NO_ARCO
                        )
                        h2 = (
                            tavoliere.get_adiacente(
                                Nodo(f"{c_dx}{riga}"),
                                self.__COSTANTI.ARCO_ADIACENTE_SOTTO,
                            )
                            == self.__COSTANTI.NO_ARCO
                        )
                        v1 = (
                            tavoliere.get_adiacente(
                                Nodo(f"{c_sx}{riga}"),
                                self.__COSTANTI.ARCO_ADIACENTE_DESTRA,
                            )
                            == self.__COSTANTI.NO_ARCO
                        )
                        v2 = (
                            tavoliere.get_adiacente(
                                Nodo(f"{c_sx}{riga - 1}"),
                                self.__COSTANTI.ARCO_ADIACENTE_DESTRA,
                            )
                            == self.__COSTANTI.NO_ARCO
                        )

                        # Se due muri si toccano, l'incrocio si colora
                        if (h1 and h2) or (v1 and v2):
                            id_int = f"int-{c_sx}{riga}"
                            if id_int in nodi:
                                nodi[id_int].add_class("muro-piazzato")

                # --- 6. PIAZZAMENTO GIOCATORI ---
                giocatori_ordinati = sorted(giocatori, key=lambda x: x.get_id())

                for indice, g in enumerate(giocatori_ordinati, start=1):
                    # ==========================================
                    # LA PROTEZIONE SALVA-CRASH:
                    # Se il giocatore è stato eliminato o si è arreso,
                    # non ha più una posizione sul tabellone. Lo saltiamo!
                    # ==========================================
                    if not g.is_attivo() or g.get_posizione() is None:
                        continue
                    pos = g.get_posizione().get_valore_id_nodo()
                    id_casella = f"btn-{pos}"
                    if id_casella in nodi:
                        nodi[id_casella].label = g.get_id()
                        nodi[id_casella].add_class(f"giocatore-{indice}")

            except Exception:
                self.__app.log(f"[ERRORE TAVOLIERE]:\n{traceback.format_exc()}")

        # Invio al thread grafico
        try:
            self.__app.call_from_thread(_aggiorna_grafica)
        except RuntimeError:
            # Se siamo già nel thread principale della UI (es. durante il Replay),
            # l'eccezione scatta e noi eseguiamo la funzione direttamente!
            _aggiorna_grafica()
