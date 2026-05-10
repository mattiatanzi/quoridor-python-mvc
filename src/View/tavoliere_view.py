from Model.costanti import Costanti
from Model.giocatore import Giocatore
from Model.nodo import Nodo
from Model.tavoliere import Tavoliere


class TavoliereView:
    """Rappresenta l'insieme di operazioni per mostrare a video il tavoliere.

    Costanti
    --------
        nome: COSTANTI
        Costante di tipo costanti che contiene tutte le costanti

    Metodi
    -------
    nome: stampa_tavoliere
        Stampa il tavoliere di gioco con le informazioni dei giocatori e i muri
        posizionati in partita
    """

    __COSTANTI = Costanti()

    def stampa_tavoliere(self, tavoliere: Tavoliere, giocatori: set[Giocatore]):
        stampa = " "
        muriOrizzontali = [
            self.__COSTANTI.NO_ARCO
        ] * self.__COSTANTI.NUMERO_RIGHE_COLONNE
        for i in self.__COSTANTI.COLONNE:
            stampa += self.__COSTANTI.SPAZIO_ELEMENTI + i
        stampa += "\n"
        stampa += (
            self.__COSTANTI.SPAZIO_MURO
            + "  "
            + self.__COSTANTI.MURO_DIVISORIO_ORIZZONTALE
        )
        stampa += "\n"

        i = self.__COSTANTI.PRIMA_RIGA
        while i >= self.__COSTANTI.ULTIMA_RIGA:
            stampa += (
                str(i)
                + self.__COSTANTI.SPAZIO_MURO
                + self.__COSTANTI.MURO_VERTICALE
                + self.__COSTANTI.SPAZIO_MURO
            )
            j = self.__COSTANTI.PRIMA_COLONNA
            while j <= self.__COSTANTI.ULTIMA_COLONNA:
                chiaveAttuale = Nodo(self.__COSTANTI.COLONNE[j] + str(i))
                stampa_giocatore = False
                for g in giocatori:
                    if chiaveAttuale == g.get_posizione():
                        stampa += g.get_id()
                        stampa_giocatore = True
                if not (stampa_giocatore):
                    stampa += self.__COSTANTI.CELLA_VUOTA
                if (
                    tavoliere.get_adiacente(
                        chiaveAttuale, self.__COSTANTI.ARCO_ADIACENTE_SOTTO
                    )
                    == self.__COSTANTI.NO_ARCO
                ):
                    muriOrizzontali[j] = self.__COSTANTI.MURO_PRESENTE

                if (
                    tavoliere.get_adiacente(
                        chiaveAttuale, self.__COSTANTI.ARCO_ADIACENTE_DESTRA
                    )
                    == self.__COSTANTI.NO_ARCO
                ):
                    stampa += (
                        self.__COSTANTI.SPAZIO_MURO
                        + self.__COSTANTI.MURO_VERTICALE
                        + self.__COSTANTI.SPAZIO_MURO
                    )
                else:
                    stampa += self.__COSTANTI.SPAZIO_ELEMENTI
                j += 1
            stampa += "\n"
            k = 0
            if i == self.__COSTANTI.ULTIMA_RIGA:
                stampa += self.__COSTANTI.SPAZIO_MURO + " "
            while k < self.__COSTANTI.NUMERO_RIGHE_COLONNE - 1:
                if muriOrizzontali[k] == self.__COSTANTI.MURO_PRESENTE:
                    if muriOrizzontali[k - 1] != self.__COSTANTI.MURO_PRESENTE:
                        stampa += " " + self.__COSTANTI.SPAZIO_MURO
                    stampa += self.__COSTANTI.MURO_ORIZZONTALE
                else:
                    stampa += self.__COSTANTI.SPAZIO_ELEMENTI
                k += 1
            if muriOrizzontali[k] == self.__COSTANTI.MURO_PRESENTE:
                if muriOrizzontali[k - 1] != self.__COSTANTI.MURO_PRESENTE:
                    stampa += " " + self.__COSTANTI.SPAZIO_MURO
                stampa += self.__COSTANTI.MURO_ORIZZONTALE

            stampa += "\n"
            muriOrizzontali = [
                self.__COSTANTI.NO_ARCO
            ] * self.__COSTANTI.NUMERO_RIGHE_COLONNE

            i -= 1
        print(stampa)
