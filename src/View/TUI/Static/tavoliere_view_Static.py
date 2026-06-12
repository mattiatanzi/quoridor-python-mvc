from textual import events
from textual.app import ComposeResult
from textual.containers import Grid, Horizontal, Vertical
from textual.message import Message
from textual.widgets import Button, Label, Static

from src.Model.costanti_tavoliere import Costanti


class MuroCliccato(Message):
    """Messaggio personalizzato per notificare il clic su un muro."""

    def __init__(self, ID_muro: str) -> None:
        super().__init__()
        self.ID_muro = ID_muro


class MuroVerticale(Static):
    """Un pezzo di muro verticale basato su Static, ultra-leggero."""

    def on_click(self) -> None:
        if self.id:
            # Inviamo il messaggio verso l'alto (verrà catturato dal Tavoliere stesso)
            self.post_message(MuroCliccato(self.id))


class MuroOrizzontale(Static):
    """Un pezzo di muro orizzontale basato su Static, ultra-leggero."""

    def on_click(self) -> None:
        if self.id:
            self.post_message(MuroCliccato(self.id))


class TavoliereViewStatic(Static):
    """Il Widget puro che disegna il tabellone 17x17 e le coordinate esterne."""

    def __init__(self, coda_input, is_replay=False, **kwargs):
        super().__init__(**kwargs)
        self._coda_input = coda_input
        self._muri_attualmente_hoverati = []
        self._is_replay = is_replay

    def compose(self) -> ComposeResult:
        colonna = Costanti.COLONNE

        with Vertical(id="contenitore-tavoliere-completo"):
            # --- 1. RIGA LETTERE (Spostata in alto) ---
            with Horizontal(id="riga-lettere"):
                for col in colonna:
                    yield Label(col, classes="label-lettera")

            with Horizontal(id="fascia-centrale"):
                # --- 2. COLONNA NUMERI (a sinistra) ---
                with Vertical(id="colonna-numeri"):
                    for riga in range(9, 0, -1):
                        yield Label(str(riga), classes="label-numero")

                # --- 3. LA GRIGLIA GIOCABILE ---
                with Grid(id="griglia-tavoliere"):
                    for riga in range(9, 0, -1):
                        # --- RIGA DISPARI: Caselle (8) e Muri Verticali (2) ---
                        for c_idx, col in enumerate(colonna):
                            yield Button("", id=f"btn-{col}{riga}", classes="casella")
                            if c_idx < 8:
                                yield MuroVerticale(
                                    "", id=f"btn-{col}{riga}v", classes="muro-v"
                                )

                        # --- RIGA PARI: Muri Orizzontali (8) e Intersezioni (2) ---
                        if riga > 1:
                            for c_idx, col in enumerate(colonna):
                                # 1. Sotto la casella mettiamo il muro orizzontale
                                yield MuroOrizzontale(
                                    "", id=f"btn-{col}{riga}h", classes="muro-h"
                                )

                                # 2. Sotto il muro verticale mettiamo l'intersezione (solo per le prime 8 colonne)
                                if c_idx < 8:
                                    yield Static(
                                        "",
                                        id=f"int-{col}{riga}",
                                        classes="intersezione",
                                        disabled=True,
                                    )

    def on_button_pressed(self, event: Button.Pressed):
        """Cattura il click su QUALSIASI cosa (casella o lineetta) e lo invia al controller."""
        id_premuto = event.button.id
        if id_premuto and id_premuto.startswith("btn-"):
            mossa = id_premuto.replace("btn-", "")
            self._coda_input.put(mossa)

    def on_muro_cliccato(self, event: MuroCliccato) -> None:
        """Cattura il messaggio inviato da MuroVerticale o MuroOrizzontale."""
        id_premuto = event.ID_muro
        if id_premuto and id_premuto.startswith("btn-"):
            mossa = id_premuto.replace("btn-", "")
            self._coda_input.put(mossa)  # Invia al controller esattamente come prima!

    def on_mouse_move(self, event: events.MouseMove) -> None:
        """Gestisce l'hover unendo visivamente i due segmenti del muro e l'intersezione centrale."""
        if self._is_replay:
            return
        try:
            widget_sotto_mouse, _ = self.screen.get_widget_at(
                event.screen_x, event.screen_y
            )
        except Exception:
            return

        w_id = widget_sotto_mouse.id if widget_sotto_mouse else None

        # Controlliamo se siamo sopra un pezzo di muro non ancora piazzato stabilmente
        is_muro = (
            w_id
            and w_id.startswith("btn-")
            and (w_id.endswith("h") or w_id.endswith("v"))
        )
        esclusi_piazzati = (
            widget_sotto_mouse and "muro-piazzato" not in widget_sotto_mouse.classes
        )

        nuovi_id_da_colorare = []

        if is_muro and esclusi_piazzati:
            # 1. Aggiungiamo il pezzo corrente sotto il mouse
            nuovi_id_da_colorare.append(w_id)

            tipo = w_id[-1]  # 'h' o 'v'
            corpo = w_id[4:-1]  # es: "e5"
            col = corpo[0]
            riga = int(corpo[1])
            colonne = Costanti.COLONNE

            if tipo == "h":
                # --- MURO ORIZZONTALE ---
                try:
                    idx = colonne.index(col)
                    if idx < len(colonne) - 1:
                        prossima_col = colonne[idx + 1]
                        # Secondo pezzo di muro a destra
                        nuovi_id_da_colorare.append(f"btn-{prossima_col}{riga}h")
                        # L'INTERSEZIONE in mezzo (sotto il muro verticale della colonna corrente)
                        nuovi_id_da_colorare.append(f"int-{col}{riga}")
                except ValueError:
                    pass
            elif tipo == "v":
                # --- MURO VERTICALE ---
                if riga > 1:
                    # Secondo pezzo di muro sotto
                    nuovi_id_da_colorare.append(f"btn-{col}{riga - 1}v")
                    # L'INTERSEZIONE in mezzo (all'altezza della riga corrente)
                    nuovi_id_da_colorare.append(f"int-{col}{riga}")

        # Se il blocco sotto l'hover è cambiato rispetto a prima
        if nuovi_id_da_colorare != self._muri_attualmente_hoverati:
            # 1. RIPRISTINO: Spegniamo i vecchi elementi (muri o intersezioni)
            for vecchio_id in self._muri_attualmente_hoverati:
                try:
                    w = self.query_one(f"#{vecchio_id}")
                    if "muro-piazzato" not in w.classes:
                        w.styles.background = "black"
                except Exception:
                    pass

            # 2. ACCENSIONE: Coloriamo i nuovi elementi uniti
            self._muri_attualmente_hoverati = []
            for nuovo_id in nuovi_id_da_colorare:
                try:
                    w = self.query_one(f"#{nuovo_id}")
                    if "muro-piazzato" not in w.classes:
                        w.styles.background = "ansi_bright_green"
                        self._muri_attualmente_hoverati.append(nuovo_id)
                except Exception:
                    pass
