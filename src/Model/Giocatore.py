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


    """

    __idGiocatore: str

    def __init__(self, newIdGiocatore: str):
        self.setID(newIdGiocatore)

    def getID(self) -> str:
        return self.__idGiocatore

    def setID(self, newIdGiocatore: str):
        self.__idGiocatore = newIdGiocatore
