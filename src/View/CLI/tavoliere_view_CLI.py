from src.Model.costanti_tavoliere import Costanti
from src.Model.giocatore import Giocatore
from src.Model.nodo import Nodo
from src.Model.tavoliere import Tavoliere
from src.View.tavoliere_view import TavoliereviewAstratta


class TavoliereViewCLI(TavoliereviewAstratta):
    """Rappresenta l'insieme di operazioni per mostrare a video il tavoliere in versione CLI.

    Costanti
    
        __COSTANTI
            Costante di tipo Costanti che contiene tutte le costanti utilizzate
            per la stampa del tavoliere

    Metodi
    
        Stessi della classe astratta TavoliereViewAstratta
        
        def stampa_tavoliere(
            self,
            tavoliere: Tavoliere,
            giocatori: set[Giocatore]
        ):
        DESCRIZIONE
            Stampa la rappresentazione testuale del tavoliere,
            mostrando la posizione dei giocatori e dei muri.
    """

    __COSTANTI = Costanti()

    def stampa_tavoliere(self, tavoliere: Tavoliere, giocatori: set[Giocatore]):
        stampa = ""
        muri_orizzontali = [
            self.__COSTANTI.NO_ARCO
        ] * self.__COSTANTI.NUMERO_RIGHE_COLONNE
        for i in self.__COSTANTI.COLONNE:
            stampa += self.__COSTANTI.SPAZIO_COLONNE_INTESTAZIONE + i
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
                chiave_attuale = Nodo(self.__COSTANTI.COLONNE[j] + str(i))
                stampa_giocatore = False
                for g in giocatori:
                    if chiave_attuale == g.get_posizione() and g.is_attivo():
                        stampa += g.get_id()
                        stampa_giocatore = True
                if not (stampa_giocatore):
                    stampa += f"{self.__COSTANTI.CELLA_VUOTA:<2}"
                if (
                    tavoliere.get_adiacente(
                        chiave_attuale, self.__COSTANTI.ARCO_ADIACENTE_SOTTO
                    )
                    == self.__COSTANTI.NO_ARCO
                ):
                    muri_orizzontali[j] = self.__COSTANTI.MURO_PRESENTE

                if (
                    tavoliere.get_adiacente(
                        chiave_attuale, self.__COSTANTI.ARCO_ADIACENTE_DESTRA
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
                if muri_orizzontali[k] == self.__COSTANTI.MURO_PRESENTE:
                    if muri_orizzontali[k - 1] != self.__COSTANTI.MURO_PRESENTE:
                        stampa += " " + self.__COSTANTI.SPAZIO_MURO
                    stampa += self.__COSTANTI.MURO_ORIZZONTALE
                else:
                    stampa += self.__COSTANTI.SPAZIO_MURI_ORIZZONTALI
                k += 1
            if muri_orizzontali[k] == self.__COSTANTI.MURO_PRESENTE:
                if muri_orizzontali[k - 1] != self.__COSTANTI.MURO_PRESENTE:
                    stampa += " " + self.__COSTANTI.SPAZIO_MURO
                stampa += self.__COSTANTI.MURO_ORIZZONTALE

            stampa += "\n"
            muri_orizzontali = [
                self.__COSTANTI.NO_ARCO
            ] * self.__COSTANTI.NUMERO_RIGHE_COLONNE

            i -= 1
        print(stampa)
