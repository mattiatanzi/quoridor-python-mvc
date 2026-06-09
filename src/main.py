import sys

from src.Controller.quoridor_controller import QuoridorController


def main():
    """Permette di avviare il menu iniziale.

    Crea un oggetto quoridor su cui richiama il menu iniziale dove ci saranno le
    scelte di gioco
    """
    if len(sys.arv)>1 and sys.argv[1] in ("--gui"):
        quoridor = QuoridorController(False) 
    else:
        quoridor = QuoridorController(True) 
        
    quoridor.gioca()


if __name__ == "__main__":
    main()
