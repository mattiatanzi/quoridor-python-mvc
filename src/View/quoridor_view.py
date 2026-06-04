from src.View.funzioni_utili_stampa import pulisci_schermo, chiedi_input_utente


class QuoridorView:
    """Stampa del menu di base.

    Metodi
    ------
    nome: menu_base:
        Permette di stampare la base del menu che è solo visiva

    nome: menu_di_gioco:
        Permette di stampare il menu di base e restituisce l'input che riceve
        dall'utente

    nome: stampa_messaggio:
        Permette di stampare un messaggio nella fase di menu
    """

    def __menu_base(self):
        pulisci_schermo()
        print("Benvenuto in Quoridor \n")
        print("1 - Avvia una nuova partita \n")
        print("0 - Esci dal gioco \n")

        print("h - Aiuto (Comandi di gioco) \n")

    def menu_di_gioco(self):
        self.__menu_base()

    def get_input_menu(self) -> str:
        return input("Seleziona un'opzione: ")

    def stampa_messaggio(self, messaggio: str):
        print(messaggio)

    def get_input_modalita_partita(self) -> str:
        messaggio = """Selezionare Una Modalità Di Gioco:

        1. Partita con Timer

        2. Partita senza Timer

        3. Torna Indietro
        """

        return chiedi_input_utente(messaggio)

    def get_input_limite_tempo(self) -> str:
        messaggio = """Selezionare Un Limite di Tempo:

        1. 3 Minuti

        2. 5 Minuti

        3. Torna Indietro

        (In alternativa, digitare il limite di tempo nel formato HH:MM:SS)
        """

        return chiedi_input_utente(messaggio)
