class Giocatore:
    """Classe Giocatore.

    Descrizione:
        Contiene informazioni relative al giocatore

    Attributi:

        - idGiocatore

            Privato

            Tipo stringa

            l'ID del giocatore, necessario a determinarne la posizione sul
            tavoliere (oltre a eventualmente distinguerlo dagli altri giocatori)

            Indicata nel formato 'Pn', dove
                n appartiene a [1,4]

            Esempi:
                P1 (Giocatore 1)
                P3 (Giocatore 3)

        - posizioneCorrente

            Privato

            Tipo stringa

            La posizione del giocatore rispetto al tavoliere nella partita in corso

            Viene riportata nel formato 'an', come le posizioni del tavoliere

            Per informazioni sulla notazione usata per le posizioni consultare
            la documentazione sul tavoliere di gioco

    """

    # Variabili
    __idGiocatore: str
    __posizioneCorrente: str

    # Costanti
    __DEF_POSIZIONE = "a1"

    # Metodi

    # Costruttore

    def __init__(self, newIdGiocatore: str, newPosizione: str = __DEF_POSIZIONE):
        self.set_id(newIdGiocatore)
        self.set_posizione(newPosizione)

    # Modificatori / Osservatori

    def get_id(self) -> str:
        return self.__idGiocatore

    def set_id(self, newIdGiocatore: str):
        self.__idGiocatore = newIdGiocatore

    def get_posizione(self) -> str:
        return self.__posizioneCorrente

    def set_posizione(self, newPosizione: str):
        self.__posizioneCorrente = newPosizione
