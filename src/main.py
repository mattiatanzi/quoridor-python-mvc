import sys

from src.Controller.quoridor_controller import QuoridorController
from src.View.giocatore_view import GiocatoreView
from src.View.partita_view import PartitaView
from src.View.tavoliere_view import TavoliereView


def main():
    """Permette di avviare il menu iniziale.

    Crea un oggetto quoridor su cui richiama il menu iniziale dove ci saranno le
    scelte di gioco
    """
    # Controllo flag di help all'avvio
    if len(sys.argv) > 1 and sys.argv[1] in ("--help", "-h"):
        view = PartitaView(GiocatoreView(), TavoliereView())
        view.stampa_aiuto()
        return
    
    quoridor = QuoridorController()
    quoridor.gioca()


if __name__ == "__main__":
    main()
