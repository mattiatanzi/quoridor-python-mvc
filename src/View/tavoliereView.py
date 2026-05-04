from Model.tavoliere import Tavoliere

class TavoliereView:
    """Rappresenta l'insieme di operazioni per mostrare a video il tavoliere
    
    Attributi:
    ----------
        Costanti:
        ---------
        nome: COLONNE
            Tupla con elementi costanti contenente elementi da "a" ad "i" in ordine
        nome: PRIMA_RIGA
            Indica la prima riga del grafo
        nome: ULTIMA_RIGA
            Indica l'ultima riga del grafo
        nome: PRIMA_COLONNA
            Indica la prima colonna del grafo
        nome: ULTIMA_COLONNA
            Indica l'ultima colonan del grafo
        nome: SPAZIO_ELEMENTI
            Indica lo spazio che c'è tra ogni elemento del tavoliere
        nome: SPAZIO_MURO
            Indica lo spazio da tenere presente quando si stampa a video un muro
        nome: MURO_VERTICALE
            Indica il carattere del muro verticale
        nome: MURO_DIVISORIO_ORIZZONTALE
            Indica il muro divisorio che divide l'intestazione delle colonne dalle celle 
        nome: CELLA_VUOTA
            Indica il valore presente nel tavoliere per rappresentare una cella
    """

    __COLONNE = ("a","b","c","d","e","f","g","h","i")

    __PRIMA_RIGA = 9
    __ULTIMA_RIGA = 1
    __PRIMA_COLONNA = 0
    __ULTIMA_COLONNA = 8

    __SPAZIO_ELEMENTI = "\t"
    __SPAZIO_MURO = "   "

    __MURO_VERTICALE = "|"
    __MURO_DIVISORIO_ORIZZONTALE = "-----------------------------------------------------------------------"

    __CELLA_VUOTA = "."


    def stampa_tavoliere(self):
        
        stampa = " "
        for i in self.__COLONNE:
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