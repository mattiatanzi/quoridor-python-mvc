from Model.grafo import Grafo
from Model.nodo import Nodo
from Model.costanti import Costanti

class ErroreTavoliere(Exception):
    """"""
    pass
class Tavoliere:
    """Contiene il tavoliere di gioco.
    
    Attributi
    ---------
    nome: tavoliere
        Il tavoliere di gioco realizzato con un grafo
    
    Metodi:
    -------

    nome get_adiacente
        Restituisce l'adiacente presente ad un nodo specifico
    """

    __COSTANTI = Costanti()
    def __init__(self):
        self.__tavoliere = Grafo()

    def get_adiacente(self,nodo,posizione):
        return self.__tavoliere.get_adiacente(nodo,posizione)
    
    def __piazza_muro(self, primo_nodo : Nodo, secondo_nodo : Nodo):
        self.__tavoliere.rimuovi_arco(primo_nodo,secondo_nodo)

    def piazza_muro_orizzontale(self, azione: str):
        
        if azione[0] == 'i': # Caso speciale, piazzamento muro nell'ultima colonna
            nodo_muro_dx_alto = Nodo(azione[0:2])
            nodo_muro_dx_bass = self.get_adiacente(nodo_muro_dx_alto,self.__COSTANTI.ARCO_ADIACENTE_SOTTO)
            nodo_muro_sx_alto = self.get_adiacente(nodo_muro_dx_alto,self.__COSTANTI.ARCO_ADIACENTE_SINISTRA)
            nodo_muro_sx_bass = self.get_adiacente(nodo_muro_sx_alto,self.__COSTANTI.ARCO_ADIACENTE_SOTTO)
        else:
            nodo_muro_sx_alto = Nodo(azione[0:2])
            nodo_muro_sx_bass = self.get_adiacente(nodo_muro_sx_alto,self.__COSTANTI.ARCO_ADIACENTE_SOTTO)
            nodo_muro_dx_alto = self.get_adiacente(nodo_muro_sx_alto,self.__COSTANTI.ARCO_ADIACENTE_DESTRA)
            nodo_muro_dx_bass = self.get_adiacente(nodo_muro_dx_alto,self.__COSTANTI.ARCO_ADIACENTE_SOTTO)


        if not(self.__tavoliere.esiste_arco(nodo_muro_sx_alto,nodo_muro_sx_bass)):
            raise ErroreTavoliere(f"Errore: Muro già piazzato tra le due celle {nodo_muro_sx_alto.get_valore_id_nodo()} {nodo_muro_sx_bass.get_valore_id_nodo() }")

        if not(self.__tavoliere.esiste_arco(nodo_muro_dx_alto,nodo_muro_dx_bass)):
            raise ErroreTavoliere(f"Errore: Muro già piazzato tra le due celle {nodo_muro_dx_alto.get_valore_id_nodo()} {nodo_muro_dx_bass.get_valore_id_nodo()}")
        
        self.__piazza_muro(nodo_muro_sx_alto,nodo_muro_sx_bass)
        self.__piazza_muro(nodo_muro_dx_alto,nodo_muro_dx_bass)

