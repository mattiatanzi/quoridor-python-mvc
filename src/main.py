import sys
import threading

from src.Controller.quoridor_controller import QuoridorController
from src.View.TUI.quoridor_view_TUI import QuoridorViewTUI
from src.View.CLI.quoridor_view_CLI import QuoridorViewCLI
from src.View.TUI.partita_view_TUI import PartitaViewTUI # Da realizzare
from src.View.CLI.partita_view_CLI import PartitaViewCLI


def main():
    """Permette di avviare il menu iniziale.

    Crea un oggetto quoridor su cui richiama il menu iniziale dove ci saranno le
    scelte di gioco
    """
    if len(sys.argv)>1 and sys.argv[1] in ("--gui"):
        quoridor_view = QuoridorViewTUI()
        partita_view = PartitaViewTUI()
        quoridor = QuoridorController(quoridor_view,partita_view)

        thread_gioc = threading.Thread(target=quoridor.gioca,daemon=True)
        thread_gioc.start()
        quoridor_view.avvia_gui()
    else:
        quoridor_view = QuoridorViewCLI()
        partita_view = PartitaViewCLI()
        quoridor = QuoridorController(quoridor_view,partita_view)
        quoridor.gioca()


if __name__ == "__main__":
    main()
