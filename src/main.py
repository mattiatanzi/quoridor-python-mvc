from Controller.quoridor_controller import QuoridorController


def main():
    """Permette di avviare il menu iniziale.

    Crea un oggetto quoridor su cui richiama il menu iniziale dove ci saranno le
    scelte di gioco
    """
    quoridor = QuoridorController()
    quoridor.gioca()


if __name__ == "__main__":
    main()
