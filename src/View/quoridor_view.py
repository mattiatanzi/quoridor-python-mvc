from src.View.funzioni_utili_stampa import pulisci_schermo, chiedi_input_utente
from src.View.costanti_quoridor_view import CostantiQuoridorView


class QuoridorView:
    """Stampa del menu di base.

    Metodi
    ------
    def __menu_base(self):
        Permette di stampare la base del menu che è solo visiva

    def menu_di_gioco(self):
        Permette di stampare il menu di base e restituisce l'input che riceve
        dall'utente

    def stampa_messaggio(self, messaggio: str):
        Permette di stampare un messaggio nella fase di menu

    def get_input_modalita_partita(self) -> str:
        DESCRIZIONE
            Chiede all'utente se giocare ad una partita con limite di tempo o senza.
            Permette all'utente anche di scegliere di tornare indietro

    def get_input_limite_tempo(self) -> str:
        DESCRIZIONE
            Chiede all'utente quale limite di tempo usare.
            Presenta anche dei limiti di tempo predefiniti, in alternativa
            l'utente può digitare la stringa in un formato prestabilito.
            Permette all'utente anche di scegliere di tornare indietro
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

        pulisci_schermo()

        messaggio = "Selezionare Una Modalità Di Gioco:\n"

        for chiave, descrizione in CostantiQuoridorView._POSSIBILI_SCELTE_MODALITA.items():
            messaggio = messaggio + f"\n{chiave}. {descrizione}\n"

        return chiedi_input_utente(messaggio)

    def get_input_limite_tempo(self) -> str:

        pulisci_schermo()

        messaggio = "Selezionare Un Limite di Tempo:"

        for chiave, descrizione in CostantiQuoridorView._POSSIBILI_TIMER_DEFAULT.items():
            messaggio = messaggio + f"\n{chiave}. {descrizione}\n"

        messaggio = messaggio + CostantiQuoridorView._MESSAGGIO_ALTERNATIVO_SCELTA_TIMER

        return chiedi_input_utente(messaggio)
