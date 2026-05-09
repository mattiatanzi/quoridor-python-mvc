from Model.nodo import Nodo


class Costanti:
    """Costanti presenti per tutte le classi.
    
    Costanti
    ----------
    nome : COLONNE
        Tupla con elementi costanti contenente elementi da "a" ad "i" in ordine
    nome: PRIMA_RIGA
        Indica la prima riga del grafo
    nome: ULTIMA_RIGA
        Indica l'ultima riga del grafo
    nome: PRIMA_COLONNA
        Indica la prima colonna del grafo
    nome: ULTIMA_COLONNA
        Indica l'ultima colonan del grafo
    nome: NO_ARCO
        Indica l'elemento che rappresenta che non c'è un arco tra due nodi
    nome: ARCO_ADIACENTE_SOPRA
        Indica la posizione nella lista degli adiacenti dell'arco che ha il nodo verso sopra
    nome: ARCO_ADIACENTE_SOTTO
        Indica la posizione nella lista degli adiacenti dell'arco che ha il nodo verso sotto
    nome: ARCO_ADIACENTE_SINISTRA
        Indica la posizione nella lista degli adiacenti dell'arco che ha il nodo verso sinistra
    nome: ARCO_ADIACENTE_DESTRA
        Indica la posizione nella lista degli adiacenti dell'arco che ha il nodo verso destra
    nome: NUMERO_ADIACENTI
        Indica il numero degli adiacenti presenti
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

    COLONNE = ("a", "b", "c", "d", "e", "f", "g", "h", "i")

    PRIMA_RIGA = 9
    ULTIMA_RIGA = 1
    PRIMA_COLONNA = 0
    ULTIMA_COLONNA = 8
    NO_ARCO = Nodo("0")

    ARCO_ADIACENTE_SOPRA = 0
    ARCO_ADIACENTE_SOTTO = 1
    ARCO_ADIACENTE_SINISTRA = 2
    ARCO_ADIACENTE_DESTRA = 3

    NUMERO_ADIACENTI = 4

    SPAZIO_ELEMENTI = "\t"
    SPAZIO_MURO = "   "

    MURO_VERTICALE = "|"
    MURO_DIVISORIO_ORIZZONTALE = (
        "-----------------------------------------------------------------------"
    )

    CELLA_VUOTA = "."
