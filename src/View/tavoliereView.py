from Model.tavoliere import Tavoliere

class TavoliereView:
    """Rappresenta l'insieme di operazioni per mostrare a video il tavoliere
    """

    __PRIMA_RIGA = 9
    __ULTIMA_RIGA = 1
    __PRIMA_COLONNA = 0
    __ULTIMA_COLONNA = 8
    __NO_ARCO = "0" 

    __ARCO_ADIACENTE_SOPRA = 0
    __ARCO_ADIACENTE_SOTTO = 1
    __ARCO_ADIACENTE_SINISTRA = 2
    __ARCO_ADIACENTE_DESTRA = 3 

    __SPAZIO_ELEMENTI = "\t"
    __SPAZIO_MURO = "   "

    __MURO_PRESENTE = 1
    __MURO_VERTICALE = "|"
    __MURO_ORIZZONTALE = "--------"
    __MURO_DIVISORIO_ORIZZONTALE = "-----------------------------------------------------------------------"

    __GIOCATORE1 = "1"
    __GIOCATORE2 = "2"

    __CELLA_VUOTA = "."

    __NUMERO_RIGHE_COLONNE = 9

    def stampaTavoliere(self):
        colonne = ("a","b","c","d","e","f","g","h","i")
        stampa = " "
        for i in colonne:
            stampa += self.__SPAZIO_ELEMENTI + i 
        stampa += "\n"
        stampa += self.__SPAZIO_MURO+"  "+ self.__MURO_DIVISORIO_ORIZZONTALE
        stampa +="\n"

        i = self.__PRIMA_RIGA
        while i>=self.__ULTIMA_RIGA:
            stampa += str(i) + self.__SPAZIO_MURO + self.__MURO_VERTICALE+self.__SPAZIO_MURO
            j = self.__PRIMA_COLONNA
            while j<=self.__ULTIMA_COLONNA:
                stampa += self.__CELLA_VUOTA
                stampa += self.__SPAZIO_ELEMENTI
                j +=1
            stampa +="\n"
            stampa+="\n"
            i-=1
        print(stampa)