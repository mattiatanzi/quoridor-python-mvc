import sys
import threading
import os

from src.Controller.quoridor_controller import QuoridorController
from src.View.TUI.quoridor_view_TUI import QuoridorViewTUI
from src.View.CLI.quoridor_view_CLI import QuoridorViewCLI
from src.View.TUI.partita_view_TUI import PartitaViewTUI 
from src.View.CLI.partita_view_CLI import PartitaViewCLI
from src.View.CLI.giocatore_view_CLI import GiocatoreViewCLI
from src.View.CLI.tavoliere_view_CLI import TavoliereViewCLI
from src.View.TUI.giocatore_view_TUI import GiocatoreViewTUI
from src.View.TUI.tavoliere_view_TUI import TavoliereViewTUI



def main():
    """Permette di avviare il menu iniziale.

    Crea un oggetto quoridor su cui richiama il menu iniziale dove ci saranno le
    scelte di gioco
    """

    if len(sys.argv)>1 and sys.argv[1] in ("--gui"):
        # FIX PER DOCKER: Forza il supporto ai colori
        os.environ["TERM"] = "xterm-256color"
        os.environ["COLORTERM"] = "truecolor"

        quoridor_view = QuoridorViewTUI()
        app_condivisa = quoridor_view.get_app()
        partita_view = PartitaViewTUI(GiocatoreViewTUI(app_condivisa),TavoliereViewTUI(app_condivisa),app_condivisa)
        quoridor = QuoridorController(quoridor_view,partita_view)
        thread_gioc = threading.Thread(target=quoridor.gioca,daemon=True)
        thread_gioc.start()
        quoridor_view.avvia_gui()
    
    elif len(sys.argv) > 1 and sys.argv[1] in ("--help", "-h"):
        view = PartitaViewCLI(GiocatoreViewCLI(), TavoliereViewCLI())
        view.stampa_aiuto()
        return
    else:
        quoridor_view = QuoridorViewCLI()
        partita_view = PartitaViewCLI(GiocatoreViewCLI(),TavoliereViewCLI())
        quoridor = QuoridorController(quoridor_view,partita_view)
        quoridor.gioca()


if __name__ == "__main__":
    main()
