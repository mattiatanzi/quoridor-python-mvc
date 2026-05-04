from Model.tavoliere import Tavoliere
from Model.costanti import Costanti

class TavoliereView:
    """Rappresenta l'insieme di operazioni per mostrare a video il tavoliere
    Costanti
    --------
        nome: COSTANTI
        Costante di tipo costanti che contiene tutte le costanti
    """

    __COSTANTI = Costanti()

    def stampa_tavoliere(self):
        
        stampa = " "
        for i in self.__COSTANTI.COLONNE:
            stampa += self.__COSTANTI.SPAZIO_ELEMENTI + i 
        stampa += "\n"
        stampa += self.__COSTANTI.SPAZIO_MURO+"  "+ self.__COSTANTI.MURO_DIVISORIO_ORIZZONTALE
        stampa +="\n"

        i = self.__COSTANTI.PRIMA_RIGA
        while i>=self.__COSTANTI.ULTIMA_RIGA:
            stampa += str(i) + self.__COSTANTI.SPAZIO_MURO + self.__COSTANTI.MURO_VERTICALE+self.__COSTANTI.SPAZIO_MURO 
            j = self.__COSTANTI.PRIMA_COLONNA
            while j<=self.__COSTANTI.ULTIMA_COLONNA:
                stampa += self.__COSTANTI.CELLA_VUOTA
                stampa += self.__COSTANTI.SPAZIO_ELEMENTI
                j +=1
            stampa +="\n"
            stampa+="\n"
            i-=1
        print(stampa)